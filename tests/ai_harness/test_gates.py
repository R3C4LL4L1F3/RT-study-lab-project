import unittest
from tools.ai_harness.evaluator import evaluate_snapshot
from tests.ai_harness.common import ROOT, base_task, load_fixture

class GateTests(unittest.TestCase):
    def test_tier3_complete_with_qa_pending_incomplete(self):
        r=evaluate_snapshot(load_fixture('incomplete','FIX-006-tier3-qa-pending-complete.json'),repo_root=ROOT)
        self.assertEqual(r['deterministic_status'],'INCOMPLETE'); self.assertFalse(r['recommendation']['requested_transition_permitted'])
    def test_complete_with_pending_gate_contradictory(self):
        r=evaluate_snapshot(load_fixture('contradictory','FIX-022-contradictory-complete.json'),repo_root=ROOT)
        self.assertEqual(r['deterministic_status'],'CONTRADICTORY')
    def test_ready_for_release_distinct(self):
        task=base_task(); task.update({'work_state':'IN_VALIDATION','requested_transition':'READY_FOR_RELEASE'})
        r=evaluate_snapshot(task,repo_root=ROOT); self.assertEqual(r['recommendation']['requested_transition'],'READY_FOR_RELEASE')
if __name__=='__main__': unittest.main()
