"""Class for LoadTesting kinesis ingest Constructor"""
import json
import logging
import os
import sys
from pathlib import Path
from typing import List, TypedDict

import aws_cdk
import yaml
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.glue import Guest360Glue
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.guest360_constructs.state_machine import Guest360StateMachine
from app.guest360_constructs.load_testing.static.load_testing_static import LoadTestingStatic
from app.src.reliability.utils import LambdaFunctionName, LogGroup, StackName, StateMachine
from aws_cdk import Stack, Token, aws_dynamodb, aws_ec2, aws_iam, aws_kms, aws_s3, aws_ssm, aws_lambda
from cdk_nag import NagSuppressions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Load_testing_kinesis_ingest | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

KMS_DECRYPT_ACTION = "kms:Decrypt"


class LoadTestingProps(TypedDict):
    region: str  # Region name in AWS
    guest360_execute_all_system_test: dict  # main orchestrator statemachine
    guest360_system_test_kinesis: dict  # system test executor statemachine


class LoadTestingKinesisIngest(Construct360):
    """Class for LoadTesting kinesis ingest Constructor"""

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        props: dict,
        environment_config,
        load_test_static: LoadTestingStatic,
        **kwargs,
    ) -> None:
        """Construct to create resources for loadtesting kinesis ingest
        Args:
            scope (Construct360):
            construct_id (str): Construct ID
            props (dict): Configurations for LoadTesting kinesis ingest - see LoadTestingProps TypedDict
            load_test_static (IStack): load test static object to configure permissions and configs to step functions
        """

        super().__init__(scope, construct_id, **kwargs)

        self.prefix = self.node.try_get_context("prefix")
        self.naming_prefix = f"{self.prefix}-{construct_id}"
        self.construct_id = construct_id
        self.load_test_static = load_test_static
        # Get current environment
        self.environment = self.node.try_get_context("environment")

        # envs
        self.state_action = "states:DescribeExecution"

        # Get stack
        self.stack = Stack.of(self)

        # pathing
        full_path = os.path.realpath(__file__)
        config_dir = f"{os.path.dirname(full_path)}/../../../infrastructure/load_testing/statemachines"

        self.sfn_role = self.create_role(
            f"{construct_id}-sfn-role", "states.amazonaws.com", "generic role for stepfunctions resources"
        )
        # giving permission to events required by sfn role
        self.events_permissions()

        # create step function system test kinesis ingest
        self.deploy_sfn_system_test_kinesis_ingest(props, config_dir, environment_config)

        # create step function execute all system test
        self.deploy_sfn_execute_all_system_test(props, config_dir)
        # Add permission to table to guest360_execute_all_load_test_scenarios role
        self.load_test_static.dynamo_db["guest360-load-testing-static-sfn-exec-state"].table.grant_read_write_data(
            self.sfn_role.role
        )
        self.load_test_static.get_app_config_lambda.function.grant_invoke(self.sfn_role.role)
        self.load_test_static.get_list_app_config_lambda.function.grant_invoke(self.sfn_role.role)

        # add nag supresions
        self.add_nag_suppresions()

    #### Functions #####

    def load_definition_by_file(self, config_dir, file_name):
        with open(f"{config_dir}/{file_name}", mode="r", encoding="utf-8") as state_file:
            state_machine_definition = yaml.safe_load(state_file)
        return state_machine_definition

    def deploy_sfn_execute_all_system_test(self, props, config_dir):
        all_load_test_scenarios_definition_file = props["guest360_execute_all_system_test"]["definition_file"]
        all_load_test_scenarios_state_machine_definition = self.load_definition_by_file(
            config_dir, all_load_test_scenarios_definition_file
        )
        # Creation of StateMachines with substitutions
        all_load_test_scenario_substitution = {
            "execution_status_table": self.load_test_static.dynamo_db[
                "guest360-load-testing-static-sfn-exec-state"
            ].table.table_name,  # Validate the object of dynamo
            "guest360_execute_load_test_scenario_arn": self.guest360_system_test_kinesis_ingest.state_machine.attr_arn,
            "bucket_scenarios_path": self.environment,
            "role_arn": self.sfn_role.role.role_arn,
            "lambda_get_list_app_config_arn": self.load_test_static.get_list_app_config_lambda.function_name,
            "lambda_get_app_config_arn": self.load_test_static.get_app_config_lambda.function_name,
        }
        props["guest360_execute_all_system_test"][
            "name"
        ] = f"{self.construct_id}-{props['guest360_execute_all_system_test']['name']}"

        self.guest360_execute_all_load_test = Guest360StateMachine(
            self,
            StateMachine(self.naming_prefix, "execute_all_test_statemachine").name(),
            all_load_test_scenarios_state_machine_definition,
            props["guest360_execute_all_system_test"],
            **all_load_test_scenario_substitution,
        )

    def deploy_sfn_system_test_kinesis_ingest(self, props, config_dir, environment_config):
        system_test_scenarios_definition_file = props["guest360_system_test_kinesis_ingest"]["definition_file"]
        system_test_scenarios_state_machine_definition = self.load_definition_by_file(
            config_dir, system_test_scenarios_definition_file
        )

        subnets_ids = [
            f"{subnet['id']}"
            for subnet in environment_config["networking"][self.stack.region]["subnets"]["non-routable"]
        ]
        subnets_str = '","'.join(subnets_ids)

        system_test_scenario_state_machine_definition_replaced = json.loads(
            json.dumps(system_test_scenarios_state_machine_definition).replace("${subnets_ids}", subnets_str)
        )
        task_definition_arn = self.load_test_static.ecs_cluster.fargate_services[0].task_definition.task_definition_arn
        # Creation of StateMachines with substitutions
        system_test_scenario_substitution = {
            "fargate_cluster_arn": self.load_test_static.ecs_cluster.cluster.cluster_arn,
            "security_groups_id": self.load_test_static.ecs_cluster.fargate_services[0]
            .connections.security_groups[0]
            .security_group_id,
            "task_definition_arn": task_definition_arn,
            "container_name": self.load_test_static.ecs_cluster.fargate_services[
                0
            ].task_definition.default_container.container_name,
            "prefix": self.prefix,
            "environment": self.environment,
            "limit_records": props["guest360_system_test_kinesis_ingest"]["step_function_parameters"]["limit_records"],
            "role_arn": self.sfn_role.role.role_arn,
        }
        props["guest360_system_test_kinesis_ingest"][
            "name"
        ] = f"{self.construct_id}-{props['guest360_system_test_kinesis_ingest']['name']}"

        self.guest360_system_test_kinesis_ingest = Guest360StateMachine(
            self,
            StateMachine(self.naming_prefix, "system_test_scenarios_statemachine").name(),
            system_test_scenario_state_machine_definition_replaced,
            props["guest360_system_test_kinesis_ingest"],
            **system_test_scenario_substitution,
        )

        statemachine_policy_statement_ecs = aws_cdk.aws_iam.PolicyStatement(
            actions=["ecs:RunTask", "ecs:StopTask", "ecs:DescribeTasks", "ecs:ListTagsForResource"],
            resources=[
                task_definition_arn,
                self.load_test_static.ecs_cluster.cluster.cluster_arn,
                self.get_wildcard_arn_statement_policy(
                    self.stack.region,
                    self.stack.account,
                    self.load_test_static.ecs_cluster.cluster.cluster_name,
                    "task",
                ),
            ],
            effect=aws_cdk.aws_iam.Effect.ALLOW,
        )

        statemachine_policy_pass_role_ecs = aws_cdk.aws_iam.PolicyStatement(
            actions=["iam:PassRole"],
            resources=[
                f"{self.load_test_static.ecs_cluster.ecs_execution_role.role.role_arn}",
                f"{self.load_test_static.ecs_task_role.role.role_arn}",
            ],
            effect=aws_cdk.aws_iam.Effect.ALLOW,
        )
        statemachine_policy_statement_states = aws_cdk.aws_iam.PolicyStatement(
            actions=["states:StartExecution", self.state_action, "states:StopExecution"],
            resources=[f"{self.guest360_system_test_kinesis_ingest.state_machine.attr_arn}"],
            effect=aws_cdk.aws_iam.Effect.ALLOW,
        )
        statemachine_policy_ecs = aws_cdk.aws_iam.Policy(
            self,
            f"{self.prefix}-ecs-role-policy",
            statements=[
                statemachine_policy_statement_ecs,
                statemachine_policy_pass_role_ecs,
                statemachine_policy_statement_states,
            ],
        )
        self.sfn_role.role.attach_inline_policy(statemachine_policy_ecs)

    def get_wildcard_arn_statement_policy(self, region, account_id, cluster_name, type_service):
        return f"arn:aws:ecs:{region}:{account_id}:{type_service}/{cluster_name}/*"

    def events_permissions(self):
        # Add policy for access states and events to guest360_execute_all_load_test role
        # Adding in this way because the states and events doesn't have the grant method

        # required by statemachine
        statemachine_policy_statement_events = aws_cdk.aws_iam.PolicyStatement(
            actions=["events:PutTargets", "events:PutRule", "events:DescribeRule"],
            resources=[f"arn:aws:events:{self.stack.region}:{self.stack.account}:*"],
            effect=aws_cdk.aws_iam.Effect.ALLOW,
        )
        statemachine_policy_states_events = aws_cdk.aws_iam.Policy(
            self,
            f"{self.prefix}-states-event-policy",
            statements=[statemachine_policy_statement_events],
        )
        self.sfn_role.role.attach_inline_policy(statemachine_policy_states_events)

    def create_role(self, role_name, assumed_by, description):
        """this function creates a generic role for use by any kind of resource"""
        role_props = {
            "role_name": role_name,
            "assumed_by": aws_iam.CompositePrincipal(aws_iam.ServicePrincipal(f"{assumed_by}")),
            "description": description,
        }

        return Guest360IamRole(self, StackName(self.prefix, role_name).name(), role_props)

    def add_nag_suppresions(self):
        # Nags
        NagSuppressions.add_resource_suppressions(
            self.sfn_role.role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "we need to add * on resources for events",
                }
            ],
            True,
        )

        NagSuppressions.add_resource_suppressions(
            [
                self.guest360_execute_all_load_test.state_machine,
                self.guest360_system_test_kinesis_ingest.state_machine,
            ],
            [
                {
                    "id": "AwsSolutions-SF2",
                    "reason": "XRay enabled are not required",
                },
                {
                    "id": "AwsSolutions-SF1",
                    "reason": "Not logging all events",
                },
            ],
            True,
        )
