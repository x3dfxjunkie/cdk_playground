"""
File for Guest360 AppConfig construct
"""
import json
from aws_cdk import aws_appconfig, aws_kms
from typing import TypedDict, Optional, Union

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.kms_key import Guest360KMSKey
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired
from app.src.reliability.utils import AppConfigName


@match_class_typing
class AppConfigProfileProps(TypedDict):
    """
    Guest360 AppConfig Profile Properties
    """

    name: Optional[str]  # A name for the configuration profile
    location_uri: Optional[
        str
    ]  # A URI to locate the configuration. Default: "hosted". For more info see https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_appconfig/CfnConfigurationProfile.html#aws_cdk.aws_appconfig.CfnConfigurationProfile.location_uri
    description: NotRequired[str]  # A description of the configuration profile
    retrieval_role_arn: NotRequired[
        str
    ]  # The ARN of an IAM role with permission to access the configuration at the specified LocationUri. Not required for configurations stored in the AWS AppConfig hosted configuration store
    type: NotRequired[
        str
    ]  # The type of configurations contained in the profile. AWS AppConfig supports feature flags and freeform configurations
    validators: NotRequired[list]  # A list of methods for validating the configuration


@match_class_typing
class AppConfigHostedConfigurationVersionProps(TypedDict):
    """
    Guest360 AppConfig Hosted Configuration Version Properties
    """

    content: Union[dict, None]  # The content of the configuration or the configuration data
    content_type: Optional[str]  # A standard MIME type describing the format of the configuration content
    description: NotRequired[str]  # A description of the configuration
    latest_version_number: NotRequired[
        int
    ]  # An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version
    version_label: NotRequired[str]  # A user-defined label for an AWS AppConfig hosted configuration version


@match_class_typing
class AppConfigDeploymentProps(TypedDict):
    """
    Guest360 AppConfig Deployment Properties
    """

    encryption_key: Optional[
        aws_kms.Key
    ]  # The AWS KMS key, AWS AppConfig uses this ID to encrypt the configuration data using a customer managed key.
    description: NotRequired[str]  # A description of the deployment


@match_class_typing
class AppConfigProps(TypedDict):
    """
    Guest360 AppConfig Deployment Properties
    """

    application_id: Union[str, None]  # The AppConfig application ID
    deployment_strategy_id: Union[str, None]  # The AppConfig deployment strategy ID
    environment_id: Union[str, None]  # The AppConfig environment ID

    deployment: Optional[dict]  # AppConfig Deployment Properties. This should be AppConfigDeploymentProps
    configuration_profile: Optional[
        dict
    ]  # AppConfig Configuration Profile properties. This should be AppConfigProfileProps

    hosted_configuration: NotRequired[
        dict
    ]  # AppConfig Hosted Configuration Version properties. This should be AppConfigHostedConfigurationVersionProps


class Guest360AppConfig(Construct360):
    """
    Guest360 AppConfig Construct
    """

    @property
    def key(self):
        return self._encryption_key

    @property
    def configuration_id(self):
        return self._profile.ref

    def __init__(self, scope: Construct360, construct_id: str, props: AppConfigProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # App props check
        Guest360AppConfig.app_config_properties_validation(props)  # type: ignore

        self.prefix = self.node.try_get_context("prefix")

        app_id = props["application_id"]
        env_id = props["environment_id"]
        strategy_id = props["deployment_strategy_id"]

        # Create AppConfig Configuration Profile
        self.create_app_config_configuration_profile(
            props["configuration_profile"], application_id=app_id, construct_id=construct_id
        )

        # Create AppConfig Hosted Configuration Version
        if props.get("hosted_configuration"):
            self.create_app_config_hosted_configuration(props["hosted_configuration"], application_id=app_id, construct_id=construct_id)  # type: ignore

        # Create AppConfig Deployment
        self.create_app_config_deployment(
            props["deployment"],
            construct_id=construct_id,
            application_id=app_id,
            environment_id=env_id,
            deployment_strategy_id=strategy_id,
        )

    @staticmethod
    def app_config_properties_validation(props: dict):
        AppConfigProps(props)  # type: ignore

        # Set default
        props.setdefault("configuration_profile", {})
        props.setdefault("deployment", {})

        AppConfigProfileProps(props.get("configuration_profile", None))

        AppConfigDeploymentProps(props.get("deployment", None))

        if hosted_configuration := props.get("hosted_configuration"):
            AppConfigHostedConfigurationVersionProps(hosted_configuration)

    def create_app_config_configuration_profile(self, profile_props: dict, application_id: str, construct_id: str):
        """
        Function to create an AppConfig Configuration Profile
        """
        # Build profile name
        profile_props["name"] = AppConfigName(self.prefix, profile_props.get("name", f"{construct_id}-profile")).name()

        # Update application id
        profile_props["application_id"] = application_id

        # Set default description
        profile_props.setdefault("description", f"{self.prefix} {construct_id} AppConfig Profile")

        # Set default hosted location_uri
        profile_props.setdefault("location_uri", "hosted")

        self._profile = aws_appconfig.CfnConfigurationProfile(
            self, profile_props.get("name", f"{construct_id}-profile"), **profile_props
        )

    def create_app_config_hosted_configuration(self, hosted_config_props: dict, application_id: str, construct_id: str):
        """
        Function to create an AppConfig Hosted Configuration
        """

        # Skip if not hosted location uri value is specified
        if self._profile.location_uri != "hosted":
            return

        # Update application and profile id
        hosted_config_props["application_id"] = application_id
        hosted_config_props["configuration_profile_id"] = self._profile.ref  # type: ignore

        # Set default content type
        hosted_config_props.setdefault("content_type", "application/json")

        # Update content format
        hosted_config_props["content"] = json.dumps(hosted_config_props["content"])

        # Set default description
        hosted_config_props.setdefault(
            "description", f"{self.prefix} {construct_id} AppConfig Hosted Configuration Version"
        )

        self._hosted_config = aws_appconfig.CfnHostedConfigurationVersion(self, f"{construct_id}-hosted-cfg", **hosted_config_props)  # type: ignore

    def create_app_config_deployment(
        self,
        deployment_props: dict,
        application_id: str,
        environment_id: str,
        deployment_strategy_id: str,
        construct_id: str,
    ):
        """
        Function to create an AppConfig Deployment
        """
        # Set KMS key
        if "encryption_key" not in deployment_props:
            self._encryption_key = Guest360KMSKey(
                self,
                "AppConfigEncryptionKey",
                {"alias": construct_id, "description": f"{self.prefix}-{construct_id}-AppConfigEncryptionKey"},
            ).key
        else:
            self._encryption_key = deployment_props["encryption_key"]

        # Set default description
        deployment_props.setdefault("description", f"{self.prefix}-{construct_id}-AppConfigDeployment")

        # AppConfig Deployment definition
        self.deployment = aws_appconfig.CfnDeployment(
            self,
            f"{construct_id}-deployment",
            application_id=application_id,
            configuration_profile_id=self._profile.ref,
            configuration_version=(
                deployment_props["configuration_version"]
                if deployment_props.get("configuration_version")
                else self._hosted_config.ref
            ),
            deployment_strategy_id=deployment_strategy_id,
            environment_id=environment_id,
            description=deployment_props["description"],
            kms_key_identifier=self._encryption_key.key_id,
        )
