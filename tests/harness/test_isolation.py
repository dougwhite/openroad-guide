import importlib.util
from pathlib import Path
import shutil
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('evaluate', ROOT/'tools/evaluate.py')
evaluate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaluate)

class IsolationTests(unittest.TestCase):
    def test_baseline_has_only_task(self):
        workspace = evaluate.prepare('baseline', 'C001')
        self.addCleanup(shutil.rmtree, workspace)
        self.assertEqual(['TASK.md'], sorted(p.name for p in workspace.iterdir()))
        self.assertFalse(workspace.is_relative_to(ROOT))

    def test_guided_has_articles_without_hidden_rubrics(self):
        workspace = evaluate.prepare('guided', 'C001', True)
        self.addCleanup(shutil.rmtree, workspace)
        self.assertTrue((workspace/'.llm/OPENROAD.md').is_file())
        self.assertTrue((workspace/'.llm/rules/OR-NAME-001.md').is_file())
        self.assertFalse(any('rubric' in str(p) or p.name == 'manifest.json' for p in workspace.rglob('*')))

    def test_candidates_block_normal_guided_run(self):
        with self.assertRaises(ValueError):
            evaluate.prepare('guided', 'C001')

    def test_unknown_case_rejected(self):
        with self.assertRaises(ValueError):
            evaluate.prepare('baseline', '../rules/manifest')

if __name__ == '__main__':
    unittest.main()
