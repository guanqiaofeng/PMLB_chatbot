from chatbot.labguru_api import (
    list_pmlb_cases,
    list_pmlb_specimens,
    list_pmlb_organoids,
    list_pmlb_xenografts,
    list_growth_assay,
    list_pathogen_assay,
    list_flow_assay,
    list_STR_assay,
    list_histology_assay,
    list_WES,
    list_RNAseq,
    list_ATAC
)
from chatbot.nlu_llm import parse_with_llm
import json
import re

def handle_intent(intent, filters):
    if intent == "count_specimens":
        specimens = list_pmlb_specimens()
        print(f"✅ Found {len(specimens)} PMLB specimens.")
    elif intent == "list_organoids":
        organoids = list_pmlb_organoids()
        prefix = filters.get("organoid_name_startswith", "").lower()
        filtered = [o for o in organoids if o.get("name", "").lower().startswith(prefix)]
        for org in filtered:
            print(f"- {org.get('name')}")
        print(f"✅ Found {len(filtered)} organoids starting with '{prefix}'.")
    else:
        print("❓Sorry, I didn't understand that request.")

def main():
    print("💬 Welcome to the PMLB Labguru Chatbot!")
    print("Type something like 'how many specimens' or 'list organoids starting with CSC'. Type 'exit' to quit.\n")

    while True:
        user_input = input("> ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("👋 Goodbye!")
            break

        print("🤖 Parsing with LLaMA3...")
        response_text = parse_with_llm(user_input)

        try:
            # Clean up backticks or code block formatting
            cleaned = re.sub(r"^```(?:json)?|```$", "", response_text.strip(), flags=re.MULTILINE).strip()
            parsed = json.loads(cleaned)
            
            intent = parsed.get("intent")
            filters = parsed.get("filters", {})
            handle_intent(intent, filters)
        except Exception as e:
            print("⚠️ Failed to interpret response:", e)
            print("Raw response:", response_text)

if __name__ == "__main__":
    main()