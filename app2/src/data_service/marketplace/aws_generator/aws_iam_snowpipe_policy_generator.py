#!/bin/env python
"""
AWS IAM Snowpipe Policy Generator
"""
import argparse
import importlib
import os
import sys

from jinja2 import Environment, FileSystemLoader

dir_path = os.path.dirname(os.path.realpath(__file__))
output = sys.stdout


def get_configs(environment: str) -> list:
    # import here due to dynamic environment from context
    snow_pipe_configs = importlib.import_module(f"app.infrastructure.data_service.configs.aws_snow_pipe.{environment}")
    return snow_pipe_configs.get_configs()


def generate(s3_bucket_name: str, s3_bucket_prefix: str, s3_bucket_keys: list):  # pylint: disable=unused-argument
    data = locals()
    environment = Environment(loader=FileSystemLoader(f"{dir_path}/templates"))
    template = environment.get_template("guest360_iam_user_policy.json.jinja")
    content = template.render(data)
    return content


def args_parse():
    parser = argparse.ArgumentParser(description="Aws IAM Snowpipe Policy Generator")
    parser.add_argument("-e", "--environment", help="Environment of config to read", required=True)
    return parser.parse_args()


def main():
    args = args_parse()
    for config in get_configs(args.environment):
        content = generate(
            s3_bucket_name=config["snowpipe"]["s3_bucket_name"],
            s3_bucket_prefix=config["snowpipe"]["s3_bucket_prefix"],
            s3_bucket_keys=config["snowpipe"].get("s3_bucket_keys", []),
        )
        sys.stdout.write(content)


if __name__ == "__main__":
    main()
