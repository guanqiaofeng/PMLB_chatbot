import requests
import json
import re
from chatbot.schema_utils import load_schema

def build_prompt(user_input: str, schema: dict) -> str:
    schema_description = json.dumps(schema, indent=2)
    return f"""
You are a Labguru assistant. The database schema is:

{schema_description}

Given a user's message, extract the **intent** and any optional **filters**.

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

def parse_with_llm(user_input: str) -> dict:
    schema = load_schema()
    prompt = build_prompt(user_input, schema)

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })

    raw = response.json().get("response", "")
    
    try:
        # Try to extract JSON using regex (the first {...} block)
        match = re.search(r'{.*}', raw, re.DOTALL)
        if match:
            json_str = match.group(0)
            parsed = json.loads(json_str)
            return parsed
        else:
            raise ValueError("No JSON block found")
    except Exception as e:
        print("⚠️ LLM failed:", e)
        print("Raw response:", raw)
        return {"intent": "unknown"}