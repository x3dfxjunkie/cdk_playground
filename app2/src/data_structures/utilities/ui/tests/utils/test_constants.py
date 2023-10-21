from app.src.data_structures.utilities.ui.dataclass_generator.utils.constants import init_json_schema, get_constraints


def test_init_json_schema():
    json_schema = init_json_schema()
    assert isinstance(json_schema, dict)
    assert "$schema" in json_schema


def test_get_constraints():
    dict_constraints = get_constraints()
    assert isinstance(dict_constraints, dict)
    assert "CONSTRAINT" in dict_constraints["properties"]
