"""Wrapper for py_lambda_zip that interfaces with py_lambda_library macro
"""

load("//app/tools/build_rules/lambda_packaging:lambda.bzl", "contains", "endswith", "py_lambda_zip", "startswith")

default_ignore = [
    contains("/__pycache__/"),
    endswith(".pyc"),
    endswith(".pyo"),

    # Ignore boto since it's provided by Lambda.
    startswith("pypi__boto3/"),
    startswith("pypi__botocore/"),

    # With the move to hermetic toolchains, the zip gets a lib/ directory containing the
    # python runtime. We don't need that.
    startswith("lib/"),
]

def zip_py_lambda_library(name, target, data = [], ignore = default_ignore, **kwargs):
    """Wrapper for py_lambda_zip that interfaces with py_lambda_library macro

    Args:
        name (string): _description_
        target (Label, string): targets
        ignore ([string], optional): _description_. Defaults to default.
        **kwargs (dict): additional kwargs for py_lambda_zip
        data (Label[], string[]): list of files, targets, or directories added to the root of zip
    """
    zip_data = [] + data
    if not kwargs.pop("disable_otel", False):
        zip_data.append("//app/src:otel_config")

    if type(target) == "Label":
        target_label = native.package_relative_label(target.name + "_without_aws_packages")
    else:
        target_label = native.package_relative_label(target + "_without_aws_packages")

    py_lambda_zip(
        name = name,
        target = target_label,
        ignore = ignore,
        data = zip_data,
        **kwargs
    )
