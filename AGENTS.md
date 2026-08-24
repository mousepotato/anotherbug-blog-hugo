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

## AdSense (Google 广告)

Publisher: `ca-pub-2012267054436559`（与 `static/app-ads.txt` 中的 AdMob 同一账号）。
**只在 anotherbug.com 博客投放** —— ai./octoflow./tudouflow. 三个产品子域名保持无广告，
避免干扰付费转化漏斗。AdSense 已取消子域名独立管理，root 的 `static/ads.txt` 同时覆盖所有子域名，
不需要在 tudou-ai-home / octoflow 仓库另建。

### 相关文件

| 文件 | 作用 |
|------|------|
| `static/ads.txt` | IAB 授权卖家声明，与 `app-ads.txt` 同一行内容 |
| `layouts/partials/adsense-enabled.html` | **唯一的资格判定入口**，loader 与广告单元共用 |
| `layouts/partials/extend_head.html` | 覆盖主题 stub，按需注入 loader 脚本 |
| `layouts/partials/adsense-unit.html` | 响应式 display 单元，接收 `dict "slot" ...` |
| `layouts/_default/single.html` | **主题文件的副本**，只多了文末广告位调用 |
| `assets/css/extended/adsense.css` | 广告位间距 + 无填充时折叠 |
| `content/privacy-policy.md` | 站点隐私政策（**可索引**，不同于 `static/` 下的 App 法务页） |

### 规则

- 加广告位改 `adsense-enabled.html` 一处即可，**不要**在模板里另写判定条件。
- `config.toml` 的 `params.adsense.articleEndSlot` 留空时全站不加载任何 AdSense 代码。
  上线新广告位前必须先在 AdSense 后台创建单元拿到 slot ID。
- 不投放：列表页、tags、`/about/`、`/thoughts/`、`/main/`、`products` tag、
  `章鱼花园期刊` tag、字数低于 `params.adsense.minWords`、`noAds: true` 的文章。
- `/privacy-policy/` **不要**加进 `data/legal_pages.yaml`——那是屏蔽名单，这一页必须能被抓取。
- `layouts/_default/single.html` 是 `themes/tapa/` 同名文件的副本，升级主题时需手动合并。

## 已知问题

- 本地 Hugo 0.165.0 构建会失败：`content/main/index.html` 触发 `security.allowContent`
  对 `text/html` 的默认封禁。CI 固定在 0.160.1，不受影响。本地验证可用
  `HUGO_SECURITY_ALLOWCONTENT='.' hugo` 绕过。升级 CI Hugo 版本前需要先处理这一项。
