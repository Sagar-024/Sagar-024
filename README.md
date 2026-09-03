<div align="center">

## Currently

</div>
Top 5 PRs merged into [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow):

- **#373** [Check the no-B-frame constraint in doctor and the encoder](https://github.com/Hebbian-Robotics/hflow/pull/373): enforce a video safety invariant that earlier code only trusted, closing a silent decode-loss path.
- **#175** [Cache frame_stats per video to fix doubled decode cost](https://github.com/Hebbian-Robotics/hflow/pull/175): cut repeated video decode in half by memoizing frame-level computation per source video.
- **#103** [examples/lerobot: pusht to canonical MCAP converter](https://github.com/Hebbian-Robotics/hflow/pull/103): shipped the first end-to-end LeRobot dataset to canonical MCAP conversion path.
- **#127** [fix(catalog): coerce NumPy scalar measurements at the boundary; refuse the rest](https://github.com/Hebbian-Robotics/hflow/pull/127): stopped silent NumPy scalar corruption from reaching persisted measurements.
- **#345** [fix(video): refuse B-frame streams whose reorder tail a remux drops](https://github.com/Hebbian-Robotics/hflow/pull/345): reject input streams where remux drops the reorder tail, preventing downstream decode failures.

Issues I opened in the same window:

- **#376** [The fixed-GOP promise is stamped into provenance as "actually used" but is never measured on pass-through video](https://github.com/Hebbian-Robotics/hflow/issues/376)
- **#379** [prepared-manifest.json records how many episodes were converted but not which ones, so a corrupt or missing episode cannot be detected from the delivery](https://github.com/Hebbian-Robotics/hflow/issues/379)

[See all my merged PRs in HFlow](https://github.com/Hebbian-Robotics/hflow/pulls?q=is%3Apr+author%3ASagar-024+is%3Aclosed)

---

<div align="center">

## Who I Am

</div>
- 22-year-old engineer currently contributing at [HFlow](https://github.com/Hebbian-Robotics/hflow), a YC-backed robotics data platform.
- Merged 10 PRs in my first public week, including a LeRobot to MCAP converter and a silent NumPy data-corruption fix that passed unnoticed by the test suite.
- Work reviewed by Kingston Kuan, co-founder of HFlow (YC S26), available as a reference.
- Built a client-facing website from scratch during my summer Full-Stack Development internship, owning major features from requirements through pixel-perfect React and Tailwind implementation.
- Built a Land Purchase Risk Assessment project for Mireye's Co-founder & CTO, Shashwat Kapoor, who called it "excellent work" and praised the architecture and product thinking.
- Researched and published a hybrid AI resume-screening pipeline using Sentence-BERT and Phi-3.5, evaluated across 8,000 resume-JD pairs.
- Drove a 4-person team from data collection and experimentation through final publication.

---

<div align="center">

## Projects I Built on the Way

</div>
- **[Repatch](https://github.com/Sagar-024/Repatch)** (★1): Autonomous engineering agent that reproduces bugs, authors tests, applies fixes, opens PRs. 7-step state-machine orchestration (UNDERSTAND → EXPLORE → REPRODUCE → PLAN → EXECUTE → VERIFY → SUBMIT). Structured tool calling, Docker/Nixpacks sandboxing, Map of Truth / Semantic Path Grounding.
- **[vela-cascade-eval](https://github.com/Sagar-024/vela-cascade-eval)**: Deterministic evaluation harness for scheduling agents. 500+ seeded scenarios, 713 conflicts generated, 10 machine-checkable invariants, 1,000 determinism checks (byte-identical replay). Naive baseline: 888 double-bookings, 841 priority violations. Cascade-aware agent: zero safety violations, 121 recovery failures (true resource exhaustion).
- **[groundedness-engine](https://github.com/Sagar-024/groundedness-engine)**: Zero-LLM structural verification for AI claims. 4 ordered deterministic checks: citation present → section exists → section retrieved → quote matched. Catches "3 years → 5 years" hallucinations without a single model call. Standalone npm package.
- **[CAREERLENS](https://github.com/Sagar-024/CAREERLENS)** (★1): 6-stage semantic resume ↔ JD matching pipeline. SBERT bi-encoder (all-MiniLM-L6-v2) + cosine similarity in 384-dim space. 59-node skill ontology (NetworkX DiGraph) with 2-hop transferability (e.g., Docker → Kubernetes). Implicit skill recovery surfaces 25% more skills vs keyword baselines. 9.1% accuracy gain over tools like Jobscan. Dynamic weight allocation per role type. SHAP-style explainability + PDF report generation.
- **[Nexa](https://github.com/Sagar-024/Nexa)** (★1) · [Live](https://nexa0ai.netlify.app): AI trip planner powered by Gemini. Personalized itineraries from preferences, not generic guides. React/Next.js, Node/Express, Tailwind, Framer Motion.

---

<div align="center">

## What I Work On

</div>
### AI Agents & Agentic Systems

| Project | What It Does | Key Signal |
|---|---|---|
| **[Repatch](https://github.com/Sagar-024/Repatch)** | Autonomous bug-fixing agent | 7-step state-machine orchestration, structured tool calling, Docker/Nixpacks sandboxing, Map of Truth |
| **[vela-cascade-eval](https://github.com/Sagar-024/vela-cascade-eval)** | Deterministic evaluation harness | 10 invariants, 713 conflicts, seeded replay, honest failure model |
| **[groundedness-engine](https://github.com/Sagar-024/groundedness-engine)** | Structural claim verification | Zero-LLM deterministic checks, citation→section→retrieval→quote |
| **[hermes-agent](https://github.com/NousResearch/hermes-agent)** | Self-improving agent system | Contributor: TUI, MCP, cron, multi-platform gateway |

### Evaluation & Verification

| Project | What It Does | Key Signal |
|---|---|---|
| **[vela-cascade-eval](https://github.com/Sagar-024/vela-cascade-eval)** | Deterministic evaluation harness | 500+ scenarios, 10 invariants, 1,000 determinism checks |
| **[groundedness-engine](https://github.com/Sagar-024/groundedness-engine)** | Zero-LLM structural verification | 4 ordered checks, retrieval tracing, standalone npm pkg |
| **[Repatch](https://github.com/Sagar-024/Repatch)** | Empirical TDD loop | Reproduction tests authored before any fix, sandboxed verification |

### Full-Stack & Product Engineering

| Project | What It Does | Stack |
|---|---|---|
| **[Nexa](https://github.com/Sagar-024/Nexa)** | AI trip planner, personalized itineraries | Next.js, Gemini API, Tailwind, Framer Motion |
| **[CAREERLENS](https://github.com/Sagar-024/CAREERLENS)** | Semantic resume ↔ JD matching | Next.js, FastAPI, SBERT, NetworkX, PostgreSQL |
| **[EatHere](https://github.com/Sagar-024/Eathere)** | Location-based food discovery | React 19, Express, MongoDB, Geoapify |
| **[Job Board](https://github.com/Sagar-024/Job-board-web-app)** | Full-stack MERN job board | React, Node, Express, MongoDB, JWT |

---

<div align="center">

## GitHub Activity

</div>
![Profile Details](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Sagar-024)

![Top Languages](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Sagar-024)

---

<div align="center">

## What I'm Doing

</div>
- Building AI agent systems: autonomous engineering agents, orchestration, tool calling, verification, and agentic workflows.
- Engineering evaluation-first: deterministic experiments, invariants, seeded scenarios, replayable results, and honest failure models.
- Building full-stack products: React/Next.js, Node.js, Python, APIs, databases, deployment, and production interfaces.
- Learning in public: how determinism, verification, and reliable failure handling make AI systems trustworthy.
- Open to roles in AI engineering, agentic software engineering, full-stack, backend, and early-stage startup work.

---

<div align="center">

## Latest Writings & Talks

</div>
<!-- BLOG-POST-LIST:START -->
- [Deterministic Agent Evaluation: Why Invariants Beat Vibes](https://github.com/Sagar-024/vela-cascade-eval/blob/main/results/analysis.md)
- [Zero-LLM Verification: Catching Hallucinations Without Models](https://github.com/Sagar-024/groundedness-engine)
- [Semantic Resume Matching: Beyond Keyword Overlap](https://github.com/Sagar-024/CAREERLENS)
<!-- BLOG-POST-LIST:END -->

---

<div align="center">

## Recognition

</div>
- **Repatch**: Autonomous engineering agent with empirical TDD loop and sandboxed verification.
- **vela-cascade-eval**: Honest failure model with 121 recovery failures (true resource exhaustion), not weakened assertions.
- **groundedness-engine**: Structural verification layer designed to sit below semantic evaluation.
- **CAREERLENS**: 9.1% accuracy gain over keyword tools via SBERT + ontology transferability.
- **Finalist**: Task API Take-Home Assignment (production-grade MERN app).

---

<div align="center">

## Philosophy

</div>
> **Determinism over vibes. Empirical verification over claims. Honest failure models over hidden edge cases.**

I build tools where the verification *is* the product. If you can't replay it byte-for-byte, it's not evaluated, it's hoped for.

---

<div align="center">

## Connect

</div>
[![LinkedIn](https://img.shields.io/badge/-Sagar_Kharal-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/sagar-kharal)
[![Email](https://img.shields.io/badge/-sagarkharal024@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:sagarkharal024@gmail.com)
[![GitHub](https://img.shields.io/badge/-Follow-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sagar-024)
[![X](https://img.shields.io/badge/-@skharal4_s-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/skharal4_s)

---

<details>
<summary>Random Facts</summary>

- Run 3-5 agent instances concurrently for eval (Repatch, vela-cascade-eval, groundedness-engine all at once).
- Obsessed with seeded RNG determinism: `mulberry32` > `Math.random()` every time.
- Powered by filter coffee & late-night invariant debugging.
- "It works on my machine" → "It works in the sandbox with Nixpacks detection."
- Will genuinely do a 2-week trial. No bureaucracy. Ship or don't.

</details>

---

<div align="center">
<sub>if you made it this far, you might as well just reach out</sub>
</div>