import unittest
from tools.ai_harness.evaluator import evaluate_snapshot
from tests.ai_harness.common import ROOT, base_task

class ApprovalTests(unittest.TestCase):
    def test_ai_advisory_not_human_approval(self):
        t=base_task(); t['approvals']=[{'approval_id':'APR-1','approval_type':'MASTER','decision':'APPROVED','actor':{'actor_id':'AI-1','actor_type':'AI_ADVISORY','authority_role':'MASTER_PROJECT_CONTROL'},'scope':'','evidence_ref':'','timestamp':'2026-08-10T19:00:00Z'}]
        r=evaluate_snapshot(t,repo_root=ROOT); failed={f['rule_id'] for f in r['deterministic_findings'] if f['status']=='FAIL'}
        self.assertIn('AIH-V0-R050',failed); self.assertIn('AIH-V0-R051',failed)
    def test_wrong_authority_rejected(self):
        t=base_task(); t['approvals']=[{'approval_id':'APR-1','approval_type':'QA','decision':'APPROVED','actor':{'actor_id':'H-1','actor_type':'HUMAN','authority_role':'PLANNING_ARCHITECTURE'},'scope':'','evidence_ref':'','timestamp':'2026-08-10T19:00:00Z'}]
        r=evaluate_snapshot(t,repo_root=ROOT); failed={f['rule_id'] for f in r['deterministic_findings'] if f['status']=='FAIL'}; self.assertIn('AIH-V0-R052',failed)
    def test_human_approval_cannot_legalize_forbidden(self):
        t=base_task(); t['requested_transition']='COMPLETE'; t['approvals']=[{'approval_id':'APR-1','approval_type':'MASTER','decision':'APPROVED','actor':{'actor_id':'H-1','actor_type':'HUMAN','authority_role':'MASTER_PROJECT_CONTROL'},'scope':'','evidence_ref':'','timestamp':'2026-08-10T19:00:00Z'}]
        r=evaluate_snapshot(t,repo_root=ROOT); self.assertFalse(r['recommendation']['requested_transition_permitted'])
if __name__=='__main__': unittest.main()
