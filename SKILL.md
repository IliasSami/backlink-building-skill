---
name: foundation-launch-citations
description: Run a legitimate product-launch and citation campaign for a website, app, or open-source project. Use when the user wants listings in tool directories, package or marketplace registries, ownership-verified claims, profiles, or intro content, plus a tracked status table. Provides a setup interview, venue qualification, browser-automation recipes, verification, and guardrails. Do not use for disposable accounts, captcha or anti-bot circumvention, fake reviews, or link pyramids.
---

# Foundation Launch & Citation Builder

Get a real product discovered across directories, registries, profiles, and content platforms using the
owner's real identity. Optimize for durable, indexable placements — never for link count.

## Quick start (read this first)
1. Scrape the product page + repo + docs; copy `assets/LAUNCH_CONTEXT.template.md` to `LAUNCH_CONTEXT.md` and fill it.
2. Run the setup interview (`references/interview-questions.md`); confirm the context file.
3. Build and qualify the venue list (§3). Drop paid/paused/dead/geo-blocked venues now.
4. Claim ownership-verified registries first (§5).
5. Submit to free, relevant directories using the owner's real accounts (§5).
6. Publish one unique intro article on an open platform and one on your own domain.
7. Verify every placement (§6). A "submitted" page is never a success.
8. Report the status table and owner action items (§7).

## Operating rules
1. Use the owner's real identity. One honest account per platform.
2. Get explicit consent before logging into anything. Store secrets securely.
3. Obey ToS, robots, and rate limits. If a site fights automation, stop and hand the human step over.
4. Prefer quality over quantity. Five relevant indexed placements beat fifty noindex ones.
5. Never fabricate product claims, reviews, or authors.
6. Verify before you count. HTTP 200 + both URLs present + robots meta inspected.
7. Be idempotent. Check the status table before every submission; never re-submit a row that is `live`, `pending_review`, or `blocked`.
8. Stay inside the guardrails (§9). No disposable accounts, no captcha/anti-bot circumvention.

## Agent decision tree
- Ownership-verifiable (repo/package/registry)? → claim it (§5, tier 1).
- Open API, no account needed? → publish (§5, tier 2).
- Free form, needs only the owner's real login? → submit (§5, tier 3).
- Paid-only / SMS / OAuth-only / interactive captcha? → mark `blocked`, add an owner action item, move on.

## 0. Scope
- **In scope:** announce a product/repo/app; listings in directories, registries, "awesome" lists, marketplaces; profiles/citations/PR carrying product URL + source URL + author; a repeatable supervised process.
- **Out of scope (never):** disposable-account creation, account farming, captcha/anti-bot circumvention, fake reviews, reciprocal/tiered link pyramids, duplicate content for links.

## 1. Phase 0 — Setup interview
Run before any submission. Ask in small batches; offer "auto" (agent infers by scraping).
- **Auto-research first:** scrape the product page, repo, docs, and store listing. Extract brand, descriptor, features, category, pricing, platforms, author, and existing listings. Present a filled draft and ask the owner to confirm/correct.
- **Question bank + full tables:** `references/interview-questions.md`.
- **Always resolve the credential/identity model (A/B/C)** in §3.

## 2. Phase 1 — Context files
Create two files and keep them separate:
- `LAUNCH_CONTEXT.md` — immutable product facts. Start from `assets/LAUNCH_CONTEXT.template.md`.
- `LAUNCH_STATUS.md` — living status table (§7).

Rules:
- Every asset must carry: money URL + source URL + author entity + verbatim descriptor.
- Keep the descriptor identical everywhere to avoid entity fragmentation.
- Secrets never go in either file.

## 3. Phase 2 — Venue discovery & qualification
**Sources**
- Category tool directories (tool/AI/dev/design/SaaS).
- Package/marketplace registries (often derived from repo metadata).
- "Awesome" lists and community directories (usually a PR → human/GitHub step).
- Competitor/alternative comparison directories.
- Profile and startup listings.

**Qualification checklist (score every venue):**

| Check | Pass condition |
|-------|----------------|
| Relevance | Category genuinely matches |
| Free path | A genuinely free submission/claim route exists |
| Mode | Web form, API, or ownership-verified claim — not paid |
| Auth need | No SMS, no OAuth-only (or owner accepts the human step) |
| Anti-bot | No interactive captcha required to complete |
| Link behavior | Record dofollow/nofollow and indexed/noindex |
| Indexability history | `site:venue.com "similar listing"` — if prior similar listings are noindexed/gone, deprioritize |
| Owner effort | Estimate human steps (0 / 1 click / full account). Prefer 0–1 |
| Moderation | Reasonable or clearly stated |
| Dedup | Product not already listed |

- **Output:** a prioritized table `venue | type | free? | auth | mode | expected link | owner_effort | status` in `LAUNCH_STATUS.md`.
- **Discard** dead (404), paid-only, paused, or geo-blocked venues before building any submission.

## 4. Phase 3 — Credentials & identity
Model (ask the owner to choose; **default A**):
- **A — Owner's real accounts (recommended):** owner provides login for accounts they already own.
- **B — Owner-managed inbox:** owner provides a real mailbox for verification links (app password/API); owner approves account creation.
- **C — Manual handoff:** agent prepares everything, then pauses; owner completes account creation / OAuth consent / captcha / SMS.

Hard rules:
- Never invent identities or use disposable/temp email to create accounts.
- Never automate OAuth consent for account creation — that is a human step (model C).
- For scale, the owner may use their own real domain aliases (e.g. `+launch@theirdomain`).
- Prefer ownership-verified claims; they are the strongest and most durable listings.
- Store secrets in a `chmod 600` file or a secret manager. Never log them.

## 5. Phase 4 — Submission loop (priority order)
Run this order. Do not skip to a lower tier while a higher tier is available.
1. **Ownership-verified registries** (package / marketplace / registry claims).
2. **Open publishing APIs** (no account required).
3. **Free directories** that need only the owner's real login.
4. **Profiles and citations.**
5. **Content and community** (own domain + open platforms + genuine participation).

Per venue:
1. Check `LAUNCH_STATUS.md` — never re-submit a `live` / `pending_review` / `blocked` row.
2. Open the free route (skip if the only route is paid).
3. Fill verbatim from `LAUNCH_CONTEXT.md` (descriptor, both URLs, author).
4. Complete verification via the approved inbox or ownership proof.
5. Capture the confirmation ID and the expected live URL.
6. Write the status row immediately.

- Browser technique details: `references/browser-recipes.md`.
- **Content quality rule:** open-platform content must be genuinely useful and unique — never a link dump. Thin or duplicated content gets removed.

## 6. Phase 5 — Verification (non-negotiable)
A placement is not a success until all of these pass:
| Check | Method |
|-------|--------|
| HTTP 200 | `curl -I` with a browser UA, or a live browser |
| Both URLs present | Product URL + source URL in rendered source |
| Indexability | Inspect `<meta name="robots">`; record noindex/nofollow |
| Correct entity | Brand + author render as intended |

Then re-verify every `live` row after 48–72 h for retroactive moderation removal.
Record the effective value: `live+indexed+dofollow` > `live+noindex` > `pending` > `blocked`.

## 7. Phase 6 — Track & report
`LAUNCH_STATUS.md` schema:
```
venue | type | mode | submitted_at | confirm_id | live_url | link_rel | robots | status | owner_action_needed
```
Statuses: `todo` · `blocked(paid|sms|oauth|captcha|geo|policy)` · `submitted` · `pending_review` · `live` · `live_noindex` · `removed`.

Report: counts per status + the list of `owner_action_needed` items (one clear human step each).

## 8. Success criteria
- At least N ownership-verified or high-relevance live placements (N set by the owner).
- Every claimed URL confirmed live + indexable, or explicitly marked noindex.
- Zero disposable accounts and zero anti-abuse workarounds used.
- Clean `LAUNCH_CONTEXT.md` + `LAUNCH_STATUS.md` the owner can continue from.
- Owner action items limited to genuine human steps (OAuth consent, SMS, etc.).

## 9. Guardrails — never do
- Create accounts with disposable/temp email or fabricate identities.
- Solve or bypass captchas, SMS, or anti-bot challenges.
- Automate OAuth consent flows for account creation.
- Post fake reviews, ratings, or testimonials.
- Build tiered/bookmark link pyramids or reciprocal link farms.
- Cross-post duplicate content to manufacture links.
- Ignore robots/ToS or hammer endpoints.

If a venue requires any of these, mark it `blocked` and move on, or hand the single human step to the owner.

## 10. Failure handling
Short table here; full matrix in `references/failure-modes.md`.
| Symptom | Action |
| Form API 400 "missing fields" | Framework state; re-fill with the native setter; check hidden required radios |
| Interactive captcha | Stop; mark `blocked(captcha)`; offer a human step |
| Confirmation email never arrives | Try another route or the real mailbox; else blocked |
| Content removed after publish | Mark `removed`; do not re-post the duplicate |
| Cloudflare/WAF block | Cool down; lower request rate; do not escalate |
| Paid wall | Mark `blocked(paid)`; skip |

## 11. Dependencies & setup
- CDP-capable browser automation (Playwright / Puppeteer / equivalent).
- HTTP client for verification (`curl` / fetch).
- Secret storage (`chmod 600` file or OS keychain/manager).
- Optional: registry CLI for the target ecosystem.
- Never install or use a captcha-solving service.

## References & assets
- `references/interview-questions.md` — full setup question bank.
- `references/browser-recipes.md` — extended automation recipes and edge cases.
- `references/failure-modes.md` — full failure matrix.
- `references/venue-examples.md` — curated venue categories to seek.
- `assets/LAUNCH_CONTEXT.template.md` — starting template for `LAUNCH_CONTEXT.md`.
