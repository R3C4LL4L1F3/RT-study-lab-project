import unittest
from tools.ai_harness.evaluator import evaluate_snapshot
from tests.ai_harness.common import ROOT, base_task

class FinalRecheckTests(unittest.TestCase):
    def test_normal_recheck_passes(self):
        r=evaluate_snapshot(base_task(),repo_root=ROOT); self.assertTrue(r['final_policy_recheck']['performed']); self.assertTrue(r['final_policy_recheck']['passed'])
    def test_TEST_AIH_V0_FINAL_RECHECK_001(self):
        t=base_task(); t['requested_transition']='COMPLETE'; r=evaluate_snapshot(t,repo_root=ROOT,corrupt_candidate_for_test=True); self.assertFalse(r['final_policy_recheck']['passed']); self.assertTrue(r['final_policy_recheck']['problems'])
if __name__=='__main__': unittest.main()
