# Venue Categories — Where to Seek (and What to Skip)

Categories, not a fixed list. Verify each with the qualification checklist in `SKILL.md` §4 before
building a submission.

## Tier 0 — Multi-Platform Cloud Stacks & Edge Infrastructures (DA 90–100)
- **Google Cloud Storage (`storage.googleapis.com` — DA 100):** Standalone entity nodes, XML sitemaps, robots.txt.
- **Cloudflare Pages Global Edge (`pages.dev` — DA 92):** Clean URLs, global edge caching, instant indexing.
- **Cloudflare Workers Edge API (`workers.dev` — DA 92):** Dynamic JSON-LD schema resolvers and developer tools.
- **Amazon AWS S3 (`s3.amazonaws.com` — DA 96):** Static website buckets with public read policies.
- **Google Colab Notebooks (`colab.research.google.com` — DA 95):** Interactive `.ipynb` developer notebooks with executable code and contextual entity links.
- **Wayback Machine / Internet Archive (`archive.org` — DA 99):** Permanent historical snapshots of master cloud hubs.
*Why Tier 0:* Unrivaled crawl priority, root domain authority inheritance, zero account friction, and multi-referring domain diversification. See `references/cloud-stacking-recipes.md`.

## Tier 1 — Ownership-verified registries (find these first)
- Language package registries (PyPI, npm, crates.io, Maven Central, RubyGems, NuGet, Go module proxy).
- Plugin/marketplace registries for the relevant platform.
- Domain-specific model/tool registries (e.g. MCP-style registries) where ownership is proven from a repo or package.
- Store listings tied to an account the owner owns.
*Why first:* Durable, auto-imported by downstream directories, no anti-abuse friction.

## Tier 2 — Open publishing (no account)
- Platforms with an open content API where publishing needs no signup (e.g., Telegra.ph, Write.as).
*Use sparingly and only with genuinely useful, unique content. Enforce rate limit backoffs.*

## Tier 3 — Free directories that accept submissions
- Category tool directories (developer, AI, design, SaaS, productivity, open-source).
- "Alternative to <competitor>" directories (e.g., OpenAlternative).
- Open-source and startup listing directories.
*Look for a genuinely free submission/claim route; skip anything paid-only.*

## Tier 4 — Profiles & citations
- Developer/social profiles, startup profiles, bookmark/curation platforms that are public.
*Expect many to be noindex/nofollow — value is entity/citation and brand co-occurrence, not ranking.*

## Tier 5 — Content & community
- The owner's own domain (docs, changelog, comparisons, tutorials).
- Genuine community participation where the product answers a real question.

## Skip immediately
- **Automated GitHub PRs, Issues, Gists, or repos for SEO backlinks:** Violates GitHub Acceptable Use Policies and Community Guidelines against search engine manipulation and spam; puts the owner's GitHub account at risk of suspension.
- Paid-only listings.
- SMS/phone-verified or OAuth-only (unless the owner performs the human step).
- Interactive-captcha walls.
- Paused or dead submissions.
- Geo-blocked from the owner's region.
- Anything requiring disposable accounts, fabricated identities, or anti-bot circumvention.
- Reciprocal/tiered link networks and duplicate-content farms.

## Qualification reminders
- **Referring Domain Diversification:** Spread links across multiple root platforms rather than bunching on a single venue.
- Check whether prior similar listings are indexed (`site:venue.com "similar tool"`) before investing.
- Record expected `link_rel` and `robots` at qualification time so verification is fast.
- Prefer venues with zero-to-one human steps.
