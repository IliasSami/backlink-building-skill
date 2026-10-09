# Cloud Stacking & Referring Domain (RD) Recipes

Cloud Stacking is an advanced entity-engineering methodology that deploys standalone, entity-optimized HTML assets across major cloud hyper-scalers (Google Cloud, Cloudflare, Amazon AWS). These assets inherit the immense crawl priority and Domain Authority (**DA 90–100**) of the parent cloud infrastructure while funneling topical relevance and link equity to the canonical money site.

---

## 1. Core Principles

### Principle 1: Referring Domain (RD) Diversification
Never build an entire cloud stack on a single platform (e.g. 20 links on Google Cloud Storage). Search engines value **unique referring domains**. A high-performance cloud stack must span distinct root domains:
- `storage.googleapis.com` (Google Cloud Storage — DA 100)
- `pages.dev` (Cloudflare Pages — DA 92)
- `workers.dev` (Cloudflare Workers — DA 92)
- `s3.amazonaws.com` (Amazon AWS S3 — DA 96)
- `colab.research.google.com` (Google Colab — DA 95)
- `archive.org` / `web.archive.org` (Wayback Machine — DA 99)

### Principle 2: Deep Entity Graph Injection
Every cloud node must embed nested JSON-LD schema with unambiguous `@id` referencing:
- `TechArticle` / `WebPage` representing the cloud asset.
- `Person` with legal name, alternate name, job title, and verified `sameAs` social/entity URLs.
- `Organization` representing the core brand or agency.
- `Service` or `Product` declaring the exact topical offerings on the canonical money site.

### Principle 3: Cross-Cloud Mesh Ring Interlinking
Rather than isolated silos, all cloud platforms should form a **bidirectional mesh ring**:
- Cloudflare Pages links to Google Cloud Storage and Cloudflare Workers.
- Google Cloud Storage links to Cloudflare Pages and Google Colab assets.
- Cloudflare Workers expose dynamic JSON-LD schema APIs referencing both clouds.
- All nodes funnels primary anchor equity to the canonical money site (`https://example.com`).

### Principle 4: Search Engine Discovery Protocols
Cloud assets are useless if search engine crawlers cannot discover them. Every cloud deployment must include:
1. **XML Sitemap (`sitemap.xml`):** Listing all cloud nodes with `lastmod`, `priority`, and `changefreq`.
2. **Robots.txt (`robots.txt`):** Explicitly declaring `User-agent: *`, `Allow: /`, and `Sitemap: <url>/sitemap.xml`.
3. **Wayback Machine Snapshot:** Submitting master cloud hubs to `https://web.archive.org/save/<url>` for permanent third-party historical trust.

---

## 2. Cloudflare Pages Deployment Recipe (`pages.dev` — DA 92)

Cloudflare Pages provides global edge distribution, automated SSL, clean URLs, and DA 92 root authority.

### Automated CLI Deployment:
```bash
# 1. Install or run Wrangler non-interactively
npx -y wrangler pages deploy ./dist \
  --project-name=brand-seo-cloudstack \
  --commit-dirty=true \
  --force
```

### Key Gotchas & Solutions:
- **Wrangler 4 Delegation Warning:** Wrangler 4 attempts to delegate `pages deploy` to Workers and prompts for interactive input in headless environments. Always pass `--force` on initial setup to bypass delegation and prevent agent stalling.
- **Clean URLs:** Cloudflare Pages automatically serves `/page.html` as `/page` with a 308 permanent redirect. Ensure internal stack links use clean URLs or resolve cleanly.
- **Sitemap & Robots:** Place `sitemap.xml` and `robots.txt` in the root of the upload directory (`./dist`).

---

## 3. Google Cloud Storage Recipe (`storage.googleapis.com` — DA 100)

Google Cloud Storage provides direct hosting on Google's own infrastructure with DA 100 root authority.

### Deployment CLI Commands:
```bash
# 1. Create a public multi-region bucket
gcloud storage buckets create gs://brand-seo-cloudstack --location=US

# 2. Grant public read access to all objects
gcloud storage buckets add-iam-policy-binding gs://brand-seo-cloudstack \
  --member=allUsers \
  --role=roles/storage.objectViewer

# 3. Upload HTML nodes, sitemap, and robots.txt
gcloud storage cp -r ./dist/* gs://brand-seo-cloudstack/

# 4. Verify HTTP 200 serving
curl -s -I https://storage.googleapis.com/brand-seo-cloudstack/index.html
```

### Key Gotchas & Solutions:
- **Uniform Bucket-Level Access:** Modern GCP buckets enforce uniform bucket-level access. Grant `roles/storage.objectViewer` at the bucket level rather than modifying object ACLs individually.
- **Service Account Drive Quota:** Note that GCP service accounts have `0 bytes` Google Drive quota by default and cannot upload to personal Drive unless a Google Workspace Shared Drive is used or OAuth user delegation is active.

---

## 4. Cloudflare Workers Edge API Recipe (`workers.dev` — DA 92)

Cloudflare Workers can serve dynamic JSON-LD entity resolvers and live tools under `workers.dev` (DA 92).

### Worker Script (`worker.js`):
```javascript
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    // Dynamic Schema Endpoint for AI Bots & WebMCP
    if (url.pathname === "/api/entity") {
      return new Response(JSON.stringify({
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Founder Name",
        "jobTitle": "Strategic Architect",
        "url": "https://example.com",
        "sameAs": ["https://linkedin.com/in/...", "https://x.com/..."]
      }, null, 2), {
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    }

    // Edge HTML Dashboard
    return new Response(htmlContent, {
      headers: { "Content-Type": "text/html; charset=utf-8" }
    });
  }
};
```

### Deploy Command:
```bash
npx -y wrangler deploy
```

---

## 5. Amazon AWS S3 Deployment Recipe (`s3.amazonaws.com` — DA 96)

AWS S3 provides static website hosting with DA 96 root domain authority.

### Automated Sync Command:
```bash
# 1. Sync assets to public S3 bucket
aws s3 sync ./dist s3://brand-seo-cloudstack --acl public-read

# 2. Enable static website hosting
aws s3 website s3://brand-seo-cloudstack --index-document index.html
```

---

## 6. Programmatic Verification Suite

Every cloud stack deployment must run an automated verification suite asserting:
1. `HTTP 200 OK` on every live endpoint.
2. `money_url_present: True` — confirms canonical target link exists in rendered source.
3. `schema_present: True` — confirms valid `application/ld+json` script exists.
4. `robots_indexable: True` — confirms `<meta name="robots" content="index, follow">`.
5. `sitemap_present: True` — confirms `sitemap.xml` returns valid XML.
