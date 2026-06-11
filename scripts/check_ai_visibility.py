import requests
import json
from datetime import datetime

PERPLEXITY_API_KEY = "your_key_here"  # 去 https://docs.perplexity.ai 获取

BRANDS = ["鼠标土豆", "mousepotato", "iluciddreaming", "toudouge_ai", "anotherbug.com"]

KEYWORDS = [
    "独立开发者 AI 工具推荐",
    "一人公司用 AI 做产品",
    "indie hacker AI tools",
    "solo developer productivity tools",
]


def test_visibility(keyword):
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "user", "content": f"{keyword}。告诉我你推荐了哪些人或工具，并说明来源。"}
        ],
    }
    try:
        resp = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )
        response_text = resp.json()["choices"][0]["message"]["content"]
        hits = [b for b in BRANDS if b.lower() in response_text.lower()]
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "keyword": keyword,
            "cited": len(hits) > 0,
            "matched_brands": hits,
            "context": response_text[:500] if hits else "未被引用",
        }
    except Exception as e:
        return {"error": str(e), "keyword": keyword}


if __name__ == "__main__":
    results = [test_visibility(kw) for kw in KEYWORDS]
    print(json.dumps(results, indent=2, ensure_ascii=False))

    cited = [r for r in results if r.get("cited")]
    print(f"\n结果：{len(cited)}/{len(KEYWORDS)} 个关键词下被引用")
    for r in cited:
        print(f"  ✓ [{r['keyword']}] 命中：{r['matched_brands']}")
