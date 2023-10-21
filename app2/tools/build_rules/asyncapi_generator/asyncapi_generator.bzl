"""
This is a custom bazel build tool that is used to package python aws lambdas for deployment.
When the lambda is package it will include all dependencies need to run the lambda function on AWS.
"""

def _asyncapi_generator_impl(ctx):
    # print("analyzing asyncapi_generator ", ctx.label)
    # print("template to generate template=", ctx.attr.template)
    output_directories = []
    for file in ctx.files.srcs:
        #directory = ctx.actions.declare_directory(ctx.label.name)
        directory = ctx.actions.declare_directory(file.basename + ".agout")

        # print("src=", file.path)
        # print("agout=",directory.path)
        output_directories.append(directory)
        ctx.actions.run_shell(
            inputs = [file],
            outputs = [directory],
            arguments = [file.root.path + file.path, ctx.attr.template, "-o", directory.path],
            command = "ag $@",
            use_default_shell_env = True,
        )
    return [DefaultInfo(files = depset(output_directories))]

asyncapi_generator = rule(
    implementation = _asyncapi_generator_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = [".yml", ".yaml"], mandatory = True),
        "template": attr.string(),
    },
)
