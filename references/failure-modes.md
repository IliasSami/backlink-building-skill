# Failure Modes — Full Matrix

Every failure maps to a status and an action. Never work around a control; log and move on.

| Symptom | Likely cause | Action | Status |
|---------|--------------|--------|--------|
| **GitHub Account Policy Risk** | Creating PRs, issues, gists, or repos for SEO backlinks | **CRITICAL:** Hard stop. Never build SEO links on GitHub; violates Acceptable Use. Protect owner's GitHub account | `blocked(policy)` |
| **Single-Platform Stagnation** | Building 20+ links on 1 domain (e.g. only GCS) | Enforce Referring Domain (RD) diversification across distinct root platforms (Google, Cloudflare, AWS, etc.) | `failed_diversification` |
| **Write.as 429 Too Many Requests** | Anonymous rate limit reached after 3–4 rapid posts | Enforce exponential backoff or use account auth tokens | `rate_limited` |
| **Rentry `<meta robots="noindex">`** | Markdown host enforces noindex on anonymous pastes | Mark as citation-only; do not count toward organic SERP indexed link targets | `live_noindex` |
| **dpaste / Pastebin 403 WAF block** | Cloudflare / anti-scraper bot challenge on verification | Use a real headless browser or deprioritize venue | `blocked(waf)` |
| **GCP Service Account 0-Quota** | Service accounts lack personal Google Drive storage | Use Google Workspace Shared Drives or request user OAuth consent | `blocked(oauth)` |
| **Wrangler 4 Delegation Prompt** | Wrangler 4 prompts when deploying new Pages projects | Pass `--force` to deploy directly to Pages without interactive prompts | `configuration_error` |
| Form API 400 "missing fields" | Framework state not updated; hidden required radio | Re-fill with native setter; check hidden required radios/selects | retry once, else `blocked(policy)` |
| Interactive captcha appears | reCAPTCHA/hCaptcha/Turnstile challenge | Stop; hand the single click to the owner | `blocked(captcha)` |
| Confirmation email never arrives | Relay/mail deliverability wall | Try a different route or the owner's real mailbox; else stop | `blocked` |
| Content removed after publish | Retroactive moderation | Mark removed; do NOT re-post the duplicate | `removed` |
| Cloudflare / WAF block | IP/fingerprint reputation or rate | Cool down; lower request rate; do not escalate | `blocked(waf)` (retry later) |
| Paid wall appears | Free lane removed | Skip the paid route | `blocked(paid)` |
| SMS/phone verification | Identity gate | Hand off to owner; else skip | `blocked(sms)` |
| OAuth-only login | No email/password path | Owner completes consent (model C), or skip | `blocked(oauth)` |
| Geo-block | Regional gating | Skip | `blocked(geo)` |
| Form silently 403s | Honeypot echo fields | Resubmit with the minimal field set | retry once |
| Duplicate-detected | Product already listed | Update the existing listing instead of re-submitting | `live` (update existing) |
| Content removed as thin/duplicate | Link-dump content | Republish genuinely unique, useful content with information gain | `removed` |
| Placeholder domain banned | Disposable-domain blocklist | Never use disposable domains; use the owner's real domain | `blocked(policy)` |

## Escalation rule
Every blocked venue becomes exactly one **owner action item** (one human step). Do not batch
unrelated human steps into one item.
