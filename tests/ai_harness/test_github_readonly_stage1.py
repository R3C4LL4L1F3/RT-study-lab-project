from __future__ import annotations

import inspect
import unittest

from tools.ai_harness.github_readonly.provider import (
    CollectionCompleteness, CredentialCapability, DisabledEvidenceProvider,
    EvidenceRequest, EvidenceState, FixtureTransport, GitHubReadOnlyEvidenceProvider,
    Operation, PROJECT_CONTROL_ALIAS, StaticCredentialSource, TransportResponse,
    resolve_evidence_state, validate_content_path, validate_permission_manifest,
)

READ={"metadata":"read","contents":"read","pull_requests":"read","checks":"read"}
REPO={"id":1328584202,"node_id":"R_kgDOTzCWCg","full_name":"R3C4LL4L1F3/RT-study-lab-project","default_branch":"main"}
def req(op,subject="1",ref=None,path=None):return EvidenceRequest(PROJECT_CONTROL_ALIAS,op,subject,ref=ref,path=path)
def provider(*responses,manifest=READ,headers=None):
    t=FixtureTransport(responses); return GitHubReadOnlyEvidenceProvider(StaticCredentialSource(manifest,headers=headers),t),t
def with_repo(*responses):return (TransportResponse(200,REPO),*responses)

class FrozenGoldenContract(unittest.TestCase):
    def test_GH_001_repository_identity_verified(self):
        p,_=provider(*with_repo()); self.assertEqual(p.retrieve(req(Operation.REPO_GET)).evidence_state,EvidenceState.VERIFIED)
    def test_GH_002_repository_allowlist_rejects_other_alias(self):
        p,_=provider(*with_repo())
        with self.assertRaises(ValueError):p.retrieve(EvidenceRequest("OTHER",Operation.REPO_GET,"repo"))
    def test_GH_003_repository_identity_mismatch_is_contradictory(self):
        p,_=provider(TransportResponse(200,{**REPO,"id":999})); r=p.retrieve(req(Operation.REPO_GET)); self.assertEqual(r.evidence_state,EvidenceState.CONTRADICTORY); self.assertEqual(r.repository_id,999)
    def test_GH_004_commit_found_verified(self):
        p,_=provider(*with_repo(TransportResponse(200,{"sha":"a"*40}))); self.assertEqual(p.retrieve(req(Operation.COMMIT_GET,"a"*40,ref="a"*40)).evidence_state,EvidenceState.VERIFIED)
    def test_GH_005_commit_absent_missing_only_after_preflight(self):
        p,_=provider(*with_repo(TransportResponse(404,endpoint_supports_absence=True))); self.assertEqual(p.retrieve(req(Operation.COMMIT_GET,"deadbeef")).evidence_state,EvidenceState.MISSING)
    def test_GH_006_permission_failure_unverified(self):
        p,t=provider(*with_repo(),manifest={"metadata":"read","contents":"none","pull_requests":"read","checks":"read"}); r=p.retrieve(req(Operation.REPO_GET)); self.assertEqual(r.evidence_state,EvidenceState.UNVERIFIED); self.assertEqual(t.calls,[])
    def test_GH_007_explicit_file_verified(self):
        path="docs/ai-harness/x.md"; p,_=provider(*with_repo(TransportResponse(200,{"path":path,"sha":"b"*40}))); self.assertEqual(p.retrieve(req(Operation.CONTENT_GET,"file",ref="a"*40,path=path)).evidence_state,EvidenceState.VERIFIED)
    def test_GH_008_disallowed_path_rejected(self):
        p,_=provider(*with_repo())
        with self.assertRaises(ValueError):p.retrieve(req(Operation.CONTENT_GET,"file",ref="a"*40,path="README.md"))
    def test_GH_009_current_pr_head_verified(self):
        sha="c"*40; payload={"number":22,"state":"open","head":{"sha":sha},"base":{"ref":"main"}}; p,_=provider(*with_repo(TransportResponse(200,payload))); self.assertEqual(p.retrieve(req(Operation.PR_GET,"22",ref=sha)).evidence_state,EvidenceState.VERIFIED)
    def test_GH_010_changed_pr_head_is_stale(self):
        payload={"number":22,"state":"open","head":{"sha":"d"*40},"base":{"ref":"main"}}; p,_=provider(*with_repo(TransportResponse(200,payload))); self.assertEqual(p.retrieve(req(Operation.PR_GET,"22",ref="c"*40)).evidence_state,EvidenceState.STALE)
    def test_GH_011_pr_files_current_complete(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"filename":"x.py","status":"modified"}]))); r=p.retrieve(req(Operation.PR_FILES_LIST,"22")); self.assertEqual((r.evidence_state,r.collection_completeness),(EvidenceState.VERIFIED,CollectionCompleteness.COMPLETE))
    def test_GH_012_pr_commit_membership_current(self):
        sha="e"*40; p,_=provider(*with_repo(TransportResponse(200,[{"sha":sha}]))); r=p.retrieve(req(Operation.PR_COMMITS_LIST,"22",ref=sha)); self.assertEqual(r.evidence_state,EvidenceState.VERIFIED); self.assertEqual(r.payload["derived_fact"]["evidence_state"],"VERIFIED")
    def test_GH_013_pr_review_current_normalized(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"id":1,"state":"APPROVED","user":{"login":"qa"},"commit_id":"e"*40}]))); r=p.retrieve(req(Operation.PR_REVIEWS_LIST,"22",ref="e"*40)); self.assertEqual(r.evidence_state,EvidenceState.VERIFIED); self.assertEqual(r.payload["items"][0]["evidence_state"],"VERIFIED")
    def test_GH_014_pr_commit_membership_old_head_is_derived_fact_not_collection_state(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"sha":"f"*40}]))); r=p.retrieve(req(Operation.PR_COMMITS_LIST,"22",ref="e"*40)); self.assertEqual(r.evidence_state,EvidenceState.VERIFIED); self.assertEqual(r.payload["derived_fact"]["evidence_state"],"STALE")
    def test_GH_015_checks_current_success_fact(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"id":1,"status":"completed","conclusion":"success","head_sha":"a"*40}]))); r=p.retrieve(req(Operation.CHECK_RUNS_LIST,"a"*40)); self.assertEqual(r.evidence_state,EvidenceState.VERIFIED); self.assertEqual(r.payload["items"][0]["evidence_state"],"VERIFIED")
    def test_GH_016_checks_old_head_preserves_stale_item_not_stale_collection(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"id":1,"status":"completed","conclusion":"success","head_sha":"a"*40}]))); r=p.retrieve(req(Operation.CHECK_RUNS_LIST,"old")); self.assertEqual(r.evidence_state,EvidenceState.VERIFIED); self.assertEqual(r.payload["items"][0]["evidence_state"],"STALE")
    def test_GH_017_checks_pending_is_repository_fact(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"id":1,"status":"in_progress","conclusion":None,"head_sha":"sha"}]))); r=p.retrieve(req(Operation.CHECK_RUNS_LIST,"sha")); self.assertEqual(r.payload["items"][0]["status"],"in_progress")
    def test_GH_018_checks_unavailable_unverified(self):
        p,_=provider(*with_repo(TransportResponse(503,{}))); self.assertEqual(p.retrieve(req(Operation.CHECK_RUNS_LIST,"sha")).evidence_state,EvidenceState.UNVERIFIED)
    def test_GH_019_merged_state_read(self):
        p,_=provider(*with_repo(TransportResponse(204))); self.assertEqual(p.retrieve(req(Operation.PR_MERGED_CHECK,"22")).payload,{"merged":True})
    def test_GH_020_provider_has_no_write_methods(self):
        names={n.lower() for n,_ in inspect.getmembers(GitHubReadOnlyEvidenceProvider,inspect.isfunction)}; self.assertTrue({"create","update","delete","merge","comment","push"}.isdisjoint(names))
    def test_GH_021_post_rejected_pre_transport(self):
        with self.assertRaises(PermissionError):FixtureTransport([]).request("POST")
    def test_GH_022_patch_rejected_pre_transport(self):
        with self.assertRaises(PermissionError):FixtureTransport([]).request("PATCH")
    def test_GH_023_delete_rejected_pre_transport(self):
        with self.assertRaises(PermissionError):FixtureTransport([]).request("DELETE")
    def test_GH_024_absent_credential_unverified(self):
        p,t=provider(*with_repo(),manifest=None); self.assertEqual(p.retrieve(req(Operation.REPO_GET)).credential_capability,CredentialCapability.NOT_CONFIGURED); self.assertEqual(t.calls,[])
    def test_GH_025_secret_never_serialized(self):
        p,t=provider(*with_repo(),headers={"Authorization":"Bearer TOPSECRET"}); r=p.retrieve(req(Operation.REPO_GET)); self.assertNotIn("TOPSECRET",repr((r,t.calls)))
    def test_GH_026_provider_absent_offline_v0_boundary(self):self.assertEqual(DisabledEvidenceProvider().retrieve(req(Operation.REPO_GET)).evidence_state,EvidenceState.UNVERIFIED)
    def test_GH_027_review_fact_does_not_encode_qa_pass(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"id":1,"state":"APPROVED","user":{"login":"qa"},"commit_id":"e"*40}]))); self.assertNotIn("qa_pass",repr(p.retrieve(req(Operation.PR_REVIEWS_LIST,"22",ref="e"*40))).lower())
    def test_GH_028_check_success_does_not_encode_qa_pass(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"id":1,"status":"completed","conclusion":"success","head_sha":"sha"}]))); self.assertNotIn("qa_pass",repr(p.retrieve(req(Operation.CHECK_RUNS_LIST,"sha"))).lower())
    def test_GH_029_unknown_reviewer_authority_not_inferred(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"id":1,"state":"APPROVED","user":{"login":"someone"},"commit_id":"e"*40}]))); self.assertNotIn("authority_role",repr(p.retrieve(req(Operation.PR_REVIEWS_LIST,"22",ref="e"*40))))
    def test_GH_030_final_policy_recheck_integration_is_separate_module(self):
        import tools.ai_harness.github_readonly.integration as integration; self.assertTrue(callable(integration.evaluate_snapshot_with_evidence))
    def test_GH_031_ambiguous_404_unverified(self):
        p,_=provider(*with_repo(TransportResponse(404,endpoint_supports_absence=False))); self.assertEqual(p.retrieve(req(Operation.CONTENT_GET,"file",ref="a"*40,path="docs/ai-harness/x.md")).evidence_state,EvidenceState.UNVERIFIED)
    def test_GH_032_authoritative_404_missing_derived_by_provider(self):
        p,_=provider(*with_repo(TransportResponse(404,endpoint_supports_absence=True))); self.assertEqual(p.retrieve(req(Operation.CONTENT_GET,"file",ref="a"*40,path="docs/ai-harness/x.md")).evidence_state,EvidenceState.MISSING)
    def test_GH_033_required_permission_none_is_not_verified_read_only(self):self.assertEqual(validate_permission_manifest({"metadata":"read","contents":"none","pull_requests":"read","checks":"read"}),CredentialCapability.UNVERIFIED)
    def test_GH_034_write_permission_is_overprivileged(self):self.assertEqual(validate_permission_manifest({"metadata":"read","contents":"write","pull_requests":"read","checks":"read"}),CredentialCapability.OVERPRIVILEGED)
    def test_GH_035_precedence_contradictory_highest(self):self.assertEqual(resolve_evidence_state(list(EvidenceState)),EvidenceState.CONTRADICTORY)
    def test_GH_036_precedence_unverified_over_stale_missing_verified(self):self.assertEqual(resolve_evidence_state([EvidenceState.VERIFIED,EvidenceState.MISSING,EvidenceState.STALE,EvidenceState.UNVERIFIED]),EvidenceState.UNVERIFIED)
    def test_GH_037_precedence_stale_over_missing_verified(self):self.assertEqual(resolve_evidence_state([EvidenceState.VERIFIED,EvidenceState.MISSING,EvidenceState.STALE]),EvidenceState.STALE)
    def test_GH_038_incomplete_collection_cannot_claim_exhaustive(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"filename":"x","status":"modified"}],next_page=2),TransportResponse(500,{}))); r=p.retrieve(req(Operation.PR_FILES_LIST,"22")); self.assertEqual(r.collection_completeness,CollectionCompleteness.INCOMPLETE); self.assertNotIn("exhaustive",r.payload)
    def test_GH_039_positive_observation_survives_incomplete_collection(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"id":123,"state":"APPROVED","user":{"login":"qa"},"commit_id":"e"*40}],next_page=2),TransportResponse(500,{}))); r=p.retrieve(req(Operation.PR_REVIEWS_LIST,"22",ref="e"*40)); self.assertEqual(r.payload["items"][0]["id"],123); self.assertEqual(r.payload["items"][0]["evidence_state"],"VERIFIED"); self.assertEqual(r.evidence_state,EvidenceState.UNVERIFIED)
    def test_GH_040_exhausted_error_free_pagination_complete_not_qa_pass(self):
        p,_=provider(*with_repo(TransportResponse(200,[{"filename":"a","status":"modified"}],next_page=2),TransportResponse(200,[{"filename":"b","status":"added"}],next_page=None))); r=p.retrieve(req(Operation.PR_FILES_LIST,"22")); self.assertEqual(r.collection_completeness,CollectionCompleteness.COMPLETE); self.assertTrue(r.payload["exhaustive"]); self.assertNotIn("qa_pass",repr(r).lower())

class AdditionalStructuralTests(unittest.TestCase):
    def test_S1_STRUCT_001_required_operation_set_is_nine(self):
        from tools.ai_harness.github_readonly.provider import ALLOWED_OPERATIONS; self.assertEqual(len(ALLOWED_OPERATIONS),9)
    def test_S1_STRUCT_002_path_traversal_rejected(self):
        for path in ("docs/ai-harness/../x","docs/ai-harness/%2e%2e/x","/docs/ai-harness/x"):
            with self.assertRaises(ValueError):validate_content_path(path)
    def test_S1_STRUCT_003_invalid_scalar_payload_unverified(self):
        p,_=provider(*with_repo(TransportResponse(200,{"number":22}))); self.assertEqual(p.retrieve(req(Operation.PR_GET,"22")).evidence_state,EvidenceState.UNVERIFIED)
    def test_S1_STRUCT_004_mixed_review_history_does_not_stale_collection(self):
        head="e"*40; old="d"*40
        p,_=provider(*with_repo(TransportResponse(200,[{"id":1,"state":"APPROVED","user":{"login":"qa1"},"commit_id":old},{"id":2,"state":"APPROVED","user":{"login":"qa2"},"commit_id":head}])))
        r=p.retrieve(req(Operation.PR_REVIEWS_LIST,"22",ref=head)); self.assertEqual(r.evidence_state,EvidenceState.VERIFIED); self.assertEqual([i["evidence_state"] for i in r.payload["items"]],["STALE","VERIFIED"]); self.assertEqual(r.payload["derived_fact"]["current_count"],1)

if __name__=="__main__":unittest.main()
