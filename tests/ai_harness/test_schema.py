import unittest
from tools.ai_harness.errors import SchemaError, UnknownKernelError
from tools.ai_harness.schemas import load_config, validate_task
from tests.ai_harness.common import ROOT, base_task

class SchemaTests(unittest.TestCase):
    def setUp(self): self.config = load_config(ROOT)
    def test_valid_tier1(self): self.assertEqual(validate_task(base_task(), self.config)["priority"], "P2")
    def test_unknown_priority_rejected(self):
        task=base_task(); task["priority"]="P4"
        with self.assertRaises(SchemaError): validate_task(task,self.config)
    def test_unknown_gate_state_rejected(self):
        task=base_task(); task["gates"]=[{"gate_id":"QA","obligation":{"required":True,"origin":{"type":"RISK_TIER","ref":"x"}},"execution":{"state":"UNKNOWN"},"authority":{"owner_role":"QA_REGRESSION_RELEASE"},"disposition":{"decision":None,"actor":None,"evidence_refs":[]}}]
        with self.assertRaises(SchemaError): validate_task(task,self.config)
    def test_unknown_kernel_fails_closed(self):
        task=base_task(); task["kernel"]["version_ref"]="UNKNOWN"
        with self.assertRaises(UnknownKernelError): validate_task(task,self.config)
if __name__ == '__main__': unittest.main()
