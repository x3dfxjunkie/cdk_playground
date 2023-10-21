"""
Guest360 AWS RDS Instance
"""

from typing import List, TypedDict

import aws_cdk
from aws_cdk import aws_ec2, aws_iam, aws_rds
from aws_cdk import custom_resources as cr
from cdk_nag import NagSuppressions
from typing_extensions import NotRequired

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.kms_key import Guest360KMSKey
from app.src.reliability.utils import StackName


class Guest360RDSInstanceProps(TypedDict):
    engine: aws_rds.IInstanceEngine
    database_name: str
    iam_authentication: bool
    parameters: NotRequired[dict]


class Guest360RDSInstance(Construct360):
    """
    Guest360 AWS RDS istance construct
    """

    @property
    def rds_instance(self) -> aws_rds.DatabaseInstance:
        """
        Return RDS instance
        """
        return self.db_instance

    @property
    def iam_access_authentication_policy(self) -> aws_iam.Policy:
        """
        Return IAM access authentication policy
        """
        return self._access_iam_authentication_policy

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        environment_config: dict,
        props: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.init_config(construct_id, props)
        self.networking_config(environment_config, props)
        self.add_encryption_key(construct_id, props)
        self.db_instance = aws_rds.DatabaseInstance(self, construct_id, **props)

        self.add_iam_authentication_policy(props)
        self.add_nag_suppressions()

    def init_config(self, construct_id, props):
        """init_config"""
        self._stack = aws_cdk.Stack.of(self)
        self._prefix = self.node.try_get_context("prefix")
        self._naming_prefix = f"{self._prefix}-{construct_id}"
        Guest360RDSInstanceProps(props)

    def networking_config(self, environment_config, props):
        """networking config"""
        subnets_config = environment_config["networking"][self._stack.region]["subnets"]["non-routable"]
        vpc_config = environment_config["networking"][self._stack.region]["vpc"]["id"]
        self._account_id = self._stack.account
        subnet_id_list: List[str] = []

        for subnet in subnets_config:
            subnet_id_list.append(subnet["id"])

        # Grab the VPC from lookup
        vpc = aws_ec2.Vpc.from_lookup(self, StackName(self._naming_prefix, "vpc").name(), vpc_id=vpc_config)
        props["vpc"] = vpc
        # Grab subnets
        props["vpc_subnets"] = aws_ec2.SubnetSelection(
            subnets=[
                aws_ec2.Subnet.from_subnet_id(scope=self, id=f"{self._prefix}-{subnt_id}", subnet_id=subnt_id)
                for subnt_id in subnet_id_list
            ]
        )

    def add_encryption_key(self, construct_id, props):
        """add_encryption_key"""
        # if no encryption set create custom encryption key using Guest360KMSKey
        if props.get("storage_encrypted", True) and props.get("storage_encryption_key") is None:
            props["storage_encryption_key"] = Guest360KMSKey(
                self,
                "StorageEncryptionKey",
                {
                    "alias": construct_id,
                    "description": f"{self._prefix}-{construct_id}-RDSInstanceStorageEncryptionKey",
                },
            ).key

            props["storage_encryption_key"].grant_encrypt_decrypt(aws_iam.AccountRootPrincipal())

    def add_iam_authentication_policy(self, props):
        """Add policy for access to db instance if iam_authentication is set to TRUE. Only applies to mySQL/MariaDB, is not supported for Oracle"""
        self.db_resource_id = self.get_db_resource_id()
        if props["iam_authentication"]:
            self.dbuser = self.db_resource_id.get_response_field("DBInstances.0.DbiResourceId")
            access_policy_statement = aws_iam.PolicyStatement(
                actions=["rds-db:connect"],
                resources=[
                    f"arn:aws:rds-db:{self._stack.region}:{self._account_id}:dbuser:{self.dbuser}/{self.db_instance.secret.secret_value_from_json('username').unsafe_unwrap(),}"
                ],
                effect=aws_cdk.aws_iam.Effect.ALLOW,
            )
            self._access_iam_authentication_policy = aws_iam.Policy(
                self,
                f"{self._prefix}-rds-access-autenthication-policy",
                statements=[access_policy_statement],
            )

    def get_db_resource_id(self):
        """get_db_resource_id"""

        return cr.AwsCustomResource(
            self,
            f"{self._naming_prefix}-describe-instance",
            on_update=cr.AwsSdkCall(
                service="RDS",
                action="describeDBInstances",
                parameters={"DBInstanceIdentifier": self.db_instance.instance_identifier},
                physical_resource_id=cr.PhysicalResourceId.of(self.db_instance.instance_identifier),
                output_paths=["DBInstances.0.DbiResourceId"],
            ),
            policy=cr.AwsCustomResourcePolicy.from_sdk_calls(resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE),
        )

    def add_nag_suppressions(self):
        """add_nag_suppressions"""
        add_nag_suppression(self.db_instance, "AwsSolutions-SMG4", "Have backlog story to add lambda rotator")
        add_nag_suppression(
            self.db_instance,
            "AwsSolutions-RDS3",
            "It's ok the non-Aurora RDS DB instance does not have multi-AZ support enabled.",
        )
        add_nag_suppression(
            self.db_instance,
            "AwsSolutions-RDS10",
            "It's ok the RDS instance or Aurora DB cluster does not have deletion protection enabled.",
        )
        add_nag_suppression(
            self.db_instance,
            "AwsSolutions-RDS11",
            "It's ok the RDS instance or Aurora DB cluster uses the default endpoint port.",
        )
        add_nag_suppression(
            self.db_resource_id,
            "AwsSolutions-IAM5",
            "wild card permission ok for describe instance",
        )


def add_nag_suppression(resource, id_nag, reason):
    """add nad suppression function"""
    NagSuppressions.add_resource_suppressions(
        resource,
        [
            {
                "id": id_nag,
                "reason": reason,
            }
        ],
        True,
    )
