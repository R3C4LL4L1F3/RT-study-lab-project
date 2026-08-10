from __future__ import annotations

from copy import deepcopy
import unittest

from tests.ai_harness.common import ROOT, base_task
from tools.ai_harness.github_readonly.integration import (
    evaluate_snapshot_with_evidence,
    record_evidence_ref,
)
from tools.ai_harness.github_readonly.provider import (
    EvidenceRequest, EvidenceState, FixtureTransport, GitHubReadOnlyEvidenceProvider,
    Operation, PROJECT_CONTROL_ALIAS, StaticCredentialSource, TransportResponse,
)

READ={"metadata":"read","contents":"read","pull_requests":"read","checks":"read"}
REPO={"id":1328584202,"node_id":"R_kgDOTzCWCg","full_name":"R3C4LL4L1F3/RT-study-lab-project","default_branch":"main"}

def repository_evidence():
    provider=GitHubReadOnlyEvidenceProvider(StaticCredentialSource(READ),FixtureTransport([TransportResponse(200,REPO)]))
    return provider.retrieve(EvidenceRequest(PROJECT_CONTROL_ALIAS,Operation.REPO_GET,"repository"))

def confirmed_defect_task(evidence_ref:str):
    task=base_task()
    task["findings"]=[{
        "finding_id":"S1-INTEGRATION-DEFECT",
        "type":"CONFIRMED_DEFECT",
        "evidence":{
            "evidence_refs":[evidence_ref],
            "produced_by":{"actor_id":"github-provider","actor_type":"VERIFIED_TOOL","authority_role":None},
        },
        "classification":{
            "decision":"CONFIRMED_DEFECT",
            "classified_by":{"actor_id":"independent-qa","actor_type":"HUMAN","authority_role":"QA_REGRESSION_RELEASE"},
        },
    }]
    return task

class GitHubEvidenceIntegrationTests(unittest.TestCase):
    def test_S1_INTEGRATION_001_evidence_is_bound_before_v0_and_final_recheck(self):
        evidence=repository_evidence(); token=record_evidence_ref(evidence); task=confirmed_defect_task(token)
        result=evaluate_snapshot_with_evidence(task,evidence=[evidence],repo_root=ROOT)
        self.assertTrue(result["evidence_binding"]["performed_before_deterministic_evaluation"])
        self.assertTrue(result["final_policy_recheck"]["performed"])
        self.assertTrue(result["final_policy_recheck"]["passed"])
        r071=[r for r in result["deterministic_findings"] if r["rule_id"]=="AIH-V0-R071"]
        self.assertEqual(r071[0]["status"],"PASS")

    def test_S1_INTEGRATION_002_missing_normalized_evidence_changes_existing_v0_requirement(self):
        evidence=repository_evidence(); token=record_evidence_ref(evidence); task=confirmed_defect_task(token)
        result=evaluate_snapshot_with_evidence(task,evidence=[],repo_root=ROOT)
        r071=[r for r in result["deterministic_findings"] if r["rule_id"]=="AIH-V0-R071"]
        self.assertEqual(r071[0]["status"],"FAIL")
        self.assertEqual(result["deterministic_status"],"INCOMPLETE")
        self.assertTrue(result["final_policy_recheck"]["performed"])
        self.assertTrue(result["final_policy_recheck"]["passed"])

    def test_S1_INTEGRATION_003_non_github_evidence_authority_is_not_filtered(self):
        task=confirmed_defect_task("clinical:authoritative-record-1")
        result=evaluate_snapshot_with_evidence(task,evidence=[],repo_root=ROOT)
        r071=[r for r in result["deterministic_findings"] if r["rule_id"]=="AIH-V0-R071"]
        self.assertEqual(r071[0]["status"],"PASS")

    def test_S1_INTEGRATION_004_input_task_not_mutated(self):
        evidence=repository_evidence(); task=confirmed_defect_task(record_evidence_ref(evidence)); before=deepcopy(task)
        evaluate_snapshot_with_evidence(task,evidence=[evidence],repo_root=ROOT)
        self.assertEqual(task,before)

if __name__=="__main__":unittest.main()
