"""Guest360DMSReplicationTasks Construct
"""
from typing import TypedDict  # , Union

from aws_cdk import aws_dms, aws_cloudwatch, Duration
from strongtyping.strong_typing import match_class_typing

import json
from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import DMSResourceName
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.src.utils.feature_flag.feature_flag import FeatureFlag


@match_class_typing
class DMSReplicationTasksProps(TypedDict):
    replication_instance_arn: str
    migration_type: str  #  Valid values: full-load | cdc | full-load-and-cdc
    source_endpoint_arn: str
    target_endpoint_arn: str
    table_mappings: dict
    replication_task_identifier: str


class Guest360DMSReplicationTask(Construct360):
    """Guest360 Construct for DMS Replication Tasks"""

    @property
    def dms_replication_task(self) -> aws_dms.CfnReplicationTask:
        return self._dms_replication_task

    @property
    def dms_replication_name(self) -> str:
        return self._dms_replication_name

    def __init__(self, scope: Construct360, construct_id: str, props: DMSReplicationTasksProps, **kwargs) -> None:
        """__init__.
        Construct to create DMS Replication Tasks
        Args:
            scope (Construct360)
            construct_id (str): Construct ID
            props (dict) : Configuration for DMS Endpoint - See DMSEndpointProps
        Returns:
            None
        """
        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        DMSReplicationTasksProps(props)

        prefix = self.node.try_get_context("prefix")
        environment = self.node.try_get_context("environment").lower()
        project_path = self.project_dir

        task_props: dict = props

        # add prefix to the value of replication_task_identifier
        self._dms_replication_name = DMSResourceName(prefix, task_props["replication_task_identifier"]).name()
        task_props["replication_task_identifier"] = self._dms_replication_name

        # The expected type for table_mappings for CDK is str
        task_props["table_mappings"] = json.dumps(task_props["table_mappings"])

        self._dms_replication_task = aws_dms.CfnReplicationTask(
            self, task_props["replication_task_identifier"], **task_props
        )

        #####################################################################################################################
        # DMS REPLICATION TASK ALARMS (default and custom alarms)
        # Custom alarm to create Service Now Tickets in case of failed DMS Tasks after "x" retries
        # It is needed to set "p_level_in_prod" to "p3" to  create snow ticket -> sns topic "wdpr-guest360-{env}-snow-pri[3|4]"
        # By default it sends notifications to sns topic: "lst-use1-guest360-alarm-notifications" (it does not create snow ticket)
        # For custom metric "CustomDMSTaskFailure", it should have the same values with dms_task_manager_lambda_props in
        #  app/infrastructure/ingestion/ingestion_dms_task_manager.py
        # The values for metric "CustomDMSTaskFailure" will be sent to it for app/src/ingestion/dms/dms_task_manager/lambda_task_manager.py
        #######################################################################################################################
        default_alarms = [
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="DMSTaskFailed",  # Custom Namespace
                    metric_name="CustomDMSTaskFailure",  ## Custom Metric
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(30),
                    dimensions_map={
                        "ReplicationTaskArn": self._dms_replication_task.ref,
                        "ReplicationInstanceArn": task_props["replication_instance_arn"],
                    },
                ),
                "evaluation_periods": 1,
                "threshold": 3,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
                "snow_integration_enabled": True,  # Defaults to True if environment is static
                "alarm_actions_disabled": False,  # Actions are enabled for static env by default. Disable it(True) if needed. Can not be disabled if snow tickets are desired.
            }
        ]

        # If feature flag "create_snow_tickets" is enabled for the environment create service now tickets
        config_path = f"{project_path}/app/configs/{environment}-infra-feature-flags.yaml"
        with FeatureFlag(
            environment, "dms_stacks.create_snow_tickets_in_event_of_failure", config_path
        ) as create_snow_tickets_flag:
            if create_snow_tickets_flag:
                # Use "p3" to create ServiceNow tickets; otherwise, Guest360Alarm will set it to "default_topic."
                default_alarms[0]["p_level_in_prod"] = "p3"

        for cw_alarm in default_alarms:
            Guest360Alarm(
                self,
                f"{task_props['replication_task_identifier']}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )
