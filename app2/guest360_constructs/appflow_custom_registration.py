""" AppFlow Custom Connector Registration Construct """
import os
from typing import TypedDict
from aws_cdk import Stack, CfnResource, cloudformation_include as cfn_inc
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired
from app.guest360_constructs.construct_360 import Construct360


@match_class_typing
class Guest360AppFlowCustomRegistrationProps(TypedDict):
    custom_connector_label: str  # Assing Connector label name
    custom_lambda_arn: str  # Inform the lambda arn who stores the custom connector
    custom_description: NotRequired[str]  # Assign Connector description
    preserve_logical_ids: NotRequired[bool]  # Use to let CDK generate new resourceID (false suggested by docs)


class Guest360AppFlowCustomRegistration(Construct360):
    """App Flow Custom Connector Registration.It uses a mix of Cloud Formation template and CDK code
    because Appflow connector registration does not have a CDK construct (L1 or above).
    Args:
        Construct (Construct360): Defined as a re-usable Contruct object
    """

    @property
    def get_custom_appflow_connector(self) -> CfnResource:
        return self._custom_appflow_connector

    def __init__(
        self, scope: Construct360, construct_id: str, props: Guest360AppFlowCustomRegistrationProps, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        Guest360AppFlowCustomRegistrationProps(props)

        prefix = self.node.try_get_context("prefix")
        stack = Stack.of(self)

        # path to the generic appflow custom connector template
        full_path = os.path.realpath(__file__)
        config_dir = f"{os.path.dirname(full_path)}/../infrastructure/ingestion/config/appflow"

        # if not props["preserve_logical_ids"] defined set to false (suggested when working with CDK to generate new resource ID)
        if props.get("preserve_logical_ids") is None:
            props["preserve_logical_ids"] = False

        # Create custom connector using CF template and imported to CDK
        custom_appflow_template = cfn_inc.CfnInclude(
            stack,
            f"Template_{props['custom_connector_label']}",
            template_file=f"{config_dir}/appflow_custom_connector.yaml",
            preserve_logical_ids=props["preserve_logical_ids"],
            parameters={
                "custom_connector_label": f"{prefix}-{props['custom_connector_label']}",
                "custom_lambda_arn": props["custom_lambda_arn"],
                "custom_description": props["custom_description"],
            },
        )
        self._custom_appflow_connector = custom_appflow_template.get_resource("CustomAppFlowConnector")
