import unittest
from tools.ai_harness.evaluator import evaluate_snapshot
from tests.ai_harness.common import ROOT, base_task

class FindingTests(unittest.TestCase):
    def test_validation_gap_stays_gap(self):
        t=base_task(); t['findings']=[{'finding_id':'F-1','type':'VALIDATION_GAP','summary':'manual QA pending'}]
        r=evaluate_snapshot(t,repo_root=ROOT); passed={f['rule_id'] for f in r['deterministic_findings'] if f['status']=='PASS'}; self.assertIn('AIH-V0-R070',passed)
    def test_tool_evidence_without_classifier_incomplete(self):
        t=base_task(); t['findings']=[{'finding_id':'F-2','type':'CONFIRMED_DEFECT','summary':'test failure','evidence':{'evidence_refs':['TEST-1'],'produced_by':{'actor_id':'TOOL-1','actor_type':'VERIFIED_TOOL','authority_role':None},'evidence_status':'VERIFIED'},'classification':None}]
        r=evaluate_snapshot(t,repo_root=ROOT); self.assertEqual(r['deterministic_status'],'INCOMPLETE')
    def test_authorized_qa_classification(self):
        t=base_task(); t['findings']=[{'finding_id':'F-3','type':'CONFIRMED_DEFECT','summary':'confirmed','evidence':{'evidence_refs':['TEST-1'],'produced_by':{'actor_id':'TOOL-1','actor_type':'VERIFIED_TOOL','authority_role':None},'evidence_status':'VERIFIED'},'classification':{'decision':'CONFIRMED_DEFECT','classified_by':{'actor_id':'QA-1','actor_type':'HUMAN','authority_role':'QA_REGRESSION_RELEASE'},'classification_basis':'reviewed','classified_at':'2026-08-10T19:00:00Z'}}]
        r=evaluate_snapshot(t,repo_root=ROOT); failed={f['rule_id'] for f in r['deterministic_findings'] if f['status']=='FAIL'}; self.assertNotIn('AIH-V0-R073',failed); self.assertNotIn('AIH-V0-R074',failed)
if __name__=='__main__': unittest.main()
