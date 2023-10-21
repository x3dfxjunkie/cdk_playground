import os
import json
from aws_cdk import aws_iam, aws_lambda, aws_kms


def name_convention(prefix: str, short_resource_description: str) -> str:
    """Creates necessary naming convention
    Args:
        short_resource_description (str): Name of the resource.
    Returns:
        str: Formatted naming with desired conventions.
    """
    name = f"{prefix}-{short_resource_description}"
    return name


class ErrorAppConfigRegionExtension(Exception):
    """
    App Config Region Exception exception class
    """


def app_config_get_layer_arn(region: str):
    """Function to get the arn of the app config layer extension for a specific region

    Args:
        region (str): AWS region name

    Raises:
        ErrorAppConfigRegionExtension: exception return value if no layers were found.

    Returns:
        str: layer arn value.
    """

    # Load app config lambda extension layer arns
    full_path = os.path.realpath(__file__)
    config_file = open(f"{os.path.dirname(full_path)}/config/app_config_lambda_extensions.json")
    layer_arns = json.load(config_file)

    # AppConfig layer validation
    try:
        return next(layer_arn for layer_region, layer_arn in layer_arns.items() if region == layer_region)

    except StopIteration as exc:
        raise ErrorAppConfigRegionExtension(f"No AppConfig Layer Arn was found for the {region} region") from exc


def app_config_role_grants(
    app_config_role: aws_iam.Role,
    app_config_key: aws_kms.Key,
    region: str,
    account: str,
):
    """Set AppConfig account role permissions

    Args:
        app_config_role (aws_iam.Role): AppConfig IAM role assumed by account principal
        app_config_key: (aws_kms.Key) : AppConfig KMS Encryption key
        region (str): AWS region name
        account (str): AWS account
    """

    app_config_role.add_to_policy(
        aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["appconfig:StartConfigurationSession", "appconfig:GetLatestConfiguration"],
            resources=[f"arn:aws:appconfig:{region}:{account}:*"],
        ),
    )

    app_config_role.add_to_policy(
        aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "kms:Decrypt",
                "kms:DescribeKey",
                "kms:GenerateDataKey*",
                "kms:ReEncrypt*",
            ],
            resources=[app_config_key.key_arn],
        )
    )

    app_config_key.add_to_resource_policy(
        aws_iam.PolicyStatement(
            actions=[
                "kms:Decrypt",
            ],
            principals=[app_config_role],
            resources=["*"],
        )
    )


def app_config_lambda_configuration(
    lambda_function: aws_lambda.Function,
    app_config_role: aws_iam.Role,
    app_config,
    app_config_base,
):
    """Set the required lambda environment variables and permissions for AppConfig layer integration

    Args:
        lambda_function (aws_lambda.Function): Lambda function with AppConfig extension
        app_config (Guest360AppConfig): An instance of Guest360AppConfig
        app_config_base (Guest360AppConfigBase): An instance of Guest360AppConfigBase
        app_config_role (aws_iam.Role): AppConfig IAM role assumed by account principal
    """

    lambda_function.add_to_role_policy(
        aws_iam.PolicyStatement(
            actions=["sts:AssumeRole"],
            effect=aws_iam.Effect.ALLOW,
            resources=[app_config_role.role_arn],
        )
    )

    prefetch_list = [
        (
            f"applications/{app_config_base._app.ref}/environments/{app_config_base.environment.ref}/configurations/{app_config._profile.ref}"
        )
    ]

    config_path = f"http://localhost:2772/applications/{app_config_base._app.name}/environments/{app_config_base.environment.name}/configurations/{app_config._profile.name}"

    # Set AppConfig environment variables
    extension_environment = {
        "AWS_APPCONFIG_EXTENSION_PREFETCH_LIST": ",".join(prefetch_list),
        "AWS_APPCONFIG_EXTENSION_ROLE_ARN": app_config_role.role_arn,
        "APPCONFIG_URL_PATH": config_path,
    }

    for key, value in extension_environment.items():
        lambda_function.add_environment(key, value)
