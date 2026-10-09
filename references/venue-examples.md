# Venue Categories — Where to Seek (and What to Skip)

Categories, not a fixed list. Verify each with the qualification checklist in `SKILL.md` §4 before
building a submission.

## Tier 1 — Ownership-verified registries (find these first)
- Language package registries (PyPI, npm, crates.io, Maven Central, RubyGems, NuGet, Go module proxy).
- Plugin/marketplace registries for the relevant platform.
- Domain-specific model/tool registries (e.g. MCP-style registries) where ownership is proven from a
  repo or package.
- Store listings tied to an account the owner owns.
Why first: durable, auto-imported by downstream directories, no anti-abuse friction.

## Tier 2 — Open publishing (no account)
- Platforms with an open content API where publishing needs no signup.
Use sparingly and only with genuinely useful, unique content.

## Tier 3 — Free directories that accept submissions
- Category tool directories (developer, AI, design, SaaS, productivity, open-source).
- "Alternative to <competitor>" directories.
- Open-source and startup listing directories.
Look for a genuinely free submission/claim route; skip anything paid-only.

## Tier 4 — Profiles & citations
- Developer/social profiles, startup profiles, bookmark/curation platforms that are public.
Expect many to be noindex/nofollow — value is entity/citation, not ranking.

## Tier 5 — Content & community
- The owner's own domain (docs, changelog, comparisons, tutorials).
- "Awesome" lists and community directories (usually a GitHub pull request — a human step).
- Genuine participation where the product answers a real question.

## Skip immediately
- Paid-only listings.
- SMS/phone-verified or OAuth-only (unless the owner performs the human step).
- Interactive-captcha walls.
- Paused or dead submissions.
- Geo-blocked from the owner's region.
- Anything requiring disposable accounts, fabricated identities, or anti-bot circumvention.
- Reciprocal/tiered link networks and duplicate-content farms.

## Qualification reminders
- Check whether prior similar listings are indexed (`site:venue.com "similar tool"`) before investing.
- Record expected `link_rel` and `robots` at qualification time so verification is fast.
- Prefer venues with zero-to-one human steps.
