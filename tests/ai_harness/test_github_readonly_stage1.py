from __future__ import annotations

import inspect
import unittest

from tools.ai_harness.github_readonly.provider import (
    ALLOWED_OPERATIONS,
    COLLECTION_OPERATIONS,
    CollectionCompleteness,
    CredentialCapability,
    DisabledEvidenceProvider,
    EvidenceRequest,
    EvidenceState,
    FixtureTransport,
    GITHUB_API_VERSION,
    GitHubReadOnlyEvidenceProvider,
    Operation,
    PROJECT_CONTROL_ALIAS,
    StaticCredentialSource,
    TransportResponse,
    resolve_evidence_state,
    validate_content_path,
    validate_permission_manifest,
)


def req(op: Operation, *, subject: str = "subject", ref: str | None = None, path: str | None = None, states=(), absence_eligible: bool = False):
    return EvidenceRequest(PROJECT_CONTROL_ALIAS, op, subject, ref=ref, path=path, observed_states=tuple(states), absence_eligible=absence_eligible)


def provider(*responses: TransportResponse, capability=CredentialCapability.VERIFIED_READ_ONLY, headers=None):
    transport = FixtureTransport(responses)
    credentials = StaticCredentialSource(capability, headers=headers)
    return GitHubReadOnlyEvidenceProvider(credentials, transport), transport


class GitHubGoldenTests(unittest.TestCase):
    def test_GH_001_provider_contract_retrieves_normalized_record(self):
        p, _ = provider(TransportResponse(200, {"id": 1328584202}))
        r = p.retrieve(req(Operation.REPO_GET))
        self.assertEqual(r.evidence_state, EvidenceState.VERIFIED)
        self.assertEqual(r.operation, Operation.REPO_GET.value)

    def test_GH_002_repository_alias_allowlist_fails_closed(self):
        p, _ = provider(TransportResponse(200, {}))
        with self.assertRaises(ValueError):
            p.retrieve(EvidenceRequest("OTHER", Operation.REPO_GET, "repo"))

    def test_GH_003_operation_allowlist_is_frozen(self):
        self.assertEqual(len(ALLOWED_OPERATIONS), 9)

    def test_GH_004_content_allowlist_accepts_aih001(self):
        self.assertEqual(validate_content_path("ai-harness/RTSL-AIH-001/x.md"), "ai-harness/RTSL-AIH-001/x.md")

    def test_GH_005_content_allowlist_accepts_aih002(self):
        self.assertEqual(validate_content_path("ai-harness/RTSL-AIH-002/x.md"), "ai-harness/RTSL-AIH-002/x.md")

    def test_GH_006_content_allowlist_accepts_docs(self):
        self.assertEqual(validate_content_path("docs/ai-harness/x.md"), "docs/ai-harness/x.md")

    def test_GH_007_content_allowlist_accepts_config(self):
        self.assertEqual(validate_content_path("config/ai_harness/x.json"), "config/ai_harness/x.json")

    def test_GH_008_content_allowlist_rejects_arbitrary_path(self):
        with self.assertRaises(ValueError): validate_content_path("README.md")

    def test_GH_009_content_allowlist_rejects_plain_traversal(self):
        with self.assertRaises(ValueError): validate_content_path("docs/ai-harness/../README.md")

    def test_GH_010_content_allowlist_rejects_encoded_traversal(self):
        with self.assertRaises(ValueError): validate_content_path("docs/ai-harness/%2e%2e/README.md")

    def test_GH_011_content_allowlist_rejects_absolute_path(self):
        with self.assertRaises(ValueError): validate_content_path("/docs/ai-harness/x")

    def test_GH_012_content_operation_requires_explicit_ref(self):
        p, _ = provider(TransportResponse(200, {}))
        with self.assertRaises(ValueError): p.retrieve(req(Operation.CONTENT_GET, path="docs/ai-harness/x.md"))

    def test_GH_013_disabled_provider_is_offline_unverified(self):
        r = DisabledEvidenceProvider().retrieve(req(Operation.REPO_GET))
        self.assertEqual(r.evidence_state, EvidenceState.UNVERIFIED)
        self.assertFalse(DisabledEvidenceProvider.enabled)

    def test_GH_014_not_configured_fails_preflight_without_transport(self):
        p, t = provider(TransportResponse(200, {}), capability=CredentialCapability.NOT_CONFIGURED)
        r = p.retrieve(req(Operation.REPO_GET))
        self.assertEqual(r.evidence_state, EvidenceState.UNVERIFIED)
        self.assertEqual(t.calls, [])

    def test_GH_015_unverified_fails_preflight_without_transport(self):
        p, t = provider(TransportResponse(200, {}), capability=CredentialCapability.UNVERIFIED)
        self.assertEqual(p.retrieve(req(Operation.REPO_GET)).credential_capability, CredentialCapability.UNVERIFIED)
        self.assertEqual(t.calls, [])

    def test_GH_016_invalid_fails_preflight_without_transport(self):
        p, t = provider(TransportResponse(200, {}), capability=CredentialCapability.INVALID)
        self.assertEqual(p.retrieve(req(Operation.REPO_GET)).evidence_state, EvidenceState.UNVERIFIED)
        self.assertEqual(t.calls, [])

    def test_GH_017_overprivileged_fails_preflight_without_transport(self):
        p, t = provider(TransportResponse(200, {}), capability=CredentialCapability.OVERPRIVILEGED)
        self.assertEqual(p.retrieve(req(Operation.REPO_GET)).credential_capability, CredentialCapability.OVERPRIVILEGED)
        self.assertEqual(t.calls, [])

    def test_GH_018_permission_manifest_accepts_exact_read_ceiling(self):
        perms = {"metadata":"read","contents":"read","pull_requests":"read","checks":"read"}
        self.assertEqual(validate_permission_manifest(perms), CredentialCapability.VERIFIED_READ_ONLY)

    def test_GH_019_permission_manifest_rejects_write(self):
        perms = {"metadata":"read","contents":"write","pull_requests":"read","checks":"read"}
        self.assertEqual(validate_permission_manifest(perms), CredentialCapability.OVERPRIVILEGED)

    def test_GH_020_permission_manifest_missing_capabilities_is_unverified(self):
        self.assertEqual(validate_permission_manifest({"metadata":"read"}), CredentialCapability.UNVERIFIED)

    def test_GH_021_transport_is_get_only(self):
        t = FixtureTransport([])
        with self.assertRaises(PermissionError): t.request("POST")

    def test_GH_022_provider_exposes_no_mutation_methods(self):
        names = {n.lower() for n, _ in inspect.getmembers(GitHubReadOnlyEvidenceProvider, inspect.isfunction)}
        forbidden = {"create","update","delete","merge","comment","push","release","dispatch","rerun"}
        self.assertTrue(forbidden.isdisjoint(names))

    def test_GH_023_api_version_is_pinned(self):
        self.assertEqual(GITHUB_API_VERSION, "2026-03-10")

    def test_GH_024_transport_call_records_no_secret_values(self):
        p, t = provider(TransportResponse(200, {}), headers={"Authorization":"Bearer SUPERSECRET"})
        p.retrieve(req(Operation.REPO_GET))
        self.assertNotIn("SUPERSECRET", repr(t.calls))

    def test_GH_025_evidence_payload_redacts_secret_keys(self):
        p, _ = provider(TransportResponse(200, {"token":"SUPERSECRET", "ok": True}))
        r = p.retrieve(req(Operation.REPO_GET))
        self.assertNotIn("SUPERSECRET", repr(r))
        self.assertEqual(r.payload["token"], "[REDACTED]")

    def test_GH_026_audit_contains_required_provenance(self):
        p, _ = provider(TransportResponse(200, {}))
        a = p.retrieve(req(Operation.REPO_GET)).audit
        for key in ("provider","repository_alias","repository_id","repository_node_id","operation","subject","github_api_version","evidence_state","credential_capability","payload_sha256"):
            self.assertIn(key, a)

    def test_GH_027_audit_contains_no_authorization_header(self):
        p, _ = provider(TransportResponse(200, {}), headers={"Authorization":"Bearer SUPERSECRET"})
        self.assertNotIn("SUPERSECRET", repr(p.retrieve(req(Operation.REPO_GET)).audit))

    def test_GH_028_successful_scalar_is_verified(self):
        p, _ = provider(TransportResponse(200, {"sha":"abc"}))
        self.assertEqual(p.retrieve(req(Operation.COMMIT_GET)).evidence_state, EvidenceState.VERIFIED)

    def test_GH_029_non404_error_is_unverified(self):
        p, _ = provider(TransportResponse(403, {"message":"forbidden"}))
        self.assertEqual(p.retrieve(req(Operation.REPO_GET)).evidence_state, EvidenceState.UNVERIFIED)

    def test_GH_030_collection_operation_set_is_exact(self):
        self.assertEqual(COLLECTION_OPERATIONS, {Operation.PR_COMMITS_LIST, Operation.PR_FILES_LIST, Operation.PR_REVIEWS_LIST, Operation.CHECK_RUNS_LIST})

    def test_GH_031_ambiguous_404_is_unverified(self):
        p, _ = provider(TransportResponse(404, endpoint_supports_absence=False))
        self.assertEqual(p.retrieve(req(Operation.CONTENT_GET, ref="abc", path="docs/ai-harness/x.md")).evidence_state, EvidenceState.UNVERIFIED)

    def test_GH_032_eligible_authoritative_404_is_missing(self):
        p, _ = provider(TransportResponse(404, endpoint_supports_absence=True))
        self.assertEqual(p.retrieve(req(Operation.CONTENT_GET, ref="abc", path="docs/ai-harness/x.md", absence_eligible=True)).evidence_state, EvidenceState.MISSING)

    def test_GH_033_merged_check_204_means_verified_true(self):
        p, _ = provider(TransportResponse(204, endpoint_supports_absence=True))
        r = p.retrieve(req(Operation.PR_MERGED_CHECK))
        self.assertEqual((r.evidence_state, r.payload), (EvidenceState.VERIFIED, {"merged": True}))

    def test_GH_034_merged_check_404_means_verified_false_only_when_eligible(self):
        p, _ = provider(TransportResponse(404, endpoint_supports_absence=True))
        r = p.retrieve(req(Operation.PR_MERGED_CHECK, absence_eligible=True))
        self.assertEqual((r.evidence_state, r.payload), (EvidenceState.VERIFIED, {"merged": False}))

    def test_GH_035_evidence_precedence_is_deterministic(self):
        self.assertEqual(resolve_evidence_state([EvidenceState.VERIFIED, EvidenceState.MISSING, EvidenceState.STALE, EvidenceState.UNVERIFIED, EvidenceState.CONTRADICTORY]), EvidenceState.CONTRADICTORY)

    def test_GH_036_unverified_precedes_missing(self):
        self.assertEqual(resolve_evidence_state([EvidenceState.MISSING, EvidenceState.UNVERIFIED]), EvidenceState.UNVERIFIED)

    def test_GH_037_stale_precedes_missing(self):
        self.assertEqual(resolve_evidence_state([EvidenceState.MISSING, EvidenceState.STALE]), EvidenceState.STALE)

    def test_GH_038_complete_paginated_collection_is_exhaustive(self):
        p, t = provider(TransportResponse(200, [1,2], next_page=2), TransportResponse(200, [3], next_page=None))
        r = p.retrieve(req(Operation.PR_FILES_LIST))
        self.assertEqual(r.collection_completeness, CollectionCompleteness.COMPLETE)
        self.assertEqual(r.payload, {"items":[1,2,3], "exhaustive":True})
        self.assertEqual(len(t.calls), 2)

    def test_GH_039_incomplete_collection_cannot_establish_absence(self):
        p, _ = provider(TransportResponse(200, [1], next_page=2), TransportResponse(500, None))
        r = p.retrieve(req(Operation.PR_REVIEWS_LIST))
        self.assertEqual(r.collection_completeness, CollectionCompleteness.INCOMPLETE)
        self.assertEqual(r.evidence_state, EvidenceState.UNVERIFIED)
        self.assertEqual(r.payload["items"], [1])
        self.assertNotIn("exhaustive", r.payload)

    def test_GH_040_observed_contradiction_survives_successful_retrieval(self):
        p, _ = provider(TransportResponse(200, {"ok":True}))
        r = p.retrieve(req(Operation.REPO_GET, states=(EvidenceState.CONTRADICTORY,)))
        self.assertEqual(r.evidence_state, EvidenceState.CONTRADICTORY)


class NegativeCapabilityTests(unittest.TestCase):
    def test_write_methods_are_absent_and_non_get_transport_fails_before_response(self):
        p, t = provider()
        for name in ("create", "update", "delete", "merge", "comment", "review", "rerun", "dispatch", "push", "release"):
            self.assertFalse(hasattr(p, name))
        for method in ("POST", "PUT", "PATCH", "DELETE"):
            with self.assertRaises(PermissionError): t.request(method)

    def test_provider_disabled_never_calls_transport(self):
        disabled = DisabledEvidenceProvider()
        r = disabled.retrieve(req(Operation.CHECK_RUNS_LIST))
        self.assertEqual(r.collection_completeness, CollectionCompleteness.UNVERIFIED)
        self.assertEqual(r.evidence_state, EvidenceState.UNVERIFIED)

    def test_secret_leakage_is_blocked_from_evidence_and_audit(self):
        p, t = provider(TransportResponse(200, {"authorization":"Bearer LEAKME", "private_key":"KEY", "nested":{"secret":"S"}}), headers={"Authorization":"Bearer REQUESTSECRET"})
        r = p.retrieve(req(Operation.REPO_GET))
        combined = repr((r, t.calls))
        for secret in ("LEAKME", "KEY", "REQUESTSECRET"):
            self.assertNotIn(secret, combined)


if __name__ == "__main__":
    unittest.main()
