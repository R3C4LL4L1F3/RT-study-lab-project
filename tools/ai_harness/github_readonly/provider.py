from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib, json, re
from typing import Any, Mapping, Protocol, Sequence
from urllib.parse import unquote

GITHUB_API_VERSION="2026-03-10"; PROVIDER_ID="github-readonly-v1"; PROJECT_CONTROL_ALIAS="PROJECT_CONTROL"
EXPECTED_REPOSITORY="R3C4LL4L1F3/RT-study-lab-project"; EXPECTED_REPOSITORY_ID=1328584202; EXPECTED_NODE_ID="R_kgDOTzCWCg"; EXPECTED_DEFAULT_BRANCH="main"

class EvidenceState(str,Enum):
    VERIFIED="VERIFIED"; MISSING="MISSING"; STALE="STALE"; UNVERIFIED="UNVERIFIED"; CONTRADICTORY="CONTRADICTORY"
EVIDENCE_PRECEDENCE=(EvidenceState.CONTRADICTORY,EvidenceState.UNVERIFIED,EvidenceState.STALE,EvidenceState.MISSING,EvidenceState.VERIFIED)
class CollectionCompleteness(str,Enum):
    COMPLETE="COMPLETE"; INCOMPLETE="INCOMPLETE"; UNVERIFIED="UNVERIFIED"
class CredentialCapability(str,Enum):
    NOT_CONFIGURED="NOT_CONFIGURED"; UNVERIFIED="UNVERIFIED"; INVALID="INVALID"; OVERPRIVILEGED="OVERPRIVILEGED"; VERIFIED_READ_ONLY="VERIFIED_READ_ONLY"
class Operation(str,Enum):
    REPO_GET="GH-OP-REPO-GET"; COMMIT_GET="GH-OP-COMMIT-GET"; CONTENT_GET="GH-OP-CONTENT-GET"; PR_GET="GH-OP-PR-GET"
    PR_COMMITS_LIST="GH-OP-PR-COMMITS-LIST"; PR_FILES_LIST="GH-OP-PR-FILES-LIST"; PR_REVIEWS_LIST="GH-OP-PR-REVIEWS-LIST"
    PR_MERGED_CHECK="GH-OP-PR-MERGED-CHECK"; CHECK_RUNS_LIST="GH-OP-CHECK-RUNS-LIST"
ALLOWED_OPERATIONS=frozenset(Operation)
COLLECTION_OPERATIONS=frozenset({Operation.PR_COMMITS_LIST,Operation.PR_FILES_LIST,Operation.PR_REVIEWS_LIST,Operation.CHECK_RUNS_LIST})
CONTENT_PREFIXES=("ai-harness/RTSL-AIH-001/","ai-harness/RTSL-AIH-002/","docs/ai-harness/","config/ai_harness/")
READ_ONLY_PERMISSION_CEILING={"metadata":"read","contents":"read","pull_requests":"read","checks":"read"}
SECRET_HEADER_NAMES=frozenset({"authorization","proxy-authorization","x-github-token"})

class EvidenceProvider(Protocol):
    enabled:bool
    def retrieve(self,request:"EvidenceRequest")->"EvidenceRecord":...
class CredentialSource(Protocol):
    def permission_manifest(self,repository_alias:str)->Mapping[str,str]|None:...
    def request_headers(self,repository_alias:str)->Mapping[str,str]:...
class ReadOnlyTransport(Protocol):
    def get(self,*,operation:Operation,repository:str,subject:str,headers:Mapping[str,str],page:int|None=None)->"TransportResponse":...

@dataclass(frozen=True)
class EvidenceRequest:
    repository_alias:str; operation:Operation; subject:str; ref:str|None=None; path:str|None=None
@dataclass(frozen=True)
class TransportResponse:
    status_code:int; payload:Any=None; next_page:int|None=None; endpoint_supports_absence:bool=False
@dataclass(frozen=True)
class EvidenceRecord:
    provider:str; repository_alias:str; repository_id:int|None; repository_node_id:str|None; operation:str; subject:str; ref:str|None; api_version:str
    evidence_state:EvidenceState; credential_capability:CredentialCapability; collection_completeness:CollectionCompleteness|None; payload:Any; payload_sha256:str; audit:Mapping[str,Any]

class StaticCredentialSource:
    def __init__(self,manifest:Mapping[str,str]|None=None,headers:Mapping[str,str]|None=None)->None:
        self._manifest=None if manifest is None else dict(manifest); self._headers=dict(headers or {})
    def permission_manifest(self,repository_alias:str)->Mapping[str,str]|None:return None if self._manifest is None else dict(self._manifest)
    def request_headers(self,repository_alias:str)->Mapping[str,str]:return dict(self._headers)
class FixtureTransport:
    def __init__(self,responses:Sequence[TransportResponse])->None:self._responses=list(responses); self.calls:list[dict[str,Any]]=[]
    def get(self,*,operation:Operation,repository:str,subject:str,headers:Mapping[str,str],page:int|None=None)->TransportResponse:
        self.calls.append({"method":"GET","operation":operation.value,"repository":repository,"subject":subject,"page":page,"header_names":sorted(headers)})
        if not self._responses:raise RuntimeError("fixture transport has no remaining response")
        return self._responses.pop(0)
    def request(self,method:str,**_:Any)->TransportResponse:raise PermissionError(f"non-GET transport method rejected before network: {method.upper()}")
class DisabledEvidenceProvider:
    enabled=False
    def retrieve(self,request:EvidenceRequest)->EvidenceRecord:
        return _record(request,EvidenceState.UNVERIFIED,CredentialCapability.NOT_CONFIGURED,CollectionCompleteness.UNVERIFIED if request.operation in COLLECTION_OPERATIONS else None,{"reason":"provider-disabled"},None)

class GitHubReadOnlyEvidenceProvider:
    enabled=True
    def __init__(self,credentials:CredentialSource,transport:ReadOnlyTransport)->None:self._credentials=credentials; self._transport=transport
    def retrieve(self,request:EvidenceRequest)->EvidenceRecord:
        _validate_request(request)
        capability=validate_permission_manifest(self._credentials.permission_manifest(request.repository_alias))
        if capability is not CredentialCapability.VERIFIED_READ_ONLY:
            return _record(request,EvidenceState.UNVERIFIED,capability,CollectionCompleteness.UNVERIFIED if request.operation in COLLECTION_OPERATIONS else None,{"reason":"credential-preflight-failed"},None)
        headers={**self._credentials.request_headers(request.repository_alias),"X-GitHub-Api-Version":GITHUB_API_VERSION}
        try:repo_response=self._transport.get(operation=Operation.REPO_GET,repository=EXPECTED_REPOSITORY,subject=EXPECTED_REPOSITORY,headers=headers)
        except Exception:return _record(request,EvidenceState.UNVERIFIED,capability,CollectionCompleteness.UNVERIFIED if request.operation in COLLECTION_OPERATIONS else None,{"reason":"repository-identity-retrieval-failed"},None)
        repo_state,identity,repo_payload=_normalize_repository(repo_response)
        if repo_state is not EvidenceState.VERIFIED:
            return _record(request,repo_state,capability,CollectionCompleteness.UNVERIFIED if request.operation in COLLECTION_OPERATIONS else None,{"repository":repo_payload,"reason":"repository-identity-preflight-failed"},identity)
        if request.operation is Operation.REPO_GET:return _record(request,EvidenceState.VERIFIED,capability,None,repo_payload,identity)
        return self._collection(request,capability,headers,identity) if request.operation in COLLECTION_OPERATIONS else self._scalar(request,capability,headers,identity)
    def _scalar(self,request,capability,headers,identity):
        try:r=self._transport.get(operation=request.operation,repository=EXPECTED_REPOSITORY,subject=request.subject,headers=headers)
        except Exception:return _record(request,EvidenceState.UNVERIFIED,capability,None,{"reason":"operation-retrieval-failed"},identity)
        state,payload=_normalize_scalar(request,r,identity); return _record(request,state,capability,None,payload,identity)
    def _collection(self,request,capability,headers,identity):
        items=[]; page=1; seen=set()
        while page is not None:
            if page in seen:return _record(request,EvidenceState.UNVERIFIED,capability,CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED,{"items":items,"reason":"pagination-cycle"},identity)
            seen.add(page)
            try:r=self._transport.get(operation=request.operation,repository=EXPECTED_REPOSITORY,subject=request.subject,headers=headers,page=page)
            except Exception:return _record(request,EvidenceState.UNVERIFIED,capability,CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED,{"items":items,"reason":"collection-retrieval-failed"},identity)
            if r.status_code!=200:return _record(request,EvidenceState.UNVERIFIED,capability,CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED,{"items":items,"status_code":r.status_code},identity)
            state,page_items=_normalize_collection_page(request,r.payload)
            if state is not EvidenceState.VERIFIED:return _record(request,state,capability,CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED,{"items":items,"reason":"invalid-collection-page"},identity)
            items.extend(page_items); page=r.next_page
        payload={"items":items,"exhaustive":True}
        fact=_derive_collection_fact(request,items)
        if fact is not None:payload["derived_fact"]=fact
        return _record(request,EvidenceState.VERIFIED,capability,CollectionCompleteness.COMPLETE,payload,identity)

def resolve_evidence_state(states:Sequence[EvidenceState])->EvidenceState:
    p=set(states)
    for s in EVIDENCE_PRECEDENCE:
        if s in p:return s
    return EvidenceState.UNVERIFIED

def validate_permission_manifest(permissions:Mapping[str,str]|None)->CredentialCapability:
    if permissions is None:return CredentialCapability.NOT_CONFIGURED
    n={str(k).lower():str(v).lower() for k,v in permissions.items()}
    if not n:return CredentialCapability.UNVERIFIED
    for name,value in n.items():
        if value not in {"read","none"}:return CredentialCapability.OVERPRIVILEGED
        if name not in READ_ONLY_PERMISSION_CEILING and value!="none":return CredentialCapability.OVERPRIVILEGED
    return CredentialCapability.VERIFIED_READ_ONLY if all(n.get(k)==v for k,v in READ_ONLY_PERMISSION_CEILING.items()) else CredentialCapability.UNVERIFIED

def validate_content_path(path:str)->str:
    if not isinstance(path,str) or not path:raise ValueError("content path is required")
    d=path
    for _ in range(3):
        n=unquote(d)
        if n==d:break
        d=n
    d=d.replace("\\","/")
    if d.startswith("/") or re.match(r"^[A-Za-z]:/",d):raise ValueError("absolute content paths are prohibited")
    seg=d.split("/")
    if any(s in {"",".",".."} for s in seg):raise ValueError("path traversal or normalization escape prohibited")
    n="/".join(seg)
    if not any(n.startswith(p) for p in CONTENT_PREFIXES):raise ValueError("content path is outside the governed allowlist")
    return n

def _validate_request(r:EvidenceRequest)->None:
    if r.repository_alias!=PROJECT_CONTROL_ALIAS:raise ValueError("repository alias is not allowlisted")
    if r.operation not in ALLOWED_OPERATIONS:raise ValueError("operation is not allowlisted")
    if r.operation is Operation.CONTENT_GET:
        if r.path is None:raise ValueError("content operation requires an explicit path")
        validate_content_path(r.path)
        if not r.ref:raise ValueError("content operation requires an explicit ref")

def _normalize_repository(r:TransportResponse):
    if r.status_code!=200 or not isinstance(r.payload,Mapping):return EvidenceState.UNVERIFIED,None,{"status_code":r.status_code}
    p=dict(r.payload); keys={"id","node_id","full_name","default_branch"}
    if not keys.issubset(p):return EvidenceState.UNVERIFIED,None,{"reason":"repository-required-field-missing"}
    ident={k:p[k] for k in keys}; expected={"id":EXPECTED_REPOSITORY_ID,"node_id":EXPECTED_NODE_ID,"full_name":EXPECTED_REPOSITORY,"default_branch":EXPECTED_DEFAULT_BRANCH}
    return (EvidenceState.VERIFIED,ident,_redact(p)) if ident==expected else (EvidenceState.CONTRADICTORY,ident,_redact(p))

def _normalize_scalar(req:EvidenceRequest,r:TransportResponse,ident):
    if req.operation is Operation.PR_MERGED_CHECK:
        if r.status_code==204:return EvidenceState.VERIFIED,{"merged":True}
        if r.status_code==404 and r.endpoint_supports_absence and _merged_absence_eligible(req):return EvidenceState.VERIFIED,{"merged":False}
        return EvidenceState.UNVERIFIED,{"status_code":r.status_code}
    if r.status_code==404:
        return (EvidenceState.MISSING,{"missing":True}) if r.endpoint_supports_absence and _missing_eligible(req,ident) else (EvidenceState.UNVERIFIED,{"status_code":404,"reason":"ambiguous-not-found"})
    if not 200<=r.status_code<300:return EvidenceState.UNVERIFIED,{"status_code":r.status_code}
    if not isinstance(r.payload,Mapping):return EvidenceState.UNVERIFIED,{"reason":"scalar-payload-not-object"}
    return _normalize_operation_payload(req,dict(r.payload))

def _normalize_operation_payload(req,p):
    if req.operation is Operation.COMMIT_GET:
        sha=p.get("sha")
        if not isinstance(sha,str) or not sha:return EvidenceState.UNVERIFIED,{"reason":"commit-sha-missing"}
        n={"sha":sha}; return (EvidenceState.STALE,n) if req.ref and re.fullmatch(r"[0-9a-fA-F]{40}",req.ref) and sha.lower()!=req.ref.lower() else (EvidenceState.VERIFIED,n)
    if req.operation is Operation.CONTENT_GET:
        if not isinstance(p.get("path"),str) or not isinstance(p.get("sha"),str) or not p["path"] or not p["sha"]:return EvidenceState.UNVERIFIED,{"reason":"content-required-field-missing"}
        path=validate_content_path(p["path"]); n={"path":path,"sha":p["sha"]}
        return (EvidenceState.CONTRADICTORY,n) if path!=validate_content_path(req.path or "") else (EvidenceState.VERIFIED,n)
    if req.operation is Operation.PR_GET:
        if not {"number","state","head","base"}.issubset(p):return EvidenceState.UNVERIFIED,{"reason":"pr-required-field-missing"}
        try:num=int(req.subject)
        except (TypeError,ValueError):return EvidenceState.UNVERIFIED,{"reason":"pr-subject-not-number"}
        if p["number"]!=num:return EvidenceState.CONTRADICTORY,{"number":p["number"]}
        if not isinstance(p["head"],Mapping) or not isinstance(p["base"],Mapping):return EvidenceState.UNVERIFIED,{"reason":"pr-head-base-invalid"}
        head=p["head"].get("sha"); base=p["base"].get("ref")
        if not isinstance(head,str) or not head or not isinstance(base,str) or not base:return EvidenceState.UNVERIFIED,{"reason":"pr-head-base-required-field-missing"}
        n={"number":num,"state":p["state"],"head_sha":head,"base_ref":base}; return (EvidenceState.STALE,n) if req.ref and re.fullmatch(r"[0-9a-fA-F]{40}",req.ref) and head.lower()!=req.ref.lower() else (EvidenceState.VERIFIED,n)
    return EvidenceState.UNVERIFIED,{"reason":"unsupported-scalar-normalizer"}

def _normalize_collection_page(req:EvidenceRequest,payload:Any):
    if not isinstance(payload,list):return EvidenceState.UNVERIFIED,[]
    out=[]
    for raw in payload:
        if not isinstance(raw,Mapping):return EvidenceState.UNVERIFIED,[]
        if req.operation is Operation.PR_COMMITS_LIST:
            sha=raw.get("sha")
            if not isinstance(sha,str) or not sha:return EvidenceState.UNVERIFIED,[]
            out.append({"sha":sha,"evidence_state":EvidenceState.VERIFIED.value})
        elif req.operation is Operation.PR_FILES_LIST:
            fn,st=raw.get("filename"),raw.get("status")
            if not isinstance(fn,str) or not fn or not isinstance(st,str) or not st:return EvidenceState.UNVERIFIED,[]
            out.append({"filename":fn,"status":st,"evidence_state":EvidenceState.VERIFIED.value})
        elif req.operation is Operation.PR_REVIEWS_LIST:
            rid,st,user,cid=raw.get("id"),raw.get("state"),raw.get("user"),raw.get("commit_id")
            if rid is None or not isinstance(st,str) or not isinstance(user,Mapping) or not isinstance(user.get("login"),str) or not isinstance(cid,str) or not cid:return EvidenceState.UNVERIFIED,[]
            item_state=EvidenceState.STALE if req.ref and cid.lower()!=req.ref.lower() else EvidenceState.VERIFIED
            out.append({"id":rid,"state":st,"user_login":user["login"],"commit_id":cid,"evidence_state":item_state.value})
        elif req.operation is Operation.CHECK_RUNS_LIST:
            cid,st,concl,head=raw.get("id"),raw.get("status"),raw.get("conclusion"),raw.get("head_sha")
            if cid is None or not isinstance(st,str) or not isinstance(head,str) or not head:return EvidenceState.UNVERIFIED,[]
            item_state=EvidenceState.STALE if head.lower()!=req.subject.lower() else EvidenceState.VERIFIED
            out.append({"id":cid,"status":st,"conclusion":concl,"head_sha":head,"evidence_state":item_state.value})
        else:return EvidenceState.UNVERIFIED,[]
    return EvidenceState.VERIFIED,out

def _derive_collection_fact(req,items):
    if req.operation is Operation.PR_COMMITS_LIST and req.ref:
        present=req.ref.lower() in {str(i["sha"]).lower() for i in items}
        return {"type":"commit_membership","ref":req.ref,"present":present,"evidence_state":(EvidenceState.VERIFIED if present else EvidenceState.STALE).value}
    if req.operation is Operation.PR_REVIEWS_LIST and req.ref:
        return {"type":"current_head_reviews","ref":req.ref,"current_count":sum(i.get("evidence_state")==EvidenceState.VERIFIED.value for i in items),"historical_count":sum(i.get("evidence_state")==EvidenceState.STALE.value for i in items)}
    if req.operation is Operation.CHECK_RUNS_LIST:
        return {"type":"checks_for_ref","ref":req.subject,"current_count":sum(i.get("evidence_state")==EvidenceState.VERIFIED.value for i in items),"stale_count":sum(i.get("evidence_state")==EvidenceState.STALE.value for i in items)}
    return None

def _missing_eligible(req,ident):
    if ident.get("id")!=EXPECTED_REPOSITORY_ID or ident.get("node_id")!=EXPECTED_NODE_ID:return False
    if req.operation is Operation.CONTENT_GET:return bool(req.ref and req.path and validate_content_path(req.path))
    if req.operation is Operation.COMMIT_GET:return bool(req.subject)
    if req.operation is Operation.PR_GET:
        try:return int(req.subject)>0
        except (TypeError,ValueError):return False
    return False
def _merged_absence_eligible(req):
    try:return req.operation is Operation.PR_MERGED_CHECK and int(req.subject)>0
    except (TypeError,ValueError):return False

def _canonical_hash(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,default=str).encode()).hexdigest()
def _redact(v):
    if isinstance(v,Mapping):
        return {str(k):("[REDACTED]" if str(k).lower() in SECRET_HEADER_NAMES or "token" in str(k).lower() or "secret" in str(k).lower() or "private_key" in str(k).lower() else _redact(x)) for k,x in v.items()}
    if isinstance(v,list):return [_redact(x) for x in v]
    if isinstance(v,tuple):return tuple(_redact(x) for x in v)
    return v
def _record(req,state,cap,complete,payload,ident):
    safe=_redact(payload); ph=_canonical_hash(safe); rid=ident.get("id") if ident else None; node=ident.get("node_id") if ident else None
    audit={"provider":PROVIDER_ID,"repository_alias":req.repository_alias,"repository_id":rid,"repository_node_id":node,"operation":req.operation.value,"subject":req.subject,"ref":req.ref,"github_api_version":GITHUB_API_VERSION,"evidence_state":state.value,"credential_capability":cap.value,"collection_completeness":complete.value if complete else None,"payload_sha256":ph}
    return EvidenceRecord(PROVIDER_ID,req.repository_alias,rid,node,req.operation.value,req.subject,req.ref,GITHUB_API_VERSION,state,cap,complete,safe,ph,audit)
