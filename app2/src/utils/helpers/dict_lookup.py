"""python dict helper"""


def dict_lookup(config: dict, key_path: str):
    """This method is used to access items in the dict object using a access key. example:

       config = {'foo': {'bar': {'baz': 'test'}}}
       value = lookup(d, 'foo.bar.baz')
       print(value) # Output will be test

    Args:
        config (dict): This is the dictionary to perform the lookup on
        key_path (str): This is the path to the object in the dict.

    Returns:
        Any: returns the object in the config dictionary that matches the given key path
    """
    keys = key_path.split(".")
    value = config

    for key in keys:
        if isinstance(value, (list)):
            key = int(key)
            value = value[key]
        elif isinstance(value, (dict)):
            if key in value:
                value = value[key]

            else:
                return None
        else:
            raise Exception(f"unsupported key/value pair {type(value)}")

    return value
