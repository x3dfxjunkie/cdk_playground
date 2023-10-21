load("//app/tools/pytest:defs.bzl", "pytest_test")

def contracts_unit_tests(name, args = []):
    """contracts unit tests"""

    pytest_test(
        name = name,
        srcs = native.glob(["tests/**/test_data_contracts.py"]),
        args = args,
        data = native.glob(["tests/**/**/*.json"]),
        deps = [":data_contracts"],
    )
