---
name: foundation-launch-citations
description: Run a legitimate product-launch, citation, and multi-platform cloud-stacking campaign for a website, app, or open-source project. Use when the user wants listings in tool directories, package registries, ownership-verified claims, multi-cloud entity stacks (Google Cloud, Cloudflare, AWS), profiles, or intro content, plus a tracked status table and a self-contained HTML status dashboard. Provides a setup interview, venue qualification, cloud-stacking recipes, browser-automation recipes, verification, and strict platform safety guardrails. Do not use for disposable accounts, captcha/anti-bot circumvention, GitHub SEO PR/gist spam, fake reviews, or link pyramids.
---

# Foundation Launch, Citation & Cloud Stack Builder

Get a real product discovered across directories, registries, profiles, high-authority cloud infrastructures, and content platforms using the owner's real identity. Optimize for durable, indexable placements across diverse referring domains — never for raw link count.

## Quick start (read this first)
1. Scrape the product page + repo + docs; copy `assets/LAUNCH_CONTEXT.template.md` to `LAUNCH_CONTEXT.md` and fill it.
2. Run the setup interview (`references/interview-questions.md`); confirm the context file.
3. Build and qualify the venue list (§3). Drop paid/paused/dead/geo-blocked venues now.
4. Deploy Tier 0 Multi-Platform Cloud Stacks across distinct hyper-scalers (Google Cloud, Cloudflare, AWS) with XML sitemaps and mesh ring interlinking (§5 & `references/cloud-stacking-recipes.md`).
5. Claim ownership-verified registries (§5, Tier 1).
6. Submit to free, relevant directories using the owner's real accounts (§5, Tier 3).
7. Publish unique intro articles on open platforms and canonical technical writeups on your own domain.
8. Verify every placement (§6). A "submitted" page is never a success.
9. Report the status table, generate the self-contained HTML status dashboard, and list owner action items (§7).

## Operating rules
1. **Real Identity Only:** Use the owner's real identity. One honest account per platform.
2. **Strict GitHub Account Protection:** **NEVER build backlinks on GitHub.** Do not create automated pull requests (e.g. awesome-lists), issues, public gists, or disposable repositories for SEO links. Violating GitHub Acceptable Use policies puts the owner's GitHub account at risk of shadowbanning or termination.
3. **Referring Domain (RD) Diversification:** Never concentrate an entire campaign on a single platform (e.g. 20 links on Google Cloud Storage only). Maximize unique, high-authority root referring domains (`pages.dev`, `workers.dev`, `storage.googleapis.com`, `s3.amazonaws.com`, `telegra.ph`, `archive.org`).
4. **Cloud Mesh Ring Interlinking:** Cloud nodes must be interconnected in a bidirectional mesh ring, cross-referencing each other while funneling all primary PageRank and entity triples to the canonical money domain.
5. **Discovery & Indexation Protocols:** Every cloud deployment MUST include a valid `sitemap.xml` and an explicit `robots.txt` (`User-agent: *`, `Allow: /`, `Sitemap: ...`).
6. **Explicit Consent & Secrets:** Get explicit consent before logging into anything. Store secrets securely (`chmod 600`).
7. **Obey ToS & Rate Limits:** If a site enforces rate limits (e.g. Write.as 429) or WAF blocks, stop, back off, or hand over. Never fight anti-bot defenses.
8. **Entity Graph Integrity:** Embed nested JSON-LD schema (`TechArticle`, `Person`, `Organization`, `Service`) with unambiguous `@id` cross-referencing and `sameAs` entity correlations to resolve entity debt.
9. **Verify Before Counting:** HTTP 200 + target money URL present + robots meta verified (`index, follow`).
10. **Idempotency:** Check `LAUNCH_STATUS.md` before every action; never re-submit a row that is `live`, `pending_review`, or `blocked`.
11. **Guardrails (§9):** No disposable accounts, no captcha/anti-bot circumvention, no spun content.

## Agent decision tree
- Multi-cloud infrastructure available (GCP, Cloudflare, AWS)? → deploy Tier 0 Cloud Stack nodes with sitemaps & schema (§5, Tier 0).
- Ownership-verifiable (repo/package/registry)? → claim it (§5, Tier 1).
- Open API, no account needed? → publish with rate-limit backoff (§5, Tier 2).
- Free form, needs only the owner's real login? → submit (§5, Tier 3).
- GitHub PR / Gist for SEO link? → **ABORT.** Mark `blocked(policy)`, protect GitHub account (§9).
- Paid-only / SMS / OAuth-only / interactive captcha? → mark `blocked`, add an owner action item, move on.

## 0. Scope
- **In scope:** announce a product/repo/app; multi-platform cloud stacking across Google Cloud, Cloudflare, and AWS; listings in directories, registries, marketplaces; profiles/citations/PR carrying product URL + source URL + author entity; XML sitemaps and indexation protocols; repeatable supervised process.
- **Out of scope (never):** GitHub link spamming, disposable-account creation, account farming, captcha/anti-bot circumvention, fake reviews, reciprocal/tiered link pyramids, duplicate content for links.

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
- Multi-Platform Cloud Stacks (Google Cloud Storage, Cloudflare Pages/Workers, AWS S3).
- Category tool directories (tool/AI/dev/design/SaaS).
- Package/marketplace registries (often derived from repo metadata).
- Competitor/alternative comparison directories (e.g. OpenAlternative).
- Profile, citation, and startup listings.

**Qualification checklist (score every venue):**

| Check | Pass condition |
|-------|----------------|
| Relevance | Category genuinely matches |
| Referring Domain | Adds a distinct root referring domain (not redundant) |
| Free path | A genuinely free submission/claim/deploy route exists |
| Mode | Web form, API, CLI deployment, or ownership-verified claim — not paid |
| Platform Safety | Complies with platform policies (zero GitHub link spamming) |
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
- **A — Owner's real accounts (recommended):** owner provides login/CLIs for accounts they already own (e.g., `gcloud`, `wrangler`, `aws`).
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
0. **Tier 0 — Multi-Platform Cloud Stacks (DA 90–100):**
   - Deploy standalone, entity-rich HTML nodes to Google Cloud Storage (`storage.googleapis.com`), Cloudflare Pages (`pages.dev`), Cloudflare Workers (`workers.dev`), and AWS S3 (`s3.amazonaws.com`).
   - Inject nested JSON-LD schema (`TechArticle`, `Person`, `Organization`, `Service`).
   - Generate and upload `sitemap.xml` and `robots.txt` (`Allow: /`, `Sitemap: ...`).
   - Interlink all nodes in a cross-cloud mesh ring and submit master hubs to Wayback Machine (`web.archive.org` — DA 99).
   - Technical details: `references/cloud-stacking-recipes.md`.
1. **Tier 1 — Ownership-verified registries:**
   - Package / marketplace / registry claims (npm, PyPI, crates.io, etc.).
2. **Tier 2 — Open publishing APIs:**
   - Long-form markdown publishing (Telegra.ph, Write.as). Apply rate-limit backoff on HTTP 429.
3. **Tier 3 — Free directories:**
   - Free tool directories and comparison sites (e.g. OpenAlternative) using the owner's real login.
4. **Tier 4 — Profiles and citations:**
   - Public founder profiles and business directory listings.
5. **Tier 5 — Content and community:**
   - Authoritative tutorials, open developer notebooks (Google Colab `.ipynb`), and docs on own domain.

Per venue:
1. Check `LAUNCH_STATUS.md` — never re-submit a `live` / `pending_review` / `blocked` row.
2. Open the free route (skip if the only route is paid).
3. Fill verbatim from `LAUNCH_CONTEXT.md` (descriptor, both URLs, author).
4. Complete verification via the approved inbox or ownership proof.
5. Capture the confirmation ID and the expected live URL.
6. Write the status row immediately.

- Technical techniques: `references/browser-recipes.md` and `references/cloud-stacking-recipes.md`.
- **Content quality rule:** Open-platform content must be genuinely useful, deeply researched, and unique — never a link dump. Thin or duplicated content gets deindexed.

## 6. Phase 5 — Verification (non-negotiable)
A placement is not a success until all of these pass:
| Check | Method |
|-------|--------|
| HTTP 200 | `curl -I` with a browser UA, or a live browser |
| Both URLs present | Product URL + source URL in rendered source |
| Indexability | Inspect `<meta name="robots">`; record noindex/nofollow |
| Schema Valid | Verify nested JSON-LD schema renders without syntax errors |
| Correct entity | Brand + author render as intended |

Then re-verify every `live` row after 48–72 h for retroactive moderation removal.
Record the effective value: `live+indexed+dofollow` > `live+noindex` > `pending` > `blocked`.

## 7. Phase 6 — Track & report
`LAUNCH_STATUS.md` schema:
```
venue | type | mode | submitted_at | confirm_id | live_url | link_rel | robots | status | owner_action_needed
```
Statuses: `todo` · `blocked(paid|sms|oauth|captcha|geo|policy)` · `submitted` · `pending_review` · `live` · `live_noindex` · `removed`.

Report: counts per status, unique Referring Domains (RDs), and the list of `owner_action_needed` items (one clear human step each).

**Deliver a status dashboard, not just a table.** Render `LAUNCH_STATUS.md` as a
self-contained HTML dashboard with `assets/build_status_dashboard.py`:

```bash
python3 assets/build_status_dashboard.py --input LAUNCH_STATUS.md \
  --out LAUNCH_DASHBOARD.html --title "Acme launch — citation status"
```

It shows summary stat cards (total, live, blocked, todo), **unique referring
domains** across live placements, an indexability split (`live` vs
`live_noindex`), the open `owner_action_needed` items, a status distribution
chart, and a searchable/filterable table. No CDN, no build step — safe to open
offline or email to the owner. Ship the HTML **alongside** the Markdown: the
Markdown stays the source of truth, the HTML is the human-facing view.

- Keep `LAUNCH_STATUS.md` as the single source of truth; the dashboard is
  generated output, never hand-edited.
- One row per venue, updated immediately after each submission or verification.
- Never mark `live` without the Phase 5 checks passing.

## 8. Success criteria
- At least N high-relevance live placements across M distinct referring domains.
- Every claimed URL confirmed live + indexable, or explicitly marked noindex.
- Zero GitHub backlink submissions (full account safety).
- Zero disposable accounts and zero anti-abuse workarounds used.
- Valid XML sitemaps and robots.txt active on all cloud stacks.
- Clean `LAUNCH_CONTEXT.md` + `LAUNCH_STATUS.md` the owner can continue from.
- A self-contained HTML status dashboard generated from `LAUNCH_STATUS.md`.

## 9. Guardrails — never do
- **Never build backlinks on GitHub:** Do not create PRs to awesome-lists, open issues, create public gists, or build disposable repos on GitHub for SEO links. Protect the owner's GitHub account from policy flags and bans.
- Create accounts with disposable/temp email or fabricate identities.
- Solve or bypass captchas, SMS, or anti-bot challenges.
- Automate OAuth consent flows for account creation.
- Post fake reviews, ratings, or testimonials.
- Build tiered/bookmark link pyramids or reciprocal link farms.
- Cross-post duplicate or spun content to manufacture links.
- Ignore robots/ToS or hammer endpoints.

If a venue requires any of these, mark it `blocked` and move on, or hand the single human step to the owner.

## 10. Failure handling
Short table here; full matrix in `references/failure-modes.md`.
| Symptom | Action |
|---------|--------|
| GitHub Link Building Attempt | **ABORT.** Mark `blocked(policy)`. Never risk GitHub account status |
| Single-Platform Stagnation | Diversify across distinct root platforms (Google, Cloudflare, AWS) |
| Write.as 429 Too Many Requests | Enforce exponential backoff; pause automated submissions |
| Rentry `<meta robots="noindex">` | Mark as `live_noindex`; count toward citations only |
| GCP Service Account 0-Quota | Use Shared Drives or request user OAuth consent for personal Drive |
| Wrangler 4 Delegation Prompt | Pass `--force` to deploy directly to Pages without interactive prompts |
| Interactive captcha | Stop; mark `blocked(captcha)`; offer a human step |
| Confirmation email never arrives | Try another route or the real mailbox; else blocked |
| Cloudflare/WAF block | Cool down; lower request rate; do not escalate |
| Paid wall | Mark `blocked(paid)`; skip |

## 11. Dependencies & setup
- Cloud CLIs (optional but recommended: `gcloud`, `wrangler`, `aws`).
- CDP-capable browser automation (Playwright / Puppeteer / equivalent).
- HTTP client for verification (`curl` / fetch / python `urllib`).
- Secret storage (`chmod 600` file or OS keychain/manager).
- Never install or use a captcha-solving service.

## References & assets
- `references/cloud-stacking-recipes.md` — full multi-cloud stacking guide (Google, Cloudflare, AWS, Mesh rings, Sitemaps).
- `references/interview-questions.md` — full setup question bank.
- `references/browser-recipes.md` — extended automation recipes and edge cases.
- `references/failure-modes.md` — full failure matrix.
- `references/venue-examples.md` — curated venue categories to seek.
- `assets/LAUNCH_CONTEXT.template.md` — starting template for `LAUNCH_CONTEXT.md`.
- `assets/build_status_dashboard.py` — renders `LAUNCH_STATUS.md` as a self-contained HTML status dashboard (status counts, unique referring domains, indexability split, owner actions, filterable table).
