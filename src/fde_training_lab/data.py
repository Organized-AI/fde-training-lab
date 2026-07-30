from dataclasses import dataclass


@dataclass(frozen=True)
class Module:
    slug: str
    title: str
    summary: str
    outputs: tuple[str, ...]
    prompt: str


MODULES = {
    "workflow-audit": Module(
        slug="workflow-audit",
        title="Workflow Audit",
        summary="Map how work actually happens, including exceptions, approvals, hidden tribal knowledge, and whether the problem actually deserves an FDE motion.",
        outputs=(
            "operating map",
            "buyer / operator technicality map",
            "exception list",
            "approval points",
            "pain-point summary",
            "FDE fit memo",
        ),
        prompt=(
            "Act like an AI forward deployed engineer auditing a real business workflow. "
            "Help me map the trigger, actors, tools, steps, exceptions, approvals, current metrics, and whether the buyer is technical enough to self-implement. "
            "Return a granular workflow map, an FDE-fit memo, and call out where AI should be used, where deterministic software should be used, and where human review should remain."
        ),
    ),
    "agent-systems": Module(
        slug="agent-systems",
        title="Agent Systems",
        summary="Build one real-loop system with tools, traces, deliberate human approval points, and reusable primitives.",
        outputs=(
            "working agent loop",
            "architecture sketch",
            "reusable primitives inventory",
            "trace sample",
            "integration map",
        ),
        prompt=(
            "Help me design a deployment-grade agent system for the workflow I audited. "
            "Use a tool-using architecture with explicit boundaries between deterministic software, model judgment, human approval, and shared platform primitives. "
            "Return components, control flow, trace requirements, likely failure points, and which primitives should be reusable across deployments."
        ),
    ),
    "evals-reliability": Module(
        slug="evals-reliability",
        title="Evals and Reliability",
        summary="Turn the system into something measurable with a golden dataset and failure taxonomy.",
        outputs=(
            "golden dataset",
            "failure taxonomy",
            "eval rubric",
            "before/after results",
        ),
        prompt=(
            "Help me create an eval plan for this AI workflow system. "
            "Define a golden dataset, pass/fail criteria, major failure modes, and a human-in-the-loop escalation policy. "
            "Optimize for deployment confidence, not benchmark theater."
        ),
    ),
    "deployment-integration": Module(
        slug="deployment-integration",
        title="Deployment and Integration",
        summary="Design the rollout path that fits the current stack and de-risks adoption.",
        outputs=(
            "shadow mode plan",
            "rollback path",
            "monitoring plan",
            "integration boundaries",
            "bespoke vs shared product boundary",
        ),
        prompt=(
            "Help me design a rollout plan for this AI workflow system into an existing enterprise stack. "
            "Assume the buyer is risk-sensitive and does not want a rip-and-replace migration. "
            "Return a phased deployment plan from sandbox to shadow mode to controlled autonomy to production, plus a clear line between bespoke deployment logic and what should migrate back into the shared platform."
        ),
    ),
    "business-value": Module(
        slug="business-value",
        title="Business Value and Trust",
        summary="Frame the system in stakeholder-safe language across ROI, risk, and adoption.",
        outputs=(
            "ROI framing",
            "risk framing",
            "stakeholder pitch points",
            "objection handling",
            "why this needs an FDE motion",
        ),
        prompt=(
            "Act like an FDE preparing a stakeholder brief. "
            "Translate this technical system into a business case using revenue uplift, risk mitigation, and cost savings. "
            "Also include adoption concerns, organizational incentives, likely objections, and why this work requires a customer-facing engineer on top of a platform instead of self-serve software or a pure services shop."
        ),
    ),
    "capstone": Module(
        slug="capstone",
        title="Capstone Packaging",
        summary="Turn the project into explicit FDE proof with case-study quality packaging.",
        outputs=(
            "case study",
            "audit summary",
            "eval summary",
            "deployment plan",
            "stakeholder pitch",
            "platform extraction memo",
        ),
        prompt=(
            "Help me package this project as proof that I can do forward deployed engineering. "
            "I need a case study that covers the workflow audit, system design, reusable primitives, failure modes, eval evidence, deployment plan, and business value. "
            "Write it so a founder, hiring manager, or client can quickly see why this is credible and why the work is FDE rather than a custom dev engagement."
        ),
    ),
}


WEEK_PLAN = {
    1: {
        "theme": "Build one real-loop system",
        "focus": (
            "choose one real workflow",
            "qualify whether it is actually FDE-shaped",
            "map the steps",
            "build a working system",
            "include traces and approval points",
        ),
        "done": "A non-trivial task completes repeatedly, you can show what happened step by step, and you can explain why the workflow needs a customer-facing deployment motion.",
    },
    2: {
        "theme": "Harden for reality",
        "focus": (
            "add structure to inputs and outputs",
            "handle unhappy paths",
            "log failures and recoveries",
            "extract reusable primitives versus bespoke deployment logic",
            "stop building only for the happy path",
        ),
        "done": "You know how the system fails and how major exceptions get mitigated or routed.",
    },
    3: {
        "theme": "Measure value",
        "focus": (
            "build a golden dataset",
            "run evals",
            "estimate economics",
            "improve cost, accuracy, and reliability",
        ),
        "done": "You can defend the system with evidence and speak about revenue, risk, or cost impact.",
    },
    4: {
        "theme": "Package and pitch",
        "focus": (
            "create a case study",
            "write the rollout plan",
            "rehearse the pitch",
            "show what should stay bespoke versus what should move back into the platform",
            "get feedback from real people",
        ),
        "done": "You have one project that looks like genuine FDE proof.",
    },
}


SCORECARD = (
    ("Workflow Understanding", "Granular operating map with exceptions, stakeholders, and metrics."),
    ("System Design", "Deployment-grade boundary between tools, models, and humans."),
    ("Reliability / Evals", "Golden dataset, failure taxonomy, measurable improvements."),
    ("Deployment Readiness", "Shadow mode, approvals, monitoring, rollback."),
    ("Business Value", "Revenue uplift, risk mitigation, cost savings framing."),
    ("Stakeholder Trust", "Can explain, defend, and de-risk the system for non-technical stakeholders."),
    ("FDE Fit and Platform Leverage", "Clear reason this needs a customer-facing engineer on top of reusable platform primitives instead of self-serve software or one-off services."),
)


RESOURCE_SECTIONS = (
    (
        "Role and Mental Models",
        (
            ("Source video", "https://www.youtube.com/watch?v=zXysLUTLjw4", "Seed framing for the first version of this repo."),
            ("Forward Deployed Engineering 101 — Kevin Bai", "https://www.youtube.com/watch?v=KwhgfwOSToQ", "Sharp framing for when FDE is actually the right motion and why platform primitives matter."),
            ("Kevin Bai source notes", "docs/source-notes/kevin-bai-fde-101.md", "Transcript-grounded takeaways on GTM fit, platform requirements, and the customer-facing engineer profile."),
            ("Product brief", "docs/product-brief.md", "Internal thesis for what this repo believes FDE work is."),
            ("Assessment rubric", "docs/assessment-rubric.md", "Checklist for whether a project looks deployment-grade."),
        ),
    ),
    (
        "Workflow Discovery and Operations",
        (
            ("Workflow audit template", "templates/workflow-audit-template.md", "Start here before touching models."),
            ("GitLab Handbook", "https://about.gitlab.com/handbook/", "Public example of explicit operating process."),
            ("Google SRE Book", "https://sre.google/sre-book/table-of-contents/", "Strong baseline for operational thinking and service maturity."),
        ),
    ),
    (
        "Agent Systems",
        (
            ("Building Effective Agents", "https://www.anthropic.com/engineering/building-effective-agents", "Practical framing for agent patterns and tradeoffs."),
            ("Training modules", "curriculum/modules.md", "Internal module map for the FDE path."),
            ("Workshop labs", "curriculum/workshop-labs.md", "Turn theory into proof artifacts."),
        ),
    ),
    (
        "Evals and Reliability",
        (
            ("OpenAI Evals: getting started", "https://cookbook.openai.com/examples/evaluation/getting_started_with_openai_evals", "Practical starting point for eval loops."),
            ("Eval report template", "templates/eval-report-template.md", "Package evidence in a decision-ready format."),
            ("30-Day FDE Plan", "curriculum/30-day-plan.md", "Week 3 focuses on measurement and economics."),
        ),
    ),
    (
        "Deployment and Integration",
        (
            ("The Twelve-Factor App", "https://12factor.net/", "Operational discipline that still matters."),
            ("90-Day FDE Acceleration Plan", "curriculum/90-day-acceleration-plan.md", "Deeper path after the first capstone."),
            ("Client / stakeholder pitch template", "templates/client-pitch-template.md", "Translate the work into approval-ready language."),
        ),
    ),
)
