"""Drop in replacement for py_library to integrate better with aws. Adds lambda without aws_packages.
"""

load("@bazel_skylib//lib:new_sets.bzl", "sets")
load("@aws_lambda_modules//:requirements.bzl", aws_requirements_set = "requirements_set")

def py_lambda_library(name, deps = [], srcs = [], imports = [], data = [], opentelemetry = True, visibility = ["//visibility:public"], srcs_version = "PY2AND3", compatible_with = [], deprecation = None, distribs = [], target_compatible_with = [], exec_properties = {}, features = [], tags = [], **kwargs):
    """Drop in replacement for py_library to integrate better with aws. Adds lambda without aws_packages.

    Args:
        name (_type_): A unique name for this target.
        deps (list, optional): The list of other libraries to be linked in to the binary target. Defaults to [].
        srcs (list, optional): source files, .py and .pyc files in the source. Defaults to [].
        imports (list, optional): List of import directories to be added to the PYTHONPATH.. Defaults to [].
        data (list, optional): additional files in library. Defaults to [].
        visibility (list, optional): Package Visibility. Defaults to ["//visibility:public"].
        srcs_version (str, optional): This attribute declares the target's srcs to be compatible with either Python 2, Python 3, or both.. Defaults to "PY2AND3".
        opentelemetry (bool, optional): Attach Open Telemetry Config File. Defaults to True.
        srcs_version (str, optional): Python Version. Defaults to "PY2AND3".
        compatible_with (list, optional): The list of environments this target can be built for, in addition to default-supported environments. Defaults to [].
        deprecation (_type_, optional): An explanatory warning message associated with this target. Defaults to None.
        distribs (list, optional): _description_. Defaults to [].
        target_compatible_with (list, optional): _description_. Defaults to [].
        exec_properties (dict, optional): A dictionary of strings that will be added to the exec_properties of a platform selected for this target. . Defaults to {}.
        features (list, optional): A feature is string tag that can be enabled or disabled on a target. The meaning of a feature depends on the rule itself. Defaults to [].
        tags (list, optional): Tags. Defaults to [].
        **kwargs (dict): additional kwargs
    """

    requirements_set = sets.make([dep for dep in deps if dep.startswith("@external_python_packages")])

    library_deps_without_aws = ["//" + native.package_relative_label(dep).package + ":" + native.package_relative_label(dep).name + "_without_aws_packages" for dep in deps if not dep.startswith("@external_python_packages")]

    lib_data = [] + data  # Removes unmutability

    if opentelemetry:
        lib_data = lib_data + [kwargs.pop("otel_config", "//app/src:otel_config")]

    reqs_without_aws_packages = sets.to_list(sets.difference(requirements_set, aws_requirements_set))

    native.py_library(
        name = name + "_without_aws_packages",
        deps = reqs_without_aws_packages + library_deps_without_aws,
        srcs = srcs,
        data = lib_data,
        visibility = visibility,
        imports = imports,
        srcs_version = srcs_version,
        compatible_with = compatible_with,
        deprecation = deprecation,
        distribs = distribs,
        target_compatible_with = target_compatible_with,
        exec_properties = exec_properties,
        features = features,
        tags = tags,
    )

    native.py_library(
        name = name,
        deps = deps,
        srcs = srcs,
        data = lib_data,
        visibility = visibility,
        imports = imports,
        srcs_version = srcs_version,
        compatible_with = compatible_with,
        deprecation = deprecation,
        distribs = distribs,
        target_compatible_with = target_compatible_with,
        exec_properties = exec_properties,
        features = features,
        tags = tags,
    )
