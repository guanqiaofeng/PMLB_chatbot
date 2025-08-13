def parse(user_input: str) -> dict:
    """
    Parse user input into a structured intent.

    Returns:
        dict: {"intent": str}
    """
    user_input = user_input.lower()

    if "case" in user_input:
        return {"intent": "list_cases"}
    elif "specimen" in user_input:
        return {"intent": "list_specimens"}
    elif "organoid" in user_input:
        return {"intent": "list_organoids"}
    elif "xenograft" in user_input:
        return {"intent": "list_xenografts"}
    else:
        return {"intent": "unknown"}
