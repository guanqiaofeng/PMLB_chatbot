from chatbot import labguru_api
from chatbot.nlu_llm import parse_with_llm
import json
import re

# Maps keywords like 'organoids' or 'WES' to their respective list_* functions
RESOURCE_FUNCTIONS = {
    "patients": labguru_api.list_pmlb_cases,
    "specimens": labguru_api.list_pmlb_specimens,
    "organoids": labguru_api.list_pmlb_organoids,
    "xenografts": labguru_api.list_pmlb_xenografts,
    "growth_assay": labguru_api.list_growth_assay,
    "pathogen_assay": labguru_api.list_pathogen_assay,
    "flow_assay": labguru_api.list_flow_assay,
    "STR_assay": labguru_api.list_STR_assay,
    "histology_assay": labguru_api.list_histology_assay,
    "WES": labguru_api.list_WES,
    "WGS": labguru_api.list_WGS,
    "RNAseq": labguru_api.list_RNAseq,
    "ATAC": labguru_api.list_ATAC,
}

# Alias map to handle variations (case insensitive)
RESOURCE_ALIASES = {
    "patients": "patients",
    "case": "patients",
    "cases": "patients",
    "patient": "patients",
    "specimens": "specimens",
    "organoids": "organoids",
    "xenografts": "xenografts",
    "growth_assay": "growth_assay",
    "pathogen_assay": "pathogen_assay",
    "flow_assay": "flow_assay",
    "str": "STR_assay",
    "str_assay": "STR_assay",
    "histology_assay": "histology_assay",
    "wes": "WES",
    "wgs": "WGS",
    "rnaseq": "RNAseq",
    "rna_seq": "RNAseq",
    "atac": "ATAC",
    "atacseq": "ATAC",
}

def normalize_resource_name(resource: str) -> str:
    return RESOURCE_ALIASES.get(resource.lower(), resource)

def handle_intent(intent, filters):
    # Handle count_*
    if intent.startswith("count_"):
        resource_raw = intent.replace("count_", "").lower()
        resource = RESOURCE_ALIASES.get(resource_raw, resource_raw)
        print(f"🛠 Resolved resource: {resource}")
        list_func = RESOURCE_FUNCTIONS.get(resource)
        if list_func:
            items = list_func()
            print(f"✅ Found {len(items)} PMLB {resource}.")
        else:
            print(f"❓Unknown resource type: {resource}")

    # Handle list_*
    elif intent.startswith("list_"):
        resource_raw = intent.replace("list_", "").lower()
        resource = RESOURCE_ALIASES.get(resource_raw, resource_raw)
        print(f"🛠 Resolved resource: {resource}")
        list_func = RESOURCE_FUNCTIONS.get(resource)
        if list_func:
            items = list_func()
            name_key = "name"

            # Optional prefix filter (like "name starts with")
            prefix = filters.get(f"{resource}_name_startswith", "").lower()
            if prefix:
                items = [item for item in items if item.get(name_key, "").lower().startswith(prefix)]
                for item in items:
                    print(f"- {item.get(name_key)}")
                print(f"✅ Found {len(items)} {resource} starting with '{prefix}'.")
            else:
                for item in items:
                    print(f"- {item.get(name_key)}")
                print(f"✅ Found {len(items)} total {resource}.")
        else:
            print(f"❓Unknown resource type: {resource}")

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
        parsed = parse_with_llm(user_input)
        print(parsed)
        intent = parsed.get("intent")

        if intent and ("_" in intent):
            action, resource = intent.split("_", 1)
            normalized_resource = normalize_resource_name(resource)
            intent = f"{action}_{normalized_resource}"

        elif intent is None:
            print("❓Sorry, I didn't understand that request.")
            return
        filters = parsed.get("filters", {})
        handle_intent(intent, filters)

if __name__ == "__main__":
    main()