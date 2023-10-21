"""Class for LoadTesting step function dms rds Constructor"""
import json
import logging
import os
import sys
from pathlib import Path
from typing import List, TypedDict

import aws_cdk
import yaml
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.state_machine import Guest360StateMachine
from app.guest360_constructs.load_testing.static.load_testing_static import LoadTestingStatic
from app.src.reliability.utils import StackName, StateMachine
from aws_cdk import Stack, aws_iam
from cdk_nag import NagSuppressions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Load_testing_dms_rds | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class LoadTestingDmsRdsIngest(Construct360):
    """Class for LoadTesting dms ingest Constructor"""

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        props: dict,
        environment_config,
        load_test_static: LoadTestingStatic,
        dms_stack_extension: list,
        **kwargs,
    ) -> None:
        """Construct to create resources for loadtesting rds dms
        Args:
            scope (Construct360):
            construct_id (str): Construct ID
            props (dict): Configurations for LoadTesting dms rds
            load_test_static (IStack): load test static object to configure permissions and configs to step function
        """

        super().__init__(scope, construct_id, **kwargs)

        self.prefix = self.node.try_get_context("prefix")
        self.naming_prefix = f"{self.prefix}-{construct_id}"
        self.construct_id = construct_id
        self.load_test_static = load_test_static
        # Get current environment
        self.environment = self.node.try_get_context("environment")

        # Get stack
        self.stack = Stack.of(self)

        # pathing
        full_path = os.path.realpath(__file__)
        config_dir = f"{os.path.dirname(full_path)}/../../infrastructure/load_testing/statemachines"

        # Create sfn role
        self.sfn_role = self.create_role(
            f"{self.naming_prefix}-sfn-role", "states.amazonaws.com", "generic role for stepfunction resource"
        )

        self.load_test_static.get_list_app_config_lambda.function.grant_invoke(self.sfn_role.role)
        # Create sfn rds
        sfn_system_test_rds = self.deploy_sfn_system_test_rds(
            props, config_dir, environment_config, construct_id, dms_stack_extension
        )

        # giving permission to events required by sfn role
        self.events_permissions()

        # Nags for sfn
        NagSuppressions.add_resource_suppressions(
            [sfn_system_test_rds.state_machine],
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

    #### Functions #####

    def deploy_sfn_system_test_rds(self, props, config_dir, environment_config, construct_id, dms_stack_extension):
        system_test_rds_definition_file = props["execute_system_test_rds_dms"]["definition_file"]
        system_test_rds_definition = self.load_definition_by_file(config_dir, system_test_rds_definition_file)
        subnets_ids = [
            f"{subnet['id']}"
            for subnet in environment_config["networking"][self.stack.region]["subnets"]["non-routable"]
        ]
        subnets_str = '","'.join(subnets_ids)

        system_test_rds_definition_replaced = json.loads(
            json.dumps(system_test_rds_definition).replace("${subnets_ids}", subnets_str)
        )
        dms_stack_extension_str = '","'.join(dms_stack_extension)
        system_test_rds_definition_replaced = json.loads(
            json.dumps(system_test_rds_definition_replaced).replace("${dms_stack_extension}", dms_stack_extension_str)
        )

        system_test_rds_substitution = {
            "limit_records": "100",
            "fargate_cluster_arn": self.load_test_static.ecs_cluster.cluster.cluster_arn,
            "security_groups_id": self.load_test_static.ecs_cluster.fargate_services[0]
            .connections.security_groups[0]
            .security_group_id,
            "task_definition_arn": self.load_test_static.ecs_cluster.fargate_services[
                0
            ].task_definition.task_definition_arn,
            "container_name": self.load_test_static.ecs_cluster.fargate_services[
                0
            ].task_definition.default_container.container_name,
            "prefix": self.prefix,
            "role_arn": self.sfn_role.role.role_arn,
            "lambda_list_app_config": self.load_test_static.get_list_app_config_lambda.function_name,
        }
        props["execute_system_test_rds_dms"]["name"] = f"{props['execute_system_test_rds_dms']['name']}"

        return Guest360StateMachine(
            self,
            StateMachine(self.naming_prefix, "system_test_rds_statemachine").name(),
            system_test_rds_definition_replaced,
            props["execute_system_test_rds_dms"],
            **system_test_rds_substitution,
        )

    def load_definition_by_file(self, config_dir, file_name):
        with open(f"{config_dir}/{file_name}", mode="r", encoding="utf-8") as state_file:
            state_machine_definition = yaml.safe_load(state_file)
        return state_machine_definition

    def get_wildcard_arn_statement_policy(self, region, account_id, cluster_name, type_service):
        return f"arn:aws:ecs:{region}:{account_id}:{type_service}/{cluster_name}/*"

    def events_permissions(self):
        # Add policy for access states and events to sfn role
        # Adding in this way because the states and events doesn't have the grant method
        # required by statemachine
        statemachine_policy_statement_events = aws_cdk.aws_iam.PolicyStatement(
            actions=["events:PutTargets", "events:PutRule", "events:DescribeRule"],
            resources=[f"arn:aws:events:{self.stack.region}:{self.stack.account}:*"],
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
        statemachine_policy_statement_ecs = aws_cdk.aws_iam.PolicyStatement(
            actions=["ecs:RunTask", "ecs:StopTask", "ecs:DescribeTasks", "ecs:ListTagsForResource"],
            resources=[
                self.load_test_static.ecs_cluster.fargate_services[0].task_definition.task_definition_arn,
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
        statemachine_policy_states_events = aws_cdk.aws_iam.Policy(
            self,
            f"{self.prefix}-states-event-policy",
            statements=[
                statemachine_policy_statement_events,
                statemachine_policy_statement_ecs,
                statemachine_policy_pass_role_ecs,
            ],
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
