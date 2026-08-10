import unittest
from tools.ai_harness.schemas import load_config
from tools.ai_harness.transitions import transition_enumerated, resume_target_valid
from tests.ai_harness.common import ROOT, base_task


class TransitionTests(unittest.TestCase):
    def setUp(self): self.config=load_config(ROOT)

    def test_every_frozen_transition_enumerated(self):
        for current,targets in self.config.transitions["transitions"].items():
            for target in targets:
                task=base_task(); task["work_state"]=current
                if current=='PAUSED': task['pause']={'reason':'x','resume_condition':'x','previous_state':'READY'}
                if current=='BLOCKED': task['blocker']={'description':'x','owner':'MASTER_PROJECT_CONTROL','unblock_condition':'x','previous_state':'READY'}
                self.assertTrue(transition_enumerated(task,target,self.config.transitions))

    def test_forbidden_ready_to_complete(self):
        task=base_task(); self.assertFalse(transition_enumerated(task,'COMPLETE',self.config.transitions))

    def test_paused_resume_previous_state(self):
        task=base_task(); task.update({'work_state':'PAUSED','pause':{'reason':'q','resume_condition':'r','previous_state':'READY','resume_condition_satisfied':True,'resume_evidence_refs':['EVID-1']}})
        self.assertTrue(resume_target_valid(task,'READY',self.config.transitions)); self.assertFalse(resume_target_valid(task,'IN_VALIDATION',self.config.transitions))

    def test_terminal_no_transitions(self): self.assertEqual(self.config.transitions['transitions']['COMPLETE'],[])


if __name__=='__main__': unittest.main()
