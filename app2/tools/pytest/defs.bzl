load("@aspect_rules_py//py:defs.bzl", "py_test")
load("@external_python_packages//:requirements.bzl", "requirement")

# NOTE: we should eventually move back to load("@rules_python//python:defs.bzl", "py_test") for consistency,
# once the issue with aws-cdk is resolved: https://github.com/aws/jsii/issues/3881
def pytest_test(name, srcs, deps = [], args = [], data = [], **kwargs):
    """
        Call pytest
    """
    py_test(
        name = name,
        srcs = [
            "//app/tools/pytest:pytest_wrapper.py",
        ] + srcs,
        main = "//app/tools/pytest:pytest_wrapper.py",
        args = [
            "-v",
            "-s",
            # "--black",
            # "--capture=no",
            "--cov-config=$(location //app/tools/pytest:.coveragerc)",
            # "--func_cov=code",
            "--json-report",
            "--cov-config=$(location //app/tools/pytest:.coveragerc)",
            "--func_cov=code",
            "--json-report-file=workspace/report.json",
            "--pylint-rcfile=$(location //app/tools/pytest:.pylintrc)",
            # "--mypy",
            # "--pylint",
            "--pylint-rcfile=$(location //app/tools/pytest:.pylintrc)",
        ] + args + ["$(location :%s)" % x for x in srcs],
        deps = deps + [
            requirement("pytest"),
            requirement("pytest-black"),
            requirement("pytest-pylint"),
            requirement("pytest-json-report"),
            requirement("pytest-cov"),
            requirement("pytest-sugar"),
            requirement("pytest-func-cov"),
            requirement("coverage"),
        ],
        data = [
            "//app/tools/pytest:.pylintrc",
            "//app/tools/pytest:.coveragerc",
        ] + data,
        **kwargs
    )
