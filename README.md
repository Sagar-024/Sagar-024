<div align="center">

<h1>hey, i'm sagar</h1>

<p><em>building autonomous agents & evaluation infrastructure at the intersection of AI and systems — one deterministic loop at a time</em></p>

[![LinkedIn](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sagar-kharal)
[![Email](https://img.shields.io/badge/email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sagarkharal024@gmail.com)
[![GitHub](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sagar-024)

</div>

---

## currently shipping

> **Repatch** — Autonomous engineering agent that reproduces bugs, authors tests, applies fixes, and opens PRs. 100% autonomous bug lifecycle. Built-in "Inviolable Loop" for empirical verification. Semantic Path Grounding to eliminate hallucinations. [`TypeScript` `Docker` `Nixpacks` `LLM Tool Calling`](https://github.com/Sagar-024/Repatch)

> **vela-cascade-eval** — Deterministic evaluation harness for scheduling agents. Two agents, 10 machine-checkable invariants, 500+ seeded scenarios, byte-identical determinism. Proves cascade-aware architecture eliminates 888 double-bookings & 841 priority violations. [`TypeScript` `Vitest` `Property-Based Testing`](https://github.com/Sagar-024/vela-cascade-eval)

> **groundedness-engine** — Zero-LLM structural verification for AI claims. 4 ordered deterministic checks (citation → section → retrieval → quote match). Catches "3 years → 5 years" hallucinations without a single model call. [`TypeScript` `Deterministic Verification`](https://github.com/Sagar-024/groundedness-engine)

---

## tech stack

<div align="center">

**languages & runtimes**

![TypeScript](https://img.shields.io/badge/typescript-007ACC?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)

**frontend & full-stack**

![Next.js](https://img.shields.io/badge/next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/react-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Tailwind CSS](https://img.shields.io/badge/tailwindcss-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)
![Framer Motion](https://img.shields.io/badge/framer_motion-0055FF?style=flat-square&logo=framer&logoColor=white)

**AI / ML / evaluation**

![SBERT](https://img.shields.io/badge/sbert-FF6F00?style=flat-square&logo=pytorch&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![NetworkX](https://img.shields.io/badge/networkx-013243?style=flat-square&logo=python&logoColor=white)
![Gemini API](https://img.shields.io/badge/gemini_api-4285F4?style=flat-square&logo=google&logoColor=white)

**infrastructure & tooling**

![Docker](https://img.shields.io/badge/docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-316192?style=flat-square&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/mongodb-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Git](https://img.shields.io/badge/git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github_actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)

</div>

---

## featured projects

<table>
<tr>
<td width="50%" valign="top">

### [Repatch](https://github.com/Sagar-024/Repatch) ���
**Autonomous Engineering Agent — "Junior Dev in a Box"**

- **Empirical TDD**: Authors reproduction tests before any code modification
- **Inviolable Loop**: State-machine orchestration (UNDERSTAND → EXPLORE → REPRODUCE → PLAN → EXECUTE → VERIFY → SUBMIT) with backtracking
- **Semantic Grounding**: Map of Truth file-tree indexing eliminates path hallucinations
- **Sandboxed Execution**: Ephemeral OCI-compliant environments via Nixpacks + Docker
- **Multi-LLM**: OpenAI, Anthropic, Gemini, Mimo — strategy pattern for inference

`TypeScript` `Node.js` `Docker` `Nixpacks` `Git` `LLM Tool Calling` `State Machines`

</td>
<td width="50%" valign="top">

### [vela-cascade-eval](https://github.com/Sagar-024/vela-cascade-eval)
**Deterministic Scheduling Agent Evaluation Harness**

- **Two agents, one clean diff**: NaiveAgent (baseline) vs CascadeAwareAgent (global view) — identical except for cascade awareness
- **10 machine-checkable invariants**: No double-booking, priority consistency, invalidation propagation, determinism (byte-identical replay)
- **500+ seeded scenarios**: 9 cascade classes, 713 conflicts generated, deterministic via mulberry32 RNG
- **Honest failure model**: Reference agent shows 121 recovery failures (true resource exhaustion), not weakened assertions

`TypeScript` `Vitest` `Property-Based Testing` `State Machines` `Evaluation Infrastructure`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [groundedness-engine](https://github.com/Sagar-024/groundedness-engine)
**Deterministic Structural Verification for AI Claims**

- **Zero LLM calls** — all checks are string-based, deterministic, auditable
- **4 ordered checks**: citation_present → section_exists → section_retrieved → quote_matched
- **Catches hallucinations**: "3 years" → "5 years" quote mismatch detected without semantic reasoning
- **Retrieval tracing**: Detects when AI cites a section it never actually saw
- **Standalone npm package** — import into any pipeline (legal, medical, financial, technical)

`TypeScript` `Deterministic Verification` `Zero-LLM Architecture`

</td>
<td width="50%" valign="top">

### [CAREERLENS](https://github.com/Sagar-024/CAREERLENS) ���
**Asynchronous Semantic Resume ↔ JD Matching Engine**

- **6-stage async pipeline**: Parse → Extract → Embed → Graph → Score → Explain
- **SBERT bi-encoder** (`all-MiniLM-L6-v2`) + cosine similarity in 384-dim space
- **59-node skill ontology** (NetworkX DiGraph) with 2-hop transferability (Docker → Kubernetes)
- **Implicit skill recovery**: 25% more skills surfaced from experience bullets vs keyword baselines
- **Dynamic weight allocation**: Same resume scored differently for startup vs research-lab JDs
- **PDF report generation** with SHAP-style explainability & interview intelligence

`Next.js 14` `FastAPI` `Python` `SBERT` `spaCy` `NetworkX` `PostgreSQL` `Prisma`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa](https://github.com/Sagar-024/Nexa) ��� · [Live ↗](https://nexa0ai.netlify.app)
**AI Trip Planner — Personalized Itineraries from Preferences**

- **Gemini API** powered: top-10 recommendations + custom day-wise itineraries
- **Smart destination engine** learns preferences, cuts through generic guides
- **Fully responsive** with Framer Motion animations, mobile-first
- **Deployed on Vercel** — production-grade frontend

`React` `Next.js` `Gemini API` `Tailwind CSS` `Framer Motion`

</td>
<td width="50%" valign="top">

### [ValoCoach Dashboard](https://github.com/Sagar-024/ValoCoach-Player-Dashboard) ���
**Valorant Player Analytics Dashboard**

- **Real-time stats**: K/D, headshot %, combat score — all animated
- **Match history** with Won/Lost/Draw filtering
- **Dark/Light theme** (no flash bug — SSR hydration solved)
- **Data viz with Recharts**, Framer Motion polish

`Next.js 15` `TypeScript` `Recharts` `Framer Motion` `Tailwind CSS`

</td>
</tr>
</table>

---

## what i care about

| principle | what it means in practice |
|-----------|---------------------------|
| **determinism over vibes** | Seeded RNG, byte-identical replay, zero-flaky tests, invariant-based evaluation |
| **empirical verification** | Every claim backed by reproducible artifact (test, trace, benchmark, report) |
| **systems thinking** | Agents as state machines, not prompt chains; orchestration > prompting |
| **honest failure models** | Recovery exhaustion �� bug; double-booking �� "edge case" — it's a violated invariant |
| **zero-LLM verification** | Structural checks first, semantic reasoning layered on top, never the reverse |

---

## experience

**Web Developer Intern** · XpertStim IT Services Pvt. Ltd. · *May 2025 – Jul 2025 · Remote*

- Sole frontend dev on a Tours & Travel product — built 8+ UI sections (hero, itinerary cards, booking flow) from scratch
- Built reusable component library with Framer Motion animations; pixel-perfect across mobile, tablet, desktop
- Stack: React.js, Tailwind CSS

---

## open to work

**Final-year CS student** (graduating May 2026, GPA 8.4) actively looking for **frontend or full-stack roles at startups** — especially teams building:

- AI agent infrastructure / evaluation / observability
- Developer tooling (CLI, IDE extensions, CI/CD)
- High-trust systems where determinism & verification matter

I don't just apply — I build. If you want someone to come in, ship fast, and care about the product, let's talk.

Open to **2–3 week trial arrangements**. No bureaucracy needed.

���� **[shoot me an email](mailto:sagarkharal024@gmail.com)** or find me on **[LinkedIn](https://linkedin.com/in/sagar-kharal)**

---

<div align="center">
<sub>if you made it this far, you might as well just reach out ���</sub>
</div>