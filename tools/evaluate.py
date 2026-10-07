"""Manual Codex evaluation preparation; no model calls or automated grading."""
import argparse
import json
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def prepare(mode, case_id, allow_candidates=False, root=ROOT):
    cases = root / 'tests/agent/cases'
    known = {p.stem for p in cases.glob('*.json')}
    if case_id not in known:
        raise ValueError('Unknown case')
    if mode not in ('baseline', 'guided'):
        raise ValueError('Unknown mode')
    manifest = json.loads((root/'rules/manifest.json').read_text())
    if mode == 'guided' and not allow_candidates:
        if any(r['status'] != 'verified' for r in manifest):
            raise ValueError('Guide has candidates; establish native evidence first or use --allow-candidates for a pilot')
    case = json.loads((cases/f'{case_id}.json').read_text())
    workspace = Path(tempfile.mkdtemp(prefix='or-eval-'))
    try:
        for relative, content in case['files'].items():
            destination = workspace/relative
            if not destination.resolve().is_relative_to(workspace.resolve()):
                raise ValueError('Case file escapes workspace')
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content)
        (workspace/'TASK.md').write_text(case['task']+'\n')
        if mode == 'guided':
            guide = workspace/'.llm'
            guide.mkdir()
            shutil.copyfile(root/'OPENROAD.md', guide/'OPENROAD.md')
            (guide/'rules').mkdir()
            for article in (root/'rules').glob('OR-*.md'):
                shutil.copyfile(article, guide/'rules'/article.name)
            (workspace/'AGENTS.md').write_text('Read .llm/OPENROAD.md before answering TASK.md. Consult linked articles when needed. Record any article consulted in your answer.\n')
        return workspace
    except Exception:
        shutil.rmtree(workspace)
        raise

def report(path):
    result = json.loads(Path(path).read_text())
    print('| Model | Case | Before | After | Guide tokens | Articles read |')
    print('|---|---|---:|---:|---:|---|')
    for trial in result['trials']:
        values = [result['model'], trial['case'], trial.get('baseline_score'), trial.get('guided_score'), trial.get('guide_tokens_added'), trial.get('extended_articles_read')]
        print('| '+' | '.join('unknown' if v is None else str(v).replace('|','\\|') for v in values)+' |')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    prep = commands.add_parser('prepare')
    prep.add_argument('mode', choices=['baseline','guided'])
    prep.add_argument('case')
    prep.add_argument('--allow-candidates', action='store_true')
    view = commands.add_parser('report')
    view.add_argument('result')
    args = parser.parse_args()
    try:
        if args.command == 'prepare':
            print(prepare(args.mode, args.case, args.allow_candidates))
        else:
            report(args.result)
    except (ValueError, OSError) as exc:
        parser.exit(2, str(exc)+'\n')

if __name__ == '__main__':
    main()
