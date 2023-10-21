"""
Guest360AppConfig construct tests
"""

from app.guest360_constructs.app_config import Guest360AppConfig
from app.guest360_constructs.app_config_base import Guest360AppConfigBase
from aws_cdk import App, Aspects, Environment, Stack
from app.guest360_constructs.kms_key import Guest360KMSKey
from cdk_nag import AwsSolutionsChecks
from aws_cdk.assertions import Template
import pytest

app_config_checks = [
    {
        # Lite default app config configuration
        "props": {
            "app_config_base": {
                "deployment_strategy": {
                    "deployment_duration_in_minutes": 0,
                    "growth_factor": 100,
                    "replicate_to": "NONE",
                },
            },
            "app_config": {
                "deployment": {
                    "configuration_version": "1",
                },
            },
        },
        "template": {
            "deploy_template": {
                "ConfigurationVersion": "1",
                "Description": "lst-TestStack-use1-TestAppConfig-AppConfigDeployment",
            },
            "profile_template": {
                "Description": "lst-TestStack-use1 TestAppConfig AppConfig Profile",
                "Name": "lst-teststack-use1-testappconfig-profile",
                "LocationUri": "hosted",
            },
            "app_template": {
                "Description": "lst-TestStack-use1 TestAppConfig AppConfig Application",
                "Name": "lst-teststack-use1-testappconfig-app",
            },
            "environment_template": {
                "Description": "lst-TestStack-use1 TestAppConfig AppConfig Environment",
                "Name": "lst-teststack-use1-testappconfig-env",
            },
            "deployment_strategy_template": {
                "Description": "lst-TestStack-use1 TestAppConfig AppConfig Deployment Strategy",
                "Name": "lst-teststack-use1-testappconfig-dep-strategy",
                "GrowthFactor": 100,
                "ReplicateTo": "NONE",
            },
        },
    },
    {
        # Custom hosted app config configuration
        "props": {
            "app_config_base": {
                "application": {
                    "name": "app-custom-name",
                    "description": "This is app config custom app",
                },
                "environment": {
                    "name": "env-custom-name",
                    "description": "This is app config custom env",
                },
                "deployment_strategy": {
                    "deployment_duration_in_minutes": 0,
                    "growth_factor": 100,
                    "replicate_to": "NONE",
                    "name": "deployment-strategy-custom-name",
                    "description": "This is app config custom deployment strategy",
                    "final_bake_time_in_minutes": 10,
                    "growth_type": "LINEAR",
                },
            },
            "app_config": {
                "configuration_profile": {
                    "name": "profile-custom-name",
                    "description": "This is app config custom configuration profile",
                    "location_uri": "hosted",
                    "retrieval_role_arn": "arn:aws:iam::123456789012:role/TestRole",
                    "type": "AWS.AppConfig.FeatureFlags",
                    "validators": [
                        {
                            "Content": "arn:aws:lambda:us-east-1:123456789012:function:ValidatorSchemaLambda",
                            "Type": "LAMBDA",
                        },
                    ],
                },
                "deployment": {
                    "configuration_version": "1",
                    "encryption_key": None,
                    "description": "This is app config custom deployment",
                },
                "hosted_configuration": {
                    "content": {
                        "boolEnableLimitResults": True,
                        "intResultLimit": 5,
                    },
                    "content_type": "application/json",
                    "description": "This is app config custom hosted configuration",
                    "latest_version_number": 1,
                    "version_label": "latest",
                },
            },
        },
        "template": {
            "deploy_template": {
                "ConfigurationVersion": "1",
                "Description": "This is app config custom deployment",
            },
            "profile_template": {
                "Description": "This is app config custom configuration profile",
                "Name": "lst-teststack-use1-profile-custom-name",
                "LocationUri": "hosted",
                "RetrievalRoleArn": "arn:aws:iam::123456789012:role/TestRole",
                "Type": "AWS.AppConfig.FeatureFlags",
            },
            "app_template": {
                "Description": "This is app config custom app",
                "Name": "lst-teststack-use1-app-custom-name",
            },
            "environment_template": {
                "Description": "This is app config custom env",
                "Name": "lst-teststack-use1-env-custom-name",
            },
            "hosted_cfg_template": {
                "Description": "This is app config custom hosted configuration",
                "LatestVersionNumber": 1,
                "VersionLabel": "latest",
                "Content": '{"boolEnableLimitResults": true, "intResultLimit": 5}',
                "ContentType": "application/json",
            },
            "deployment_strategy_template": {
                "Description": "This is app config custom deployment strategy",
                "Name": "lst-teststack-use1-deployment-strategy-custom-name",
                "GrowthFactor": 100,
                "GrowthType": "LINEAR",
                "ReplicateTo": "NONE",
                "DeploymentDurationInMinutes": 0,
            },
        },
    },
]


test_context = {
    "environment": "latest",
    "stack_name": "testStack",
    "prefix": "lst-TestStack-use1",
    "prefix_global": "lst-testStack",
    "account": "123456789",
    "region": "us-east-1",
}

stack_id = "TestStack"
construct_id = "TestAppConfig"


@pytest.fixture
def stack_test():
    test_app = App(context=test_context)
    aspects = Aspects.of(test_app)
    aspects.add(AwsSolutionsChecks(verbose=True))
    stack_test = Stack(
        test_app, stack_id, env=Environment(account=test_context["account"], region=test_context["region"])
    )
    yield stack_test


@pytest.mark.parametrize("checks", app_config_checks)
def test_hosted_app_config_provisioning(checks: dict, stack_test):
    """Test the successful creation of AppConfig hosted deploy resources"""

    app_config_base = Guest360AppConfigBase(
        stack_test,
        construct_id,
        props=checks["props"]["app_config_base"],
    )

    # Custom encryption key
    deployment_props = checks["props"]["app_config"]["deployment"]
    if "encryption_key" in deployment_props:
        deployment_props["encryption_key"] = Guest360KMSKey(
            stack_test,
            "AppConfigEncryptionKey",
            {"alias": construct_id, "description": f"{construct_id}-CustomEncryptionKey"},
        ).key

    # Updated AppConfig props
    checks["props"]["app_config"].update(
        {
            "application_id": app_config_base._app.ref,
            "deployment_strategy_id": app_config_base._deployment_strategy.ref,
            "environment_id": app_config_base.environment.ref,
        }
    )

    Guest360AppConfig(
        stack_test,
        construct_id,
        props=checks["props"]["app_config"],
    )
    # render template
    template = Template.from_stack(stack_test)

    template.has_resource_properties(
        "AWS::AppConfig::Deployment",
        props=checks["template"]["deploy_template"],
    )

    template.has_resource_properties(
        "AWS::AppConfig::Application",
        props=checks["template"]["app_template"],
    )

    template.has_resource_properties(
        "AWS::AppConfig::Environment",
        props=checks["template"]["environment_template"],
    )

    template.has_resource_properties(
        "AWS::AppConfig::ConfigurationProfile",
        props=checks["template"]["profile_template"],
    )

    if "hosted_cfg_template" in checks["template"]:
        template.has_resource_properties(
            "AWS::AppConfig::HostedConfigurationVersion",
            props=checks["template"]["hosted_cfg_template"],
        )

    template.has_resource_properties(
        "AWS::AppConfig::DeploymentStrategy",
        props=checks["template"]["deployment_strategy_template"],
    )
