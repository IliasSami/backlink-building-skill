# Backlink Building Skill for Claude, Codex & OpenCode

**Foundation Launch & Citation Builder** — a reusable AI-agent skill that runs a structured,
legitimate backlink-building and citation campaign for a website, app, or open-source project.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Format: Agent Skill](https://img.shields.io/badge/format-SKILL.md-blue.svg)
![Agents: Claude Code · Codex · OpenCode](https://img.shields.io/badge/agents-Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20OpenCode-purple.svg)

> Build **foundation backlinks** the right way: ownership-verified registries, free tool
> directories, profiles, citations, and genuinely useful content — with a setup interview, venue
> qualification, browser-automation recipes, verification, and hard guardrails.

## Table of contents
- [What is this?](#what-is-this)
- [Who it's for](#who-its-for)
- [Highlights](#highlights)
- [Compatibility](#compatibility)
- [Install](#install)
- [Quick start](#quick-start)
- [What's inside](#whats-inside)
- [Guardrails — what this skill will NOT do](#guardrails--what-this-skill-will-not-do)
- [FAQ](#faq)
- [Keywords](#keywords)
- [License](#license)

## What is this?

A **backlink building skill** packaged as a portable `SKILL.md` + `references/` bundle. Any AI
coding agent that supports skills — **Claude Code, Codex, OpenCode**, and other harnesses — can load
it and run a supervised link-building / citation campaign from an interview to verified, tracked
placements.

It is the *legitimate* playbook: real identity, ownership-verified registry claims, free directories
that invite submissions, and one honest account per platform. It optimizes for **durable, indexable
placements**, not raw link count.

## Who it's for

- **Indie makers and founders** launching a product, app, or SaaS.
- **Open-source maintainers** who want a project discovered in tool directories and registries.
- **SEO, growth, and digital-PR folks** who want a repeatable, agent-runnable process.
- **AI-agent users** who want a ready-made skill instead of re-prompting from scratch.

## Highlights

- **Setup interview** — a structured question bank that builds full campaign context, with an
  auto-research step that pre-fills answers by scraping the product page, repo, and docs.
- **Venue discovery & qualification** — a checklist to score directories, registries, and profiles,
  including indexability-history and owner-effort checks.
- **Priority order** — ownership-verified registries → open publishing APIs → free directories →
  profiles → content, so effort goes to the highest-value, lowest-friction placements first.
- **Browser-automation recipes** — the general, neutral techniques that actually work for filling
  modern forms (native value setters, react-select comboboxes, iframe scoping, snapshot refs).
- **Verification** — HTTP 200 + both URLs present + robots meta inspected, plus a 48–72 h re-check.
- **Tracking** — a status schema and a clean `LAUNCH_CONTEXT.md` / `LAUNCH_STATUS.md` handoff.
- **Guardrails** — explicit limits that keep the campaign legitimate.

## Compatibility

| Agent / harness | How to use |
|-----------------|------------|
| **Claude Code** | Place the folder in your skills directory (e.g. `~/.claude/skills/`) |
| **Codex CLI** | Place the folder in your skills directory |
| **OpenCode** | Place the folder in your skills directory |
| **Cursor / other agents** | Paste `SKILL.md` into context, or point the agent at the file |

> The folder name should match the `name` in the `SKILL.md` frontmatter:
> `foundation-launch-citations`. Check your harness docs for its exact skills path.

## Install

```bash
git clone https://github.com/IliasSami/backlink-building-skill.git \
  ~/.claude/skills/foundation-launch-citations
```

Then ask your agent to use the **`foundation-launch-citations`** skill.

## Quick start

1. The agent scrapes your product page, repo, and docs and drafts `LAUNCH_CONTEXT.md`.
2. It runs the setup interview and confirms the context.
7. It builds and qualifies the venue list.
4. It claims ownership-verified registries first.
5. It submits to free, relevant directories using your real accounts.
6. It publishes one unique intro article on an open platform and one on your own domain.
7. It verifies every placement.
8. It reports the status table and any owner action items.

## What's inside

```
foundation-launch-citations/
├── SKILL.md                          # core playbook (lean)
├── references/
│   ├── interview-questions.md        # full setup question bank
│   ├── browser-recipes.md            # extended automation recipes
│   ├── failure-modes.md              # full failure matrix
│   └── venue-examples.md             # venue tiers to seek / skip
└── assets/
    └── LAUNCH_CONTEXT.template.md    # ready-to-fill product-facts template
```

## Guardrails — what this skill will NOT do

- Create accounts with disposable/temp email or fabricate identities.
- Solve or bypass captchas, SMS, or anti-bot challenges.
- Automate OAuth consent flows for account creation.
- Post fake reviews, ratings, or testimonials.
- Build tiered/bookmark link pyramids or reciprocal link farms.
- Cross-post duplicate content to manufacture links.

If a venue requires any of these, the skill marks it `blocked` and moves on.

## FAQ

**Is this black-hat SEO?**
No. It is built around real identity, ownership-verified listings, and directories that invite
submissions. It explicitly refuses disposable-account farming, captcha circumvention, and link
pyramids.

**Which AI agents does it work with?**
Claude Code, Codex, and OpenCode are the primary targets, but any agent that can read a `SKILL.md`
can use it.

**Does it need my Google/Gmail account?**
Only if you choose the owner-managed inbox model for verification links. The skill supports a
manual-handoff model where you complete any OAuth/captcha step yourself.

**What is a "foundation backlink"?**
The first set of authoritative listings, citations, and profiles that establish a new site's or
product's entity and discoverability.

**Do I need SEO experience?**
No. The skill runs the setup interview and handles qualification and tracking.

**Is it free?**
Yes — the skill and repo are MIT-licensed. The campaign targets free venues; paid placements are
explicitly skipped.

## Keywords

backlink building · backlink building skill · link building · SEO skill for AI agents · Claude skill ·
Claude Code skills · agent skills · Codex skill · OpenCode skill · citation building ·
directory submission · digital PR · foundation backlinks · agentic SEO · AI agent SEO ·
technical SEO · SEO automation · startup launch SEO

## License

MIT © 2026 Ilias Ahmed. See [LICENSE](LICENSE).
