"""Integration Test for Processing"""
import pytest
import boto3
from app.src.data_structures.object_lookup import lookup


def pytest_addoption(parser):
    parser.addoption(
        "--stack-name",
        action="store",
        default="Guest360",
        help='Stack name for CDK. Feature branch deployments use "<USERID>-<PR#>"',
    )

    parser.addoption(
        "--target-env",
        action="store",
        default="local",
        help="Environment targetted for integration testing. Local will target localstack.",
    )


# TODO: Create Cfn Export to file and obtain table names dynamically


@pytest.fixture
def setup_aws(request):
    pytest.stack_name = request.config.getoption("--stack-name")
    pytest.target_environment = request.config.getoption("--target-env")
    pytest.base_identity_table_name = "identity-local"
    pytest.base_profile_table_name = "profile-table"
    pytest.base_source_stream_name = "wdw-lightning-lane-stream"
    pytest.base_events_table_name = "curated-experiences"
    pytest.short_region_name = "use1"
    pytest.localstack_endpoint_url = "http://localhost:4566"

    if pytest.target_environment == "local":
        pytest.short_env_name = "lcl"
    elif pytest.target_environment == "feature":
        pytest.short_env_name = "lst"
    else:
        pytest.short_env_name = "lst"

    pytest.identity_table_name = f"{pytest.short_env_name}-{pytest.short_region_name}-{pytest.stack_name.lower()}-{pytest.base_identity_table_name}"
    pytest.source_stream_name = f"{pytest.short_env_name}-{pytest.short_region_name}-{pytest.stack_name.lower()}-{pytest.base_source_stream_name}"
    pytest.events_table_name = f"{pytest.short_env_name}-{pytest.short_region_name}-{pytest.stack_name.lower()}-{pytest.base_events_table_name}"
    pytest.profile_table_name = f"{pytest.short_env_name}-{pytest.short_region_name}-{pytest.stack_name.lower()}-{pytest.base_profile_table_name}"

    if pytest.target_environment == "local":
        pytest.kinesis = boto3.client(
            "kinesis",
            region_name="us-east-1",
            endpoint_url=pytest.localstack_endpoint_url,
            aws_access_key_id="localstack",
            aws_secret_access_key="localstack",
        )
        pytest.dynamodb_resource = boto3.resource(
            "dynamodb",
            region_name="us-east-1",
            endpoint_url=pytest.localstack_endpoint_url,
            aws_access_key_id="localstack",
            aws_secret_access_key="localstack",
        )
    else:
        pytest.session = boto3.Session(profile_name="wdpr-guest360-dev")
        pytest.kinesis = pytest.session.client("kinesis")
        pytest.dynamodb_resource = pytest.session.resource("dynamodb")

    pytest.data_lookup = lookup.DynamoDBLookupFactory.get_dynamodb_lookup(
        pytest.dynamodb_resource,
        pytest.kinesis,
        pytest.profile_table_name,
        pytest.events_table_name,
        pytest.identity_table_name,
    )
