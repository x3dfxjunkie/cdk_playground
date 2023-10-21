""" Module to return constants """


def init_json_schema() -> dict:
    """
    Returns the beginning of the JSON Schema dictionary.
    Returns:
        dict: Beginning of JSON Schema.
    """
    json_schema = {
        "$schema": "https://json-schema.org/schema#",
        "type": "object",
        "properties": {"data": {"type": "object"}},
    }

    return json_schema


def get_constraints() -> dict:
    """
    Gets constraing dictionary to add primary to Data Contract.
    Returns:
        dict: Constraint primary key dictionary.
    """
    return {"type": "object", "description": "", "properties": {"CONSTRAINT": {"primary_key": []}}}
