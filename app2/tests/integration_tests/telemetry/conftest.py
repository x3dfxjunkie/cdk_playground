"""Integration Test for Processing"""
import boto3
import pytest
import argparse
import pathlib

def pytest_addoption(parser):
    root_path = str(pathlib.Path(__file__).parent.joinpath("../../../../").resolve())
    parser.addoption(
        "--stack-prefix",
        action="store",
        default="lst-use1-guest360",
        help='Stack name prefix for CDK. Feature branch deployments use "lst-<SHORT_REGION>-<PR#>"',
    )
    parser.addoption(
        "--ingestion-config",
        action="store",
        default=f"{root_path}/app/infrastructure/ingestion/config/pipelines/latest",
        help='File or (Directory loops all files in directory) of pipeline to test'
    )

def pytest_configure(config):
    pytest.ingestion_config_path = config.getoption('--ingestion-config')
    pytest.stack_prefix = config.getoption('--stack-prefix')
