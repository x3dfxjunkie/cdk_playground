def _parse_requirements(rctx):
    requirements_file = rctx.read(rctx.attr.input_directory)
    requirements = requirements_file.splitlines()
    if requirements[-1] == "":
        requirements = requirements[:-1]
    return requirements

def _read_requirements_impl(rctx):
    requirements = _parse_requirements(rctx)
    content = "requirements = {requirements}".format(requirements = requirements)
    content = content + "\ndef list_requirements(): \n    return requirements"
    rctx.file("requirements.bzl", content = content)
    rctx.file("BUILD.bazel")
    return

read_requirements = repository_rule(
    implementation = _read_requirements_impl,
    attrs = {
        "input_directory": attr.label(mandatory = True),
    },
)
