from __future__ import annotations

import unittest

from tools.ai_harness.evaluator import evaluate_snapshot
from tests.ai_harness.common import ROOT, base_task


PROFILE = "RTSL-KERNEL-AUTONOMY-001-CONTROLLED"
CONTRACT_REF = "project-control://RTSL-KERNEL-AUTONOMY-001/contract"


def actor(actor_id: str, role: str) -> dict[str, str]:
    return {"actor_id": actor_id, "actor_type": "HUMAN", "authority_role": role}


def gate(
    gate_id: str,
    *,
    required: bool = True,
    state: str = "PASS",
    owner: str,
    implementation_actor: str | None = None,
    origin: dict[str, str] | None = None,
    evidence_refs: list[str] | None = None,
) -> dict:
    gate_actor = None
    if state == "PASS":
        gate_actor = actor(implementation_actor or f"{gate_id}-ACTOR", owner)
    return {
        "gate_id": gate_id,
        "obligation": {
            "required": required,
            "origin": origin or {"type": "RISK_TIER", "ref": "TIER_2"},
        },
        "execution": {"state": state},
        "authority": {"owner_role": owner},
        "disposition": {
            "decision": "PASS" if state == "PASS" else None,
            "actor": gate_actor,
            "evidence_refs": evidence_refs or (["CLINICAL-REF"] if gate_id == "CLINICAL_EVIDENCE" and state == "PASS" else []),
        },
    }


def tier2_complete_gates(*, independent_required: bool, independent_required_state: str = "PASS") -> list[dict]:
    result = [
        gate("CLINICAL_EVIDENCE", owner="CLINICAL_VALIDATION_SOURCES"),
        gate("IMPLEMENTATION", owner="PLANNING_ARCHITECTURE", implementation_actor="IMPL-1"),
        gate("QA", owner="QA_REGRESSION_RELEASE", implementation_actor="QA-1"),
        gate("GITHUB_PROVENANCE", owner="GITHUB_PR_DOCUMENTATION"),
    ]
    if independent_required:
        result.append(gate("INDEPENDENT_REVIEW", owner="QA_REGRESSION_RELEASE", implementation_actor="QA-1", state=independent_required_state))
    return result


def conditional_governance(decision: str = "NOT_REQUIRED") -> dict:
    return {
        "pr_state": "OPEN",
        "handoff_required": False,
        "independent_review": {
            "decision": decision,
            "basis": "AUTHORITATIVE_CONTRACT",
            "contract_ref": CONTRACT_REF,
            "contract_revision": "autonomy-contract-r1",
            "authority": actor("MASTER-1", "MASTER_PROJECT_CONTROL"),
        },
    }


class AutonomyGoldenScenarioTests(unittest.TestCase):
    def evaluate(self, task: dict, **kwargs):
        return evaluate_snapshot(task, repo_root=ROOT, governance_profile=PROFILE, **kwargs)

    # AUTONOMY-001: preparation does not change the current default evaluator profile.
    def test_AUTONOMY_001_default_profile_is_current_kernel(self):
        result = evaluate_snapshot(base_task(), repo_root=ROOT)
        self.assertNotIn("governance_profile", result)
        self.assertTrue(result["final_policy_recheck"]["passed"])
        direct_completion = base_task()
        direct_completion.update({"work_state": "IN_VALIDATION", "requested_transition": "COMPLETE"})
        current_result = evaluate_snapshot(direct_completion, repo_root=ROOT)
        self.assertFalse(current_result["recommendation"]["requested_transition_permitted"])

    # AUTONOMY-002: Tier 1 may use self-validation when no independent gate exists.
    def test_AUTONOMY_002_tier1_self_validation_sufficient(self):
        result = self.evaluate(base_task())
        self.assertEqual(result["deterministic_status"], "VALID")
        self.assertTrue(result["recommendation"]["requested_transition_permitted"])
        self.assertEqual(next(x for x in result["deterministic_findings"] if x["rule_id"] == "AIH-V0-R063")["status"], "NOT_APPLICABLE")

    # AUTONOMY-003: an explicit low-risk independent gate remains enforceable.
    def test_AUTONOMY_003_explicit_tier1_independent_gate_is_required(self):
        task = base_task()
        task["gates"] = [
            gate("IMPLEMENTATION", owner="PLANNING_ARCHITECTURE", implementation_actor="IMPL-1"),
            gate("INDEPENDENT_REVIEW", owner="QA_REGRESSION_RELEASE", implementation_actor="REVIEW-1"),
        ]
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "VALID")
        self.assertEqual(next(x for x in result["deterministic_findings"] if x["rule_id"] == "AIH-V0-R063")["status"], "PASS")

    # AUTONOMY-004: Tier 2 cannot silently remove independence without a contract.
    def test_AUTONOMY_004_tier2_missing_contract_fails_closed(self):
        task = base_task()
        task.update({"risk_tier": "TIER_2", "gates": [gate("INDEPENDENT_REVIEW", required=False, state="NOT_REQUIRED", owner="QA_REGRESSION_RELEASE")]})
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "INCOMPLETE")
        self.assertFalse(result["recommendation"]["requested_transition_permitted"])

    # AUTONOMY-005: Tier 2 can be NOT_REQUIRED only through an authoritative contract.
    def test_AUTONOMY_005_tier2_authoritative_contract_allows_not_required(self):
        task = base_task()
        task.update({"risk_tier": "TIER_2", "governance": conditional_governance(), "gates": tier2_complete_gates(independent_required=False) + [gate("INDEPENDENT_REVIEW", required=False, state="NOT_REQUIRED", owner="QA_REGRESSION_RELEASE", origin={"type": "CONDITIONAL_CONTRACT", "ref": CONTRACT_REF, "authority_role": "MASTER_PROJECT_CONTROL"})]})
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "VALID")
        self.assertTrue(result["recommendation"]["requested_transition_permitted"])
        self.assertEqual(next(x for x in result["deterministic_findings"] if x["rule_id"] == "AIH-V0-R062")["status"], "PASS")

    # AUTONOMY-006: an authoritative Tier 2 REQUIRED decision retains the gate.
    def test_AUTONOMY_006_tier2_required_contract_retains_independent_gate(self):
        task = base_task()
        task.update({"risk_tier": "TIER_2", "governance": conditional_governance("REQUIRED"), "gates": tier2_complete_gates(independent_required=True)})
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "VALID")
        self.assertEqual(next(x for x in result["deterministic_findings"] if x["rule_id"] == "AIH-V0-R063")["status"], "PASS")

    # AUTONOMY-007: a claimed conditional exception with the wrong gate origin fails closed.
    def test_AUTONOMY_007_unverified_conditional_exception_fails_closed(self):
        task = base_task()
        task.update({"risk_tier": "TIER_2", "governance": conditional_governance(), "gates": tier2_complete_gates(independent_required=False) + [gate("INDEPENDENT_REVIEW", required=False, state="NOT_REQUIRED", owner="QA_REGRESSION_RELEASE")]})
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "INCOMPLETE")
        self.assertFalse(result["recommendation"]["requested_transition_permitted"])

    # AUTONOMY-008: Tier 3 independence remains mandatory.
    def test_AUTONOMY_008_tier3_not_required_is_rejected(self):
        task = base_task()
        task.update({"risk_tier": "TIER_3", "gates": [gate("CLINICAL_EVIDENCE", owner="CLINICAL_VALIDATION_SOURCES"), gate("ARCHITECTURE", owner="PLANNING_ARCHITECTURE"), gate("QA", owner="QA_REGRESSION_RELEASE", implementation_actor="QA-1"), gate("GITHUB_PROVENANCE", owner="GITHUB_PR_DOCUMENTATION"), gate("INDEPENDENT_REVIEW", required=False, state="NOT_REQUIRED", owner="QA_REGRESSION_RELEASE")]})
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "INCOMPLETE")
        self.assertFalse(result["recommendation"]["requested_transition_permitted"])

    # AUTONOMY-009: Tier 3 independent reviewer identity must differ from implementation.
    def test_AUTONOMY_009_tier3_independent_identity_is_distinct(self):
        task = base_task()
        task.update({"risk_tier": "TIER_3", "work_state": "IN_VALIDATION", "requested_transition": "COMPLETE", "gates": [gate("CLINICAL_EVIDENCE", owner="CLINICAL_VALIDATION_SOURCES"), gate("ARCHITECTURE", owner="PLANNING_ARCHITECTURE"), gate("IMPLEMENTATION", owner="PLANNING_ARCHITECTURE", implementation_actor="IMPL-1"), gate("INDEPENDENT_REVIEW", owner="QA_REGRESSION_RELEASE", implementation_actor="REVIEW-1"), gate("QA", owner="QA_REGRESSION_RELEASE", implementation_actor="QA-1"), gate("GITHUB_PROVENANCE", owner="GITHUB_PR_DOCUMENTATION")]})
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "VALID")
        self.assertTrue(result["recommendation"]["requested_transition_permitted"])

    # AUTONOMY-010: prior established requirements cannot be erased.
    def test_AUTONOMY_010_no_gate_downgrade_remains_enforced(self):
        task = base_task()
        task.update({"risk_tier": "TIER_2", "gates": [gate("INDEPENDENT_REVIEW", required=False, state="NOT_REQUIRED", owner="QA_REGRESSION_RELEASE", origin={"type": "PRIOR_RISK_TIER", "ref": "TIER_3"})]})
        result = self.evaluate(task)
        self.assertEqual(next(x for x in result["deterministic_findings"] if x["rule_id"] == "AIH-V0-R041")["status"], "FAIL")

    # AUTONOMY-011: the Harness cannot become a gate authority by actor input.
    def test_AUTONOMY_011_unauthorized_gate_owner_fails(self):
        task = base_task()
        task["gates"] = [gate("QA", owner="AI_HARNESS", implementation_actor="QA-1")]
        result = self.evaluate(task)
        self.assertEqual(next(x for x in result["deterministic_findings"] if x["rule_id"] == "AIH-V0-R064")["status"], "FAIL")

    # AUTONOMY-012: bounded tasks may complete directly from validation when no release gate exists.
    def test_AUTONOMY_012_bounded_direct_completion_is_legal(self):
        task = base_task()
        task.update({"work_state": "IN_VALIDATION", "requested_transition": "COMPLETE"})
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "VALID")
        self.assertTrue(result["recommendation"]["requested_transition_permitted"])

    # AUTONOMY-013: project release/closure cannot hide behind bounded completion.
    def test_AUTONOMY_013_project_release_requires_release_gate(self):
        task = base_task()
        task.update({"work_state": "IN_VALIDATION", "requested_transition": "COMPLETE", "completion_scope": "PROJECT_RELEASE", "gates": [gate("RELEASE", state="REQUIRED_PENDING", owner="MASTER_PROJECT_CONTROL")]})
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "INCOMPLETE")
        self.assertFalse(result["recommendation"]["requested_transition_permitted"])

    # AUTONOMY-014: PR_OPEN and handoff/approval/merge authority stay separate.
    def test_AUTONOMY_014_pr_open_does_not_imply_handoff(self):
        task = base_task()
        task["governance"] = {"pr_state": "OPEN", "handoff_required": False}
        result = self.evaluate(task)
        self.assertEqual(result["deterministic_status"], "VALID")
        self.assertFalse(task["governance"]["handoff_required"])

    # AUTONOMY-015: exact PAUSED and BLOCKED resume contracts remain required.
    def test_AUTONOMY_015_paused_and_blocked_require_exact_evidence(self):
        paused = base_task()
        paused.update({"work_state": "PAUSED", "requested_transition": "READY", "pause": {"reason": "resource", "resume_condition": "resource restored", "previous_state": "READY", "resume_condition_satisfied": True, "resume_evidence_refs": ["EVID-PAUSE"]}})
        blocked = base_task()
        blocked.update({"work_state": "BLOCKED", "requested_transition": "READY", "blocker": {"description": "dependency", "owner": "MASTER_PROJECT_CONTROL", "unblock_condition": "dependency resolved", "previous_state": "READY", "unblock_condition_satisfied": True, "unblock_evidence_refs": ["EVID-BLOCK"]}})
        self.assertTrue(self.evaluate(paused)["recommendation"]["requested_transition_permitted"])
        self.assertTrue(self.evaluate(blocked)["recommendation"]["requested_transition_permitted"])

    # AUTONOMY-016: the final deterministic recheck still rejects a corrupted recommendation.
    def test_AUTONOMY_016_final_recheck_remains_mandatory(self):
        task = base_task()
        task.update({"work_state": "READY", "requested_transition": "COMPLETE"})
        result = self.evaluate(task, corrupt_candidate_for_test=True)
        self.assertTrue(result["final_policy_recheck"]["performed"])
        self.assertFalse(result["final_policy_recheck"]["passed"])


if __name__ == "__main__":
    unittest.main()
