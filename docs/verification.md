# Verification

## Install
```bash
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

## Unit tests
```bash
python3.11 -m unittest discover -s tests -v
```
