"""Validate scaffold links and coverage, not OpenROAD correctness."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    rules = json.loads((root/'rules/manifest.json').read_text())
    ids = [r['id'] for r in rules]
    assert len(ids) == len(set(ids)), 'Duplicate rule ID'
    core = (root/'OPENROAD.md').read_text()
    for rule in rules:
        rid, case = rule['id'], rule['case']
        assert re.fullmatch(r'OR-[A-Z]+-\d{3}', rid), rid
        assert f'rules/{rid}.md' in core, rid
        for path in [f'rules/{rid}.md', f'tests/compliance/probes/{rid}.md', f'tests/agent/cases/{case}.json', f'tests/agent/rubrics/{case}.json']:
            assert (root/path).is_file(), path
        rubric = json.loads((root/f'tests/agent/rubrics/{case}.json').read_text())
        assert rubric['rule'] == rid
        if rule['status'] == 'verified':
            assert rule['evidence'], f'{rid}: verified without evidence'
            for relative in rule['evidence']:
                assert (root/relative).is_file(), relative
    for path in (root/'guide_tests').glob('*.w4gl'):
        assert len(path.stem) <= 32, path.name
        assert '===' in path.read_text(), path.name
    return len(rules)

if __name__ == '__main__':
    print(f'{validate()} rule mappings validated. Native execution remains unverified.')
