"""
File for Guest360 AppConfig base resources construct
"""
from aws_cdk import aws_appconfig
from typing import TypedDict, Optional

from app.guest360_constructs.construct_360 import Construct360
from strongtyping.strong_typing import match_class_typing, TypeMisMatch
from typing_extensions import NotRequired
from app.src.reliability.utils import AppConfigName


@match_class_typing
class AppConfigAppProps(TypedDict):
    """
    Guest360 AppConfig Properties
    """

    name: Optional[str]  # A name for the application
    description: NotRequired[str]  # A description of the application


@match_class_typing
class AppConfigEnvironmentProps(TypedDict):
    """
    Guest360 AppConfig Environment Properties
    """

    name: Optional[str]  # A name for the environment
    description: NotRequired[str]  # A description of the environment


@match_class_typing
class AppConfigDeploymentStrategyProps(TypedDict):
    """
    Guest360 AppConfig Deployment Strategy Properties
    """

    deployment_duration_in_minutes: int  # Total amount of time for a deployment to last
    growth_factor: int  # The percentage of targets to receive a deployed configuration during each interval
    replicate_to: str  # Save the deployment strategy to a Systems Manager (SSM) document
    name: Optional[str]  # A name for the deployment strategy
    description: NotRequired[str]  # A description of the deployment strategy
    final_bake_time_in_minutes: NotRequired[
        int
    ]  # Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete
    growth_type: NotRequired[str]  # The algorithm used to define how percentage grows over time


@match_class_typing
class AppConfigBaseProps(TypedDict):
    """
    Guest360 AppConfig Properties
    """

    deployment_strategy: dict  # The deployment strategy ID. This should be AppConfigDeploymentStrategyProps
    application: Optional[dict]  # The application ID. This should be AppConfigAppProps
    environment: Optional[dict]  # The environment ID. This should be AppConfigEnvironmentProps


class Guest360AppConfigBase(Construct360):
    """
    Guest360 AppConfig base resources construct
    """

    @property
    def environment_id(self):
        return self.environment.ref

    @property
    def application_id(self):
        return self._app.ref

    @property
    def deployment_strategy_id(self):
        return self._deployment_strategy.ref

    def __init__(self, scope: Construct360, construct_id: str, props: AppConfigBaseProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # App props check
        Guest360AppConfigBase.app_config_properties_validation(props)  # type: ignore

        self.prefix = self.node.try_get_context("prefix")

        # Create AppConfig App
        self.create_app_config_app(props["application"], construct_id)  # type: ignore

        # Create AppConfig Environment
        self.create_app_config_environment(props["environment"], construct_id)  # type: ignore

        # Create AppConfig Deployment Strategy
        self.create_app_config_deployment_strategy(props["deployment_strategy"], construct_id)

    @staticmethod
    def app_config_properties_validation(props: dict):
        AppConfigBaseProps(props)  # type: ignore

        # Set defaults
        for key in ["application", "environment"]:
            props.setdefault(key, {})

        AppConfigAppProps(props.get("application", None))
        AppConfigEnvironmentProps(props.get("environment", None))
        AppConfigDeploymentStrategyProps(props.get("deployment_strategy", None))

    def create_app_config_app(self, app_props: dict, construct_id: str):
        """
        Function to create an AppConfig App
        """

        # Build app name
        app_props["name"] = AppConfigName(self.prefix, app_props.get("name", f"{construct_id}-app")).name()

        # Set default description
        app_props.setdefault("description", f"{self.prefix} {construct_id} AppConfig Application")

        self._app = aws_appconfig.CfnApplication(self, app_props["name"], **app_props)

    def create_app_config_environment(self, env_props: dict, construct_id: str):
        """
        Function to create an AppConfig Environment
        """

        # Build environment name
        env_props["name"] = AppConfigName(self.prefix, env_props.get("name", f"{construct_id}-env")).name()

        # Set default description
        env_props.setdefault("description", f"{self.prefix} {construct_id} AppConfig Environment")

        # Update application id
        env_props["application_id"] = self._app.ref

        self.environment = aws_appconfig.CfnEnvironment(self, env_props["name"], **env_props)

    def create_app_config_deployment_strategy(self, deployment_strategy_props: dict, construct_id: str):
        """
        Function to create an AppConfig Deployment Strategy
        """

        # Buil deployment strategy name
        deployment_strategy_props["name"] = AppConfigName(
            self.prefix, deployment_strategy_props.get("name", f"{construct_id}-dep-strategy")
        ).name()

        # Set default description
        deployment_strategy_props.setdefault(
            "description", f"{self.prefix} {construct_id} AppConfig Deployment Strategy"
        )

        self._deployment_strategy = aws_appconfig.CfnDeploymentStrategy(
            self, deployment_strategy_props["name"], **deployment_strategy_props
        )
