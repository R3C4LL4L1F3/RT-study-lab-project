import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from tests.ai_harness.common import base_task
from tools.ai_harness.cli import run


class CliTests(unittest.TestCase):
    def test_evaluate_cli_local(self):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); inp=td/'task.json'; out=td/'out'; inp.write_text(json.dumps(base_task()),encoding='utf-8')
            code=run(['evaluate',str(inp),'--output-dir',str(out)])
            self.assertEqual(code,0); self.assertTrue((out/'evaluation.json').is_file()); self.assertTrue((out/'audit.json').is_file()); self.assertEqual(json.loads(inp.read_text())['task_id'],'FIX-001')

    def test_policy_recheck_failure_returns_5_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); inp=td/'task.json'; out=td/'out'; inp.write_text(json.dumps(base_task()),encoding='utf-8')
            fake={'final_policy_recheck':{'performed':True,'passed':False,'problems':['corrupt']}}
            with patch('tools.ai_harness.cli.evaluate_snapshot', return_value=fake):
                code=run(['evaluate',str(inp),'--output-dir',str(out)])
            self.assertEqual(code,5); self.assertFalse(out.exists())

    def test_output_cannot_overwrite_input_snapshot(self):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); out=td/'out'; out.mkdir(); inp=out/'evaluation.json'; inp.write_text(json.dumps(base_task()),encoding='utf-8'); original=inp.read_text()
            code=run(['evaluate',str(inp),'--output-dir',str(out)])
            self.assertEqual(code,2); self.assertEqual(inp.read_text(),original); self.assertFalse((out/'audit.json').exists())

    def test_QA_005_existing_evaluation_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); inp=td/'task.json'; out=td/'out'; out.mkdir(); inp.write_text(json.dumps(base_task()),encoding='utf-8')
            existing=out/'evaluation.json'; existing.write_text('KEEP',encoding='utf-8')
            code=run(['evaluate',str(inp),'--output-dir',str(out)])
            self.assertEqual(code,2); self.assertEqual(existing.read_text(encoding='utf-8'),'KEEP'); self.assertFalse((out/'audit.json').exists())

    def test_QA_005_existing_audit_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); inp=td/'task.json'; out=td/'out'; out.mkdir(); inp.write_text(json.dumps(base_task()),encoding='utf-8')
            existing=out/'audit.json'; existing.write_text('KEEP-AUDIT',encoding='utf-8')
            code=run(['evaluate',str(inp),'--output-dir',str(out)])
            self.assertEqual(code,2); self.assertEqual(existing.read_text(encoding='utf-8'),'KEEP-AUDIT'); self.assertFalse((out/'evaluation.json').exists())


if __name__=='__main__': unittest.main()
