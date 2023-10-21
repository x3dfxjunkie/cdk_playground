"""Dict lookup test"""
from app.src.utils.helpers.dict_lookup import dict_lookup


def test_dict_obj_with_list():
    dict_obj_with_list = {"test": [{"test": {"test": True}}]}
    key = "test.0.test.test"
    data = dict_lookup(dict_obj_with_list, key)
    assert data is True


def test_dict_obj():
    dict_obj_with_list = {"test": {"test": {"test": True}}}
    key = "test.test.test"
    data = dict_lookup(dict_obj_with_list, key)
    assert data is True
