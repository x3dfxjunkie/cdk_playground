"""LoadTesting Framework Construct for guest360"""
import logging
import os
import sys
from pathlib import Path
from typing import List

import aws_cdk
import yaml


from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable

from app.guest360_constructs.ecs_consumer import Guest360ECS
from app.guest360_constructs.iam_role import Guest360IamRole

from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps

from app.src.reliability.utils import StackName
from aws_cdk import (
    Stack,
    aws_ec2,
    aws_iam,
    aws_lambda,
)

from cdk_nag import NagSuppressions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Load_testing_static | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

KMS_DECRYPT_ACTION = "kms:Decrypt"
TABLE_NAME_EXEC_EVAL = "guest360-load-testing-static-sfn-exec-eval"


class LoadTestingStatic(Construct360):
    """Class for LoadTestingStactis Constructor
    Creates Lambdas EvalSystem and EvalCondition"""

    def __init__(self, scope: Construct360, construct_id: str, props: dict, environment_config, **kwargs) -> None:
        """Construct to create resources for loadtesting App
        Args:
            scope (Construct360):
            construct_id (str): Construct ID
            props (dict): Configurations for LoadTesting ECS Cluster - see LoadTestingProps TypedDict
        """

        super().__init__(scope, construct_id, **kwargs)

        self.prefix = self.node.try_get_context("prefix")
        self.naming_prefix = f"{self.prefix}-{construct_id}"

        # Get current environment
        self.environment = self.node.try_get_context("environment")

        # envs
        self.lambda_handler = "lambda_function.lambda_handler"
        # Get stack
        self.stack = Stack.of(self)
        # load networking config
        self.networking_config(environment_config)
        # Create ecs cluster
        self.ecs_cluster = Guest360ECS(self, props["cluster_name"], props["ecs"])

        # Creation of dynamoDBs
        self.dynamo_db = {}
        for index, dynamo_props in enumerate(props["dynamo_db"]):
            temp_construct_id = construct_id
            if index >= 1:
                temp_construct_id = f"{construct_id}-{dynamo_props['table_name']}"

            ddb = Guest360DynamodbGlobaltable(
                self,
                temp_construct_id,
                table_name=dynamo_props["table_name"],
                partition_key=aws_cdk.aws_dynamodb.Attribute(
                    name=dynamo_props["partition_key"], type=aws_cdk.aws_dynamodb.AttributeType.STRING
                ),
                sort_key=aws_cdk.aws_dynamodb.Attribute(
                    name=dynamo_props["sort_key"], type=aws_cdk.aws_dynamodb.AttributeType.STRING
                )
                if "sort_key" in dynamo_props
                else None,
            )
            self.dynamo_db[dynamo_props["table_name"]] = ddb

        # Create lambda role
        self.lambda_role = self.create_lambda_role()

        self.lambda_role.role.add_managed_policy(
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        )
        self.lambda_role.role.add_managed_policy(
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaVPCAccessExecutionRole")
        )

        # Deploy evaluator lambda
        self.evaluator_lambda = self.create_evaluator_loadtest_lambda(self.prefix, self.lambda_role.role)
        self.evaluator_lambda_system_test = self.create_evaluator_system_test_lambda(
            construct_id, self.lambda_role.role
        )
        self.eval_conditions_lambda_system_test = self.create_eval_condition_system_test_lambda(
            construct_id, self.lambda_role.role
        )
        self.consolidate_results_lambda = self.consolidate_test_results(construct_id, self.lambda_role.role)
        self.create_metrics_lambda_evaluator_policy()
        self.lambda_role.role.attach_inline_policy(self.metrics_policy)
        # Deploy get app config to retrieve data contracts
        self.get_app_config_lambda = self.get_app_config(construct_id, self.lambda_role.role)
        self.get_list_app_config_lambda = self.get_lambda_list_app_config(construct_id, self.lambda_role.role)
        # Add permission to table to results
        self.dynamo_db[TABLE_NAME_EXEC_EVAL].table.grant_read_write_data(self.lambda_role.role)

        # Adding permissions to lambda generic role
        self.ecs_task_role = list(self.ecs_cluster.task_roles.values())[0]
        self.adding_permissions_resources(self.ecs_task_role.role, "ecs")
        # Adding permissions to ecs generic role
        self.adding_permissions_resources(self.lambda_role.role, "lambda")

        if "rabbitmq" in self.ecs_cluster.cloudmap:
            self.rabbitmq_test_lambda(
                self.prefix, self.ecs_cluster.cloudmap["rabbitmq"].namespace_name, self.lambda_role.role
            )

    #### Functions #####
    def create_evaluator_loadtest_lambda(self, construct_id, role):
        stack_path = self.node.try_get_context("stack_path")
        table_name = TABLE_NAME_EXEC_EVAL
        env_lambda_evaluator = {
            "DDB_TABLE_RESULT": self.dynamo_db[table_name].table.table_name,
        }

        return Guest360LambdaFunction(
            self,
            f"{construct_id}-evaluator-lambda",
            LambdaFunctionProps(
                function_name="evaluator-loadtest-lambda",
                description="evaluator of load and e2e Lambda for loadtest",
                code=aws_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/load_testing/evaluator.zip"),
                handler=self.lambda_handler,
                allow_public_subnet=False,
                environment=env_lambda_evaluator,
                timeout=aws_cdk.Duration.seconds(20),
                role=role,
            ),
        )

    def create_evaluator_system_test_lambda(self, construct_id, role):
        stack_path = self.node.try_get_context("stack_path")
        table_name = TABLE_NAME_EXEC_EVAL
        env_lambda_evaluator = {
            "DDB_TABLE_RESULT": self.dynamo_db[table_name].table.table_name,
        }

        return Guest360LambdaFunction(
            self,
            f"{construct_id}-evaluator-system-test-lambda",
            LambdaFunctionProps(
                function_name="evaluator-system-test-lambda",
                description="evaluator of e2e Lambda for systemtest",
                code=aws_lambda.Code.from_asset(
                    f"{stack_path}/bazel-bin/app/src/load_testing/evaluator_system_test.zip"
                ),
                handler=self.lambda_handler,
                allow_public_subnet=False,
                environment=env_lambda_evaluator,
                timeout=aws_cdk.Duration.minutes(10),
                role=role,
            ),
        )

    def create_eval_condition_system_test_lambda(self, construct_id, role):
        stack_path = self.node.try_get_context("stack_path")
        table_name = TABLE_NAME_EXEC_EVAL
        env_lambda_evaluator = {
            "DDB_TABLE_RESULT": self.dynamo_db[table_name].table.table_name,
        }

        return Guest360LambdaFunction(
            self,
            f"{construct_id}-eval-condition-system-test-lambda",
            LambdaFunctionProps(
                function_name="eval-condition-system-test-lambda",
                description="evaluator of e2e Lambda for systemtest",
                code=aws_lambda.Code.from_asset(
                    f"{stack_path}/bazel-bin/app/src/load_testing/eval_conditions_system_test.zip"
                ),
                handler="lambda_function.lambda_handler",
                allow_public_subnet=False,
                environment=env_lambda_evaluator,
                timeout=aws_cdk.Duration.minutes(10),
                role=role,
            ),
        )

    def create_metrics_lambda_evaluator_policy(self):
        metric_permissions_statement = aws_cdk.aws_iam.PolicyStatement(
            actions=["cloudwatch:GetMetricStatistics", "cloudwatch:GetMetricData"],
            resources=["*"],
            effect=aws_cdk.aws_iam.Effect.ALLOW,
        )
        self.metrics_policy = aws_cdk.aws_iam.Policy(
            self,
            f"{self.prefix}-MetricsPermissions-policy",
            statements=[metric_permissions_statement],
        )

    def consolidate_test_results(self, construct_id, role):
        stack_path = self.node.try_get_context("stack_path")
        table_name = TABLE_NAME_EXEC_EVAL
        env_lambda_consolidate = {
            "DDB_TABLE_RESULT": self.dynamo_db[table_name].table.table_name,
        }

        return Guest360LambdaFunction(
            self,
            f"{construct_id}-consolidate-test-results",
            LambdaFunctionProps(
                function_name="consolidate-tests-results",
                description="consolidate results and prep lambda for loadtest",
                code=aws_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/load_testing/consolidate_results.zip"),
                handler=self.lambda_handler,
                allow_public_subnet=False,
                environment=env_lambda_consolidate,
                timeout=aws_cdk.Duration.seconds(10),
                role=role,
            ),
        )

    def rabbitmq_test_lambda(self, construct_id, namespace_name, role):
        stack_path = self.node.try_get_context("stack_path")
        env_lambda = {
            "RABBITMQ_VHOST": "my_vhost",
            "RABBITMQ_SERVER": f"rabbitmq.{namespace_name}",
        }

        return Guest360LambdaFunction(
            self,
            f"{construct_id}-test-rabbitmq",
            LambdaFunctionProps(
                function_name="test-rabbitmq",
                description="For testing rabbitmq ECS container",
                code=aws_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/load_testing/rabbitmq_test.zip"),
                handler=self.lambda_handler,
                allow_public_subnet=False,
                environment=env_lambda,
                timeout=aws_cdk.Duration.seconds(10),
                role=role,
                vpc=self._vpc,
                vpc_subnets=self._subnet_selection,
            ),
        )

    def get_app_config(self, construct_id, role):
        """Function to build the get app config lambda,
        this lambda will be used by the step function to retrieve all
        the data contracts with the stack extension name"""
        stack_path = self.node.try_get_context("stack_path")
        env_lambda_app_config = {"prefix": self.prefix}

        return Guest360LambdaFunction(
            self,
            f"{construct_id}-get-app-config",
            LambdaFunctionProps(
                function_name="get-app-config",
                description="get app config profile to retrieve Data contracts",
                code=aws_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/load_testing/get_app_config.zip"),
                handler=self.lambda_handler,
                allow_public_subnet=False,
                environment=env_lambda_app_config,
                timeout=aws_cdk.Duration.seconds(20),
                role=role,
            ),
        )

    def get_lambda_list_app_config(self, construct_id, role):
        """Function to build the get list app config lambda,
        this lambda will be used by the step function to retrieve all
        the application ids with the stack extension name"""
        stack_path = self.node.try_get_context("stack_path")
        env_lambda_app_config = {"prefix": self.prefix}

        return Guest360LambdaFunction(
            self,
            f"{construct_id}-get-list-app-config",
            LambdaFunctionProps(
                function_name="get-list-app-config",
                description="get list app config profile to retrieve Data contracts",
                code=aws_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/load_testing/get_list_app_config.zip"),
                handler=self.lambda_handler,
                allow_public_subnet=False,
                environment=env_lambda_app_config,
                timeout=aws_cdk.Duration.seconds(30),
                role=role,
            ),
        )

    def networking_config(self, environment_config):
        """networking config"""
        subnets_config = environment_config["networking"][self.stack.region]["subnets"]["non-routable"]
        vpc_config = environment_config["networking"][self.stack.region]["vpc"]["id"]

        subnet_id_list: List[str] = []

        for subnet in subnets_config:
            subnet_id_list.append(subnet["id"])

        # Grab the VPC from lookup
        self._vpc = aws_ec2.Vpc.from_lookup(self, StackName(self.naming_prefix, "vpc").name(), vpc_id=vpc_config)

        # Grab subnets
        self._subnet_selection = aws_ec2.SubnetSelection(
            subnets=[
                aws_ec2.Subnet.from_subnet_id(scope=self, id=f"{self.prefix}-{subnt_id}", subnet_id=subnt_id)
                for subnt_id in subnet_id_list
            ]
        )

    def create_lambda_role(self):
        """this function creates a generic role for use by any kind of resource"""
        role_props = {
            "role_name": "loadtest-static-lambda-role",
            "assumed_by": aws_iam.CompositePrincipal(aws_iam.ServicePrincipal("lambda.amazonaws.com")),
            "description": "generic role for lambda resources",
        }

        return Guest360IamRole(self, StackName(self.prefix, "loadtest-static-lambda-role").name(), role_props)

    def adding_permissions_resources(self, role, resource):
        is_local_test = self.node.try_get_context("is_local_test")
        if is_local_test:
            path = self.node.try_get_context("stack_path")
        else:
            path = os.path.dirname(__file__)
        path = path.replace("static", "")
        with open(f"{path}/permissions/{self.environment}_{resource}_role.yaml", "r", encoding="UTF-8") as file:
            permission_config = yaml.unsafe_load(file)
            sid = 0
            statements = []
            for policy in permission_config["policies"]:
                aws_iam_policy_statement = aws_iam.PolicyStatement(
                    actions=policy["actions"],
                    sid=str(sid),
                    resources=[resource.replace("${prefix}", self.prefix) for resource in policy["resources"]],
                )
                statements.append(aws_iam_policy_statement)
                sid += 1
            iam_policy = aws_iam.Policy(self, f"{resource}-policy-{sid}", statements=statements)
            role.attach_inline_policy(iam_policy)
            NagSuppressions().add_resource_suppressions(
                iam_policy, [{"id": "AwsSolutions-IAM5", "reason": "Required for Loadtest/e2e role"}]
            )
