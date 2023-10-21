"""
This is a custom bazel build tool that is used to package python aws lambdas for deployment. 
When the lambda is package it will include all dependencies need to run the lambda function on AWS.
"""

def contains(pattern):
    return "contains:" + pattern

def startswith(pattern):
    return "startswith:" + pattern

def endswith(pattern):
    return "endswith:" + pattern

def _is_ignored(path, patterns):
    for p in patterns:
        if p.startswith("contains:"):
            if p[len("contains:"):] in path:
                return True
        elif p.startswith("startswith:"):
            if path.startswith(p[len("startswith:"):]):
                return True
        elif p.startswith("endswith:"):
            if path.endswith(p[len("endswith:"):]):
                return True
        else:
            fail("Invalid pattern: " + p)

    return False

def _short_path(file_):
    # Remove prefixes for external and generated files.
    # E.g.,
    #   ../py_deps_pypi__pydantic/pydantic/__init__.py -> pydantic/__init__.py
    short_path = file_.short_path
    if short_path.startswith("../"):
        short_path_list = short_path.split("/")
        short_path = "/".join(short_path_list[4:])
    return short_path

    # if short_path.startswith("pypi__"):
    #     second_slash = short_path.index("/", 3)
    #     short_path = short_path[second_slash + 1:]
    # return short_path

defult_ignore = [
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

def _py_lambda_zip_impl(ctx):
    deps = ctx.attr.target[DefaultInfo].default_runfiles.files
    f = ctx.outputs.output

    args = []
    for dep in deps.to_list():
        short_path = _short_path(dep)

        # Skip ignored patterns
        if _is_ignored(short_path, ctx.attr.ignore):
            continue

        args.append(short_path + "=" + dep.path)

    # MODIFICATION: Added source files to the map of files to zip
    source_files = ctx.attr.target[DefaultInfo].files
    for source_file in source_files.to_list():
        args.append(source_file.basename + "=" + source_file.path)

    #Add data file mapping
    # data_files = ctx.attr.data[DefaultInfo].runfiles
    for data_file in ctx.files.data:
        args.append(data_file.basename + "=" + data_file.path)

    ctx.actions.run(
        outputs = [f],
        inputs = deps,
        executable = ctx.executable._zipper,
        arguments = ["cC", f.path] + args,
        progress_message = "Creating archive...",
        mnemonic = "archiver",
    )

    out = depset(direct = [f])
    return [
        DefaultInfo(
            files = out,
        ),
        OutputGroupInfo(
            all_files = out,
        ),
    ]

_py_lambda_zip = rule(
    implementation = _py_lambda_zip_impl,
    attrs = {
        "target": attr.label(),
        "ignore": attr.string_list(),
        "_zipper": attr.label(
            default = Label("@bazel_tools//tools/zip:zipper"),
            cfg = "exec",
            executable = True,
        ),
        "data": attr.label_list(
            allow_files = True,
            doc = "Data files available to binaries using this library",
        ),
        "output": attr.output(),
    },
    executable = False,
    test = False,
)

def py_lambda_zip(name, target, ignore = defult_ignore, **kwargs):
    _py_lambda_zip(
        name = name,
        target = target,
        ignore = ignore,
        output = name + ".zip",
        **kwargs
    )
