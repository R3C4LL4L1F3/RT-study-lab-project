from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import unittest

from tools.ai_harness.intake import assemble_intake, build_github_content_requests, evaluate_assembled_v0
from tools.ai_harness.intake.authority import validate_authoritative_field
from tools.ai_harness.intake.schema import AssemblyStatus
from tools.ai_harness.github_readonly.provider import (
    CollectionCompleteness, CredentialCapability, EvidenceRecord, EvidenceState,
)
from tests.ai_harness.common import base_task

ROOT = Path(__file__).resolve().parents[2]


def request(**claims):
    return {
        "intake_schema_version": "1",
        "task": {
            "task_id": {"value": "RTSL-AIH-004", "origin": "USER_SUPPLIED"},
            "title": {"value": "Create architecture task intake", "origin": "USER_SUPPLIED"},
            "description": {"value": "Create deterministic task intake and context assembly.", "origin": "USER_SUPPLIED"},
            "requested_outcome": {"value": "Produce a reproducible task snapshot.", "origin": "USER_SUPPLIED"},
        },
        "governance_claims": claims,
        "references": {"issue_numbers": [9], "source_refs": ["project-control://RTSL-AIH-004/v1.1"], "github_content_requests": []},
    }


def authoritative(field_name, value, *, role="MASTER_PROJECT_CONTROL", source="project-control://RTSL-AIH-004/record", revision="r1", applicable=None):
    result = {"field": field_name, "value": value, "authority_role": role, "source_refs": [source], "source_revision": revision}
    if applicable is not None:
        result["applicable_field"] = applicable
    return result


def evidence(state=EvidenceState.VERIFIED, completeness=None):
    return EvidenceRecord(
        provider="github-readonly-v1", repository_alias="PROJECT_CONTROL", repository_id=1328584202,
        repository_node_id="R_kgDOTzCWCg", operation="GH-OP-PR-REVIEWS-LIST", subject="1", ref="abc",
        api_version="2026-03-10", evidence_state=state, credential_capability=CredentialCapability.VERIFIED_READ_ONLY,
        collection_completeness=completeness, payload={"items": []}, payload_sha256="a" * 64,
        audit={"evidence_state": state.value, "collection_completeness": completeness.value if completeness else None},
    )


class IntakeRegressionTests(unittest.TestCase):
    def assembled(self, raw, records=()):
        return assemble_intake(raw, repo_root=ROOT, evidence=records)["assembled_task_snapshot"]

    # INTAKE-054 through INTAKE-057 / QA-001: proposals never enter V0 authority fields.
    def test_INTAKE_054_proposed_priority_is_not_projected(self):
        result = self.assembled(request(priority_candidate={"value": "P2", "status": "PROPOSED"}))
        self.assertNotIn("priority", result["canonical_payload"]["v0_projection"]["task"])

    def test_INTAKE_055_unverified_risk_fails_closed(self):
        result = self.assembled(request(risk_tier={"value": "TIER_2", "status": "UNVERIFIED"}))
        self.assertTrue(result["canonical_payload"]["v0_projection"]["fail_closed"])

    def test_INTAKE_056_contradictory_value_stays_out_of_v0(self):
        raw = request()
        raw["authoritative_facts"] = [authoritative("priority", "P1"), authoritative("priority", "P2")]
        result = self.assembled(raw)
        self.assertIn("priority", result["canonical_payload"]["contradictions"])
        self.assertNotIn("priority", result["canonical_payload"]["v0_projection"]["task"])

    def test_INTAKE_057_proposal_remains_visible(self):
        result = self.assembled(request(priority={"value": "P2", "origin": "DETERMINISTIC_DERIVATION", "status": "PROPOSED"}))
        self.assertIn("priority", result["canonical_payload"]["proposals"])

    # INTAKE-058 through INTAKE-063 / QA-002.
    def test_INTAKE_058_role_label_alone_does_not_authenticate(self):
        self.assertNotEqual(validate_authoritative_field("priority", {"value": "P2", "authority_role": "MASTER_PROJECT_CONTROL"})["status"], "AUTHORITATIVE")

    def test_INTAKE_059_wrong_domain_is_rejected(self):
        self.assertNotEqual(validate_authoritative_field("priority", authoritative("priority", "P2", role="QA_REGRESSION_RELEASE", source="qa://record"))["status"], "AUTHORITATIVE")

    def test_INTAKE_060_malformed_source_is_rejected(self):
        self.assertNotEqual(validate_authoritative_field("priority", authoritative("priority", "P2", source="MASTER said so"))["status"], "AUTHORITATIVE")

    def test_INTAKE_061_user_claim_cannot_self_authenticate(self):
        raw = request(priority={"value": "P1", "authority_role": "MASTER_PROJECT_CONTROL", "source_refs": ["user-supplied"]})
        result = self.assembled(raw)
        self.assertNotEqual(result["canonical_payload"]["assembled_fields"]["priority"]["status"], "AUTHORITATIVE")

    def test_INTAKE_062_valid_authority_is_accepted(self):
        raw = request(); raw["authoritative_facts"] = [authoritative("priority", "P2")]
        self.assertEqual(self.assembled(raw)["canonical_payload"]["assembled_fields"]["priority"]["status"], "AUTHORITATIVE")

    def test_INTAKE_063_authoritative_conflict_fails_closed(self):
        raw = request(); raw["authoritative_facts"] = [authoritative("priority", "P1"), authoritative("priority", "P2")]
        self.assertEqual(self.assembled(raw)["canonical_payload"]["assembled_fields"]["priority"]["status"], "CONTRADICTORY")

    # INTAKE-064 through INTAKE-070 / QA-003.
    def test_INTAKE_064_authoritative_clinical_disposition_is_preserved(self):
        raw = request(); raw["authoritative_facts"] = [authoritative("clinical_disposition", "PASS", role="CLINICAL_VALIDATION_AND_SOURCES", source="clinical://validation/1")]
        self.assertEqual(self.assembled(raw)["canonical_payload"]["assembled_fields"]["clinical_disposition"]["status"], "AUTHORITATIVE")

    def test_INTAKE_065_clinical_sources_do_not_create_disposition(self):
        raw = request(risk_tier={"value": "TIER_3", "status": "AUTHORITATIVE"}); raw["references"]["source_refs"].append("clinical://guideline/1")
        self.assertIn("MISSING_CLINICAL_AUTHORITY", [x["category"] for x in self.assembled(raw)["canonical_payload"]["missing_context"]])

    def test_INTAKE_066_user_clinical_claim_is_not_authority(self):
        result = self.assembled(request(clinical_disposition={"value": "PASS", "status": "PROPOSED"}))
        self.assertNotEqual(result["canonical_payload"]["assembled_fields"]["clinical_disposition"]["status"], "AUTHORITATIVE")

    def test_INTAKE_067_github_success_does_not_create_clinical_authority(self):
        raw = request(risk_tier={"value": "TIER_3", "status": "AUTHORITATIVE"})
        self.assertIn("MISSING_CLINICAL_AUTHORITY", [x["category"] for x in self.assembled(raw, [evidence()])["canonical_payload"]["missing_context"]])

    def test_INTAKE_068_conflicting_clinical_records_fail_closed(self):
        raw = request(); raw["authoritative_facts"] = [authoritative("clinical_disposition", "PASS", role="CLINICAL_VALIDATION_AND_SOURCES", source="clinical://1"), authoritative("clinical_disposition", "FAIL", role="CLINICAL_VALIDATION_AND_SOURCES", source="clinical://2")]
        self.assertEqual(self.assembled(raw)["canonical_payload"]["assembled_fields"]["clinical_disposition"]["status"], "CONTRADICTORY")

    def test_INTAKE_069_authoritative_clinical_input_is_consumable(self):
        raw = request(); raw["authoritative_facts"] = [authoritative("clinical_disposition", "PASS", role="CLINICAL_VALIDATION_AND_SOURCES", source="clinical://1")]
        self.assertEqual(self.assembled(raw)["canonical_payload"]["assembled_fields"]["clinical_disposition"]["value"], "PASS")

    def test_INTAKE_070_no_clinical_inference_operation_exists(self):
        raw = request(); raw["references"]["source_refs"].append("clinical://guideline/1")
        self.assertNotIn("clinical_disposition", self.assembled(raw)["canonical_payload"]["assembled_fields"])

    # INTAKE-071 through INTAKE-073 / GH-001.
    def test_INTAKE_071_issue_number_is_provenance_only(self):
        result = self.assembled(request())
        self.assertEqual(result["canonical_payload"]["references"]["issue_numbers"][0]["retrieval_authorized"], False)

    def test_INTAKE_072_issue_number_cannot_synthesize_evidence(self):
        self.assertEqual(self.assembled(request())["canonical_payload"]["evidence_snapshot"], [])

    def test_INTAKE_073_implicit_issue_retrieval_is_unavailable(self):
        self.assertEqual(build_github_content_requests(request()), [])

    # INTAKE-074 through INTAKE-079 / GH-002.
    def test_INTAKE_074_collection_state_is_independent(self):
        item = self.assembled(request(), [evidence(EvidenceState.VERIFIED, CollectionCompleteness.INCOMPLETE)])["canonical_payload"]["evidence_snapshot"][0]
        self.assertEqual(item["original_evidence_state"], "VERIFIED")
        self.assertEqual(item["collection_completeness"], "INCOMPLETE")

    def test_INTAKE_075_incomplete_collection_cannot_prove_absence(self):
        item = self.assembled(request(), [evidence(EvidenceState.UNVERIFIED, CollectionCompleteness.INCOMPLETE)])["canonical_payload"]["evidence_snapshot"][0]
        self.assertNotEqual(item["collection_completeness"], "COMPLETE")

    def test_INTAKE_076_unverified_collection_cannot_prove_exhaustiveness(self):
        item = self.assembled(request(), [evidence(EvidenceState.VERIFIED, CollectionCompleteness.UNVERIFIED)])["canonical_payload"]["evidence_snapshot"][0]
        self.assertEqual(item["collection_completeness"], "UNVERIFIED")

    def test_INTAKE_077_positive_observation_survives_partial_collection(self):
        item = self.assembled(request(), [evidence(EvidenceState.VERIFIED, CollectionCompleteness.INCOMPLETE)])["canonical_payload"]["evidence_snapshot"][0]
        self.assertEqual(item["original_evidence_state"], "VERIFIED")

    def test_INTAKE_078_complete_collection_is_preserved(self):
        item = self.assembled(request(), [evidence(EvidenceState.VERIFIED, CollectionCompleteness.COMPLETE)])["canonical_payload"]["evidence_snapshot"][0]
        self.assertEqual(item["collection_completeness"], "COMPLETE")

    def test_INTAKE_079_missing_collection_completeness_is_explicit(self):
        item = self.assembled(request(), [evidence()])["canonical_payload"]["evidence_snapshot"][0]
        self.assertIsNone(item["collection_completeness"])

    # INTAKE-080 through INTAKE-085 / GH-003.
    def test_INTAKE_080_source_ref_does_not_create_github_request(self):
        self.assertEqual(build_github_content_requests(request()), [])

    def test_INTAKE_081_explicit_content_request_routes_to_ai_h002(self):
        raw = request(); raw["references"]["github_content_requests"] = [{"repository_alias": "PROJECT_CONTROL", "ref": "a" * 40, "path": "docs/ai-harness/SCHEMA.md", "requested_fact": "schema"}]
        self.assertEqual(build_github_content_requests(raw)[0].operation.value, "GH-OP-CONTENT-GET")

    def test_INTAKE_082_unapproved_path_is_rejected(self):
        raw = request(); raw["references"]["github_content_requests"] = [{"repository_alias": "PROJECT_CONTROL", "ref": "a" * 40, "path": "private/file", "requested_fact": "x"}]
        with self.assertRaises(ValueError): build_github_content_requests(raw)

    def test_INTAKE_083_aih004_path_is_not_implicitly_authorized(self):
        raw = request(); raw["references"]["github_content_requests"] = [{"repository_alias": "PROJECT_CONTROL", "ref": "a" * 40, "path": "ai-harness/RTSL-AIH-004/x", "requested_fact": "x"}]
        with self.assertRaises(ValueError): build_github_content_requests(raw)

    def test_INTAKE_084_github_like_source_ref_is_not_request(self):
        raw = request(); raw["references"]["source_refs"] = ["github://repo/path"]
        self.assertEqual(build_github_content_requests(raw), [])

    def test_INTAKE_085_traversal_and_wildcard_remain_rejected(self):
        for path in ("docs/ai-harness/../SCHEMA.md", "docs/ai-harness/**"):
            raw = request(); raw["references"]["github_content_requests"] = [{"repository_alias": "PROJECT_CONTROL", "ref": "a" * 40, "path": path, "requested_fact": "x"}]
            with self.assertRaises(ValueError): build_github_content_requests(raw)

    def test_canonical_hash_excludes_run_metadata_and_is_reproducible(self):
        raw = request(); first = self.assembled(raw); second = self.assembled(raw)
        self.assertEqual(first["deterministic_hash"]["value"], second["deterministic_hash"]["value"])

    def test_input_is_not_mutated(self):
        raw = request(); before = deepcopy(raw); self.assembled(raw); self.assertEqual(raw, before)

    def test_v0_integration_reuses_existing_evidence_and_final_recheck(self):
        raw = request(); raw["authoritative_facts"] = [
            authoritative("priority", "P1"),
            authoritative("risk_tier", "TIER_1"),
            authoritative("work_state", "IN_PROGRESS"),
            authoritative("owner", "PLANNING_ARCHITECTURE"),
        ]
        result = evaluate_assembled_v0(self.assembled(raw), evidence=[], repo_root=ROOT)
        self.assertTrue(result["final_policy_recheck"]["performed"])

    def test_human_projection_exposes_origin_status_and_gates(self):
        raw = request(); raw["authoritative_facts"] = [authoritative("risk_tier", "TIER_2")]
        result = self.assembled(raw)
        human = result["human_readable_projection"]
        self.assertIn("Origin: USER_SUPPLIED", human)
        self.assertIn("Status: AUTHORITATIVE", human)
        self.assertIn("CLINICAL_EVIDENCE: required, pending", human)

    def test_proposed_risk_produces_proposed_gate_candidates(self):
        result = self.assembled(request(risk_tier={"value": "TIER_2", "status": "PROPOSED"}))
        gates = result["canonical_payload"]["gates"]
        self.assertEqual(gates["status"], "PROPOSED")
        self.assertTrue(gates["fail_closed"])
        self.assertEqual(gates["gates"][0]["obligation"]["status"], "PROPOSED")

    def test_v0_integration_rejects_non_authoritative_copy(self):
        with self.assertRaises(Exception):
            evaluate_assembled_v0(self.assembled(request()), base_task(), evidence=[], repo_root=ROOT)


if __name__ == "__main__":
    unittest.main()
