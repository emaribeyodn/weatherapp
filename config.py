import json


with open("config.json", "r") as file:
    keys = json.loads(file.read())


def get_env_variable(key: str) -> str:
    try:
        return keys[key]
    except KeyError:
        raise KeyError(f"Set the {key} environment variable")
