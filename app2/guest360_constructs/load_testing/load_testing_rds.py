"""LoadTesting RDS Construct for guest360"""
import logging
import os
import sys
from pathlib import Path
from typing import List, TypedDict
from typing_extensions import NotRequired

import aws_cdk
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.guest360_constructs.rds_instance import Guest360RDSInstance, Guest360RDSInstanceProps

from app.src.reliability.utils import StackName

from app.src.utils.feature_flag.feature_flag import FeatureFlag
from aws_cdk import (
    Stack,
    Token,
    aws_ec2,
    aws_iam,
    aws_lambda,
)
from cdk_nag import NagSuppressions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Load_testing | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

KMS_DECRYPT_ACTION = "kms:Decrypt"


class LoadTestingRDSProps(TypedDict):
    rds: Guest360RDSInstanceProps  # RDS Instance props
    network_config: dict  # dict of networking configs
    dms_table_mappings: NotRequired[dict]


class LoadTestingRDS(Construct360):
    """Class for LoadTesting Constructor
    Creates an RDS instance and an initial lambda for load-testing"""

    def __init__(self, scope: Construct360, construct_id: str, props: dict, environment_config, **kwargs) -> None:
        """Construct to create resources for loadtesting App
        Args:
            scope (Construct360):
            construct_id (str): Construct ID
            props (dict): Configurations for LoadTesting RDS DBinstance - see LoadTestingRDSProps TypedDict
        """

        super().__init__(scope, construct_id, **kwargs)

        self.prefix = self.node.try_get_context("prefix")
        self.naming_prefix = f"{self.prefix}-{construct_id}"

        # Type check props
        LoadTestingRDSProps(props)

        # Get current environment
        self.environment = self.node.try_get_context("environment")

        # Get stack
        self.stack = Stack.of(self)
        # load networking config
        self.networking_config(environment_config)
        # pathing
        stack_path = self.node.try_get_context("stack_path")

        # Create lambda role
        self.lambda_role = self.create_role(
            f"{construct_id}-lambda-role", "lambda.amazonaws.com", "generic role for lambda resources"
        )

        self.lambda_role.role.add_managed_policy(
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        )
        self.lambda_role.role.add_managed_policy(
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaVPCAccessExecutionRole")
        )

        # Provision RDS instance
        config_path = f"{stack_path}/app/configs/{self.environment}-infra-feature-flags.yaml"

        # deploy the RDS instance just if the global feature flag is enabled
        with FeatureFlag(self.environment, "rds_instances.rds_load_testing", config_path) as rds_instance_flag:
            if rds_instance_flag:
                self.deploy_rds_instance(construct_id, environment_config, props["rds"])
                self.lambda_init_rds = self.create_init_rds_lambda(construct_id, props["rds"], self.lambda_role.role)
                # Attach permission to lambda, only required if iam_authentication set to True
                if props["rds"]["iam_authentication"]:
                    self.lambda_init_rds.function.role.attach_inline_policy(
                        self.rds_instance.iam_access_authentication_policy
                    )
                self.rds_instance.rds_instance.connections.allow_from(
                    self.lambda_init_rds.function.connections.security_groups[0],
                    aws_ec2.Port.tcp(int(Token.as_number(self.rds_instance.rds_instance.db_instance_endpoint_port))),
                )
                self.rds_instance.rds_instance.secret.grant_read(self.lambda_init_rds.function.role)

                network_config = props["network_config"]
                ingress_cidrs = network_config["allowlist"]["ingress"]["cidrs"]

                for ingress_cidr in ingress_cidrs:
                    self.rds_instance.rds_instance.connections.allow_from(
                        aws_ec2.Peer.ipv4(ingress_cidr),
                        aws_ec2.Port.tcp(
                            int(Token.as_number(self.rds_instance.rds_instance.db_instance_endpoint_port))
                        ),
                    )

                # add rds manager lambda
                self.lambda_rds_manager = self.create_rds_manager_lambda(
                    construct_id, props["rds"], self.lambda_role.role
                )

                rds_manager_policies = aws_iam.ManagedPolicy(
                    self,
                    "ManagedPolicyforRDSManagerlambda",
                    statements=[
                        aws_iam.PolicyStatement(
                            actions=[
                                "rds:StopDBInstance",
                                "rds:StartDBInstance",
                                "rds:DescribeReservedDBInstancesOfferings",
                                "rds:DescribeReservedDBInstances",
                                "rds:ListTagsForResource",
                                "rds:DescribeValidDBInstanceModifications",
                                "rds:DescribeDBInstances",
                                "rds:DescribeSourceRegions",
                                "rds:DescribePendingMaintenanceActions",
                                "rds:DescribeDBLogFiles",
                                "rds:ModifyDBInstance",
                                "rds:RebootDBInstance",
                                "rds:ApplyPendingMaintenanceAction",
                                "rds:DescribeCertificates",
                                "rds:ModifyCertificates",
                            ],
                            resources=[self.rds_instance.rds_instance.instance_arn],
                            effect=aws_iam.Effect.ALLOW,
                        ),
                        aws_iam.PolicyStatement(
                            actions=[
                                "dms:ModifyReplicationInstance",
                                "dms:RebootReplicationInstance",
                            ],
                            resources=[f"arn:aws:dms:{self.stack.region}:{self.stack.account}:rep:*"],
                            effect=aws_iam.Effect.ALLOW,
                        ),
                    ],
                )

                ## Attach custom policies to role
                self.lambda_role.role.add_managed_policy(rds_manager_policies)

                NagSuppressions.add_resource_suppressions(
                    rds_manager_policies,
                    [
                        {
                            "id": "AwsSolutions-IAM5",
                            "reason": "Allow lambda to read and interact with DMS instances ",
                        },
                    ],
                    True,
                )

        NagSuppressions.add_resource_suppressions(
            self.lambda_role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Grant Write creates wildcard policy ",
                },
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok"},
            ],
            True,
        )

    #### Functions #####
    def deploy_rds_instance(self, construct_id, environment_config, rds_props):
        """
        Deploy RDS Instance
        """
        if rds_props is not None:
            self.rds_instance = Guest360RDSInstance(self, construct_id, environment_config, rds_props)

    def create_init_rds_lambda(self, construct_id, props, role):
        stack_path = self.node.try_get_context("stack_path")
        env_lambda_init_rds = {
            "ENDPOINT": self.rds_instance.rds_instance.db_instance_endpoint_address,
            "PORT": self.rds_instance.rds_instance.db_instance_endpoint_port,
            "USER": self.rds_instance.rds_instance.secret.secret_value_from_json("username").unsafe_unwrap(),
            "REGION": self.stack.region,
            "DBNAME": props["database_name"],
            "SECRET_NAME": self.rds_instance.rds_instance.secret.secret_name,
        }
        rds_init_lambda_name = f"{construct_id}-rds-init-lambda"

        return Guest360LambdaFunction(
            self,
            f"{construct_id}-init-rds",
            LambdaFunctionProps(
                function_name=rds_init_lambda_name,
                description="RDS init Lambda",
                runtime=Guest360LambdaFunction.get_latest_version("python"),
                code=aws_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/load_testing/init_rds_lambda.zip"),
                handler="main.lambda_handler",
                allow_public_subnet=False,
                environment=env_lambda_init_rds,
                timeout=aws_cdk.Duration.seconds(60),
                vpc=self._vpc,
                vpc_subnets=self._subnet_selection,
                role=role,
            ),
        )

    def networking_config(self, environment_config):
        """networking config"""
        subnets_config = environment_config["networking"][self.stack.region]["subnets"]["non-routable"]
        vpc_config = environment_config["networking"][self.stack.region]["vpc"]["id"]

        subnet_ids = map(lambda subnet: subnet["id"], subnets_config)

        # Grab the VPC from lookup
        self._vpc = aws_ec2.Vpc.from_lookup(self, StackName(self.naming_prefix, "vpc").name(), vpc_id=vpc_config)

        # Grab subnets
        self._subnet_selection = aws_ec2.SubnetSelection(
            subnets=[
                aws_ec2.Subnet.from_subnet_id(scope=self, id=f"{self.prefix}-{subnt_id}", subnet_id=subnt_id)
                for subnt_id in subnet_ids
            ]
        )

    def create_role(self, role_name, assumed_by, description):
        """this function creates a generic role for use by any kind of resource"""
        role_props = {
            "role_name": role_name,
            "assumed_by": aws_iam.CompositePrincipal(aws_iam.ServicePrincipal(assumed_by)),
            "description": description,
        }

        return Guest360IamRole(self, StackName(self.prefix, role_name).name(), role_props)

    def create_rds_manager_lambda(self, construct_id, props, role):
        """Creating a lambda that can start/stop/reboot/modify rds and dms replication instances for DMS pattern chaos testing

        Args:
            construct_id (str): construct id for the stack
            props (dict): RDS config props to pass the dbname to the lambda
            role: lambda role

        Returns:
            GUEST360LambdaFunction: lambda function that can manage rds database and dms replication instances
        """
        stack_path = self.node.try_get_context("stack_path")
        env_lambda_rds_manager = {
            "ENDPOINT": self.rds_instance.rds_instance.db_instance_endpoint_address,
            "PORT": self.rds_instance.rds_instance.db_instance_endpoint_port,
            "USER": self.rds_instance.rds_instance.secret.secret_value_from_json("username").unsafe_unwrap(),
            "REGION": self.stack.region,
            "DBNAME": props["database_name"],
            "SECRET_NAME": self.rds_instance.rds_instance.secret.secret_name,
            "DBInstanceIdentifier": self.rds_instance.rds_instance.instance_identifier,
        }

        rds_manager_lambda_name = f"{construct_id}-rds-manager-lambda"

        return Guest360LambdaFunction(
            self,
            f"{construct_id}-rds-manager",
            LambdaFunctionProps(
                function_name=rds_manager_lambda_name,
                description="RDS manager Lambda",
                runtime=Guest360LambdaFunction.get_latest_version("python"),
                code=aws_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/load_testing/rds_manager_lambda.zip"),
                handler="main.lambda_handler",
                allow_public_subnet=False,
                environment=env_lambda_rds_manager,
                timeout=aws_cdk.Duration.seconds(60),
                vpc=self._vpc,
                vpc_subnets=self._subnet_selection,
                role=role,
            ),
        )
