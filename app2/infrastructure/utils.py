def cli_to_python_bool(var):
    return str(var).lower() in ("true", "yes", "y", "t", "1")
