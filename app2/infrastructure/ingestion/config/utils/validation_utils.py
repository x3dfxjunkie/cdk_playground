""" Config Validation utils """

import importlib


class ValidationConfigError(Exception):
    """
    Dead Letter Queue lambda handler exception class
    """


def type_validator(value, lib_path, attr_path):
    if value is None:
        return
    lib = importlib.import_module(lib_path)
    val_object = getattr(lib, attr_path)
    if not isinstance(value, val_object):
        raise ValueError(f"Type error {val_object.__name__} expected")
