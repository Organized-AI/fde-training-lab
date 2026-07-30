# Source Notes

## Primary source
- Video: Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE
- URL: https://www.youtube.com/watch?v=KwhgfwOSToQ
- Channel: AI Engineer
- Speaker: Kevin Bai
- Duration: ~17m 46s

## Executive takeaway
Kevin Bai frames forward deployed engineering as a **go-to-market and product-delivery function** for situations where a company sells a highly technical platform to a non-technical buyer. In that environment, the customer is not buying software alone or services alone; they are buying an outcome delivered by customer-facing engineers who understand the business problem, build on top of a shared platform, and turn bespoke lessons into reusable product primitives over time.

## Key grounded takeaways

### 1. FDE exists to sell outcomes, not just software licenses or services hours
Bai explains Palantir's core insight as moving from "just products" or "just services" to a combined motion where the customer buys an outcome. The point is not that the buyer should care how the underlying data platform works; the point is that the deployment team should understand the business problem and deliver something operationally useful on top of the platform. This framing shows up when he describes sending smart engineers to understand the customer's business and build a solution on top of Foundry rather than expecting the customer to self-implement the platform. (`2:36-3:50`)

### 2. The FDE motion is only necessary in a specific quadrant
The talk makes a strong distinction between:
- technical products sold to technical buyers;
- simpler configurable products sold to non-technical buyers; and
- the harder Palantir-style case: a very technical platform sold to a non-technical buyer.

Bai argues that FDE is only the right fit in that third case. If the go-to-market motion is already developer-facing or a more standard sales-led SaaS motion, other functions are likely better fits. (`4:16-5:13`, `9:48-10:41`)

### 3. FDE is enterprise-scale design partnership
Bai describes FDE as taking the early-stage startup design-partnership model and scaling it into the enterprise. Instead of limiting close co-building to the first handful of customers, the company keeps that outcome-oriented, implementation-heavy posture as a durable enterprise motion. (`7:27-8:12`)

### 4. Without a platform and shared primitives, you do not have FDE — you have a dev shop
One of the sharpest parts of the talk is Bai's warning that if each forward deployed engineer is building every customer solution from scratch, the organization is really operating as a services shop. The maintainability requirement is the differentiator: real FDE work builds on top of an existing platform with shared primitives that can be recombined into customer-specific applications. (`8:19-9:17`)

### 5. Two gating questions matter before creating an FDE function
Bai recommends asking two questions before romanticizing the role:
1. **Do we truly need an FDE function?** In his definition, that means the company must sell a technically complicated thing to a non-technical buyer.
2. **Do we already have a platform, or are we willing to invest in one?** Without that shared substrate, the maintenance burden becomes overwhelming.

This is a useful anti-hype filter for any team trying to copy the label without the underlying product and go-to-market conditions. (`9:48-11:26`)

### 6. AI makes the FDE pattern more relevant because more software is now customizable
Bai's 2026 update is that the big change is not that everyone suddenly discovered Palantir's org design. The change is that agentic and AI-native platforms are increasingly customizable, which means more customers do not understand how to implement the product successfully on their own. In his framing, that implementation gap is what expands the surface area for FDE-like work. (`11:30-12:50`)

### 7. Shared primitives can be thick or thin, but they must exist
In Q&A, Bai says the right level of primitive granularity depends on the domain and customer base. In some situations, the application can be mostly prebuilt with a smaller customization layer; in others, the platform needs much more granular configuration. His AWS analogy is useful: the platform should save teams from rebuilding obvious foundations from scratch while still leaving the right level of flexibility. (`13:12-14:48`)

### 8. Collaboration and platform extraction matter operationally
Bai explicitly endorses having multiple FDEs collaborate on a project to avoid single points of failure. He also draws a line between what should remain customer-specific and what should migrate back into the shared platform: anything bespoke can stay local, but anything generalizable should be pulled into the platform over time. That makes FDE a scouting function for product opportunities, not just a delivery function. (`15:05-16:48`)

### 9. The simplest definition of the role: a customer-facing software engineer
Bai's closing line is probably the cleanest hiring heuristic in the talk: an FDE is a software engineer you would trust in front of a customer. That combines technical execution with communication, trust, and deployment judgment. (`16:56-17:25`)

## What this means for this repo
This source strengthens a few opinions already embedded in the training lab:
- **FDE is not just "good at AI".** It is a deployment and go-to-market role with customer-contact requirements.
- **Platform thinking is central.** A strong FDE capstone should show not only a solution for one workflow, but also what reusable substrate or primitive set makes the solution maintainable.
- **Customer truth matters.** The work starts from a real buyer, operator, or workflow owner who needs an outcome rather than an abstract demo.
- **Generalization is part of the job.** The strongest artifacts show which pieces stay bespoke and which should become shared product capability.

## Suggested operator checklist derived from the talk
- Confirm that the product being sold is genuinely technical and customizable.
- Confirm that the buyer or primary deployment stakeholder is meaningfully non-technical.
- Identify the platform primitives that prevent the team from rebuilding every customer solution from scratch.
- Make the business outcome explicit before implementation starts.
- Treat each deployment as both delivery work and product discovery for what should be generalized later.
- Staff projects to avoid single points of failure.

## Bottom line
This talk is useful because it makes FDE legible as an organizational pattern rather than a prestige label. The durable lesson is that FDE works when a company must bridge a difficult implementation gap between a powerful technical platform and a buyer who cares about outcomes, not internals. The moment the platform disappears, the motion collapses into custom services; the moment the customer-facing outcome work disappears, it collapses back into ordinary product engineering.