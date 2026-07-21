# Verification

## Quick preview without install
```bash
PYTHONPATH=src python3.11 -m fde_training_lab roadmap
PYTHONPATH=src python3.11 -m fde_training_lab modules
PYTHONPATH=src python3.11 -m fde_training_lab resources
```

## Install
```bash
# If .venv already exists from an older interpreter, move it aside first.
mv .venv .venv-py39-backup 2>/dev/null || true
python3.11 -m venv .venv
source .venv/bin/activate
python3.11 -m pip install -e .
```

## Smoke tests
```bash
python3.11 -m fde_training_lab roadmap
python3.11 -m fde_training_lab modules
python3.11 -m fde_training_lab resources
python3.11 -m fde_training_lab module workflow-audit
python3.11 -m fde_training_lab week 1
python3.11 -m fde_training_lab scorecard
```

## Visual artifact checks
Confirm these render correctly on GitHub / Pages previews:
- `assets/fde-roadmap.svg`
- `assets/fde-proof-stack.svg`
- `docs/visual-roadmap.md`

## Unit tests
```bash
python3.11 -m unittest discover -s tests -v
```
