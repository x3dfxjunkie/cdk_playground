""" This file contains the top-level application stacks.
"""
import os
from pathlib import Path
from typing import Optional

from aws_cdk import Aspects, Duration, Stack, aws_cloudwatch
from cdk_nag import AwsSolutionsChecks, NagSuppressions
from app.guest360_aspects.guest360_cw_alarms import Guest360CWAlarms
from app.guest360_aspects.guest360_nagpack import Guest360Rules
from app.guest360_aspects.guest360_tagging import Guest360PathTagger
from app.guest360_aspects.guest360_termination import Guest360Termination
from app.guest360_constructs.construct_360 import Construct360
from app.infrastructure.data_contract_automater import DataContractAutomaterStack
from app.infrastructure.data_service.data_service import DataService
from app.infrastructure.identity.identity import Identity
from app.infrastructure.infrastructure import Infrastructure
from app.infrastructure.ingestion.ingestion import Ingestion
from app.infrastructure.load_testing.static.load_testing_static import LoadTestingStaticStack
from app.infrastructure.processing.processing import Processing
from app.infrastructure.onboarding_bootcamp.onboarding_bootcamp import BootcampStack
from app.infrastructure.reliability.enable_stack import DeployFlag
from app.src.reliability.utils import DashboardName, StackName


class InvalidStackDependencyError(Exception):
    """Custom exception for handling errors with our stack dependencies"""


class Guest360Stack(Stack):

    """Create all the top-level application stacks.

    This also calls the aspects for nags (audits) and path tagging
    """

    aspects = None

    def __getattr__(self, item):
        return None

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        environment_config: dict,
        env: None,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        environment = self.node.try_get_context("environment")
        stack = Stack.of(self)
        stack_name = self.node.try_get_context("stack_name")
        self.is_static_env = self.node.try_get_context("is_static_env")

        self.node.set_context("stack_path", str(Path(os.getcwd()).parents[0]))

        self.node.set_context(
            "prefix",
            "-".join(
                [
                    environment_config["short_env"],
                    environment_config["networking"][stack.region]["short_region"],
                    stack_name,
                ]
            ).lower(),
        )
        prefix = self.node.try_get_context("prefix")

        self.node.set_context(
            "prefix_global",
            "-".join([environment_config["short_env"], stack_name]).lower(),
        )

        self.prefix = self.node.try_get_context("prefix")
        self.node.set_context("termination_protection", environment == "prod")
        termination_protection = self.node.try_get_context("termination_protection")

        self.node.set_context("is_static_env", "guest360" in prefix)

        if DeployFlag.is_stack_enabled(self, "Identity"):
            self.g360_identity_stack = Identity(
                self,
                "identity",
                env=env,
                stack_name=StackName(self.prefix, "Identity").name(),
                tags=stack.tags.tag_values(),
                termination_protection=termination_protection,
                environment_config=environment_config,
            )

        if DeployFlag.is_stack_enabled(self, "Ingestion"):
            self.g360_ingestion_stack = Ingestion(
                self,
                "ingestion",
                env=env,
                stack_name=StackName(self.prefix, "Ingestion").name(),
                tags=stack.tags.tag_values(),
                termination_protection=termination_protection,
                environment_config=environment_config,
            )

        if DeployFlag.is_stack_enabled(self, "LoadTesting/Static"):
            self.g360_testing_stack = LoadTestingStaticStack(
                self,
                "LoadTestingStatic",
                stack_name=StackName(self.prefix, "LoadTestingStatic").name(),
                env=env,
                environment_config=environment_config,
                tags=stack.tags.tag_values(),
                termination_protection=termination_protection,
                dms_stack_extension=self.g360_ingestion_stack.stack_extension_dms,
            )

        if DeployFlag.is_stack_enabled(self, "DataContractAutomater"):
            self.g360_automater_stack = DataContractAutomaterStack(
                self,
                "datacontractautomater",
                env=env,
                stack_name=StackName(self.prefix, "DataContractAutomater").name(),
                tags=stack.tags.tag_values(),
                termination_protection=termination_protection,
                ingestion_stack=self.g360_ingestion_stack,
            )
            self.add_stack_dependency(self.g360_automater_stack, self.g360_ingestion_stack)
        if DeployFlag.is_stack_enabled(self, "Infrastructure"):
            self.g360_infrastructure_stack = Infrastructure(
                self,
                "infrastructure",
                env=env,
                stack_name=StackName(self.prefix, "Infrastructure").name(),
                tags=stack.tags.tag_values(),
                termination_protection=termination_protection,
                environment_config=environment_config,
            )

        if DeployFlag.is_stack_enabled(self, "Processing"):
            self.g360_processing_stack = Processing(
                self,
                "processing",
                env=env,
                stack_name=StackName(self.prefix, "Processing").name(),
                tags=stack.tags.tag_values(),
                termination_protection=termination_protection,
                environment_config=environment_config,
                # identity_stack=self.g360_identity_stack,
                # ingestion_stack=self.g360_ingestion_stack,
            )
            # self.add_stack_dependency(self.g360_processing_stack, self.g360_identity_stack)
            # self.add_stack_dependency(self.g360_processing_stack, self.g360_ingestion_stack)

        if DeployFlag.is_stack_enabled(self, "DataService"):
            self.g360_dataservice_stack = DataService(
                self,
                "data_service",
                env=env,
                stack_name=StackName(self.prefix, "DataService").name(),
                tags=stack.tags.tag_values(),
                termination_protection=termination_protection,
                environment_config=environment_config,
                # identity_stack=self.g360_identity_stack,
                # ingestion_stack=self.g360_ingestion_stack,
                # processing_stack=self.g360_processing_stack,
            )
            # self.add_stack_dependency(self.g360_dataservice_stack, self.g360_identity_stack)
            # self.add_stack_dependency(self.g360_dataservice_stack, self.g360_ingestion_stack)
            # self.add_stack_dependency(self.g360_dataservice_stack, self.g360_processing_stack)

        if environment == "local" and DeployFlag.is_stack_enabled(self, "Bootcamp"):
            self.g360_bootcamp_stack = BootcampStack(
                self,
                "Bootcamp",
                stack_name=StackName(prefix, "Bootcamp").name(),
                env=env,
                environment_config=environment_config,
                tags=stack.tags.tag_values(),
                termination_protection=termination_protection,
            )
        # self.dashboard()

        NagSuppressions.add_stack_suppressions(
            self,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Managed policies are acceptable.",
                },
                {
                    "id": "AwsSolutions-L1",
                    "reason": "CDK makes a bunch of latest runtime version.",
                },
                {"id": "AwsSolutions-IAM5", "reason": "CDK made these :("},
            ],
        )

        # Leave this as a set to be able to add latest when feature testing
        self.aspects = Aspects.of(self)
        if DeployFlag.is_auditing_enabled(self):
            self.aspects.add(AwsSolutionsChecks())
            self.aspects.add(Guest360Rules())

        self.aspects.add(Guest360PathTagger())
        self.aspects.add(Guest360Termination())
        self.aspects.add(Guest360CWAlarms())

    @staticmethod
    def add_stack_dependency(dependent: Stack, dependee: Optional[Stack]):
        if not dependee:
            raise InvalidStackDependencyError(
                f"Dependency for {dependent.stack_name} does not exist - please check the `ephemeral-stack-config.yaml`"
            )
        dependent.add_dependency(dependee)

    def dashboard(self) -> None:
        if not self.is_static_env:
            return

        self._source_dashboard = aws_cloudwatch.Dashboard(
            self, "source-dashboard", dashboard_name=DashboardName(self.prefix, "source-dashboard").name()
        )

        for source in self.g360_ingestion_stack.streams:
            self._source_dashboard.add_widgets(
                aws_cloudwatch.TextWidget(
                    markdown=f"# {source['stream_name']}",
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
                        dimensions_map={"StreamName": source["stream_name"]},
                        statistic="sum",
                    ),
                    aws_cloudwatch.Metric(
                        metric_name="GetRecords.IteratorAgeMilliseconds",
                        namespace="AWS/Kinesis",
                        dimensions_map={"StreamName": source["stream_name"]},
                        statistic="max",
                    ),
                ],
            )
            if "firehose_name" in source and source["firehose_name"] != "":
                firehose_read_records = aws_cloudwatch.GraphWidget(
                    title="Firehose",
                    left=[
                        aws_cloudwatch.Metric(
                            metric_name="DataReadFromKinesisStream.Records",
                            namespace="AWS/Firehose",
                            dimensions_map={"DeliveryStreamName": source["firehose_name"]},
                            statistic="sum",
                        ),
                    ],
                )
                firehose_s3_freshness = aws_cloudwatch.GraphWidget(
                    title="Firehose Freshness in Seconds",
                    left=[
                        aws_cloudwatch.Metric(
                            metric_name="DeliveryToS3.DataFreshness",
                            namespace="AWS/Firehose",
                            dimensions_map={"DeliveryStreamName": source["firehose_name"]},
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
                                    namespace="AWS/Firehose",
                                    dimensions_map={"DeliveryStreamName": source["firehose_name"]},
                                    statistic="avg",
                                    color="#FF69B4",
                                )
                            },
                        ),
                    ],
                )

            else:
                firehose_read_records = aws_cloudwatch.TextWidget(markdown="no firehose")
                firehose_s3_freshness = aws_cloudwatch.TextWidget(markdown="no firehose")
                firehose_s3_success = aws_cloudwatch.TextWidget(markdown="no firehose")

            self._source_dashboard.add_widgets(
                kinesis,
                firehose_read_records,
                firehose_s3_freshness,
                firehose_s3_success,
            )
