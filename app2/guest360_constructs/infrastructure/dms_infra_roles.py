""" DMS account level roles Contruct Stack
"""
from typing import TypedDict

from aws_cdk import aws_iam
from aws_cdk.aws_iam import ServicePrincipal
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import StackName


class RolesProps(TypedDict):
    role_name: str
    description: str


class DMSRolesProps(TypedDict):
    dms_vpc_role: RolesProps  # should be RolesProps
    dms_cloudwatch_role: RolesProps  # RolesProps
    dms_redshift_role: RolesProps  # RolesProps
    dms_svc_principal: ServicePrincipal


class DMSRoles(Construct360):
    """Construct class that creates a DMS account level IAM Resource"""

    def __init__(self, scope: Construct360, construct_id: str, props: DMSRolesProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        global_prefix = self.node.try_get_context("prefix_global")

        # Create generic DMS roles. Cannot use Guest360 iam_role construct as we need an explicit naming convention for the roles
        # DMS management tasks requires these IAM roles to exist at the account level

        dms_props = props
        iam_vpc_props = props["dms_vpc_role"]
        iam_cloudwatch_props = props["dms_cloudwatch_role"]

        dms_vpc_role = aws_iam.Role(
            self,
            StackName(global_prefix, iam_vpc_props["role_name"]).name(),
            assumed_by=dms_props["dms_svc_principal"],
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonDMSVPCManagementRole")
            ],
            role_name=iam_vpc_props["role_name"],
            description=iam_vpc_props["description"],
        )

        dms_cloudwatch_role = aws_iam.Role(
            self,
            StackName(global_prefix, iam_cloudwatch_props["role_name"]).name(),
            assumed_by=dms_props["dms_svc_principal"],
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AmazonDMSCloudWatchLogsRole"  # pragma: allowlist secret
                )
            ],
            role_name=iam_cloudwatch_props["role_name"],
            description=iam_cloudwatch_props["description"],
        )

        NagSuppressions.add_resource_suppressions(
            dms_vpc_role,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Managed policies are ok.",
                    "applies_to": "Policy::arn:<AWS::Partition>:iam::aws"
                    + ":policy/service-role/AmazonDMSVPCManagementRole",
                }
            ],
            True,
        )

        NagSuppressions.add_resource_suppressions(
            dms_cloudwatch_role,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Managed policies are ok.",
                    "applies_to": "Policy::arn:<AWS::Partition>:iam::aws"
                    + ":policy/service-role/AmazonDMSCloudWatchLogsRole",
                }
            ],
            True,
        )
