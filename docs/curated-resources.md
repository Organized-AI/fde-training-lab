# Curated FDE Resources

A curated and **opinionated** list of resources for people training toward AI Forward Deployed Engineering.

The selection is biased toward people who already build software, automation, or agent systems and now need to become stronger at workflow discovery, deployment reality, evals, stakeholder trust, and proof packaging.

## Contents

* [Role and mental models](#role-and-mental-models)
* [Workflow discovery and operations](#workflow-discovery-and-operations)
* [Agent systems](#agent-systems)
* [Evals and reliability](#evals-and-reliability)
* [Deployment and integration](#deployment-and-integration)
* [Communication and trust](#communication-and-trust)
* [Internal repo guides](#internal-repo-guides)
* [Related lists](#related-lists)

## Role and mental models

* [FDE: The $1M/Year AI Job Explained](https://www.youtube.com/watch?v=zXysLUTLjw4) - the seed source for this repo; useful for understanding the current market framing.
* [Forward Deployed Engineering 101 — Kevin Bai](https://www.youtube.com/watch?v=KwhgfwOSToQ) - strong framing on when FDE is the right motion, why platform primitives matter, and how AI increases the need for customer-facing deployment talent.
* [Kevin Bai source notes](source-notes/kevin-bai-fde-101.md) - transcript-grounded breakdown of the talk with repo-specific implications.
* [Product brief](product-brief.md) - internal framing for what this repository believes FDE work actually is.
* [Assessment rubric](assessment-rubric.md) - internal checklist for whether a project really looks deployment-grade.

## Workflow discovery and operations

* [Workflow audit template](../templates/workflow-audit-template.md) - start here before touching models.
* [Visual roadmap + proof stack](visual-roadmap.md) - static diagrams for the learning path and capstone evidence stack.
* [GitLab Handbook](https://about.gitlab.com/handbook/) - one of the best public examples of explicit operating process.
* [Google SRE Book](https://sre.google/sre-book/table-of-contents/) - useful for operational thinking, guardrails, and service maturity.
* [danluu/post-mortems](https://github.com/danluu/post-mortems) - study how systems fail in the real world.

## Agent systems

* [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) - practical framing for agent patterns and where complexity is worth it.
* [Training modules](../curriculum/modules.md) - the repo’s module map for workflow audit, agent systems, evals, deployment, and business value.
* [Workshop labs](../curriculum/workshop-labs.md) - use these to convert theory into artifacts.

## Evals and reliability

* [OpenAI Evals: getting started](https://cookbook.openai.com/examples/evaluation/getting_started_with_openai_evals) - practical on-ramp for thinking in eval loops.
* [Eval report template](../templates/eval-report-template.md) - package the evidence in a decision-ready format.
* [30-Day FDE Plan](../curriculum/30-day-plan.md) - week 3 focuses specifically on measurement, economics, and reliability.

## Deployment and integration

* [The Twelve-Factor App](https://12factor.net/) - still a strong baseline for operational discipline.
* [90-Day FDE Acceleration Plan](../curriculum/90-day-acceleration-plan.md) - the deeper deployment path after the first capstone.
* [Client / stakeholder pitch template](../templates/client-pitch-template.md) - deployment only matters if it can be approved and adopted.

## Communication and trust

* [Client / stakeholder pitch template](../templates/client-pitch-template.md) - explain the system in ROI, risk, and adoption language.
* [Source notes from the seed video](source-notes/greg-isenberg-fde-video.md) - highlights on packaging, business framing, and proof.
* [Implementation plan](plans/2026-07-20-fde-training-lab-implementation-plan.md) - the current repo build roadmap, written as explicit work items.

## Internal repo guides

* [README](../README.md) - primary entrypoint.
* [Visual roadmap](visual-roadmap.md) - roadmap-style SVGs for the training path and proof stack.
* [Verification guide](verification.md) - exact install and smoke-test commands.
* [Product brief](product-brief.md) - why this repo exists.
* [Assessment rubric](assessment-rubric.md) - how to judge readiness.

## Related lists

* [awesome-cto](https://github.com/kuchin/awesome-cto) - structural inspiration for this repo.
* [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) - useful contrast: broad engineering roadmaps vs. this narrower FDE path.

## Opinionated note

Most people over-rotate on model novelty and under-rotate on workflow truth, failure modes, rollout strategy, and stakeholder trust.

That is exactly why this repo emphasizes:

* workflow audits before prompts
* evals before confidence
* rollout plans before autonomy
* case-study proof before self-labeling as an FDE
