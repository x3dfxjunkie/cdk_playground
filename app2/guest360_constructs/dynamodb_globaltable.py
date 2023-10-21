"""
Guest360 AWS DynamoDB construct library
"""

from typing import Dict, List, Optional, Union, cast

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.kms_key import Guest360KMSKey
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.src.reliability.utils import DynamoDBTableName
from aws_cdk import Stack, aws_dynamodb, aws_iam, aws_kms, aws_ssm, aws_cloudwatch, Duration
from typing_extensions import Any


class Guest360DynamodbGlobaltable(Construct360):
    """
    Guest360 AWS DynamoDB construct
    """

    table: Union[aws_dynamodb.ITable, aws_dynamodb.Table]
    encryption_key: Union[aws_kms.IKey, aws_kms.Key]
    ssm_export: List[aws_ssm.StringParameter] | None

    def __init__(
        self, scope: Construct360, construct_id: str, encryption_key: Optional[aws_kms.IKey] = None, **kwargs
    ) -> None:
        """__init__.
        Guest360DynamodbGlobaltable
            *** Note this is only creating a standard table for the moment due to issues with getting globaltable replications working
            * Enforces encryption using aws_kms.Ikey
                * if Ikey is not supplied one is created using the Guest360KMSKey
        Example:
            Guest360DynamodbGlobaltable(stack, "MyDynamodbGlobaltable")
        Args:
            scope (Construct360): scope
            construct_id (str): construct_id
            encryption_key (Optional[aws_kms.IKey]): encryption_key
            **kwargs
        Returns:
            None
        """
        super().__init__(scope, construct_id)

        self._environment = self.node.try_get_context("environment")

        if kwargs.get("attributes", False):
            self.table = aws_dynamodb.Table.from_table_attributes(self, "DynamodbGlobalTable", **kwargs["attributes"])
            self.encryption_key = cast(aws_kms.IKey, self.table.encryption_key)
            return

        self.ssm_export = None

        if "table_arn" in kwargs and "kms_arn" in kwargs:
            table_arn: str = kwargs["table_arn"]
            key_arn: str = kwargs["kms_arn"]
            self.encryption_key = aws_kms.Key.from_key_arn(self, "key", key_arn)
            self.table = aws_dynamodb.Table.from_table_attributes(
                self, "DynamodbGlobalTable", encryption_key=self.encryption_key, table_arn=table_arn
            )
            return

        prefix = self.node.try_get_context("prefix")

        # force overrides for ephemeral environments (eg exclude all static environments)
        if "guest360" not in prefix:
            kwargs["billing_mode"] = aws_dynamodb.BillingMode.PAY_PER_REQUEST

        # if no encryption set create custom encryption key using Guest360KMSKey
        if encryption_key is None:
            self.encryption_key = Guest360KMSKey(
                self,
                "DynamodbGlobaltableEncryptionKey",
                {"alias": construct_id, "description": f"{prefix}-{construct_id}-DynamodbGlobaltableEncryptionKey"},  # type: ignore
            ).key
            self.encryption_key.add_to_resource_policy(
                aws_iam.PolicyStatement(
                    actions=["kms:Decrypt", "kms:CreateGrant"],
                    conditions={"StringLike": {"kms:ViaService": "dynamodb.*.amazonaws.com"}},
                    principals=[aws_iam.AccountRootPrincipal()],
                    resources=["*"],
                )
            )

        if "table_name" in kwargs:
            kwargs["table_name"] = DynamoDBTableName(prefix, kwargs["table_name"]).name()

        self.table = aws_dynamodb.Table(
            self,
            f"{prefix}-{construct_id}-DynamodbGlobaltable",
            encryption=aws_dynamodb.TableEncryption.CUSTOMER_MANAGED,
            encryption_key=cast(aws_kms.IKey, self.encryption_key),
            point_in_time_recovery=True,
            **kwargs,
        )

        if "guest360" in prefix:
            self.table.auto_scale_write_capacity(min_capacity=1, max_capacity=1000).scale_on_utilization(
                target_utilization_percent=75
            )

            self.table.auto_scale_read_capacity(min_capacity=1, max_capacity=1000).scale_on_utilization(
                target_utilization_percent=75
            )

        ## UE and SE should not occur. Strict threshold
        # UserErrors - throw an alarm if 5 data points is over 1 in the span of 1 minute
        # SystemErrors - throw an alarm if 1 data point is over 1 in the span of 1 minute
        # SuccessfulRequestLatency - throw an alarm if 5 data points is over 100ms in the span of 1 minute
        ## The next events occur frequently in a dynamodb table and are higher. Default is 15 for autoscaling
        # ThrottledRequests - throw an alarm if 15 data point is over 10 in the span of 1 minute
        ## These should not occur. Strict threshold
        # ReadThrottledRequests - throw an alarm if 1 data point is over 1 in the span of 1 minute
        # WriteThrottledRequests - throw an alarm if 1 data point is over 1 in the span of 1 minute
        ## ConsumedRead/WriteCapacity - metrics were skipped because autoscaling already creates CW alarm

        default_alarms = [
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/DynamoDB",
                    metric_name="UserErrors",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                ),
                "evaluation_periods": 5,
                "threshold": 1,
                "datapoints_to_alarm": 5,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/DynamoDB",
                    metric_name="SystemErrors",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                ),
                "evaluation_periods": 1,
                "threshold": 1,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/DynamoDB",
                    metric_name="SuccessfulRequestLatency",
                    statistic=aws_cloudwatch.Statistic.AVERAGE.value,
                    unit=aws_cloudwatch.Unit.MILLISECONDS,
                    period=Duration.minutes(1),
                ),
                "evaluation_periods": 3,
                "threshold": 100,
                "datapoints_to_alarm": 3,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/DynamoDB",
                    metric_name="ThrottledRequests",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                ),
                "evaluation_periods": 10,
                "threshold": 10,
                "datapoints_to_alarm": 10,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/DynamoDB",
                    metric_name="WriteThrottledEvents",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                ),
                "evaluation_periods": 1,
                "threshold": 1,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/DynamoDB",
                    metric_name="ReadThrottledEvents",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                ),
                "evaluation_periods": 1,
                "threshold": 1,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
        ]

        if self._environment == "latest":
            for cw_alarm in default_alarms:
                Guest360Alarm(
                    self,
                    f"{prefix}-{construct_id}-{cw_alarm['metric'].metric_name}-cw-alarm",
                    props=cw_alarm,
                )

    @staticmethod
    def from_arn(scope: Construct360, construct_id: str, table_arn: str, kms_arn: str):
        return Guest360DynamodbGlobaltable(scope, construct_id, table_arn=table_arn, kms_arn=kms_arn)

    @staticmethod
    def from_ssm(scope: Construct360, construct_id: str, stack_name: str, resource: str):
        stack = Stack.of(scope)
        prefix = stack.node.try_get_context("prefix")
        construct_name = "Guest360DynamodbGlobaltable"

        def parameter_name(component_name):
            return f"/{prefix}/{stack_name}/{construct_name}/{resource}/{component_name}"

        table_arn = aws_ssm.StringParameter.value_for_string_parameter(scope, parameter_name("table_arn"))
        kms_arn = aws_ssm.StringParameter.value_for_string_parameter(scope, parameter_name("kms_arn"))
        return Guest360DynamodbGlobaltable.from_arn(scope, construct_id, table_arn, kms_arn)

    def export_ssm(self, resource_name: str) -> str:
        prefix = self.node.try_get_context("prefix")
        stack_name = Stack.of(self).stack_name
        construct_name = "Guest360DynamodbGlobaltable"
        resource_prefix = f"/{prefix}/{stack_name}/{construct_name}/{resource_name}"

        def parameter_name(component_name: str):
            return f"{resource_prefix}/{component_name}"

        assert self.encryption_key is not None

        self.ssm_export = (
            [
                aws_ssm.StringParameter(
                    self,
                    "table_arn_parameter",
                    parameter_name=parameter_name("table_arn"),
                    string_value=self.table.table_arn,
                ),
                aws_ssm.StringParameter(
                    self,
                    "kms_arn_parameter",
                    parameter_name=parameter_name("kms_arn"),
                    string_value=self.encryption_key.key_arn,
                ),
            ]
            if self.ssm_export is None
            else self.ssm_export
        )

        return resource_prefix

    @staticmethod
    def from_attributes(scope: Construct360, construct_id: str, attributes: Dict[str, Any]):
        return Guest360DynamodbGlobaltable(scope, construct_id, attributes=attributes)
