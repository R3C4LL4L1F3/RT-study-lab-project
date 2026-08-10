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
    def test_required_pass_without_authority_disposition_fails_closed(self):
        task=base_task(); task['risk_tier']='TIER_2'; task['gates']=[
            {'gate_id':'CLINICAL_EVIDENCE','obligation':{'required':True,'origin':{'type':'RISK_TIER','ref':'TIER_2'}},'execution':{'state':'PASS'},'authority':{'owner_role':'CLINICAL_VALIDATION_SOURCES'},'disposition':{'decision':None,'actor':None,'evidence_refs':[]}},
            {'gate_id':'INDEPENDENT_REVIEW','obligation':{'required':True,'origin':{'type':'RISK_TIER','ref':'TIER_2'}},'execution':{'state':'REQUIRED_PENDING'},'authority':{'owner_role':'QA_REGRESSION_RELEASE'},'disposition':{'decision':None,'actor':None,'evidence_refs':[]}},
            {'gate_id':'QA','obligation':{'required':True,'origin':{'type':'RISK_TIER','ref':'TIER_2'}},'execution':{'state':'REQUIRED_PENDING'},'authority':{'owner_role':'QA_REGRESSION_RELEASE'},'disposition':{'decision':None,'actor':None,'evidence_refs':[]}},
            {'gate_id':'GITHUB_PROVENANCE','obligation':{'required':True,'origin':{'type':'RISK_TIER','ref':'TIER_2'}},'execution':{'state':'REQUIRED_PENDING'},'authority':{'owner_role':'GITHUB_PR_DOCUMENTATION'},'disposition':{'decision':None,'actor':None,'evidence_refs':[]}},
        ]
        r=evaluate_snapshot(task,repo_root=ROOT); failed={f['rule_id'] for f in r['deterministic_findings'] if f['status']=='FAIL'}; self.assertIn('AIH-V0-R030',failed)
    def test_clinical_pass_requires_evidence_reference(self):
        task=base_task(); task['risk_tier']='TIER_2'; task['gates']=[
            {'gate_id':'CLINICAL_EVIDENCE','obligation':{'required':True,'origin':{'type':'RISK_TIER','ref':'TIER_2'}},'execution':{'state':'PASS'},'authority':{'owner_role':'CLINICAL_VALIDATION_SOURCES'},'disposition':{'decision':'PASS','actor':{'actor_id':'CLIN-1','actor_type':'HUMAN','authority_role':'CLINICAL_VALIDATION_SOURCES'},'evidence_refs':[]}},
            {'gate_id':'INDEPENDENT_REVIEW','obligation':{'required':True,'origin':{'type':'RISK_TIER','ref':'TIER_2'}},'execution':{'state':'REQUIRED_PENDING'},'authority':{'owner_role':'QA_REGRESSION_RELEASE'},'disposition':{'decision':None,'actor':None,'evidence_refs':[]}},
            {'gate_id':'QA','obligation':{'required':True,'origin':{'type':'RISK_TIER','ref':'TIER_2'}},'execution':{'state':'REQUIRED_PENDING'},'authority':{'owner_role':'QA_REGRESSION_RELEASE'},'disposition':{'decision':None,'actor':None,'evidence_refs':[]}},
            {'gate_id':'GITHUB_PROVENANCE','obligation':{'required':True,'origin':{'type':'RISK_TIER','ref':'TIER_2'}},'execution':{'state':'REQUIRED_PENDING'},'authority':{'owner_role':'GITHUB_PR_DOCUMENTATION'},'disposition':{'decision':None,'actor':None,'evidence_refs':[]}},
        ]
        r=evaluate_snapshot(task,repo_root=ROOT); r030=[f for f in r['deterministic_findings'] if f['rule_id']=='AIH-V0-R030'][0]; self.assertEqual(r030['status'],'FAIL'); self.assertIn('evidence reference',r030['reason'])
if __name__=='__main__': unittest.main()
