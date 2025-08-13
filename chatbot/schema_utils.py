import json

def load_schema(path="config/labguru_schema.json"):
    with open(path, "r") as f:
        return json.load(f)
