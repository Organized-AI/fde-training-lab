# FDE Training Lab

A practical codebase and curriculum for training into an AI Forward Deployed Engineer (FDE).

This repo is built around one idea: **do the job before you have the title**.

Instead of treating FDE as a vague trend, this project turns it into a repeatable training loop:
- audit real workflows
- build deployment-grade agent systems
- evaluate reliability and economics
- package the result as business-ready proof

## Who this is for
- builders who already ship software or automation and want to become more customer-facing
- operators who understand workflows and want stronger AI systems fluency
- founders or consultants who want a repeatable FDE-style offer

## What’s in this repo
- a runnable CLI for exploring the roadmap and training modules
- a 30-day and 90-day FDE training plan
- hands-on labs and capstone structure
- workflow audit, eval, and pitch templates
- a rubric for judging whether a project actually looks like FDE work

## Quickstart

```bash
cd fde-training-lab
python3.11 -m venv .venv
source .venv/bin/activate
python3.11 -m pip install -e .
python3.11 -m fde_training_lab roadmap
python3.11 -m fde_training_lab modules
python3.11 -m fde_training_lab week 1
python3.11 -m fde_training_lab module workflow-audit
python3.11 -m fde_training_lab scorecard
```

## CLI commands

```bash
python3.11 -m fde_training_lab roadmap          # 30-day sprint overview
python3.11 -m fde_training_lab modules          # list modules
python3.11 -m fde_training_lab module <slug>    # inspect one module
python3.11 -m fde_training_lab week <1-4>       # week-by-week focus
python3.11 -m fde_training_lab prompt <slug>    # copy/paste AI prompt for a module
python3.11 -m fde_training_lab scorecard        # FDE readiness rubric
```

## Recommended training flow
1. Read `docs/product-brief.md`
2. Read `docs/source-notes/greg-isenberg-fde-video.md`
3. Work through `curriculum/30-day-plan.md`
4. Run one flagship capstone from `curriculum/workshop-labs.md`
5. Use `templates/` to package the project like real FDE proof
6. Use `curriculum/90-day-acceleration-plan.md` to deepen into real customer work

## Repo layout

```text
fde-training-lab/
  curriculum/
  docs/
  src/fde_training_lab/
  templates/
  tests/
```

## Capstone outcome
By the end of this repo, the learner should have:
- one audited workflow map
- one working agent system with traces and guardrails
- one eval pack with known failure modes
- one business case with ROI language
- one client- or employer-ready FDE case study

## Notes
This curriculum was seeded from Greg Isenberg + Voss’s FDE video and adapted into a Zu-specific operator/builder trajectory.
