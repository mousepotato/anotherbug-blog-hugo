# Agent Notes — anotherbug-blog

This file is for AI agents working in this repo. Read it before touching legal pages, Meta app URLs, or deploy flow.

## Site

- **Production URL:** https://anotherbug.com
- **Repo:** Hugo blog, theme `themes/tapa/`
- **Deploy:** push to `master` → GitHub Actions → GitHub Pages
- **Quick deploy:** `./deploy "message"`

## Legal / Policy Pages (important)

Legal pages are **static HTML** under `static/`. They are:

- **Not linked** from blog navigation or homepage
- **Not indexed** by search engines or AI crawlers
- **Only used** for app store / Meta / platform compliance URLs

### Current pages

| Path | Service | Purpose |
|------|---------|---------|
| `/privacy/` | Tudouge Social Threads | Privacy Policy |
| `/tos/` | Tudouge Social Threads | Terms of Service |
| `/threads/data-deletion/` | Tudouge Social Threads | Data deletion (Meta required) |
| `/octopus-garden-privacy/` | Octopus Garden | Privacy Policy |
| `/chessimprovementai-privacy/` | Chess Improvement AI | Redirect to external privacy page |

### Meta App form URLs (Tudouge Social Threads)

Use these in Meta Developer Console:

```
Privacy Policy URL:     https://anotherbug.com/privacy/
Terms of Service URL:   https://anotherbug.com/tos/
Data deletion URL:      https://anotherbug.com/threads/data-deletion/
Contact email:          paradise.lsj@gmail.com
App domain:             anotherbug.com
```

### Anti-index / anti-LLM rules

Every legal page `<head>` must include the meta block from:

```
scripts/legal-head-meta.snippet
```

Crawl blocking is centralized in:

```
data/legal_pages.yaml
```

`layouts/robots.txt` reads that file at build time. **Do not hand-edit duplicate Disallow lines in robots.txt.**

### Add a new legal page (checklist)

1. Create `static/<service>/<page>/index.html`
2. Paste `scripts/legal-head-meta.snippet` into `<head>`
3. Add path to `data/legal_pages.yaml` → `paths:`
4. Run: `python3 scripts/check_legal_pages.py`
5. Deploy: `./deploy "Add <service> legal page"`

### Naming convention for future services

Prefer service-scoped paths to avoid collisions:

```
/<service>/privacy/
/<service>/tos/
/<service>/data-deletion/
```

Threads currently uses short paths `/privacy/` and `/tos/` for Meta convenience. New services should **not** reuse those root paths.

## Threads API credentials

Stored in `~/.bash_script/agent_ai.sh`:

- `THREADS_APP_ID`
- `THREADS_APP_SECRET`
- `THREADS_ACCESS_TOKEN` (add after Meta OAuth works)

**Note:** Meta has two app IDs (Facebook App ID vs Threads App ID). OAuth / API calls use the **Threads** app ID from `agent_ai.sh`.

App ID + Secret alone cannot read posts. Need User Access Token with `threads_basic` + `threads_read_replies`.

## Local preview

```bash
HUGO_CACHEDIR=$(pwd)/.hugo_cache hugo server --bind 127.0.0.1 --port 1315 --disableFastRender
```

Legal pages preview at e.g. http://127.0.0.1:1315/privacy/

## Verify after deploy

```bash
curl -I https://anotherbug.com/privacy/
curl -s https://anotherbug.com/robots.txt | head -20
python3 scripts/check_legal_pages.py
```

## Do not

- Link legal pages from blog nav, footer, or posts
- Remove `noindex` / AI meta tags from legal pages
- Add legal paths to `llms.txt` or sitemap manually
- Put secrets in this repo