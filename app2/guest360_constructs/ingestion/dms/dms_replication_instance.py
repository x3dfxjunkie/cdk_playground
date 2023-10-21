"""Guest360 DMS Replication Instance Construct
"""
from typing import List, Optional, TypedDict

from aws_cdk import aws_dms
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import StackName, DMSResourceName


class SubnetGroupProps(TypedDict):
    group_name: str  # name of subnet group
    description: str  # description of subnet group
    subnet_list: List[str]  # List of subnets to be included in subnet group
    subnet_identifer: str  # identifier for subnet group


@match_class_typing
class DMSReplicationProps(TypedDict):
    """DMS Replication Props Class"""

    name: str  # name for the replication instance
    instance_class: str  # class size/type for replication instance e.g., dms.t2.micro
    storage: int  # size in GB for data
    auto_minor_version_upgrade: bool  # True/False if automatic minor upgrade should be applied
    allow_major_version_upgrade: bool  # flag to control controlling version upgrades if manually specified
    engine_version: str  # version of dms engine e.g., 3.4.6
    multi_az: bool  # True/False if multi AZ should be applied
    maint_window: str  # e.g., "Mon:00:00-Mon:01:00"
    instance_identifier: str  # e.g., # "Example-App-ARN1"
    security_group_ids: Optional[List[str]]  # list of security group ids ["sg-abc"]
    subnet_props: NotRequired[SubnetGroupProps]  # Props for subnet group


class Guest360DMSReplication(Construct360):
    """Class for DMS replication instance construct

    Args:
        Construct: aws_cdk construct
    """

    @property
    def dms_replication_instance(self):
        return self.instance

    @property
    def dms_replication_instance_name(self) -> str:
        return self._replication_instance_name

    def __init__(self, scope: Construct360, construct_id: str, props: DMSReplicationProps, **kwargs) -> None:
        """Construct to create DMS replication instance

        Args:
            scope (Construct):
            construct_id (str): Construct ID
            props (dict): Configurations for DMS Replication Instance - see DMSReplicationProps TypedDict
        Returns:
            None
        """

        super().__init__(scope, construct_id, **kwargs)

        prefix = self.node.try_get_context("prefix").lower()
        self.naming_prefix = f"{prefix}-{construct_id}"

        # Type check replication instance props
        replication_instance_props = props

        DMSReplicationProps(replication_instance_props)  # type: ignore

        subnet_group_props = replication_instance_props["subnet_props"]

        # add prefix to identfiers/resource names
        replication_instance_props["name"] = DMSResourceName(prefix, replication_instance_props["name"]).name()
        self._replication_instance_name = replication_instance_props["name"]
        replication_instance_props["instance_identifier"] = DMSResourceName(
            prefix, replication_instance_props["instance_identifier"]
        ).name()
        subnet_group_props["subnet_identifer"] = f"{prefix}-{subnet_group_props['subnet_identifer']}"

        # TODO:  I am leaving this for reference as we need to create a static generic DMS role for this when we build the L3 construct.  Also use the GUest360 construct for IAM.  DMS Replication Instance and SubnetGroup resource creation will fail if the dms-vpc-role IAM role doesn't already exist.
        # self.dms_vpc_role = aws_iam.Role(
        #     self,
        #     "dms-vpc-role",
        #     assumed_by=aws_iam.ServicePrincipal("dms.amazonaws.com"),
        #     managed_policies=[
        #         aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonDMSVPCManagementRole")
        #     ],
        #     role_name="dms-vpc-role",
        # )

        self.cfn_replication_subnet_group = aws_dms.CfnReplicationSubnetGroup(
            self,
            StackName(self.naming_prefix, subnet_group_props["group_name"]).name(),
            replication_subnet_group_description=subnet_group_props["description"],
            subnet_ids=subnet_group_props["subnet_list"],
            replication_subnet_group_identifier=subnet_group_props["subnet_identifer"],
        )

        #  TODO: this is a dependency for when we create the dms-vpc-role
        # self.cfn_replication_subnet_group.node.add_dependency(
        #     self.dms_vpc_role)

        self.instance = aws_dms.CfnReplicationInstance(
            self,
            StackName(self.naming_prefix, replication_instance_props["name"]).name(),
            replication_instance_class=replication_instance_props["instance_class"],
            allocated_storage=replication_instance_props["storage"],
            allow_major_version_upgrade=replication_instance_props["allow_major_version_upgrade"],
            auto_minor_version_upgrade=replication_instance_props["auto_minor_version_upgrade"],
            engine_version=replication_instance_props["engine_version"],
            multi_az=replication_instance_props["multi_az"],
            preferred_maintenance_window=replication_instance_props["maint_window"],
            publicly_accessible=False,
            replication_instance_identifier=replication_instance_props["name"],
            replication_subnet_group_identifier=subnet_group_props["subnet_identifer"],
            resource_identifier=replication_instance_props["instance_identifier"],
            vpc_security_group_ids=replication_instance_props["security_group_ids"],
        )

        self.dms_replication_instance.node.add_dependency(self.cfn_replication_subnet_group)  # self.dms_vpc_role,
