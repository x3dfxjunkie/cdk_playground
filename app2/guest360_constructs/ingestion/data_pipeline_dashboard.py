"""
Authors: Ryan Anderson, Nicole Lama

Defines base construct and defaults for Guest360's Cloudwatch Dashboards

The functions after __init__ enable different types of rows to be displayed on the dashboard
based on the source type:

*DMS
*DMZ
*Firehose
*Kinesis Stream

"""
import re

from typing import TypedDict, Any
import aws_cdk
from app.guest360_constructs.construct_360 import Construct360
from strongtyping.strong_typing import match_class_typing
from app.src.reliability.utils import DashboardName
from aws_cdk import Stack, aws_cloudwatch, Duration


# @match_class_typing
# class DashboardProps(TypedDict):
#     """
#     Defines optional values to set when creating a new CW Dashboard
#     """

#     name: str


AWS_FIREHOSE = "AWS/Firehose"
AWS_EVENTS = "AWS/Events"


class Guest360IngestionPipelineDashboard(Construct360):
    """The guest360 Construct for creating a CW dashboard"""

    @property
    def dashboard(self):
        return self._dashboard

    @property
    def dashboard_name(self):
        return self._dashboard_name

    def __init__(self, scope: Construct360, construct_id: str, name: str, **kwargs) -> None:
        """

        Args:
            scope (Construct360): _description_
            construct_id (str): _description_
            props (DashboardProps): _description_
        """
        super().__init__(scope, construct_id, **kwargs)

        # DashboardProps(props)

        self.environment = self.node.try_get_context("environment")
        self.prefix = self.node.try_get_context("prefix")
        self.stack_name = self.node.try_get_context("stack_name")
        self._construct_id = construct_id
        self._dashboard_name = name
        self._dashboard = aws_cloudwatch.Dashboard(self, id=self._construct_id, dashboard_name=self._dashboard_name)

    def add_dms(
        self, namespace: str, dms_instance_name: str, dms_instance_short_name: str, dms_task_short_name: str
    ) -> None:
        """Creates Rows on Dashboard for DMS

        Args:
            namespace (str): stackname for ingestion pipeline
            dms_instance_name (str): long name for dms replication instance (used for text descriptions)
            dms_instance_short_name (str): short name of dms instance (used in dimensions)
            dms_task_short_name (str): short name of dms instance task (used in dimensions)
        """
        rep_task_identifier = f"{namespace}-{dms_instance_name}"

        self.dashboard.add_widgets(
            aws_cloudwatch.TextWidget(
                markdown=f"# DMS - {rep_task_identifier}",
                height=1,
                width=24,
            )
        )
        # get data pipeline name (dmz kinesis stream name)
        source_latency = aws_cloudwatch.GraphWidget(
            title="CDC Latency Source",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="CDCLatencySource",
                    namespace="AWS/DMS",
                    dimensions_map={
                        "ReplicationInstanceIdentifier": dms_instance_short_name,
                        "ReplicationTaskIdentifier": dms_task_short_name,
                    },
                    statistic="sum",
                    period=Duration.minutes(5),
                ),
            ],
        )

        # {
        # "view": "timeSeries",
        # "stacked": false,
        # "metrics": [
        #     [ "AWS/DMS", "CDCLatencySource", "ReplicationInstanceIdentifier", "lst-use1-g360-cme-dlr", "ReplicationTaskIdentifier", "lst-use1-g360-cme-dlr-cdc1" ]
        # ],
        # "region": "us-east-1",
        # "title": "CDC latency source"
        # }

        target_latency = aws_cloudwatch.GraphWidget(
            title="CDC Latency Target",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="CDCLatencyTarget",
                    namespace="AWS/DMS",
                    dimensions_map={
                        "ReplicationInstanceIdentifier": dms_instance_short_name,
                        "ReplicationTaskIdentifier": dms_task_short_name,
                    },
                    statistic="average",
                    period=Duration.minutes(5),
                ),
            ],
        )

        # {
        #     "view": "timeSeries",
        #     "stacked": false,
        #     "metrics": [
        #         [ "AWS/DMS", "CDCLatencyTarget", "ReplicationInstanceIdentifier", "lst-use1-2439-cmewdw", "ReplicationTaskIdentifier", "lst-use1-pr-2439-cmewdw-cdc1" ]
        #     ],
        #     "stat": "Average",
        #     "period": 300
        #     "region": "us-east-1",
        #     "title": "CDC latency target"
        # }

        row_throughput = aws_cloudwatch.GraphWidget(
            title="Outgoing task changes for target in rows/second",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="CDCThroughputRowsTarget",
                    namespace="AWS/DMS",
                    dimensions_map={
                        "ReplicationInstanceIdentifier": dms_instance_short_name,
                        "ReplicationTaskIdentifier": dms_task_short_name,
                    },
                    statistic="sum",
                    period=Duration.minutes(1),
                ),
            ],
        )

        # {
        # "view": "timeSeries",
        # "stacked": false,
        # "metrics": [
        #     [ "AWS/DMS", "CDCThroughputRowsTarget", "ReplicationInstanceIdentifier", "lst-use1-g360-cme-dlr", "ReplicationTaskIdentifier", "lst-use1-g360-cme-dlr-cdc1" ]
        # ],
        # "region": "us-east-1",
        # "title": "CDC throughput rows target"
        # }

        cpu = aws_cloudwatch.GraphWidget(
            title="CPU Utillization",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="CPUUtilization",
                    namespace="AWS/DMS",
                    dimensions_map={
                        "ReplicationInstanceIdentifier": dms_instance_short_name,
                        "ReplicationTaskIdentifier": dms_task_short_name,
                    },
                    statistic="sum",
                    period=Duration.minutes(1),
                ),
            ],
        )

        # {
        #     "view": "timeSeries",
        #     "stacked": false,
        #     "metrics": [
        #         [ "AWS/DMS", "CPUUtilization", "ReplicationInstanceIdentifier", "lst-use1-2439-cmewdw" ]
        #     ],
        #     "region": "us-east-1",
        #     "title": "CPU utilization"
        # }

        memory = aws_cloudwatch.GraphWidget(
            title="Memory Utillization",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="MemoryUsage",
                    namespace="AWS/DMS",
                    dimensions_map={
                        "ReplicationInstanceIdentifier": dms_instance_short_name,
                        "ReplicationTaskIdentifier": dms_task_short_name,
                    },
                    statistic="sum",
                    period=Duration.minutes(1),
                ),
            ],
        )

        # {
        #     "view": "timeSeries",
        #     "stacked": false,
        #     "metrics": [
        #         [ "AWS/DMS", "MemoryUsage", "ReplicationInstanceIdentifier", "lst-use1-2752-dpi-east", "ReplicationTaskIdentifier", "ReplicationInstanceMonitor" ]
        #     ],
        #     "region": "us-east-1"
        # }
        self._dashboard.add_widgets(source_latency, target_latency, row_throughput, cpu, memory)

    def add_eventbridge(self, rule_name: str) -> None:
        """Creates Rows on Dashboard for DMZ

        Args:
            dmz_name (str): name of dmz stream
        """
        self.dashboard.add_widgets(
            aws_cloudwatch.TextWidget(
                markdown=f"# EventBridge Rule - {rule_name}",
                height=1,
                width=24,
            )
        )
        dlq_invocations = aws_cloudwatch.GraphWidget(
            title="DLQ Invocations",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="DeadLetterInvocations",
                    namespace=AWS_EVENTS,
                    dimensions_map={"DeliveryStreamName": rule_name},
                    statistic="sum",
                    period=Duration.minutes(1),
                ),
            ],
        )
        failed_invocations = aws_cloudwatch.GraphWidget(
            title="Failed Invocations",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="FailedInvocations",
                    namespace=AWS_EVENTS,
                    dimensions_map={"DeliveryStreamName": rule_name},
                    statistic="sum",
                    period=Duration.minutes(1),
                ),
            ],
        )
        ingestion_latency = aws_cloudwatch.GraphWidget(
            title="Ingestion to Invocation Start Latency",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="IngestionToInvocationStartLatency",
                    namespace=AWS_EVENTS,
                    dimensions_map={"DeliveryStreamName": rule_name},
                    statistic="average",
                    period=Duration.minutes(1),
                ),
            ],
        )
        throttled_rules = aws_cloudwatch.GraphWidget(
            title="Throttled Rules",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="ThrottledRules",
                    namespace=AWS_EVENTS,
                    dimensions_map={"DeliveryStreamName": rule_name},
                    statistic="sum",
                    period=Duration.minutes(1),
                ),
            ],
        )

        self._dashboard.add_widgets(dlq_invocations, failed_invocations, ingestion_latency, throttled_rules)

    def add_firehose(self, firehose_name: str) -> None:
        """Creates Rows on Dashboard for Firehouse

        Args:
            firehose_name (str) name of firehouse stream
        """
        self.dashboard.add_widgets(
            aws_cloudwatch.TextWidget(
                markdown=f"# Firehose - {firehose_name}",
                height=1,
                width=24,
            )
        )
        firehose_read_records = aws_cloudwatch.GraphWidget(
            title="Firehose",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="DataReadFromKinesisStream.Records",
                    namespace=AWS_FIREHOSE,
                    dimensions_map={"DeliveryStreamName": firehose_name},
                    statistic="sum",
                    period=Duration.minutes(1),
                ),
            ],
        )
        firehose_s3_freshness = aws_cloudwatch.GraphWidget(
            title="Firehose Freshness in Seconds",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="DeliveryToS3.DataFreshness",
                    namespace=AWS_FIREHOSE,
                    dimensions_map={"DeliveryStreamName": firehose_name},
                    statistic="max",
                    period=Duration.minutes(1),
                ),
            ],
        )
        firehose_s3_success = aws_cloudwatch.GaugeWidget(
            title="Firehose Delivery to S3",
            left_y_axis=aws_cloudwatch.YAxisProps(min=0, max=100, label="% Successfully Delivered to S3"),
            metrics=[
                aws_cloudwatch.MathExpression(
                    expression='METRICS("m1") *100',
                    label="Delivery To S3 Percent Success",
                    using_metrics={
                        "m1": aws_cloudwatch.Metric(
                            metric_name="DeliveryToS3.Success",
                            namespace=AWS_FIREHOSE,
                            dimensions_map={"DeliveryStreamName": firehose_name},
                            statistic="avg",
                            color="#FF69B4",
                            period=Duration.minutes(1),
                        )
                    },
                ),
            ],
        )

        self._dashboard.add_widgets(firehose_read_records, firehose_s3_freshness, firehose_s3_success)

    def add_kinesis_stream(self, stream_name: str) -> None:
        """Creates Rows on Dashboard for Kinesis Streams

        Args:
            stream_name (str): name of kinesis stream
        """
        self.dashboard.add_widgets(
            aws_cloudwatch.TextWidget(
                markdown=f"# Kinesis - {stream_name}",
                height=1,
                width=24,
            )
        )
        kinesis = aws_cloudwatch.GraphWidget(
            title="Kinesis",
            left=[
                aws_cloudwatch.Metric(
                    metric_name="IncomingRecords",
                    namespace="AWS/Kinesis",
                    dimensions_map={"StreamName": stream_name},
                    statistic="sum",
                    period=Duration.minutes(1),
                ),
                aws_cloudwatch.Metric(
                    metric_name="GetRecords.IteratorAgeMilliseconds",
                    namespace="AWS/Kinesis",
                    dimensions_map={"StreamName": stream_name},
                    statistic="max",
                    period=Duration.minutes(1),
                ),
            ],
        )

        self._dashboard.add_widgets(kinesis)

    def add_function_enrichment(self, namespace: str, subject: str, function_name: str, actions_enabled=True) -> None:
        """Creates Rows on Dashboard for rows processed in an enrichment process

        Args:
            namespace (str): otel namespace for metric grouping (stackname)
            subject (str): source kinesis stream name from cloudevent wraper
            function_name (str): function name producing enrichment metrics
        """
        self.dashboard.add_widgets(
            aws_cloudwatch.TextWidget(
                markdown=f"# Enrichment - {subject} - {function_name}",
                height=1,
                width=24,
            )
        )

        # metrics
        rows_started = aws_cloudwatch.Metric(
            metric_name="rows_started",
            namespace=namespace,
            dimensions_map={"subject": subject, "OTelLib": function_name},
            statistic="sum",
            period=Duration.minutes(1),
        )
        rows_success = aws_cloudwatch.Metric(
            metric_name="rows_success",
            namespace=namespace,
            dimensions_map={"subject": subject, "OTelLib": function_name},
            statistic="sum",
            period=Duration.minutes(1),
        )
        rows_warning = aws_cloudwatch.Metric(
            metric_name="rows_warning",
            namespace=namespace,
            dimensions_map={"subject": subject, "OTelLib": function_name},
            statistic="sum",
            period=Duration.minutes(1),
        )
        rows_failed = aws_cloudwatch.Metric(
            metric_name="rows_failed",
            namespace=namespace,
            dimensions_map={"subject": subject, "OTelLib": function_name},
            statistic="sum",
            period=Duration.minutes(1),
        )
        rows_difference = aws_cloudwatch.MathExpression(
            expression=r"(rows_success + rows_warning + rows_failed) == rows_started",
            using_metrics={
                "rows_success": rows_success,
                "rows_warning": rows_warning,
                "rows_failed": rows_failed,
                "rows_started": rows_started,
            },
            period=Duration.minutes(1),
        )

        row_validation_duration = aws_cloudwatch.Metric(
            metric_name="row_validation_duration",
            namespace=namespace,
            dimensions_map={"subject": subject, "OTelLib": function_name},
            statistic=aws_cloudwatch.Stats.AVERAGE,
            period=Duration.minutes(1),
        )

        # dashboard widgets
        rows_count_match_widget = aws_cloudwatch.GraphWidget(
            title="Enrichment Row Counts == Rows Started",
            left=[
                rows_difference,
            ],
        )
        row_status_widget = aws_cloudwatch.GraphWidget(
            title="Processing Status Metrics",
            left=[
                rows_started,
                rows_success,
                rows_warning,
                rows_failed,
            ],
        )
        row_validation_duration_widget = aws_cloudwatch.GraphWidget(
            title="Row Processing Time Avg",
            left=[
                row_validation_duration,
            ],
        )

        # alarms
        rows_warning_alarm = aws_cloudwatch.Alarm(
            self,
            id=f"{self._construct_id}-{function_name}-rows_warning_alarm",
            metric=rows_warning,
            evaluation_periods=1,
            threshold=1,
            actions_enabled=actions_enabled,
            alarm_description="Row warning - Datacontract matched with invalid fields",
            alarm_name=f"{function_name}-rows_warning_alarm",
            comparison_operator=aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            treat_missing_data=aws_cloudwatch.TreatMissingData.NOT_BREACHING,
        )
        rows_warning_alarm_widget = aws_cloudwatch.AlarmWidget(
            alarm=rows_warning_alarm,
            height=6,
            title="rows_warning",
        )
        rows_failed_alarm = aws_cloudwatch.Alarm(
            self,
            id=f"{self._construct_id}-{function_name}-rows_failed_alarm",
            metric=rows_failed,
            evaluation_periods=1,
            threshold=1,
            actions_enabled=actions_enabled,
            alarm_description="Row failed - Datacontract matched with invalid fields",
            alarm_name=f"{function_name}-rows_failed_alarm",
            comparison_operator=aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            treat_missing_data=aws_cloudwatch.TreatMissingData.NOT_BREACHING,
        )
        rows_failed_alarm_widget = aws_cloudwatch.AlarmWidget(
            alarm=rows_failed_alarm,
            height=6,
            title="rows_failed",
        )
        # create alarm from mathexpression
        rows_count_match_alarm = rows_difference.create_alarm(
            self,
            id=f"{self._construct_id}-{function_name}-rows_count_match_alarm",
            evaluation_periods=1,
            threshold=1,
            actions_enabled=actions_enabled,
            alarm_description="Row count match failed - rows_started does not equal sum of row counts",
            alarm_name=f"{function_name}-rows_count_match_alarm",
            comparison_operator=aws_cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
            treat_missing_data=aws_cloudwatch.TreatMissingData.NOT_BREACHING,
        )
        rows_count_match_alarm_widget = aws_cloudwatch.AlarmWidget(
            alarm=rows_count_match_alarm,
            height=6,
            title="rows_count_match",
        )

        # add to dashboard widgets
        self._dashboard.add_widgets(
            row_status_widget,
            rows_count_match_widget,
            row_validation_duration_widget,
        )
        self._dashboard.add_widgets(
            rows_warning_alarm_widget,
            rows_failed_alarm_widget,
            rows_count_match_alarm_widget,
        )
