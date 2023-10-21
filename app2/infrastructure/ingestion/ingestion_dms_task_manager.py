""" DMS Ingestion Task Manager Stack for DMS Ingest infrastructure.
    Lambda task manager will Start/Restart/Resume/stop(manual) and Track(event bridge events) DMS rep Tasks
    Also lambda will publish CW custom metrics that in case of exceeding the allowed failures will
    notify to slack channel and create service now ticket (alarm configured in dms task constructor)
"""
import logging
import sys
from aws_cdk import (
    Stack,
    Duration,
    aws_iam,
    aws_dynamodb,
    aws_events,
    aws_events_targets,
    aws_lambda,
    aws_logs,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as sfn_tasks,
)
from cdk_nag import NagSuppressions
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable
from app.infrastructure.workstream_stack import WorkstreamStack
from app.src.utils.feature_flag.feature_flag import FeatureFlag
from app.src.reliability.Guest360ConfigInfra.assist import static_config_from_path

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - DMS Ingestion | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class DMSTaskManager(WorkstreamStack):
    """
    Stack definition for the dms task manager, which ensures DMS tasks can be stopped/started/restarted both automatically upon an identified alert or manually
    """

    def __init__(self, scope: Stack, construct_id: str, config: dict, **kwargs) -> None:  # pylint: disable=W0613
        """Initialization method for ingestion class
        Args:
            scope (Construct360): scope for stack
            construct_id (str): ID of construct for naming purposes
            config (dict): environment configuration details
        """
        super().__init__(scope, construct_id, **kwargs)

        prefix = self.node.try_get_context("prefix")
        account_id = Stack.of(self).account
        region = Stack.of(self).region.lower()
        environment = self.node.try_get_context("environment").lower()
        project_path = self.project_dir

        # Read parameters from config files per environment
        config_dir = f"{project_path}/app/infrastructure/ingestion/config/dms_task_manager"

        task_manager_config_path = f"{config_dir}/{environment}-task-manager-config.yaml"
        task_manager_configs = static_config_from_path(task_manager_config_path)[0]

        logger.debug("task_manager_configs:%s", task_manager_configs)
        #############################################################
        # DYNAMODB TABLE SECTION: Stores the number of failures  per dms task
        #############################################################
        table_name = task_manager_configs["table_name"]
        task_manager_table = Guest360DynamodbGlobaltable(
            self,
            construct_id=table_name,
            table_name=table_name,
            partition_key=aws_dynamodb.Attribute(name="dms_task_arn", type=aws_dynamodb.AttributeType.STRING),
        ).table

        ###################################################################
        ##### POLICIES FOR LAMBDAS FUNCTION SECTION
        ###################################################################

        # Define Custom policies to be used per lambda task manager and lambda task event bridge events
        describe_rep_task_policy = aws_iam.PolicyStatement(
            actions=["dms:DescribeReplicationTasks"],
            resources=["*"],
            effect=aws_iam.Effect.ALLOW,
        )
        start_stop_rep_task_policy = aws_iam.PolicyStatement(
            actions=["dms:StartReplicationTask", "dms:StopReplicationTask"],
            resources=[f"arn:aws:dms:{region}:{account_id}:task:*"],
            effect=aws_iam.Effect.ALLOW,
        )
        cw_put_metricdata_policy = aws_iam.PolicyStatement(
            actions=["cloudwatch:PutMetricData"],
            resources=["*"],
            effect=aws_iam.Effect.ALLOW,
        )

        ###################################################################
        ##### LAMBDAS FUNCTION SECTION
        ###################################################################
        lambda_event_bridge_env_vars = task_manager_configs["lambda_event_bridge"]["env_variables"]
        lambda_event_bridge_env_vars["TABLE_NAME"] = task_manager_table.table_name

        self.dms_task_event_bridge_events_lambda = Guest360LambdaFunction(
            self,
            f"{prefix}-dms-event-bridge-events",
            LambdaFunctionProps(
                function_name="dms-event-bridge-events",
                description=task_manager_configs["lambda_event_bridge"]["description"],
                code=aws_lambda.Code.from_asset(
                    f"{project_path}/bazel-bin/app/src/ingestion/dms/dms_task_manager_archive.zip"
                ),
                handler="lambda_task_event_bridge_events.lambda_handler",
                environment=lambda_event_bridge_env_vars,
                enable_otel_tracing=False,
                timeout=Duration.seconds(task_manager_configs["lambda_event_bridge"]["timeout_seconds"]),
            ),
        ).function

        self.dms_manual_task_lambda = Guest360LambdaFunction(
            self,
            f"{prefix}-dms-manual-task",
            LambdaFunctionProps(
                function_name="dms-manual-task",
                description=task_manager_configs["lambda_manual_task"]["description"],
                code=aws_lambda.Code.from_asset(
                    f"{project_path}/bazel-bin/app/src/ingestion/dms/dms_task_manager_archive.zip"
                ),
                handler="lambda_dms_manual_task.lambda_handler",
                enable_otel_tracing=False,
                timeout=Duration.seconds(task_manager_configs["lambda_manual_task"]["timeout_seconds"]),
            ),
        ).function

        ## Attach custom policies to role
        self.dms_manual_task_lambda.role.add_to_policy(describe_rep_task_policy)
        self.dms_manual_task_lambda.role.add_to_policy(start_stop_rep_task_policy)

        self.dms_task_event_bridge_events_lambda.role.add_to_policy(describe_rep_task_policy)
        self.dms_task_event_bridge_events_lambda.role.add_to_policy(cw_put_metricdata_policy)

        # Allow lambda event bridge events read dynamo key and write in dynamo table
        task_manager_table.grant_read_write_data(self.dms_task_event_bridge_events_lambda)

        ###################################################################
        ##### STEP FUNCTION SECTION
        ###################################################################
        sfn_task_manager_configs = task_manager_configs["task_manager_state_machine"]
        # Create a log group for step function
        sfn_log_group_name = f"{prefix}-task-manager-sfn-logGroup"
        sfn_log_group = aws_logs.LogGroup(
            self,
            sfn_log_group_name,
            log_group_name=f"/aws/vendedlogs/states/{sfn_log_group_name}",
            retention=aws_logs.RetentionDays.THREE_MONTHS,
        )

        task_manual_events_lambda_invoke = sfn_tasks.LambdaInvoke(  # Run lambda task manager for manual events
            self,
            "RunLambdaManualTasks",
            lambda_function=self.dms_manual_task_lambda,
            output_path="$.Payload",
            retry_on_service_exceptions=False,  # avoid default 6 retries
        )

        task_event_bridge_events_lambda_invoke = sfn_tasks.LambdaInvoke(
            self,
            "RunLambdaEventBridgeEvents",
            lambda_function=self.dms_task_event_bridge_events_lambda,
            output_path="$.Payload",
            retry_on_service_exceptions=False,  # avoid default 6 retries
        )

        go_to_end = sfn.Succeed(
            self,
            "Finish Execution",
            comment="Finish Flow if HANDLE_CREATED_EVENTS is disabled or non desired event Bridge events received",
        )

        wait_finish_dms_task_creation = sfn.Wait(
            self,
            "Wait finish DMS task creation",
            time=sfn.WaitTime.duration(
                Duration.seconds(sfn_task_manager_configs["wait_finish_dms_task_creation_seconds"])
            ),
        )
        # Service name relation: https://docs.aws.amazon.com/step-functions/latest/dg/supported-services-awssdk.html
        # Start Replication Task when the flag autostart_created_dms_tasks is enabled, retry 2 times in case of failure after 30 seconds
        start_dms_task_retry_params = sfn_task_manager_configs["start_dms_task_api_call"]["retry_params"]
        start_dms_task = sfn_tasks.CallAwsService(
            self,
            "StartReplicationTask",
            service="databasemigration",
            action="startReplicationTask",
            parameters={
                "ReplicationTaskArn": sfn.JsonPath.string_at("$.resource"),
                "StartReplicationTaskType": "start-replication",
            },
            iam_resources=[f"arn:aws:dms:{region}:{account_id}:task:*"],
            iam_action="dms:StartReplicationTask",
        )
        start_dms_task.add_retry(
            max_attempts=start_dms_task_retry_params["max_attempts"],
            backoff_rate=start_dms_task_retry_params["backoff_rate"],
            interval=Duration.seconds(start_dms_task_retry_params["interval_seconds"]),
        )

        next_start_task_created = wait_finish_dms_task_creation.next(start_dms_task).next(go_to_end)

        event_type_var = "$.eventType"
        ## Temporal
        chain = (
            sfn.Choice(self, "Desired Event Bridge or manual task?")
            .when(sfn.Condition.is_present("$.task"), next=task_manual_events_lambda_invoke)
            .when(
                sfn.Condition.string_equals(event_type_var, "REPLICATION_TASK_CREATED"),
                sfn.Choice(self, "created event,is the autostart_created_dms_tasks' flag enabled?")
                .when(
                    sfn.Condition.boolean_equals("$.autoStartCreatedDmsTasks", True),
                    next=next_start_task_created,
                )
                .otherwise(go_to_end),
            )
            .when(
                sfn.Condition.string_equals(event_type_var, "REPLICATION_TASK_FAILED"),
                task_event_bridge_events_lambda_invoke,
            )
            .when(
                sfn.Condition.string_equals(event_type_var, "REPLICATION_TASK_STARTED"),
                task_event_bridge_events_lambda_invoke,
            )
            .otherwise(go_to_end)
        )

        task_manager_sfn_name = f"{prefix}-task-manager-sfn"
        task_manager_state_machine = sfn.StateMachine(
            self,
            task_manager_sfn_name,
            state_machine_name=task_manager_sfn_name,
            comment=sfn_task_manager_configs["comment"],
            definition_body=sfn.DefinitionBody.from_chainable(chain),
            logs=sfn.LogOptions(destination=sfn_log_group, level=sfn.LogLevel.ALL),
            timeout=Duration.seconds(sfn_task_manager_configs["timeout_seconds"]),
            tracing_enabled=sfn_task_manager_configs["tracing_enabled"],
        )

        ###################################################################
        ##### EVENT BRIDGE SECTION
        #### Just handling events: "REPLICATION_TASK_CREATED", "REPLICATION_TASK_STARTED","REPLICATION_TASK_FAILED"
        ### Not handling other like: "REPLICATION_TASK_STOPPED", "REPLICATION_TASK_DELETED","READING_PAUSED_SWAP_FILES_LIMIT_REACHED"
        ###################################################################

        # Event Bridge role
        event_bridge_role = aws_iam.Role(
            self, "event-bridge-role", assumed_by=aws_iam.ServicePrincipal("events.amazonaws.com")
        )

        dms_sfn_event_rule = aws_events.Rule(
            self,
            "DMStoStepFunctionEventRule",
            description="Task Manager -Send DMS events to StepFunction",
            event_pattern=aws_events.EventPattern(
                source=["aws.dms"],
                detail={
                    "type": ["REPLICATION_TASK"],
                    "eventType": [
                        "REPLICATION_TASK_CREATED",
                        "REPLICATION_TASK_STARTED",
                        "REPLICATION_TASK_FAILED",
                    ],
                },
            ),
        )

        # Add the state machine as event rule target , a default policy with states:StartExecution permission is created and
        # Inject autostart_created_dms_tasks flag in the event bridge rule's payload for step function and
        config_path = f"{project_path}/app/configs/{environment}-infra-feature-flags.yaml"
        with FeatureFlag(
            environment, "dms_stacks.autostart_created_dms_tasks", config_path
        ) as autostart_created_dms_tasks_flag:
            dms_sfn_event_rule.add_target(
                aws_events_targets.SfnStateMachine(
                    machine=task_manager_state_machine,
                    role=event_bridge_role,
                    input=aws_events.RuleTargetInput.from_object(
                        {
                            "resource": aws_events.EventField.from_path("$.resources[0]"),
                            "eventType": aws_events.EventField.from_path("$.detail.eventType"),
                            "autoStartCreatedDmsTasks": autostart_created_dms_tasks_flag,
                            "originalEvent": aws_events.EventField.from_path("$"),
                        }
                    ),
                )
            )

        ###################################################################
        ##### Nag Suppressions Section
        ###################################################################
        NagSuppressions.add_resource_suppressions(
            self.dms_task_event_bridge_events_lambda.role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Allow lambda to read and interact with DMS tasks, and publish cloudwatch metrics",
                }
            ],
            apply_to_children=True,
        )

        NagSuppressions.add_resource_suppressions(
            self.dms_manual_task_lambda.role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Allow lambda task manager encrypt/decrypt dynamo table key",
                }
            ],
            apply_to_children=True,  # Applied to the lambda role's default policy
        )

        NagSuppressions.add_resource_suppressions(
            task_manager_state_machine,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Allow state machine to work with logs, xray and invoke dms task manager lambda",
                }
            ],
            apply_to_children=True,  # Applied to the state machine role's default policy
        )
