import json
from chatbot.labguru_api import list_pmlb_cases

cases = list_pmlb_cases()

# for case in cases:
#     print(json.dumps(case, indent=2))
#     break  # just show one example

for case in cases:
    print(case["name"], case["stem_PPID"],case["sex"], case["oncotree_code"], case["primary_tumor_site"], case["cancer_type_detailed"])
    