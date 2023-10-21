"""test for dms alarm construct
"""
import json
import logging
import sys

import pytest
from aws_cdk import App, Environment, Stack, assertions

from app.guest360_constructs.ingestion.dms.dms_alarm import Guest360DMSAlarm

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class TestDMSAlarm:
    """Test class for DMS Alarm Construct"""

    TEST_STACK_ID = "TestStack"
    RESOURCE = "AWS::CloudWatch::Alarm"

    DIMENSIONS_MAP_INSTANCE = {
        "ReplicationInstanceIdentifier": "myreplicationinstanceid",
    }

    DIMENSIONS_MAP_TASK = {
        "ReplicationInstanceIdentifier": "myreplicationinstanceid",
        "ReplicationTaskIdentifier": "5HKBYSZ6ZATYKTXXXXXXXXXXX",
    }

    DMS_ALARM_INSTANCE = [
        {
            "metric_name": "CPUUtilization",
            "metric": {"statistic": "AVERAGE", "period_in_seconds": 300},
            "alarm": {
                "evaluation_periods": 3,
                "threshold": 80,
                "datapoints_to_alarm": 3,
                "comparison_operator": "GREATER_THAN_OR_EQUAL_TO_THRESHOLD",
            },
        }
    ]

    DMS_ALARM_TASK = [
        {
            "metric_name": "CDCThroughputRowsSource",
            "metric": {"statistic": "AVERAGE", "period_in_seconds": 60},
            "alarm": {
                "alarm_description": "Incoming task changes from the source is more than 1000 rows per second",
                "evaluation_periods": 3,
                "threshold": 1000,
                "datapoints_to_alarm": 3,
                "comparison_operator": "GREATER_THAN_OR_EQUAL_TO_THRESHOLD",
            },
        }
    ]

    #################################################
    ### SECTION FOR DMS REPLICATION TASK ALARM TESTS
    ##################################################
    @pytest.mark.timeout(30, method="signal")
    def test_default_latest_ephemeral_alarm_task(self):
        """
        Basic instantiation - no alarm action attached
        """
        test_context = {
            "environment": "latest",
            "prefix": "lst-use1-pr-1",
            "region": "us-east-1",
        }
        test_app = App(context=test_context)
        stack = Stack(test_app, self.TEST_STACK_ID, env=Environment(account="123456789", region="us-east-1"))

        Guest360DMSAlarm(stack, self.TEST_STACK_ID, self.DIMENSIONS_MAP_TASK, self.DMS_ALARM_TASK)

        template = assertions.Template.from_stack(stack)

        logger.debug(json.dumps(template.to_json(), indent=2))

        template.has_resource_properties(
            self.RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "ActionsEnabled": False,
                "AlarmActions": ["arn:aws:sns:us-east-1:123456789:lst-use1-pr-1-alarm-notifications"],
                "AlarmDescription": "Guest360DMSAlarm15dc5 failed on CDCThroughputRowsSource ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1000. Incoming task changes from the source is more than 1000 rows per second",
                "DatapointsToAlarm": 3,
                "Dimensions": [
                    {"Name": "ReplicationInstanceIdentifier", "Value": "myreplicationinstanceid"},
                    {"Name": "ReplicationTaskIdentifier", "Value": "5HKBYSZ6ZATYKTXXXXXXXXXXX"},
                ],
                "MetricName": "CDCThroughputRowsSource",
                "Namespace": "AWS/DMS",
                "Period": 60,
                "Statistic": "Average",
                "Threshold": 1000,
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_default_latest_guest360_alarm_task(self):
        """
        Testing that the latest default alarms guest360 go to topic `wdpr-guest360-prd-snow-pri4`
        """
        test_context = {
            "environment": "latest",
            "prefix": "lst-use1-guest360",
            "region": "us-east-1",
        }
        test_app = App(context=test_context)
        stack = Stack(test_app, self.TEST_STACK_ID, env=Environment(account="123456789", region="us-east-1"))

        Guest360DMSAlarm(stack, self.TEST_STACK_ID, self.DIMENSIONS_MAP_TASK, self.DMS_ALARM_TASK)

        template = assertions.Template.from_stack(stack)

        logger.debug(json.dumps(template.to_json(), indent=2))

        template.has_resource_properties(
            self.RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "ActionsEnabled": True,
                "AlarmActions": ["arn:aws:sns:us-east-1:123456789:lst-use1-guest360-alarm-notifications"],
                "AlarmDescription": "[SNOWAG:app-global-Guest360][SNOWCI:WDPR Guest360 - AWS Latest][SNOWDESC:Guest360DMSAlarm15dc5 failed on CDCThroughputRowsSource ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1000]Incoming task changes from the source is more than 1000 rows per second",
                "Dimensions": [
                    {"Name": "ReplicationInstanceIdentifier", "Value": "myreplicationinstanceid"},
                    {"Name": "ReplicationTaskIdentifier", "Value": "5HKBYSZ6ZATYKTXXXXXXXXXXX"},
                ],
                "MetricName": "CDCThroughputRowsSource",
                "Namespace": "AWS/DMS",
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_default_prod_guest360_alarm_task(self):
        """
        Testing that the latest default alarms guest360 go to topic `wdpr-guest360-prd-snow-pri3`
        """
        test_context = {
            "environment": "prod",
            "prefix": "prd-use1-guest360",
            "region": "us-east-1",
        }
        test_app = App(context=test_context)
        stack = Stack(test_app, self.TEST_STACK_ID, env=Environment(account="123456789", region="us-east-1"))

        Guest360DMSAlarm(stack, self.TEST_STACK_ID, self.DIMENSIONS_MAP_TASK, self.DMS_ALARM_TASK)

        template = assertions.Template.from_stack(stack)

        logger.debug(json.dumps(template.to_json(), indent=2))

        template.has_resource_properties(
            self.RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "ActionsEnabled": True,
                "AlarmActions": ["arn:aws:sns:us-east-1:123456789:prd-use1-guest360-alarm-notifications"],
                "AlarmDescription": "[SNOWAG:app-global-Guest360][SNOWCI:WDPR Guest360 - AWS Production][SNOWDESC:Guest360DMSAlarm15dc5 failed on CDCThroughputRowsSource ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1000]Incoming task changes from the source is more than 1000 rows per second",
                "Dimensions": [
                    {"Name": "ReplicationInstanceIdentifier", "Value": "myreplicationinstanceid"},
                    {"Name": "ReplicationTaskIdentifier", "Value": "5HKBYSZ6ZATYKTXXXXXXXXXXX"},
                ],
                "MetricName": "CDCThroughputRowsSource",
                "Namespace": "AWS/DMS",
            },
        )

    #####################################################
    ### SECTION FOR DMS REPLICATION INSTANCE ALARM TESTS
    ######################################################
    @pytest.mark.timeout(30, method="signal")
    def test_default_latest_ephemeral_alarm_instance(self):
        """
        Basic instantiation - no alarm action attached
        """
        test_context = {
            "environment": "latest",
            "prefix": "lst-use1-pr-1",
            "region": "us-east-1",
        }
        test_app = App(context=test_context)
        stack = Stack(test_app, self.TEST_STACK_ID, env=Environment(account="123456789", region="us-east-1"))

        Guest360DMSAlarm(stack, self.TEST_STACK_ID, self.DIMENSIONS_MAP_INSTANCE, self.DMS_ALARM_INSTANCE)

        template = assertions.Template.from_stack(stack)

        logger.debug(json.dumps(template.to_json(), indent=2))

        template.has_resource_properties(
            self.RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "ActionsEnabled": False,
                "AlarmActions": ["arn:aws:sns:us-east-1:123456789:lst-use1-pr-1-alarm-notifications"],
                "AlarmDescription": "Guest360DMSAlarm15dc5 failed on CPUUtilization ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 80. Guest360DMSAlarm15dc5 failed on CPUUtilization ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 80",
                "DatapointsToAlarm": 3,
                "Dimensions": [
                    {"Name": "ReplicationInstanceIdentifier", "Value": "myreplicationinstanceid"},
                ],
                "MetricName": "CPUUtilization",
                "Namespace": "AWS/DMS",
                "Period": 300,
                "Statistic": "Average",
                "Threshold": 80,
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_default_latest_guest360_alarm_instance(self):
        """
        Testing that the latest default alarms guest360 go to topic `wdpr-guest360-prd-snow-pri4`
        """
        test_context = {
            "environment": "latest",
            "prefix": "lst-use1-guest360",
            "region": "us-east-1",
        }
        test_app = App(context=test_context)
        stack = Stack(test_app, self.TEST_STACK_ID, env=Environment(account="123456789", region="us-east-1"))

        Guest360DMSAlarm(stack, self.TEST_STACK_ID, self.DIMENSIONS_MAP_INSTANCE, self.DMS_ALARM_INSTANCE)

        template = assertions.Template.from_stack(stack)

        logger.debug(json.dumps(template.to_json(), indent=2))

        template.has_resource_properties(
            self.RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "ActionsEnabled": True,
                "AlarmActions": ["arn:aws:sns:us-east-1:123456789:lst-use1-guest360-alarm-notifications"],
                "AlarmDescription": "[SNOWAG:app-global-Guest360][SNOWCI:WDPR Guest360 - AWS Latest][SNOWDESC:Guest360DMSAlarm15dc5 failed on CPUUtilization ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 80]Guest360DMSAlarm15dc5 failed on CPUUtilization ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 80",
                "Dimensions": [
                    {"Name": "ReplicationInstanceIdentifier", "Value": "myreplicationinstanceid"},
                ],
                "MetricName": "CPUUtilization",
                "Namespace": "AWS/DMS",
            },
        )
