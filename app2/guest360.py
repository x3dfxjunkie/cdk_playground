#!/usr/bin/env python3
"""
Main Guest360 App
"""
import configparser
import os

import aws_cdk as cdk
import yaml
from infrastructure.pipeline.guest360_pipeline import Guest360PipelineStack

CONFIG = configparser.ConfigParser()
CONFIG.read("guest360.ini")

app = cdk.App()
STACK_NAME = app.node.get_context("stack_name").lower()
ENVIRONMENT = app.node.get_context("environment").lower()
CONFIG["tags"]["environment"] = ENVIRONMENT

config_dir = f"{os.path.dirname(os.path.realpath(__file__))}/configs"

# Load environment config
with open(f"{config_dir}/{ENVIRONMENT}-environment.yaml", "r", encoding="utf-8") as file:
    environment_config = yaml.safe_load(file)

# Load app constants
with open(f"{config_dir}/constants.yaml", "r", encoding="utf-8") as file:
    app_constants = yaml.safe_load(file)


Guest360PipelineStack(
    app,
    "Guest360Pipeline",
    env=cdk.Environment(
        account=app_constants["account_ids"][ENVIRONMENT], region=os.environ.get("AWS_REGION", "us-east-1")
    ),
    environment_config=environment_config,
    stack_name=f"{STACK_NAME}-{ENVIRONMENT}",
    tags=dict(CONFIG.items("tags")),
    termination_protection=ENVIRONMENT == "prod",
)

app.synth()
