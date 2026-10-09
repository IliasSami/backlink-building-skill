# Setup Interview — Full Question Bank

Run before any submission. Ask in small batches. For each question, offer **"auto"** (the agent
infers the answer by scraping and the owner just confirms/corrects).

## Pre-step — Auto-research (do this first)
Scrape and summarize:
- Product page (title, meta description, H1, feature bullets, pricing).
- Source repo (description, README, topics/tags, license, version).
- Docs / store listing.
- Existing listings (search the brand plus "directory" / the category).

Extract: brand, descriptor, features, category, pricing, platforms, author, existing listings.
Present a filled draft of the sections below and ask the owner to confirm or correct. This halves
the interview and prevents factual drift.

## 1. Product identity
| # | Question | Notes |
|---|----------|-------|
| 1 | Product/app name | Exact brand string, used verbatim everywhere |
| 2 | One-line descriptor | e.g. "<Name> — the free, open-source <category> tool" |
| 3 | Primary/money URL | The page you want to rank/drive to |
| 4 | Secondary/source URL | Repo, docs, or store page |
| 5 | Author/entity name + handles | Person or org; GitHub/X/etc. |
| 6 | Category + subcategory | Determines target directories |
| 7 | Pricing model | Free / OSS / freemium / paid (filters paid-only venues) |
| 8 | Platforms supported | e.g. macOS/Windows/Linux, web, mobile |
| 9 | Blocked/forbidden claims | Trademarks, competitor names to avoid in headlines |

## 2. Keyword + positioning
| # | Question | Notes |
|---|----------|-------|
| 10 | 5–10 target keywords | One primary per asset; map intent |
| 11 | Top 3 competitors | For "alternative to X" venues |
| 12 | Unique differentiators | 3 bullets, factual |
| 13 | Target audience | Devs, marketers, SMBs, etc. |

## 3. Credentials & identity model (critical)
Ask explicitly which model the owner wants:
- **A — Owner's real accounts (recommended):** owner provides login for accounts they already own.
- **B — Owner-managed inbox:** owner provides a real mailbox the agent may read for verification
  links (app password / API), but the owner approves account creation.
- **C — Manual handoff:** agent prepares everything and pauses; owner completes account creation,
  OAuth consent, or any captcha/SMS step personally.

| # | Question |
|---|----------|
| 14 | Which platforms do you already have accounts on? |
| 15 | May the agent automate login to *your own* accounts? (y/n per platform) |
| 16 | OAuth-only venues: will you perform the consent click, or skip them? |
| 17 | Preferred password policy / secret storage location (path or manager) |

> The agent never invents identities and never uses throwaway/disposable email to create accounts.
> OAuth that requires interactive consent is a **human step** (model C) — the agent never bypasses it.

## 4. Assets + scope
| # | Question |
|---|----------|
| 18 | Logo, screenshots, OG image paths/URLs |
| 19 | Preferred tone/voice |
| 20 | Venue types in scope (directories / registries / profiles / content / PR) |
| 21 | Venue types OFF-limits |
| 22 | Geography/language constraints |
| 23 | Time budget + "must-not" list |
| 24 | Target N (success threshold) for live, high-relevance placements |

## 5. Handoff contract
Confirm with the owner, in writing:
- Which model (A/B/C) applies per platform.
- Which actions the agent may take autonomously vs. must pause for.
- Where secrets are stored and how they are rotated.
- How owner action items will be surfaced (e.g. a list at the top of `LAUNCH_STATUS.md`).
