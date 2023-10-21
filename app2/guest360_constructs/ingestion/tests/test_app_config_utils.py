import pytest
import os
import json
from app.guest360_constructs.ingestion.utils import (
    app_config_get_layer_arn,
    app_config_lambda_configuration,
    app_config_role_grants,
    ErrorAppConfigRegionExtension,
)
from aws_cdk import App, Aspects, Environment, Stack, aws_lambda, aws_iam, assertions
from cdk_nag import AwsSolutionsChecks
from app.guest360_constructs.lambda_function import Guest360LambdaFunction
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.kms_key import Guest360KMSKey
from app.guest360_constructs.app_config import Guest360AppConfig
from app.guest360_constructs.app_config_base import Guest360AppConfigBase


TEST_CONTEXT = {
    "environment": "latest",
    "stack_name": "testStack",
    "prefix": "lst-TestStack-use1",
    "prefix_global": "lst-testStack",
    "account": "123456789",
    "region": "us-east-1",
}

stack_id = "TestStack"
construct_id = "TestAppConfig"


def load_lambda_extension_json_config():
    config_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, "config", "app_config_lambda_extensions.json")
    )
    with open(config_path) as config_file:
        return json.load(config_file)


@pytest.mark.parametrize(("region", "arn"), load_lambda_extension_json_config().items())
def test_config_get_layer_arn(region, arn):
    """Test AppConfig utils get layer arn static function"""
    assert app_config_get_layer_arn(region) == arn


def test_exception_get_layer_arn():
    """Test AppConfig utils get layer arn static function exception"""
    with pytest.raises(ErrorAppConfigRegionExtension) as excinfo:
        app_config_get_layer_arn("test-east-1")
    assert str(excinfo.value) == "No AppConfig Layer Arn was found for the test-east-1 region"


@pytest.fixture(scope="module")
def stack_test():
    test_app = App(context=TEST_CONTEXT)
    aspects = Aspects.of(test_app)
    aspects.add(AwsSolutionsChecks(verbose=True))
    stack_test = Stack(
        test_app, stack_id, env=Environment(account=TEST_CONTEXT["account"], region=TEST_CONTEXT["region"])
    )
    yield stack_test


@pytest.fixture(scope="module", autouse=True)
def mock_app_config_dependencies(stack_test):
    """Mock AppConfig associated resources"""
    test_lambda_function = Guest360LambdaFunction(
        stack_test,
        construct_id,
        props={
            "handler": f"index.test_app_config_utils",
            "code": aws_lambda.Code.from_inline("""mytestcode"""),
        },
    ).function

    test_account_role = Guest360IamRole(
        stack_test,
        construct_id,
        props={
            "assumed_by": aws_iam.AccountPrincipal(TEST_CONTEXT["account"]),
            "description": "Test AppConfig utils IAM role",
            "role_name": "test-appconfig-utils-role",
        },
    ).role

    test_encryption_key = Guest360KMSKey(
        stack_test,
        construct_id,
        props={"alias": construct_id},
    ).key

    yield test_lambda_function, test_account_role, test_encryption_key


@pytest.fixture(scope="module", autouse=True)
def mock_app_config(stack_test):
    """Mock Guest360AppConfig and Guest360AppConfigBase"""

    test_app_config_base = Guest360AppConfigBase(
        stack_test,
        construct_id,
        props={
            "deployment_strategy": {
                "deployment_duration_in_minutes": 0,
                "growth_factor": 100,
                "replicate_to": "NONE",
            },
        },
    )

    test_app_config = Guest360AppConfig(
        stack_test,
        construct_id,
        props={
            "hosted_configuration": {
                "content": {
                    "boolEnableLimitResults": True,
                    "intResultLimit": 5,
                },
            },
            "application_id": test_app_config_base.application_id,
            "environment_id": test_app_config_base.environment_id,
            "deployment_strategy_id": test_app_config_base.deployment_strategy_id,
        },
    )
    yield test_app_config_base, test_app_config


def test_app_config_role_grants(stack_test, mock_app_config_dependencies):
    """Test AppConfig utils role grants"""

    test_lambda_function, test_account_role, test_encryption_key = mock_app_config_dependencies

    app_config_role_grants(
        app_config_role=test_account_role,
        app_config_key=test_encryption_key,
        account=TEST_CONTEXT["account"],
        region=TEST_CONTEXT["region"],
    )

    # Render template
    template = assertions.Template.from_stack(stack_test)

    # IAM Policy checks
    template.resource_count_is("AWS::IAM::Policy", 2)


def test_app_config_lambda_configuration(stack_test, mock_app_config_dependencies, mock_app_config):
    """Test AppConfig utils lambda environment"""
    test_lambda_function, test_account_role, test_encryption_key = mock_app_config_dependencies
    test_app_config_base, test_app_config = mock_app_config

    app_config_lambda_configuration(
        lambda_function=test_lambda_function,
        app_config_base=test_app_config_base,
        app_config=test_app_config,
        app_config_role=test_account_role,
    )

    # Render template
    template = assertions.Template.from_stack(stack_test)

    # TO DO RESOLVE HOW TO MATCH THE LAMBDA ENV UPDATES
    template.has_resource_properties(
        "AWS::Lambda::Function",
        props={
            "Environment": {
                "Variables": {},
            },
        },
    )
