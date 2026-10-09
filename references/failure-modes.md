# Failure Modes — Full Matrix

Every failure maps to a status and an action. Never work around a control; log and move on.

| Symptom | Likely cause | Action | Status |
|---------|--------------|--------|--------|
| Form API 400 "missing fields" | Framework state not updated; hidden required radio | Re-fill with native setter; check hidden required radios/selects | retry once, else `blocked(policy)` |
| Interactive captcha appears | reCAPTCHA/hCaptcha/Turnstile challenge | Stop; hand the single click to the owner | `blocked(captcha)` |
| Confirmation email never arrives | Relay/mail deliverability wall | Try a different route or the owner's real mailbox; else stop | `blocked` |
| Content removed after publish | Retroactive moderation | Mark removed; do NOT re-post the duplicate | `removed` |
| Cloudflare / WAF block | IP/fingerprint reputation or rate | Cool down; lower request rate; do not escalate | `blocked(waf)` (retry later) |
| Paid wall appears | Free lane removed | Skip the paid route | `blocked(paid)` |
| SMS/phone verification | Identity gate | Hand off to owner; else skip | `blocked(sms)` |
| OAuth-only login | No email/password path | Owner completes consent (model C), or skip | `blocked(oauth)` |
| Geo-block | Regional gating | Skip |
| Form silently 403s | Honeypot echo fields | Resubmit with the minimal field set |
| Duplicate-detected | Product already listed | Update the existing listing instead of re-submitting |
| Content removed as thin/duplicate | Link-dump content | Republish genuinely unique, useful content once |
| Placeholder domain banned | Disposable-domain blocklist | Never use disposable domains; use the owner's real domain |

## Escalation rule
Every blocked venue becomes exactly one **owner action item** (one human step). Do not batch
unrelated human steps into one item.
