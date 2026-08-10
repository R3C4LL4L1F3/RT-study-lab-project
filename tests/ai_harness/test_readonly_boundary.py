import ast
import unittest
from tools.ai_harness.evaluator import evaluate_snapshot
from tools.ai_harness.github_readonly.contract import GitHubReadOnlyEvidenceAdapter
from tests.ai_harness.common import ROOT, base_task

FORBIDDEN_NAMES={'create_issue','update_issue','add_comment','create_branch','create_commit','push','create_pull_request','merge_pull_request','submit_review','change_label','create_release','change_repository_setting'}
FORBIDDEN_RUNTIME_IMPORTS={'requests','httpx','urllib.request','socket','openai','anthropic','sub'+'process'}

class ReadOnlyBoundaryTests(unittest.TestCase):
    def test_adapter_has_no_mutation_methods(self): self.assertTrue(FORBIDDEN_NAMES.isdisjoint(set(dir(GitHubReadOnlyEvidenceAdapter))))
    def test_no_network_or_process_runtime_imports(self):
        for path in (ROOT/'tools/ai_harness').rglob('*.py'):
            tree=ast.parse(path.read_text(encoding='utf-8')); imported=set()
            for node in ast.walk(tree):
                if isinstance(node,ast.Import): imported.update(a.name for a in node.names)
                elif isinstance(node,ast.ImportFrom) and node.module: imported.add(node.module)
            self.assertTrue(FORBIDDEN_RUNTIME_IMPORTS.isdisjoint(imported),f'{path}: {imported & FORBIDDEN_RUNTIME_IMPORTS}')
    def test_input_not_mutated(self):
        t=base_task(); before=repr(t); evaluate_snapshot(t,repo_root=ROOT); self.assertEqual(repr(t),before)
    def test_duplicate_task_id_deferred(self):
        r=evaluate_snapshot(base_task(),repo_root=ROOT); self.assertNotIn('duplicate_task_id',r)
if __name__=='__main__': unittest.main()
