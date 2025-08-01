import json
from chatbot.labguru_api import list_pmlb_specimens

specimens = list_pmlb_specimens()
print(f"Found {len(specimens)} specimens")

for specimen in specimens:
    print(json.dumps(specimen, indent=2))
    break  # just show one example

# for s in specimens:
#     print(s["id"], s["name"], s.get("fields", {}).get("model_id"))
