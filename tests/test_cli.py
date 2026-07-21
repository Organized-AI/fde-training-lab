import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CLITest(unittest.TestCase):
    def run_cli(self, *args: str) -> str:
        result = subprocess.run(
            [sys.executable, "-m", "fde_training_lab", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout

    def test_roadmap_contains_week_1(self) -> None:
        output = self.run_cli("roadmap")
        self.assertIn("Week 1: Build one real-loop system", output)

    def test_modules_lists_workflow_audit(self) -> None:
        output = self.run_cli("modules")
        self.assertIn("workflow-audit", output)

    def test_module_details_include_outputs(self) -> None:
        output = self.run_cli("module", "workflow-audit")
        self.assertIn("Outputs:", output)
        self.assertIn("operating map", output)

    def test_week_command_prints_definition_of_done(self) -> None:
        output = self.run_cli("week", "3")
        self.assertIn("Definition of done", output)

    def test_prompt_command_returns_copy_paste_prompt(self) -> None:
        output = self.run_cli("prompt", "business-value")
        self.assertIn("Act like an FDE preparing a stakeholder brief", output)

    def test_scorecard_mentions_business_value(self) -> None:
        output = self.run_cli("scorecard")
        self.assertIn("Business Value", output)


if __name__ == "__main__":
    unittest.main()
