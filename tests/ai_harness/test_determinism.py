import unittest
from tools.ai_harness.evaluator import evaluate_snapshot
from tests.ai_harness.common import ROOT, base_task

class DeterminismTests(unittest.TestCase):
    def test_same_snapshot_same_hash_and_findings(self):
        a=evaluate_snapshot(base_task(),repo_root=ROOT); b=evaluate_snapshot(base_task(),repo_root=ROOT)
        self.assertEqual(a['deterministic_result_sha256'],b['deterministic_result_sha256']); self.assertEqual(a['deterministic_findings'],b['deterministic_findings'])
    def test_input_key_order_irrelevant(self):
        t=base_task(); u={k:t[k] for k in reversed(list(t.keys()))}; a=evaluate_snapshot(t,repo_root=ROOT); b=evaluate_snapshot(u,repo_root=ROOT); self.assertEqual(a['input_sha256'],b['input_sha256'])
    def test_findings_hash_explicit_and_reproducible(self):
        a=evaluate_snapshot(base_task(),repo_root=ROOT); b=evaluate_snapshot(base_task(),repo_root=ROOT)
        self.assertEqual(a['deterministic_findings_sha256'],b['deterministic_findings_sha256']); self.assertEqual(a['audit_record']['deterministic_findings_sha256'],a['deterministic_findings_sha256'])
    def test_audit_preserves_evaluation_timestamp(self):
        r=evaluate_snapshot(base_task(),repo_root=ROOT); self.assertRegex(r['audit_record']['evaluated_at'],r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$')
if __name__=='__main__': unittest.main()
