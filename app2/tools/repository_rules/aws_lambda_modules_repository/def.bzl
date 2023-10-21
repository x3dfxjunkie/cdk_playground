load("@bazel_skylib//lib:new_sets.bzl", "sets")  # This also ensures that skylib is in the repo
load("@external_python_packages//:requirements.bzl", "requirement")

def _aws_lambda_modules_repository_impl(repository_ctx):
    requirements_list = [
        requirement(req)
        for req in repository_ctx.read(
            "{root}/external_python_packages/aws_lambda_supplied/requirements.txt".format(
                root = repository_ctx.workspace_root,
            ),
        ).splitlines()
    ]

    requirement_set = sets.make(requirements_list)

    bzl_file_content = """load("@bazel_skylib//lib:new_sets.bzl", "sets")\nrequirements_set = sets.make({set})""".format(set = sets.repr(requirement_set))

    repository_ctx.file("requirements.bzl", content = bzl_file_content)
    repository_ctx.file("BUILD.bazel")
    return

aws_lambda_modules_repository = repository_rule(
    implementation = _aws_lambda_modules_repository_impl,
    attrs = {
    },
)
