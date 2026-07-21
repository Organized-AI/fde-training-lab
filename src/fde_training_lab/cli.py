from __future__ import annotations

import argparse
from textwrap import indent

from .data import MODULES, SCORECARD, WEEK_PLAN


def _roadmap_text() -> str:
    lines = ["30-Day FDE Roadmap", "==================="]
    for week, info in WEEK_PLAN.items():
        lines.append(f"Week {week}: {info['theme']}")
        for item in info["focus"]:
            lines.append(f"  - {item}")
        lines.append(f"  Done when: {info['done']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _modules_text() -> str:
    lines = ["Training Modules", "================"]
    for module in MODULES.values():
        lines.append(f"- {module.slug}: {module.title}")
        lines.append(f"  {module.summary}")
    return "\n".join(lines) + "\n"


def _module_text(slug: str) -> str:
    module = MODULES[slug]
    lines = [module.title, "=" * len(module.title), module.summary, "", "Outputs:"]
    lines.extend(f"- {output}" for output in module.outputs)
    return "\n".join(lines) + "\n"


def _week_text(number: int) -> str:
    info = WEEK_PLAN[number]
    lines = [f"Week {number}: {info['theme']}", "=" * (len(info['theme']) + 8), "Focus:"]
    lines.extend(f"- {item}" for item in info["focus"])
    lines.append("")
    lines.append(f"Definition of done: {info['done']}")
    return "\n".join(lines) + "\n"


def _prompt_text(slug: str) -> str:
    module = MODULES[slug]
    return f"Prompt for {module.title}\n{'=' * (11 + len(module.title))}\n{module.prompt}\n"


def _scorecard_text() -> str:
    lines = ["FDE Scorecard", "============="]
    for category, description in SCORECARD:
        lines.append(f"- {category}: {description}")
    lines.append("")
    lines.append("Score each category from 1 to 5. A strong capstone has no category below 3.")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="fde_training_lab", description="FDE training curriculum CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("roadmap", help="Print the 30-day roadmap")
    subparsers.add_parser("modules", help="List training modules")

    module_parser = subparsers.add_parser("module", help="Show details for one module")
    module_parser.add_argument("slug", choices=sorted(MODULES))

    week_parser = subparsers.add_parser("week", help="Show one week of the roadmap")
    week_parser.add_argument("number", type=int, choices=sorted(WEEK_PLAN))

    prompt_parser = subparsers.add_parser("prompt", help="Print a copy/paste prompt for one module")
    prompt_parser.add_argument("slug", choices=sorted(MODULES))

    subparsers.add_parser("scorecard", help="Print the FDE readiness rubric")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "roadmap":
        print(_roadmap_text(), end="")
        return 0
    if args.command == "modules":
        print(_modules_text(), end="")
        return 0
    if args.command == "module":
        print(_module_text(args.slug), end="")
        return 0
    if args.command == "week":
        print(_week_text(args.number), end="")
        return 0
    if args.command == "prompt":
        print(_prompt_text(args.slug), end="")
        return 0
    if args.command == "scorecard":
        print(_scorecard_text(), end="")
        return 0

    parser.print_help()
    return 1
