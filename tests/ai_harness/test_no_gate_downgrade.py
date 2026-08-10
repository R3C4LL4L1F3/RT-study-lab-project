import unittest
from tools.ai_harness.evaluator import evaluate_snapshot
from tests.ai_harness.common import ROOT, base_task

class NoGateDowngradeTests(unittest.TestCase):
    def test_required_gate_not_not_required(self):
        t=base_task(); t['gates']=[{'gate_id':'QA','obligation':{'required':True,'origin':{'type':'ESTABLISHED_REQUIREMENT','ref':'QA-REQ'}},'execution':{'state':'NOT_REQUIRED'},'authority':{'owner_role':'QA_REGRESSION_RELEASE'},'disposition':{'decision':None,'actor':None,'evidence_refs':[]}}]
        r=evaluate_snapshot(t,repo_root=ROOT); failed={f['rule_id'] for f in r['deterministic_findings'] if f['status']=='FAIL'}; self.assertIn('AIH-V0-R040',failed)
    def test_risk_downgrade_preserves_established_gate(self):
        t=base_task(); t['gates']=[{'gate_id':'QA','obligation':{'required':False,'origin':{'type':'PRIOR_RISK_TIER','ref':'TIER_3'}},'execution':{'state':'NOT_REQUIRED'},'authority':{'owner_role':'QA_REGRESSION_RELEASE'},'disposition':{'decision':None,'actor':None,'evidence_refs':[]}}]
        r=evaluate_snapshot(t,repo_root=ROOT); failed={f['rule_id'] for f in r['deterministic_findings'] if f['status']=='FAIL'}; self.assertIn('AIH-V0-R041',failed)
if __name__=='__main__': unittest.main()
