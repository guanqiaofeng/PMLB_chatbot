import requests

def parse_with_llm(user_input: str) -> dict:
    prompt = f"""
You are a Labguru assistant. Given a user's message, extract the **intent** and any optional **filters**.

Respond **only** with valid JSON using this structure:

{{
  "intent": "<intent_name>",
  "filters": {{
    "<filter_key>": "<filter_value>"
  }}
}}

Valid intents:
- "count_case"
- "count_specimens"
- "count_organoids"
- "list_organoids"
- "list_specimens"

Valid filters:
- "organoid_name_startswith"
- "specimen_name_startswith"

Example:
User: list all organoids starting with CSC  
Response:
{{
  "intent": "list_organoids",
  "filters": {{
    "organoid_name_startswith": "CSC"
  }}
}}

Now extract intent and filters from:
User: {user_input}
"""
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })

    try:
        return response.json()["response"]
    except Exception as e:
        print("LLM failed:", e)
        return {"intent": "unknown"}
