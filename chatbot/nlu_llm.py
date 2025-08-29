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

Respond ONLY with a valid JSON object using below structure and no other text or explanation. No markdown, no preamble.

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
- "count_xenografts"
- "count_growth_assay"
- "count_pathogen_assay"
- "count_flow_assay"
- "count_STR_assay"
- "count_histology_assay"
- "count_WES"
- "count_WGS"
- "count_RNAseq"
- "count_ATAC"
- "list_cases"
- "list_specimens"
- "list_organoids"
- "list_xenografts"
- "list_growth_assay"
- "list_pathogen_assay"
- "list_flow_assay"
- "list_STR_assay"
- "list_histology_assay"
- "list_WES"
- "list_WGS"
- "list_RNAseq"
- "list_ATAC"

Valid filters:
- "cases_name_startswith"
- "specimens_name_startswith"
- "organoids_name_startswith"
- "xenografts_name_startswith"
- "growth_assay_name_startswith"
- "pathogen_assay_name_startswith"
- "flow_assay_name_startswith"
- "STR_assay_name_startswith"
- "histology_assay_name_startswith"
- "WES_name_startswith"
- "WGS_name_startswith"
- "RNAseq_name_startswith"
- "ATAC_name_startswith"


Example:
User: list all organoids starting with CSC  
Response:
{{
  "intent": "list_organoids",
  "filters": {{
    "organoids_name_startswith": "CSC"
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

    raw_text = response.json().get("response", "")

    # Extract first valid JSON block using regex
    match = re.search(r"{.*}", raw_text, re.DOTALL)
    if not match:
        print("⚠️ LLM failed: No JSON block found")
        print("Raw response:", raw_text)
        return {"intent": "unknown"}

    json_str = match.group(0)
    try:
        parsed = json.loads(json_str)
        return parsed
    except Exception as e:
        print("⚠️ Failed to parse JSON:", e)
        print("Raw matched block:", json_str)
        return {"intent": "unknown"}