import unittest
from tools.ai_harness.evaluator import evaluate_snapshot
from tests.ai_harness.common import ROOT, base_task, load_fixture

class StateContractTests(unittest.TestCase):
    def test_paused_missing_reason_invalid(self):
        r=evaluate_snapshot(load_fixture('invalid','FIX-002-paused-missing-reason.json'),repo_root=ROOT)
        self.assertEqual(r['deterministic_status'],'INVALID')
    def test_blocked_missing_owner_invalid(self):
        t=base_task(); t.update({'work_state':'BLOCKED','requested_transition':'READY','blocker':{'description':'dependency','unblock_condition':'dependency resolved','previous_state':'READY'}})
        r=evaluate_snapshot(t,repo_root=ROOT); self.assertEqual(r['deterministic_status'],'INVALID')
    def test_valid_blocked_resume(self):
        t=base_task(); t.update({'work_state':'BLOCKED','requested_transition':'READY','blocker':{'description':'dependency','owner':'MASTER_PROJECT_CONTROL','unblock_condition':'dependency resolved','previous_state':'READY'}})
        r=evaluate_snapshot(t,repo_root=ROOT); self.assertTrue(r['recommendation']['requested_transition_permitted'])
if __name__=='__main__': unittest.main()
