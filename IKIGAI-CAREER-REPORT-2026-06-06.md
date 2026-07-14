# Ikigai And Career Strategy Report

Date: 2026-06-06

Status: Dated career-strategy working document. It informs portfolio framing but does not control repository scope or current project status.

Prepared from the documented work in:

- `D:\Repos\legal-tech-debt`
- `D:\Repos\renonerd`
- `C:\Users\DorianKlingenberg\OneDrive - RenoNerd Inc\2026-projects\grannies-house-trials`

This report is not a verdict. It is a working document: something to study, argue with, revise, and use while deciding what to build during a six-month career runway.

## Executive Thesis

Your strongest career direction is not generic AI engineering, generic legaltech, generic game development, or generic consulting.

Your center is:

> Build computational systems that reveal hidden structure, prove what they can prove, and give humans a trustworthy way to reason about the rest.

The employable version is:

> AI evidence engineer for regulated, high-stakes, document-heavy domains.

The broader life version is:

> Systems evidence engineer: someone who builds simulations, evidence workbenches, traces, reports, and review loops that make hidden rules visible.

The digital-twin version is:

> Builder of inspectable models of real systems that reveal surprising causal behavior before the real world charges full price.

The economic version is:

> Cost-aware AI engineer: someone who makes AI systems accurate, inspectable, and cheap enough to run repeatedly.

The software-engineering version is:

> Builder of agentic SDLC control systems that turn conversation and experiment evidence into scoped work, verification evidence, and human-approved progress.

Across the work I read, you repeatedly do the same rare thing:

1. Enter a messy domain.
2. Identify the real source of truth.
3. Refuse premature platform fantasy.
4. Build a constrained sandbox.
5. Record evidence with provenance.
6. Separate automation from human judgment.
7. Conserve expensive model calls by doing deterministic work first.
8. Let the model surprise you, then preserve the surprise as evidence.
9. Promote durable surprises into requirements, risks, tests, or lessons.
10. Package the result as a report, workbench, lesson, handoff, or repeatable experiment.

That pattern is valuable in AI because modern AI systems are increasingly powerful, increasingly opaque, and increasingly hard to trust without evidence. The market is actively paying people who can build retrieval systems, agent workflows, evaluation harnesses, trace systems, human review flows, audit records, and domain-specific AI reliability layers.

## The Pattern Across Your Work

### Legal Tech Debt

The legal-tech-debt work is the most directly market-aligned expression of the pattern.

You are building around:

- source-traceable evidence
- policy and regulatory document structures
- legal/code smell taxonomies
- retrieval bundles
- reviewer reports
- graph-based gap detection
- human-readable findings
- drilldown reports
- run artifacts with schema, timestamps, stable IDs, and provenance

The strongest line in this body of work is not "AI finds legal issues."

The stronger line is:

> The system creates inspectable evidence packs for high-consequence document review.

That is a meaningful distinction. Buyers and employers are wary of AI magic. They are more open to systems that produce structured evidence, show sources, expose uncertainty, and let humans make final decisions.

### RenoNerd / WindowConfigurator

RenoNerd shows the same instinct in a business workflow domain.

The core pattern is:

- the server owns authoritative truth
- measurements must be exact
- rough opening is unknown until remeasure
- CRM systems should receive completed configuration state, not own it
- webhooks are unidirectional
- product line and pricing logic must be domain-correct
- demos should preserve real business boundaries

This work proves that your thinking is not just speculative. You can reason through production boundaries, ownership, validation, pricing, workflows, tests, and integration discipline.

The important portfolio signal:

> You can turn real-world domain rules into authoritative software boundaries.

The AI integration opportunity is not a generic chatbot. It is a field-work intelligence layer around a system that already knows how to be authoritative.

Two RenoNerd ideas are especially aligned:

- **Field Measure Voice Capture:** a contractor walks a house with a phone, measures each opening, and speaks draft configurations such as "living room, 150 inches by 48 inches, triple-glazed casement picture casement." Speech-to-text plus an LLM or constrained parser turns that into a candidate configured window item. The server still validates measurements, product-line access, style compatibility, pricing-grid support, and order-readiness.
- **Pricing Capture Harness:** contractors often have authorized access to slow manufacturer/dealer configurators, but reconstructing price books requires configuring hundreds or thousands of windows. A deterministic browser-automation and test-generation harness can explore valid configurations, capture prices, screenshots, warnings, and errors, then infer pricing tables and anomalies. AI helps with label mapping, ambiguous error classification, next-batch suggestions, and evidence summaries, but the core loop should be deterministic and auditable.

The strong product sentence:

> Walk the house, speak the windows, leave with a quote.

The strong engineering sentence:

> Build AI-assisted intake and pricing-evidence systems around deterministic validation, exact measurement math, and server-authoritative pricing.

### Grannies House Trials

Grannies House Trials looks playful, but it is philosophically close to the legal-tech-debt work.

Its durable pattern is:

- deterministic hidden world truth
- constrained interventions
- visible consequences
- evidence board
- tester-facing projection
- agent-based testing
- host judgment
- small replayable scenario
- local success can still create global/contextual failure

That is not a distraction from the career pattern. It clarifies it.

You are drawn to systems where:

- something is hidden
- actions have consequences
- the evidence must be recorded
- human interpretation matters
- the point is not the joke or the interface, but the revealed structure

It is also digital-twin-adjacent. It is a small causal twin of a hidden infrastructure system: not high-fidelity industrial simulation, but a deliberately inspectable model where interventions produce surprising consequences.

The puzzle matrix work sharpens this further. It is not just a design reference. It is a structured scenario-generation and evaluation substrate:

- matrix rows define meaningful player-world interactions,
- motifs define reusable failure-mode patterns,
- goals define primary/safety/quality/discovery metrics,
- compositions define test scenarios,
- tester agents probe those scenarios with different strategies,
- the evidence board records what happened,
- and the host or human reviewer judges the meaning.

That makes Grannies a simulation-backed agent-testing harness. Builder, Chaos Tester, and Systems Auditor are not only characters. They are role-differentiated test agents that expose different classes of system truth.

### Physics / HPC Speculation

The physics/time-dilation work adds another domain, not another identity.

If handled carefully, it can be a strong technical sidecar:

- numerical simulation
- high-performance computing
- precision/error analysis
- benchmarks
- reproducibility
- baseline validation against known equations
- visualization
- scientific humility

The key is presentation. Do not present it as new physics. Present it as:

> A high-performance numerical sandbox for exploring standard relativistic relationships using time dilation as the primary computational lens.

That lets the work prove technical discipline even if nobody accepts the hypothesis.

### Quantum / Annealing Side Lane

Quantum should not become a detour into vague "quantum AI" positioning. The useful lane is narrower:

> QUBO / Ising optimization for AI workflow problems, tested against classical, simulated annealing, simulated quantum annealing, and quantum-annealing-compatible solvers.

This fits your skepticism about gate-model quantum computing. You do not need to claim quantum advantage. You can build evidence.

Good portfolio shapes:

- QUBO-based feature selection for ML workflows.
- Instance selection or dataset reduction under accuracy/cost constraints.
- RAG chunk selection under context-window and token-budget constraints.
- Prompt/tool/model routing formulated as a cost-quality optimization problem.
- Benchmark reports comparing solver quality, runtime, sparsity, stability, and implementation complexity.

Open-source ecosystems to watch or contribute around:

- D-Wave Ocean SDK, `dimod`, `dwave-samplers`, and the D-Wave scikit-learn feature-selection examples.
- OpenJij for open-source simulated annealing and simulated quantum annealing over QUBO/Ising models.
- PyQUBO and qubovert for readable QUBO formulation.
- Fixstars Amplify Benchmark for comparing annealing, Ising, and optimization solvers.

The resume sentence:

> Built a QUBO-based AI optimization benchmark comparing classical, simulated annealing, and quantum-annealing-compatible solvers for feature selection, dataset reduction, and cost-constrained AI routing.

### Sandbox 005 / Agentic SDLC Control System

Sandbox 005 adds another important expression of the same pattern.

It is not primarily valuable because it can be described as a digital twin of a software engineering team. That framing is intellectually interesting, but the stronger professional framing is:

> A repo-native agentic SDLC control system for turning conversation and experiment evidence into scoped tasks, verification evidence, risk records, and human-approved progress.

This is portfolio-worthy because companies are already struggling with AI-assisted development work that is fast but poorly governed:

- agents make untracked changes
- acceptance criteria stay vague
- experiments produce insight but do not become durable requirements
- tests pass without domain validation
- nobody knows which claims are verified
- handoffs decay across tools
- dashboards drift away from repo truth

Sandbox 005 addresses that by modeling:

- conversation-to-contract,
- experiment-to-requirement,
- task contracts,
- evidence bundles,
- risk records,
- hard/advisory/human-only gates,
- experiment-backed V&V,
- agent roles,
- generated status surfaces from repo truth.

The important V-model insight:

> Experiments are useful on both sides of the V. They discover requirements upstream, and they validate or verify implemented behavior downstream.

That is a strong AI systems engineering story. It says you are not merely using agents to code faster. You are designing the control layer that keeps AI-assisted engineering work inspectable.

## Revised Ikigai

Classic ikigai has four parts:

- what you love
- what you are good at
- what the world needs
- what you can be paid for

### What You Love

You love hidden systems.

You seem energized by domains where the surface is misleading and the interesting truth is underneath:

- insurance policy layers
- regulatory filings
- legal references
- renovation measurement/pricing constraints
- yard drainage and hidden infrastructure
- time, motion, and physical relationships
- agent behavior and AI failure modes

You also love constrained experiments. You do not merely want to talk about systems. You want to build a small world, run it, observe it, and see what the evidence says.

### What You Are Good At

You are good at:

- turning vague domain ambiguity into structured artifacts
- separating source truth from generated interpretation
- building bounded proof-of-concepts
- writing durable memory: journals, handoffs, ADRs, lessons
- identifying ownership boundaries
- resisting seductive overbuild
- designing review/report loops
- thinking in graphs, dependencies, rules, and failure modes
- noticing when "absence" is itself evidence
- packaging work so another agent or human can inherit it

That is an unusual combination. Many engineers build. Many analysts investigate. Many writers document. You combine all three.

### What The World Needs

The world increasingly needs AI systems that are not just fluent, but accountable.

High-stakes domains need:

- source-grounded outputs
- traceable reasoning artifacts
- evals and regressions
- audit logs
- retrieval diagnostics
- human review queues
- uncertainty scoring
- escalation paths
- decision records
- policy and regulatory mapping

This need is especially strong in:

- insurance
- legal operations
- financial services
- compliance
- healthcare-adjacent administration
- public-sector review
- audit and assurance
- enterprise knowledge workflows

### What You Can Be Paid For

You can be paid for the employable slice of this pattern:

- applied AI engineering
- LLM evaluation engineering
- AI observability and trace systems
- RAG and retrieval quality engineering
- legal/compliance AI workflows
- human-in-the-loop review systems
- regulated-domain AI prototypes
- evidence/report generation systems
- source-grounded agent workflows
- token-efficient AI architecture
- AI cost instrumentation and optimization
- digital twin and simulation-backed AI workflows
- benchmarking infrastructure for physical or operational systems

The likely best professional title is not one fixed title. It is a cluster:

- Applied AI Engineer
- Senior AI Engineer
- LLM Evaluation Engineer
- AI Reliability Engineer
- AI Observability Engineer
- AI Efficiency Engineer
- Legal AI Engineer
- Compliance AI Engineer
- Agent Systems Engineer
- AI Evidence Systems Consultant
- Digital Twin AI Systems Engineer
- Simulation Infrastructure Engineer

## Digital Twins As A Career Clue

The phrase "digital twin" gives a market name to a pattern that was already present across the work.

A useful broad definition:

> A digital twin is an inspectable computational model of a real or reality-like system that can be probed, compared, updated, and used to reason before acting in the real world.

The part that matters for you is not only fidelity. It is surprise.

You like models that betray assumptions:

- a yard drainage intervention routes water somewhere unexpected
- a policy clause undermines another condition
- a missing amendatory form creates a regulatory gap
- a window quote cannot become an order because the measurement state is not authoritative
- a cheap model handles most cases and an expensive model is only needed for the genuinely strange ones
- a physics simulation exposes where an intuitive time/motion framing breaks or holds

That "wait, what just happened?" moment is not a distraction. It is the point of the system. The twin becomes valuable when it reveals a hidden dependency before reality punishes the mistake.

### How Your Projects Map To Digital Twins

| Project | Digital-Twin Pattern |
|---|---|
| Legal-tech-debt | A document/regulatory twin of policy forms, filings, references, exclusions, gaps, and obligations. |
| RenoNerd / WindowConfigurator | A business/process twin of renovation configuration truth before it becomes manufacturing/order reality. |
| Grannies House Trials | A playful causal twin and agent-testing harness for hidden yard infrastructure, using a puzzle matrix to generate scenarios and tester roles to expose system behavior. |
| Physics/HPC lab | A computational twin of a physical hypothesis, benchmarked against known equations. |

This expands the career lane:

> AI systems engineer for evidence-rich digital twins, scientific benchmarking, simulation-backed agent testing, and cost-aware agent workflows.

### Why This Matters For Jobs

Digital-twin work is an especially good fit when the job combines:

- physical systems
- scientific computing
- engineering simulation
- benchmarks
- agentic reasoning
- failure analysis
- digital twin platforms
- industrial systems
- AI evals
- cost-aware infrastructure

Search terms to add:

- "digital twin" "AI systems engineer"
- "agentic AI" "digital twin"
- "AI benchmarking" "scientific computing"
- "simulation infrastructure" "AI"
- "physics-informed AI" engineer
- "scientific AI" engineer
- "engineering simulation" "LLM"
- "AI evals" "digital twin"
- "AI for engineering" "systems engineer"

### Companies And Labs To Watch

These are not all job targets in the same way. Some are startups, some are infrastructure companies, some are industrial incumbents, and some are open-source/scientific-computing ecosystems. The point is to learn the language of the market and spot aligned roles.

| Company / Ecosystem | Why It Matters |
|---|---|
| JuliaHub / Dyad | Scientific machine learning, modeling/simulation, and agentic AI for industrial digital twins. |
| Siemens | Industrial digital twin platforms, automation, simulation, and NVIDIA Omniverse partnerships. |
| NVIDIA Omniverse | Simulation, physical AI, industrial digital twins, synthetic data, and GPU-accelerated worlds. |
| Ansys / Synopsys / Cadence | Engineering simulation, EDA, multiphysics modeling, verification, and AI-assisted engineering workflows. |
| Altair | Simulation, optimization, data analytics, digital twin, and engineering AI. |
| Dassault Systemes / SIMULIA | 3DExperience, CAD/CAE, industrial modeling, and simulation-driven product design. |
| PTC / ThingWorx | Industrial IoT, connected products, and operational digital twins. |
| GE Vernova / GE Digital lineage | Asset-heavy industrial systems, predictive maintenance, and digital twin history. |
| AspenTech / Emerson | Process-industry simulation, digital twins, control, and optimization. |
| Akselos | Reduced-basis finite element simulation and asset digital twins. |
| SimScale / OnScale-style cloud simulation companies | Cloud CAE/simulation workflows where AI support and benchmarking may matter. |
| Deeptune | High-fidelity simulation environments for AI agents. |
| Simile | Agent/digital-twin simulation lineage from generative agents research. |
| Geordie AI and agent governance startups | Not digital twins directly, but aligned with governing autonomous agents in complex operational systems. |
| AI infrastructure labs using vLLM/SGLang/RouteLLM | Useful for the cost-aware simulation/agent side of the story. |

Best first target category:

> Startups or mid-size companies building AI on top of simulation/engineering workflows, not giant incumbents where the role may be narrower and more credential-heavy.

### Positions To Search And Apply For

Search by function, not only title.

Best-aligned titles:

- AI Systems Engineer
- Applied AI Systems Engineer
- Scientific AI Engineer
- AI Benchmarking Engineer
- AI Evals Engineer
- Research Engineer, Benchmarking / Evals
- Simulation Infrastructure Engineer
- Digital Twin Engineer
- Digital Twin AI Engineer
- Physics-Informed ML Engineer
- Scientific Computing Engineer
- ML Systems Engineer, Inference / Simulation
- Agentic AI Engineer
- AI Platform Engineer, Scientific Computing
- AI for Engineering Applications Engineer
- Computational Modeling Engineer, AI
- Simulation / AI Tooling Engineer

Search strings:

- `"AI Systems Engineer" "digital twin"`
- `"AI Systems Engineer" "scientific computing"`
- `"AI benchmarking" "simulation"`
- `"Research Engineer" "benchmarking" "failure analysis"`
- `"agentic AI" "industrial digital twin"`
- `"LLM agents" "engineering simulation"`
- `"scientific AI engineer" "simulation"`
- `"physics-informed" "machine learning engineer"`
- `"simulation infrastructure engineer" "AI"`
- `"digital twin" "evals"`
- `"AI for engineering" "systems engineer"`

Apply when the description includes several of:

- benchmarking
- evals
- simulation
- scientific computing
- digital twins
- agentic reasoning
- tool use
- Python systems
- model validation
- failure analysis
- computational workflows
- RAG or knowledge retrieval
- production-grade infrastructure

### Open Source Projects For Digital-Twin Signal

The best contribution targets depend on whether you want resume signal for scientific computing, digital twins, AI agents, or efficient AI infrastructure.

| Project / Ecosystem | Why It Fits | Contribution Ideas |
|---|---|---|
| SciML / DifferentialEquations.jl | Core scientific machine learning and simulation ecosystem. | Examples, docs, benchmark reproduction, simulation workflows, Python interop notes. |
| JuliaSim / ModelingToolkit ecosystem | Symbolic modeling and simulation workflows tied to digital-twin style systems. | Tutorials, examples, issue fixes, model validation notes. |
| OpenModelica | Open-source Modelica modeling/simulation platform. | Docs, examples, test cases, Python integration, model validation workflows. |
| Modelica Standard Library | Core reusable physical-system modeling components. | Documentation, examples, issue triage, simple component tests. |
| Project Chrono | Open-source physics-based simulation engine. | Examples, docs, benchmark scenarios, validation tests. |
| SOFA Framework | Simulation framework often used for physical/biomechanical simulation. | Examples, docs, Python bindings, benchmark scenarios. |
| PyBaMM | Physics-based battery modeling in Python. | Tutorials, validation notebooks, benchmark scripts, parameter-study examples. |
| OpenFOAM | CFD simulation ecosystem. | Documentation/examples first; deeper contribution if CFD becomes a chosen lane. |
| FEniCS / deal.II | Finite element/scientific computing stacks. | Tutorials, examples, test improvements, reproducible benchmark docs. |
| Gazebo / ROS 2 | Robotics simulation and physical-agent workflows. | Simulation examples, test worlds, docs, agent/eval harness ideas. |
| NVIDIA Omniverse samples / USD ecosystem | Digital twin scenes, simulation assets, synthetic data, USD workflows. | Examples, docs, small tools, reproducible scene/simulation workflows. |
| vLLM / SGLang / RouteLLM | Efficient AI serving and routing for agentic simulation workflows. | Cost-aware examples, routing benchmarks, structured-output serving docs. |

Best first open-source strategy:

- [ ] Pick one scientific/digital-twin ecosystem: SciML, OpenModelica, PyBaMM, Project Chrono, or Gazebo.
- [ ] Pick one AI efficiency/evals ecosystem: RouteLLM, vLLM, SGLang, Ragas, DeepEval, OpenInference, or Langfuse.
- [ ] Build one small bridge artifact in your own portfolio: "simulation-backed AI eval with cost accounting."

Possible bridge demo:

> A tiny physical-system simulation where an AI agent proposes interventions, the simulator evaluates consequences, an eval harness scores the outcome, and the report shows evidence, cost, and failure modes.

## Market Positioning

### The Market Is Already Paying For This

Current AI engineering compensation is noisy, but strong:

- Built In reports average US AI Engineer compensation around $184,757 base and $211,243 total compensation.
- Glassdoor reports Artificial Intelligence Engineer average around $152,041 in the United States.
- Salary.com reports a lower average around $115,674, which likely reflects broader and less specialized title matching.

More relevant than generic salary averages are current role postings in evals, agent reliability, and applied AI:

- Fieldguide AI Engineer, Quality/Evals: $170k to $220k base.
- Deepgram Model Evaluation QA Lead: $180k to $230k base plus bonus/equity.
- Firecrawl Research Engineer, Evals: $160k to $240k plus equity.
- Jump Applied AI Evaluation Scientist: $180k to $270k.
- Titan AI Applied AI Engineer: $200k to $300k.
- Newfront Senior AI Engineer: $160k to $250k.
- Eigen Labs Agentic AI Engineer: $187k to $253k.
- LeoTech AI/LLM Evaluation and Alignment Engineer: $135k to $160k.

The spread matters. The market pays more when the role is close to:

- production AI systems
- regulated/high-stakes use cases
- evals
- retrieval
- agent reliability
- domain-specific workflows
- senior ownership

### Employee Compensation Target

Your realistic target bands, given the demonstrated repo work:

| Role type | Realistic base | Strong base | Total comp upside |
|---|---:|---:|---:|
| Applied AI Engineer | $150k-$210k | $210k-$260k | $220k-$350k |
| LLM / AI Evals Engineer | $160k-$230k | $230k-$275k | $250k-$400k |
| Legal/compliance AI Engineer | $170k-$240k | $240k-$300k | $275k-$450k |
| AI Product/Systems Architect | $180k-$260k | $260k-$350k | $350k+ |

Do not aim below $150k base unless the role gives exceptional mentorship, brand value, or a clean path into regulated AI.

Your primary target should be:

> $180k-$240k base for a senior applied AI/evals/legal-compliance AI role.

Your stretch target should be:

> $250k-$300k base in a well-funded AI company, fintech, insurance, compliance, or legal AI team.

### Contractor Compensation Target

Contracting is different because you carry the risk:

- taxes
- insurance
- sales time
- unpaid gaps
- admin time
- scope risk
- client management
- context switching

Reasonable contractor bands:

| Contract type | Rate |
|---|---:|
| Generic AI dev staff augmentation | $75-$115/hr |
| Senior applied AI / RAG / agent implementation | $125-$200/hr |
| Evals, traceability, regulated-domain AI systems | $175-$300/hr |
| Advisory + architecture + evidence/report productization | $250-$400/hr |

Your likely floor:

> $125/hr.

Your normal target:

> $175-$225/hr.

Your premium package target:

> $250-$350/hr once you sell a specific evidence/evals outcome.

The best contractor offer is not "hire me to do AI." It is:

> I build source-traceable AI evidence systems for regulated document workflows: retrieval, findings, evals, reviewer state, audit trail, and exportable reports.

That is narrow enough to be credible and valuable.

## Token Efficiency And AI Cost Discipline

Token efficiency should be part of the center of the career story, not a side note.

The market talks a lot about model quality, agents, and giant context windows. It talks less clearly about whether a workflow is economically sane. In real company settings, cost matters because:

- repeated review runs get expensive
- long-context prompts hide waste
- broad retrieval creates noisy evidence
- agent loops can burn money invisibly
- teams often use frontier models where deterministic code, retrieval, caching, or smaller models would work
- companies need to know cost per document, cost per finding, cost per accepted finding, and cost per useful decision

Your instinct for cheap, efficient AI fits the rest of the ikigai. It is another form of evidence discipline:

> Do not spend model tokens where structured parsing, indexing, graph traversal, heuristics, caching, routing, or human review boundaries can do the job better.

### The Current Field

Token efficiency is not one field yet. It is split across several active lanes:

| Lane | What It Optimizes | Representative Projects / Teams |
|---|---|---|
| Model routing and cascades | Send easy tasks to cheaper models and hard tasks to stronger models. | FrugalGPT, RouteLLM, LLMRouter, LiteLLM routing, NadirClaw |
| Prompt and context compression | Reduce input tokens while preserving task quality. | Microsoft LLMLingua / LongLLMLingua, Claw Compactor, context-compression tools |
| Semantic and exact caching | Avoid repeated model calls for repeated or equivalent work. | GPTCache, Helicone caching, prompt-cache, LiteLLM cache/proxy patterns |
| Cost observability | Attribute token/cost usage by model, user, workflow, prompt, and run. | Helicone, Langfuse, LiteLLM, Phoenix/OpenTelemetry/OpenInference |
| Inference serving efficiency | Serve open-weight models with better throughput, memory use, batching, and KV-cache reuse. | vLLM, SGLang |
| Prompt/program optimization | Learn or compile better prompts and pipelines with fewer wasted calls. | DSPy, prompt optimization frameworks |
| Workflow architecture | Avoid LLM calls entirely where deterministic systems suffice. | Your legal-tech-debt pattern: parse, graph, retrieve, detect, then call model only where useful |

This fragmentation is an opportunity. A lot of people are building one piece. Fewer people are combining cost discipline with evidence, evals, provenance, and human review.

Your differentiated framing:

> I build source-traceable AI systems that are evaluated, human-reviewable, and cost-instrumented.

### People And Teams To Watch

- Lingjiao Chen, Matei Zaharia, James Zou, and collaborators: FrugalGPT and LLM cascades for cost/quality tradeoffs.
- UC Berkeley Sky Computing Lab / LMSYS contributors: RouteLLM, vLLM, cost-aware routing, and efficient serving.
- Omar Khattab / Stanford NLP / DSPy contributors: programmatic LM pipelines and prompt/program optimization.
- Microsoft Research LLMLingua team: prompt compression for long context and cost/latency reduction.
- BerriAI / LiteLLM team: LLM gateway, provider abstraction, budgets, spend tracking, routing, and proxy infrastructure.
- Helicone team: open-source LLM observability, cost tracking, caching, and prompt management.
- Zilliz / GPTCache team: semantic caching for LLM applications.
- SGLang project contributors: efficient execution of structured language model programs through prefix/KV-cache reuse and high-throughput serving.

### Best Open Source Targets For This Angle

| Project | Why It Fits | Contribution Ideas |
|---|---|---|
| LiteLLM | Gateway layer for providers, budgets, cost tracking, routing, caching, and fallbacks. | Cost accounting examples, budget policy docs, legal/evidence workflow gateway recipe, provider pricing test fixes. |
| Helicone | Observability plus cost tracking and caching. | Cost-per-workflow examples, cache/cost docs, eval/reporting examples for document review. |
| Langfuse | Traces, evals, prompt management, datasets, and cost visibility. | Token/cost dashboards for RAG pipelines, dataset/eval examples, reviewer workflow cookbook. |
| OpenInference | OpenTelemetry conventions for AI traces. | Trace attributes for retrieval bundles, source IDs, token usage, cost estimates, reviewer state. |
| RouteLLM | Cost-effective model routing framework. | Regulated-document routing benchmark, docs for quality/cost thresholds, legal/evidence workload examples. |
| LLMRouter | Open-source library for routing across models by complexity/cost/performance. | Evaluation examples, legal/RAG workload profile, documentation improvements. |
| Ragas / DeepEval | RAG and LLM evaluation. | Cost-aware eval recipes: quality per dollar, grounding per dollar, citation accuracy per token. |
| GPTCache / prompt-cache | Semantic caching. | Evidence-workflow cache examples, cache safety tests for regulated review, docs on when caching is unsafe. |
| Microsoft LLMLingua | Prompt compression. | Document-review compression examples, benchmark notes on citation preservation, failure cases. |
| vLLM / SGLang | Efficient open-weight serving. | Docs/examples first; later performance tests or structured-output serving experiments if you want deeper infra signal. |
| DSPy | Programmatic prompt/pipeline optimization. | Cost-aware legal/RAG pipeline optimization example using source-grounded eval metrics. |

Best first contribution sequence:

- [ ] Add token/cost accounting to `legal-tech-debt` first so the story is yours.
- [ ] Contribute a cost-aware RAG/evidence example to Ragas, DeepEval, Langfuse, or Helicone.
- [ ] Contribute OpenInference trace attributes or examples for source IDs, retrieval bundles, token usage, cost estimates, and reviewer state.
- [ ] Later, contribute a routing benchmark or workload profile to RouteLLM or LLMRouter.

### Portfolio Signals To Add

Add these to the flagship demo when practical:

- token counts per run
- estimated cost per run
- cost per document
- cost per finding
- cost per accepted finding after reviewer state exists
- cache hit rate
- deterministic prefilter savings
- retrieval compression ratio
- model routing policy
- "no LLM needed" stages marked explicitly

Useful demo table:

| Stage | Method | Tokens | Cost | Why This Method |
|---|---|---:|---:|---|
| Parse sources | deterministic parser | 0 | $0.00 | Stable IDs and reusable nodes |
| Candidate detection | heuristics/graph | 0 | $0.00 | Cheap recall before model review |
| Evidence bundle | retrieval/ranking | low | low | Narrow source context |
| Finding draft | LLM | measured | measured | Language synthesis with citations |
| Reviewer decision | human | 0 | $0.00 model cost | Human owns judgment |

This is not penny-pinching. It is production maturity.

### Contractor Offer Add-On

Add a specific offer:

> AI Cost And Token Efficiency Audit

Scope:

- inspect one AI workflow
- trace token usage by stage
- identify wasted context, unnecessary model calls, retrieval bloat, repeated prompts, and missing cache boundaries
- propose cheaper model routing, caching, and deterministic pre-processing
- produce a cost/quality improvement plan

Early price range:

> $5k-$20k depending on workflow complexity.

This pairs well with the RAG / AI Trust Diagnostic:

> I will tell you whether your AI workflow is trustworthy and whether it is wasting money.

## Company Pain Contracting Strategy

The solo-contractor version of this ikigai is:

> Find expensive hidden-system confusion inside companies, build a small evidence machine around it, and leave them with a clearer workflow than they had before.

The best targets are not problems so huge that a major platform will dominate them, and not problems so small that nobody will pay. Look for the middle:

- painful
- specific
- high-context
- document-heavy
- audit-sensitive
- workflow-specific
- unglamorous
- poorly served by generic tools

Good pain signals:

- "We have too many documents and nobody knows what changed."
- "Our review process lives in email, spreadsheets, and memory."
- "We tried AI, but we do not trust the outputs."
- "We need citations, audit trail, and reviewer signoff."
- "Our policies, procedures, contracts, or forms do not line up."
- "The vendor tool is too generic."
- "The big platform cannot model our weird workflow."
- "We need to prove what happened, not just summarize it."

### Best-Fit Contract Offers

Do not sell generic AI consulting. Sell specific evidence/workflow outcomes.

| Offer | Description | Early Price Range |
|---|---|---:|
| AI Evidence Audit | Inspect one messy document/process workflow and produce a source-traceable map of risks, gaps, duplicated work, missing ownership, and automation opportunities. | $5k-$15k |
| RAG / AI Trust Diagnostic | Evaluate an existing or planned chatbot/search workflow for retrieval quality, citation accuracy, hallucination risk, missed edge cases, and auditability gaps. | $8k-$25k |
| Reviewer Workbench Prototype | Build a small internal tool where AI proposes findings, sources are shown, reviewers accept/reject/escalate, and outputs become reports. | $25k-$75k |
| Regulated Document Drift Detector | Compare versions of policies, procedures, forms, filings, contracts, or SOPs and surface meaningful changes with evidence. | $20k-$80k |
| Human-In-The-Loop AI Workflow | Wrap an existing manual review process with structured intake, AI assistance, citations, reviewer states, and exportable decision records. | $40k-$120k |
| AI Evals Harness For A Company Workflow | Build tests for grounding, citation correctness, schema validity, tool-call correctness, regression cases, and failure taxonomy. | $15k-$60k |
| AI Cost And Token Efficiency Audit | Trace token/cost usage by stage, identify wasted context and unnecessary model calls, and propose cheaper routing, caching, and deterministic pre-processing. | $5k-$20k |

The strongest fixed-scope package:

> In 4 weeks, I will turn one messy expert review workflow into a source-traceable AI-assisted evidence workbench with citations, reviewer decisions, eval checks, and an exportable report.

### Why Big Vendors Do Not Automatically Replace This

Large vendors chase broad repeatable markets. Your opportunity is company-specific mess.

You want problems that are:

- too company-specific for a generic platform
- too small for enterprise vendors to customize deeply
- too sensitive to hand entirely to AI
- too workflow-specific for out-of-the-box tools
- too document-heavy for normal software teams to enjoy
- too important for "just use ChatGPT"
- too ambiguous for pure automation

You are doing the work between generic AI tooling and the company's actual weird process.

### Best Initial Buyers

Start with companies and firms that already have high-trust review workflows:

- insurance MGAs, carriers, TPAs, and compliance vendors
- legal operations teams
- regulatory/compliance consultancies
- fintech compliance teams
- healthcare-adjacent administration vendors
- construction/renovation companies with complex quoting or compliance
- small/mid-size SaaS companies drowning in internal policies and customer obligations
- expert-services firms that want AI leverage but need auditability

The most efficient path may be selling through firms that already serve regulated clients. They bring domain trust and distribution. You bring the technical evidence-system layer.

### Contractor Kit

Build a reusable kit before doing broad outreach:

- one-page offer sheet
- 3-minute demo video
- flagship repo/demo
- sample evidence report
- sample eval report
- architecture diagram
- discovery questionnaire
- fixed-scope proposal template
- security/data handling note
- 2-3 case studies

The kit should make one promise:

> I can make your messy expert review process inspectable, testable, and safer to automate.

### Progression Path

Do not guess the product too early. Let paid work teach you.

1. Custom projects: do bespoke work and learn where the pain clusters.
2. Reusable components: reuse evidence graph, trace logs, eval checks, reviewer states, report templates.
3. Productized service: sell the same shape repeatedly as a 3-6 week package.
4. Narrow product: only after repeated paid projects, extract the part clients keep needing.

The best first niche:

> Regulated document review workflows where teams need source-traceable AI outputs and human approval.

## Portfolio Diagnosis

Your repos already show technical chops. The problem is discoverability.

A busy hiring manager should not have to read a month of journals to understand the signal. You need to compress the work into portfolio surfaces.

The portfolio should prove:

1. You can build real AI systems, not demos that merely sound good.
2. You understand evidence, evals, and failure modes.
3. You can work in domain-heavy environments.
4. You can package complexity for human decision-making.
5. You can make AI systems cost-aware and token-efficient.
6. You can govern AI-assisted development work with traceability, gates, and evidence.
7. You can document and hand off work professionally.

The strongest portfolio story:

> I build trustworthy AI systems for messy, high-consequence domains. My flagship project is an AI evidence workbench for regulated insurance documents.

## Flagship Portfolio Project

Make `legal-tech-debt` the flagship.

Rename or frame the portfolio view as:

> AI Evidence Workbench For Regulated Documents

The README should quickly show:

- what it does
- who it is for
- why it matters
- how to run the demo
- screenshots
- sample output
- architecture
- evals
- limitations

### Minimum Flagship Demo

The minimum compelling demo:

1. Ingest a small real or realistic regulated document corpus.
2. Parse into stable source/node IDs.
3. Run detectors over policy-layer smells.
4. Build evidence bundles.
5. Produce reviewer-ready findings.
6. Show a static interactive drilldown report.
7. Run eval checks on grounding, schema validity, and citation presence.
8. Export a report.

The demo does not need real customers. It needs to show production-adjacent engineering maturity.

Production-adjacent means:

- real inputs, not toy prompts
- stable run IDs
- source IDs
- structured outputs
- failure cases
- testable claims
- eval checks
- reviewer states
- trace logs
- clear limits
- reproducible commands

### AI Signals To Add

Add these to make the repo read as AI-engineering-ready:

- RAG/retrieval demo with retrieval bundles
- trace JSONL for each run
- eval harness
- token/cost accounting by pipeline stage
- schema validation
- human review state: accepted, rejected, escalated
- failure taxonomy
- model/provider boundary docs
- static UI with drilldown
- performance notes
- demo video or animated walkthrough

### Suggested README Opening

Use language like:

> This project ingests regulated insurance document sources, builds a traceable evidence graph, detects policy/compliance smells, generates reviewer-ready findings, and produces audit-friendly reports with source citations. It is designed as a production-adjacent AI evidence workbench: source-grounded, eval-driven, human-reviewed, and explicit about uncertainty.

## Second Portfolio Candidate: Agentic SDLC Control System

Sandbox 005 could become a production-worthy portfolio project if it is developed into a crisp artifact.

Frame it externally as:

> Agentic SDLC Control System

or:

> Repo-Native AI Software Engineering Manager

or:

> Evidence-Driven Agentic Development Workflow

Do not force the digital-twin label in the public story. The digital-twin lens is useful privately, but the market-facing pain is clearer:

> AI-assisted software teams need a way to turn conversations and experiments into scoped work, verification evidence, risk records, and human-approved progress without creating a second planning database.

### What It Should Demonstrate

A strong Sandbox 005 portfolio version should show:

- task contracts with origin: conversation, experiment, backlog, ADR, external requirement, or mixed
- experiment-to-requirement promotion
- experiment-backed V&V records
- evidence bundles
- risk register
- hard, advisory, and human-only gates
- agent role model
- generated status surface from repo truth
- stale artifact and missing-evidence detection
- traceability from conversation/experiment to requirement to task to validation evidence

### Minimum Demo

The smallest impressive demo:

1. Start with a messy conversation or experiment note.
2. Promote one durable observation into a requirement candidate.
3. Create a task contract.
4. Run a small implementation.
5. Produce an evidence bundle.
6. Run deterministic checks.
7. Add an experiment-backed V&V note.
8. Generate a disposable status report from repo files.
9. Show human approval state.

This would be especially relevant for AI Systems Engineer, AI Evals Engineer, AI Platform Engineer, Agentic AI Engineer, and engineering-productivity roles.

## Supporting Case Studies

Create short case studies so the other work supports the main story without distracting from it.

### Case Study 1: WindowConfigurator

Title:

> Server-Authoritative Product Configuration For Renovation Workflows

Signal:

- domain modeling
- exact measurements
- pricing validation
- backend authority
- session lifecycle
- CRM-safe boundaries
- webhook handoff
- tests and roadmap discipline

One-line pitch:

> A B2B configuration platform that turns messy renovation quoting into authoritative, validated, CRM-safe configuration state.

AI extension worth preserving:

> AI-Assisted Measure-Up Intake and Pricing Capture Harness.

The voice measure-up feature is the most intuitive product wedge: the contractor dictates room, dimensions, glass package, and section/style sequence during an on-site measure-up; the system builds a draft item, then deterministic backend validation and pricing decide what is actually acceptable.

The pricing capture feature is the deeper systems wedge: authorized manufacturer/dealer configurators can be exercised by a deterministic harness that generates configurations, captures evidence, and infers pricing tables or anomalies. AI belongs around ambiguous labels, error classification, and evidence reports, not as the authority for prices.

Expanded AI systems story:

> Designed AI-assisted field intake and pricing-evidence workflows that convert spoken contractor measure-ups and authorized configurator runs into validated, auditable quote data without letting the model own pricing, dimensions, or order readiness.

### Case Study 2: Grannies House Trials

Title:

> Agent-Based Testing Harness For Hidden Infrastructure

Signal:

- simulation thinking
- causal systems
- puzzle matrix / scenario-generation grammar
- agent-based testing
- constrained interventions
- evidence projection
- human adjudication
- small repeatable slice

One-line pitch:

> A tiny simulation/game prototype where role-differentiated tester agents intervene in a hidden drainage system, expose different failure modes, and build evidence for host-judged conclusions.

### Case Study 3: Physics / HPC Lab

Title:

> High-Performance Time Dilation Simulation Lab

Signal:

- numerical computing
- C++ or Rust core
- SIMD/vectorization
- multithreading
- benchmarks
- precision/error analysis
- visualization
- known-baseline validation

One-line pitch:

> A high-performance numerical sandbox for reproducing standard relativistic time-dilation relationships and exploring alternative computational framings.

## Open Source Contribution Strategy

Open-source contributions should reinforce the resume story, not scatter it.

The resume story:

> I contribute to open-source tooling for traceable, evaluated, human-reviewable AI systems.

Pick one observability project, one eval/RAG project, and one domain-specific legal/evidence project. Avoid trying to contribute everywhere.

### Primary AI Infrastructure Targets

| Project | Why It Fits | Best Contribution Shape |
|---|---|---|
| Langfuse | Open-source LLM engineering platform for traces, evals, prompt management, and datasets. | Eval workflows, OpenTelemetry docs, self-hosting fixes, reviewer/eval recipes. |
| Arize Phoenix | AI observability and evaluation platform for traces, RAG debugging, human annotations, and experiments. | RAG/evidence examples, eval docs, integrations, bug fixes. |
| OpenInference | OpenTelemetry conventions and instrumentation for AI apps. | Instrumentation examples, semantic convention improvements, tests for agents/retrieval/tool calls. |

Best personal fit:

> OpenInference or Phoenix, because your portfolio story depends on traceability and production-adjacent AI observability.

### Primary Eval / RAG Targets

| Project | Why It Fits | Best Contribution Shape |
|---|---|---|
| Ragas | RAG evaluation, test generation, and feedback loops. | Legal/regulatory RAG eval examples, citation-grounding metrics, retrieval diagnostics. |
| DeepEval | Pytest-like LLM evaluation framework for RAG, agents, hallucination, and tool correctness. | Regulated-document review examples, schema/citation checks, custom metrics. |
| Promptfoo | LLM evals, red teaming, CI/CD testing, RAG and agent testing. | Evidence-focused test templates, legal/compliance red-team examples, CI recipes. |

Best personal fit:

> Ragas or DeepEval, because they let you connect your legal-tech-debt work to public AI eval tooling.

### Legal / Domain Targets

| Project | Why It Fits | Best Contribution Shape |
|---|---|---|
| LegalBench | Open benchmark for legal reasoning in LLMs. | Insurance/regulatory/policy-layer benchmark tasks or evaluation docs. |
| LegalBench-RAG | Legal retrieval benchmark. | Retrieval diagnostics, citation quality checks, benchmark notes, legal source grounding examples. |
| eyecite | Legal citation extraction used in open legal-data ecosystems. | Citation patterns, tests, docs, statutory/regulatory extraction improvements. |
| Free Law Project / CourtListener | Open legal data infrastructure. | API tooling, citation workflows, docs, legal-data integration examples. |

Best personal fit:

> LegalBench-RAG or eyecite, because they make the legal/evidence side credible outside your own repo.

### HPC / Scientific Computing Side Lane

Keep this as a secondary proof lane.

| Project | Why It Fits | Best Contribution Shape |
|---|---|---|
| Kokkos | Major C++ performance portability project for HPC across CPUs/GPUs. | Documentation, examples, tests, small performance-oriented fixes. |
| AMReX | Massively parallel adaptive mesh refinement framework. | Tutorials, examples, documentation, small bug fixes. |
| SciML | Scientific computing and high-performance differential equation ecosystem. | Example notebooks, solver docs, benchmark reproduction, physics/simulation examples. |

Best personal fit:

> Kokkos if you want serious C++/HPC signal; SciML if you want a smoother path into scientific-computing contribution.

### Quantum / Annealing Optimization Targets

Keep this practical and skeptical. The strongest contribution shape is not "prove quantum supremacy." It is:

> Formulate AI workflow bottlenecks as optimization problems, compare solvers, and publish the evidence.

| Project | Why It Fits | Best Contribution Shape |
|---|---|---|
| D-Wave Ocean / dimod | Core open-source QUBO/BQM modeling ecosystem for annealing and hybrid solvers. | Examples, docs, benchmark cases, AI workflow formulations. |
| D-Wave scikit-learn feature-selection examples | Direct AI/ML application of annealing-style optimization. | Better examples, reproducible reports, comparison against classical baselines. |
| OpenJij | Open-source simulated annealing and simulated quantum annealing for QUBO/Ising. | Benchmarks, tutorials, solver comparison reports, integration examples. |
| PyQUBO / qubovert | Readable QUBO formulation libraries. | Examples for RAG chunk selection, dataset reduction, model routing, or feature selection. |
| Fixstars Amplify Benchmark | Benchmarking framework for annealing, Ising machines, and mathematical solvers. | Solver comparison reports and AI-workflow benchmark scenarios. |

Best personal fit:

> OpenJij plus D-Wave Ocean examples, because they let you build a practical benchmark without needing to overclaim gate-model quantum readiness.

### Suggested Contribution Sequence

- [ ] Month 1: contribute one example/docs PR to Ragas or DeepEval using regulated-document evaluation.
- [ ] Month 2: contribute one tracing/instrumentation PR or example to OpenInference or Phoenix.
- [ ] Month 3: contribute one legal-domain PR to LegalBench-RAG or eyecite.
- [ ] Optional side lane: build one QUBO/annealing benchmark over AI feature selection, dataset reduction, RAG chunk selection, or model routing.
- [ ] Parallel: integrate one of these tools into `legal-tech-debt` and document the integration.

High-signal PR ideas:

- Citation-grounding eval example for RAG systems.
- Reviewer-state workflow example: accepted, rejected, escalated.
- OpenTelemetry trace attributes for retrieval bundles and source IDs.
- Legal/regulatory RAG evaluation cookbook.
- Schema-validity and provenance checks for LLM-generated findings.
- Sanitized insurance policy document evaluation dataset.
- Human-in-the-loop annotation workflow example.
- Failure taxonomy for RAG findings: unsupported, weak source, missing citation, retrieval miss.

## Six-Month Career Runway

You said you can remain unemployed for about six months without worrying too much. That is a real strategic asset.

The goal is not to spend six months wandering. The goal is to convert time into portfolio leverage, market clarity, and optionality.

### Month 1: Compress And Clarify

Goal:

> Make the strongest existing work legible.

Checklist:

- [ ] Create flagship README for `legal-tech-debt`.
- [ ] Create one-command demo.
- [ ] Produce one static drilldown report screenshot.
- [ ] Write case study for legal-tech-debt.
- [ ] Write case study for Sandbox 005 / Agentic SDLC Control System.
- [ ] Write case study for WindowConfigurator.
- [ ] Add a WindowConfigurator AI extension note: voice measure-up intake plus pricing capture harness.
- [ ] Write case study for Grannies House Trials.
- [ ] Draft resume positioning around applied AI/evidence/evals.
- [ ] Create a simple portfolio index.

Do not build lots of new features in Month 1. Package the signal first.

### Month 2: Add AI Evals And Traceability

Goal:

> Make the flagship read as modern AI engineering.

Checklist:

- [ ] Add trace JSONL for pipeline runs.
- [ ] Add eval checks for schema validity.
- [ ] Add eval checks for citation/source presence.
- [ ] Add eval checks for unsupported finding language.
- [ ] Add reviewer states.
- [ ] Add failure taxonomy.
- [ ] Add architecture diagram.
- [ ] Add limitations section.
- [ ] Record 3-minute demo.
- [ ] If Sandbox 005 becomes a second flagship, create a manual demo showing experiment-to-requirement-to-V&V traceability.
- [ ] If RenoNerd becomes a second/third demo, prototype voice-to-configuration as transcript-to-validated-draft first, not live microphone magic.
- [ ] Define a deterministic pricing-capture harness design before adding any AI interpretation layer.

By the end of Month 2, you should have a portfolio repo that can support job applications and contractor conversations.

### Month 3: Market Contact And Interview Readiness

Goal:

> Start testing the market while improving the artifact.

Checklist:

- [ ] Apply to 25-40 targeted roles.
- [ ] Reach out to 15-25 humans in legal AI, compliance AI, insurance AI, evals, or AI observability.
- [ ] Ask for feedback, not jobs, in the first message.
- [ ] Create a contractor one-pager.
- [ ] Prepare interview stories around each repo.
- [ ] Practice explaining evals, RAG, traces, and human review clearly.
- [ ] Build 2-3 technical deep dives from the flagship.
- [ ] Open 1-2 small, high-quality PRs against an eval or observability project.

Target roles:

- Applied AI Engineer
- Senior AI Engineer
- LLM Evaluation Engineer
- AI Reliability Engineer
- Legal AI Engineer
- Compliance AI Engineer
- Agent Systems Engineer

### Month 4: Choose A Primary Lane

Goal:

> Decide whether the strongest traction is employee, contractor, or productized pilot.

Checklist:

- [ ] Review responses from applications and outreach.
- [ ] Identify which story gets the best reaction.
- [ ] Refine demo around market feedback.
- [ ] If employee traction is strong, intensify interview prep.
- [ ] If contractor traction is strong, package a fixed-scope pilot.
- [ ] If product traction is strong, define a buyer-specific evidence report.

Possible fixed-scope contractor pilot:

> In 3 weeks, I will build a source-grounded AI review prototype over one document workflow, including retrieval bundles, findings, citations, reviewer states, eval checks, and an exportable report.

### Month 5: Close Or Double Down

Goal:

> Convert the portfolio into money or a clearly superior next step.

Checklist:

- [ ] Negotiate offers.
- [ ] Pitch 3-5 paid pilots if contracting.
- [ ] Publish one polished essay.
- [ ] Add one more demo scenario if it directly improves close rate.
- [ ] Avoid starting unrelated projects.

Essay topic:

> Building AI Evidence Systems Instead Of Chatbots

### Month 6: Decision Month

Goal:

> Pick the path with the best combination of money, learning, and fit.

Options:

- Accept strong employee role.
- Take a focused contract and continue interviewing.
- Build a productized pilot with a specific partner.
- Extend runway only if traction justifies it.

Decision criteria:

- Does this path improve your long-term career capital?
- Does it pay enough to reduce anxiety?
- Does it keep you near evidence systems, evals, domain complexity, and trustworthy AI?
- Does it avoid trapping you in repetitive low-leverage work?

## Resume Positioning

### Headline Options

Use one of these:

- Applied AI Engineer specializing in evidence systems, evals, and regulated-domain workflows.
- Senior software engineer building source-traceable AI systems for high-consequence document review.
- AI reliability/evals engineer focused on retrieval, provenance, reviewer workflows, and audit-ready outputs.
- Cost-aware AI engineer building evaluated, source-grounded workflows with token/cost instrumentation.

### Summary Option

> Applied AI/software engineer with a portfolio of source-traceable evidence systems, domain-specific workflow engines, and simulation prototypes. Strong at turning messy expert domains into structured artifacts: retrieval bundles, evidence graphs, evaluator checks, reviewer states, reports, cost traces, and authoritative backend boundaries. Interested in AI systems where correctness, provenance, human judgment, and efficient model use matter.

### Portfolio Bullets

Legal-tech-debt:

- Built a proof-of-concept AI evidence workbench for regulated insurance documents, including source indexing, policy-layer smell detection, retrieval bundles, reviewer-ready findings, and drilldown reports.
- Designed artifact contracts with run identity, timestamps, schema versions, stable source IDs, and evidence provenance.
- Implemented graph-based gap detection for missing policy-layer evidence where absence must be represented as a first-class finding.
- Positioned the pipeline for token-efficient AI use by emphasizing deterministic parsing, graph traversal, retrieval bundles, and human review before expensive model synthesis.

Sandbox 005 / Agentic SDLC:

- Designed an agentic SDLC control-system concept that turns conversation and experiment evidence into scoped task contracts, evidence bundles, risk records, and human-approved progress.
- Added experiment-to-requirement and experiment-backed V&V flows so sandbox probes, prototype surprises, failed runs, and playtest observations can become durable requirements or validation evidence.
- Separated SDLC tooling from product runtime agents, preserving distinct memory, permission, validation, and audit boundaries.

WindowConfigurator:

- Designed and implemented a domain-driven B2B configuration platform with server-authoritative pricing, validation, exact fractional measurements, session lifecycle modeling, and CRM-safe handoff boundaries.
- Converted domain rules into durable architecture decisions, tests, and implementation phases.
- Designed AI-assisted field measure-up intake where spoken contractor observations become draft configurations while deterministic backend services retain authority over pricing, validation, measurements, and order readiness.
- Proposed an authorized pricing-capture harness that uses deterministic browser automation and combinatorial test generation to reconstruct pricing evidence from painful manufacturer/dealer configurators, with AI limited to label mapping, error classification, and report synthesis.

Grannies House Trials:

- Built a deterministic simulation/playtest prototype where constrained player actions reveal hidden infrastructure state through evidence-board projection and host-judged outcomes.
- Separated simulation truth, tester-facing projection, and human adjudication into explicit system boundaries.
- Designed a puzzle-matrix vocabulary that generates scenario beats, motifs, trap paths, and goal checks for agent-based testing of hidden-system reasoning.
- Modeled Builder, Chaos Tester, and Systems Auditor roles as distinct testing strategies that reveal practical completion, stress/failure boundaries, and evidence-driven diagnosis.

Physics/HPC:

- Building a high-performance numerical simulation sandbox for relativistic time-dilation experiments, emphasizing known-baseline validation, performance benchmarking, precision analysis, and reproducible experiment configs.

## The Physics/HPC Repo Strategy

The physics work can help, but only if presented carefully.

Make it a technical proof piece, not a manifesto.

Recommended framing:

> High-performance numerical experiments in relativistic systems using time dilation as the primary computational lens. The project first reproduces standard special relativity results, then explores alternative formulations through reproducible simulations.

Recommended first milestone:

- [ ] Simulate one million constant-velocity worldlines.
- [ ] Compute Lorentz factor and accumulated proper time.
- [ ] Validate against closed-form expected values.
- [ ] Compare scalar CPU, vectorized CPU, and parallel CPU implementations.
- [ ] Plot runtime, error, and memory behavior.
- [ ] Document precision tradeoffs.

Recommended stack:

- C++20 core
- CMake
- Google Benchmark
- Catch2 or GoogleTest
- OpenMP or SIMD path
- Python only for plotting
- Optional CUDA later

The portfolio value is:

- HPC/data layout
- numerical correctness
- performance measurement
- scientific discipline
- low-level engineering

Do not lead with this for legal/compliance AI jobs. Let it be the surprising technical depth piece.

## What To Avoid

Avoid:

- generic chatbot demos
- vague AI automation claims
- five new unfinished repos
- theory-heavy physics docs without runnable simulations
- legal claims without source trails
- reports without evals
- dashboards with no evidence loop
- spending the six months only polishing
- market validation theater before you have a crisp demo
- selling yourself as a founder if you currently need a career platform

The danger is not lack of intelligence. The danger is scattering your energy across many fascinating systems without compressing any one of them into a market-readable artifact.

## The Best Next 14 Days

If I had to pick only the next 14 days:

1. Create a portfolio-grade README for legal-tech-debt.
2. Add or polish a one-command demo.
3. Generate one excellent static drilldown report.
4. Add basic eval checks.
5. Write the legal-tech-debt case study.
6. Draft the resume summary.
7. Record a rough 3-minute walkthrough.
8. Draft a one-page contractor offer sheet.
9. Choose one open-source target and find 3 candidate starter issues.
10. Add token/cost accounting notes or a lightweight cost table to the flagship demo.

Do not wait for the perfect market analysis before making the artifact sharper. A demo proves capability. Market validation proves a business. You currently need both eventually, but the demo comes first for career leverage.

## Questions To Ponder

These are worth revisiting weekly:

1. Which project gives me energy after three hard hours?
2. Which project would a stranger understand fastest?
3. Which artifact would make an employer believe I can ship trustworthy AI?
4. Which parts of the work feel like play but still produce professional value?
5. What am I avoiding because it would make the work visible to judgment?
6. Am I building a platform, or am I proving one valuable loop?
7. Does this week create portfolio evidence, market contact, or both?
8. Am I separating speculation from proof?
9. What would I show in the first 10 minutes of an interview?
10. What would I sell as a three-week paid pilot?
11. Did this requirement come from conversation, experiment evidence, external constraint, or all three?
12. Does this experiment support requirements discovery, V&V, or both?

## Final Recommendation

For the next six months, treat your life like a focused research-and-career lab.

Primary career lane:

> Applied AI / evals / evidence systems for regulated domains.

Important differentiator:

> Efficient, cost-aware AI systems that avoid wasting tokens and expose cost alongside quality.

Primary portfolio artifact:

> Legal-tech-debt as an AI Evidence Workbench.

Second portfolio candidate:

> Sandbox 005 as an Agentic SDLC Control System for evidence-driven AI-assisted development.

Secondary proof artifacts:

> WindowConfigurator for domain/backend authority, Grannies House Trials for simulation/evidence design, physics/HPC for low-level numerical chops.

Target compensation:

> $180k-$240k base as a realistic employee target, with $250k-$300k possible in the right AI/regulatory/fintech/legal role.

Contractor target:

> $175-$225/hr for implementation, $250-$350/hr for specialized regulated AI evidence/evals packages.

The deepest theme:

> You are not trying to make AI sound smart. You are trying to make complex systems inspectable.

That is a good career. It is also a good way to spend a life.

## Sources Consulted For Market Context

These sources were used for current-market grounding during the conversation:

- Built In AI Engineer Salary: https://builtin.com/salaries/us/ai-engineer
- Glassdoor Artificial Intelligence Engineer Salary: https://www.glassdoor.com/Salaries/united-states-artificial-intelligence-engineer-salary-SRCH_IL.0%2C13_KO14%2C46.htm
- Salary.com AI Engineer Salary: https://www.salary.com/research/salary/hiring/ai-engineer-salary
- Fieldguide AI Engineer, Quality/Evals posting: https://jobs.ashbyhq.com/fieldguide/f4f0aea0-826d-451f-bd17-b04772e221cc/
- Deepgram Model Evaluation QA Lead posting: https://jobs.ashbyhq.com/Deepgram/1111c5de-2f90-4f38-a353-115a64a9ca33/
- Firecrawl Research Engineer, Evals posting: https://jobs.ashbyhq.com/firecrawl/25092c0e-9a32-4191-af79-050738213704
- Jump Applied AI Evaluation Scientist posting: https://jobs.ashbyhq.com/jump-app/76f95a94-b5d8-4701-a5d2-bce54cc333b6/
- Titan AI Applied AI Engineer posting: https://jobs.ashbyhq.com/titan-ai/297cf9a9-289d-4cd5-a4a1-1e051f6f5d64/
- Newfront Senior AI Engineer posting: https://jobs.ashbyhq.com/newfront/03cb6d44-29d1-4f8f-b3b5-a330b97ffcdd/
- Eigen Labs Agentic AI Engineer posting: https://jobs.ashbyhq.com/eigen-labs/c02fa001-23c9-4d68-8c0a-e27a742d76a4
- LeoTech AI/LLM Evaluation and Alignment Engineer posting: https://jobs.lever.co/LEOTechnologies/1847504a-c707-443a-9554-eb154ef1cd60
- LangSmith AI Observability: https://info.langchain.com/AI-Observability
- Arize Phoenix docs: https://arize.com/docs/phoenix
- Braintrust: https://www.braintrust.dev/
- Langfuse docs: https://langfuse.com/docs
- Patronus AI docs: https://docs.patronus.ai/docs
- OpenAI Evals guide: https://platform.openai.com/docs/guides/evals
- OpenAI Trace Grading guide: https://platform.openai.com/docs/guides/trace-grading
- Norm Ai platform: https://www.norm.ai/platform/
- Thomson Reuters CoCounsel: https://www.thomsonreuters.com/en/cocounsel
- Harvey Knowledge: https://www.harvey.ai/brand/platform/knowledge
- Anthropic Circuit Tracing: https://transformer-circuits.pub/2025/attribution-graphs/methods.html
- Anthropic open-source circuit tracing tools: https://www.anthropic.com/research/open-source-circuit-tracing
- OpenAI sparse circuits research: https://openai.com/index/understanding-neural-networks-through-sparse-circuits/
- Langfuse GitHub: https://github.com/langfuse/langfuse
- Arize Phoenix GitHub: https://github.com/Arize-ai/phoenix
- OpenInference GitHub: https://github.com/Arize-ai/openinference
- Ragas GitHub: https://github.com/explodinggradients/ragas
- DeepEval GitHub: https://github.com/confident-ai/deepeval
- Promptfoo GitHub: https://github.com/promptfoo/promptfoo
- LegalBench GitHub: https://github.com/HazyResearch/legalbench
- LegalBench-RAG GitHub: https://github.com/zeroentropy-cc/legalbenchrag
- eyecite GitHub: https://github.com/freelawproject/eyecite
- Free Law Project GitHub: https://github.com/freelawproject
- Kokkos GitHub: https://github.com/kokkos/kokkos
- AMReX GitHub: https://github.com/AMReX-Codes/amrex
- SciML GitHub: https://github.com/SciML
- FrugalGPT paper: https://arxiv.org/abs/2305.05176
- RouteLLM project: https://sky.cs.berkeley.edu/project/routellm/
- RouteLLM GitHub: https://github.com/lm-sys/RouteLLM
- LLMRouter GitHub: https://github.com/ulab-uiuc/LLMRouter
- LiteLLM GitHub: https://github.com/BerriAI/litellm
- Helicone caching docs: https://docs.helicone.ai/features/advanced-usage/caching
- Helicone cost tracking docs: https://docs.helicone.ai/references/how-we-calculate-cost
- GPTCache GitHub: https://github.com/zilliztech/GPTCache
- prompt-cache GitHub: https://github.com/messkan/prompt-cache
- Microsoft LongLLMLingua research page: https://www.microsoft.com/en-us/research/?p=978312
- Microsoft LLMLingua GitHub: https://github.com/microsoft/LLMLingua
- vLLM GitHub: https://github.com/vllm-project/vllm
- vLLM project site: https://vllm.ai/
- SGLang docs: https://docs.sglang.io/
- SGLang GitHub: https://github.com/sgl-project/sglang
- DSPy project site: https://dspy.ai/
- DSPy GitHub: https://github.com/stanfordnlp/dspy
