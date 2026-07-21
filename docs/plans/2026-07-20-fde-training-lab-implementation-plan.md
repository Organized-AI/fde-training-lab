# FDE Training Lab Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Extend this repo into a durable FDE training environment with richer capstone tracking, artifact generation, and stakeholder-ready outputs.

**Architecture:** Keep the repo stdlib-first and content-first. The CLI should remain lightweight, while the curriculum, templates, and capstone artifacts do the heavy lifting. Add features only when they directly improve the learner’s ability to produce real FDE evidence.

**Tech Stack:** Python 3.10+, argparse, dataclasses, pathlib, unittest, markdown docs.

---

### Task 1: Add learner profile support

**Objective:** Let the CLI tailor outputs to a learner’s current strengths and gaps.

**Files:**
- Modify: `src/fde_training_lab/data.py`
- Modify: `src/fde_training_lab/cli.py`
- Create: `tests/test_profile.py`

**Step 1: Write failing test**
Create a test that expects a `profile` command to print a named learner profile.

**Step 2: Run test to verify failure**
Run: `python3.11 -m unittest tests.test_profile -v`
Expected: FAIL — command or data missing.

**Step 3: Write minimal implementation**
Add one or two sample profiles and a `profile` CLI command.

**Step 4: Run test to verify pass**
Run: `python3.11 -m unittest tests.test_profile -v`
Expected: PASS.

**Step 5: Commit**
```bash
git add src/fde_training_lab/data.py src/fde_training_lab/cli.py tests/test_profile.py
git commit -m "feat: add learner profile command"
```

### Task 2: Generate capstone checklists

**Objective:** Help the learner create a concrete capstone execution checklist.

**Files:**
- Modify: `src/fde_training_lab/data.py`
- Modify: `src/fde_training_lab/cli.py`
- Create: `tests/test_capstone_checklist.py`

**Step 1: Write failing test**
Expect `python3.11 -m fde_training_lab prompt capstone` or a dedicated checklist command to include audit, eval, and deployment sections.

**Step 2: Run test to verify failure**
Run: `python3.11 -m unittest tests.test_capstone_checklist -v`
Expected: FAIL.

**Step 3: Write minimal implementation**
Add capstone checklist output using existing module data rather than introducing a new framework.

**Step 4: Run test to verify pass**
Run: `python3.11 -m unittest tests.test_capstone_checklist -v`
Expected: PASS.

**Step 5: Commit**
```bash
git add src/fde_training_lab/data.py src/fde_training_lab/cli.py tests/test_capstone_checklist.py
git commit -m "feat: add capstone checklist output"
```

### Task 3: Add markdown export for stakeholder artifacts

**Objective:** Export a ready-to-edit audit summary or case-study draft.

**Files:**
- Modify: `src/fde_training_lab/cli.py`
- Create: `src/fde_training_lab/exporters.py`
- Create: `tests/test_exporters.py`

**Step 1: Write failing test**
Expect an export command to create a markdown file for a workflow audit or case study.

**Step 2: Run test to verify failure**
Run: `python3.11 -m unittest tests.test_exporters -v`
Expected: FAIL.

**Step 3: Write minimal implementation**
Add a simple markdown exporter using template strings and pathlib.

**Step 4: Run test to verify pass**
Run: `python3.11 -m unittest tests.test_exporters -v`
Expected: PASS.

**Step 5: Commit**
```bash
git add src/fde_training_lab/cli.py src/fde_training_lab/exporters.py tests/test_exporters.py
git commit -m "feat: add markdown exporters for stakeholder artifacts"
```

### Task 4: Add a progress scorecard command

**Objective:** Make the rubric actionable by letting learners self-score a capstone.

**Files:**
- Modify: `src/fde_training_lab/cli.py`
- Modify: `docs/assessment-rubric.md`
- Create: `tests/test_scorecard_output.py`

**Step 1: Write failing test**
Expect the CLI to print categories in a stable, user-friendly order.

**Step 2: Run test to verify failure**
Run: `python3.11 -m unittest tests.test_scorecard_output -v`
Expected: FAIL.

**Step 3: Write minimal implementation**
Add richer formatting or guidance under the existing `scorecard` command.

**Step 4: Run test to verify pass**
Run: `python3.11 -m unittest tests.test_scorecard_output -v`
Expected: PASS.

**Step 5: Commit**
```bash
git add src/fde_training_lab/cli.py docs/assessment-rubric.md tests/test_scorecard_output.py
git commit -m "feat: improve scorecard command"
```

### Task 5: Document verification workflow

**Objective:** Make it obvious how to verify the repo still works after edits.

**Files:**
- Modify: `README.md`
- Create: `docs/verification.md`

**Step 1: Write docs update**
Document exact install, smoke-test, and unittest commands.

**Step 2: Run verification**
Run:
```bash
python3.11 -m pip install -e .
python3.11 -m fde_training_lab roadmap
python3.11 -m unittest discover -s tests -v
```
Expected: commands succeed.

**Step 3: Commit**
```bash
git add README.md docs/verification.md
git commit -m "docs: add verification workflow"
```
