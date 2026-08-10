from __future__ import annotations

import unittest

from tests.ai_harness.common import ROOT, base_task
from tools.ai_harness.github_readonly.integration import evaluate_snapshot_with_evidence
from tools.ai_harness.github_readonly.provider import (
    EvidenceRequest,
    EvidenceState,
    FixtureTransport,
    GitHubReadOnlyEvidenceProvider,
    Operation,
    PROJECT_CONTROL_ALIAS,
    StaticCredentialSource,
    TransportResponse,
)

READ = {"metadata":"read","contents":"read","pull_requests":"read","checks":"read"}
REPO = {"id":1328584202,"node_id":"R_kgDOTzCWCg","full_name":"R3C4LL4L1F3/RT-study-lab-project","default_branch":"main"}


class GitHubEvidenceIntegrationTests(unittest.TestCase):
    def test_S1_INTEGRATION_001_normalized_evidence_preserves_v0_final_recheck(self):
        provider = GitHubReadOnlyEvidenceProvider(
            StaticCredentialSource(READ),
            FixtureTransport([TransportResponse(200, REPO)]),
        )
        evidence = provider.retrieve(EvidenceRequest(PROJECT_CONTROL_ALIAS, Operation.REPO_GET, "repository"))
        self.assertEqual(evidence.evidence_state, EvidenceState.VERIFIED)

        result = evaluate_snapshot_with_evidence(base_task(), evidence=[evidence], repo_root=ROOT)
        self.assertTrue(result["final_policy_recheck"]["performed"])
        self.assertTrue(result["final_policy_recheck"]["passed"])
        self.assertEqual(result["evidence_provenance"][0]["evidence_state"], "VERIFIED")

    def test_S1_INTEGRATION_002_evidence_does_not_mutate_v0_snapshot(self):
        task = base_task()
        before = repr(task)
        provider = GitHubReadOnlyEvidenceProvider(
            StaticCredentialSource(READ),
            FixtureTransport([TransportResponse(200, REPO)]),
        )
        evidence = provider.retrieve(EvidenceRequest(PROJECT_CONTROL_ALIAS, Operation.REPO_GET, "repository"))
        evaluate_snapshot_with_evidence(task, evidence=[evidence], repo_root=ROOT)
        self.assertEqual(repr(task), before)


if __name__ == "__main__":
    unittest.main()
