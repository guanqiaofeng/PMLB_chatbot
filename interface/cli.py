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

def handle_query(user_input: str) -> str:
    """Route user input to the appropriate Labguru function."""
    user_input = user_input.lower()

    try:
        if "case" in user_input:
            items = list_pmlb_cases()
            return f"✅ Found {len(items)} PMLB cases."
        elif "specimen" in user_input:
            items = list_pmlb_specimens()
            return f"✅ Found {len(items)} PMLB specimens."
        elif "organoid" in user_input:
            items = list_pmlb_organoids()
            return f"✅ Found {len(items)} PMLB organoids."
        elif "xenograft" in user_input:
            items = list_pmlb_xenografts()
            return f"✅ Found {len(items)} PMLB xenografts."
        else:
            return "❌ Sorry, I didn't understand that."
    except Exception as e:
        return f"❌ Error: {e}"

def start_chat():
    print("💬 Welcome to the PMLB Labguru Chatbot!")
    print("Type something like 'show me all specimens'. Type 'exit' to quit.\n")

    while True:
        user_input = input("> ")
        if user_input.strip().lower() == "exit":
            print("👋 Goodbye!")
            break

        response = handle_query(user_input)
        print(response)

if __name__ == "__main__":
    start_chat()