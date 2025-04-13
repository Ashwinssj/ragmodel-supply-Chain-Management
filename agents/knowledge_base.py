import requests

TAVILY_API_KEY=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

def fetch_web_insight(query):
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {'TAVILY_API_KEY'}}
    payload = {
        "query": query,
        "search_depth": "advanced",
        "include_answer": True
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["answer"] if response.ok else "No web insight available."
