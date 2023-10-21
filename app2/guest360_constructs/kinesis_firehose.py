"""Guest360KinesisFirehose Construct
"""
import copy
import logging
from typing import Dict, TypedDict, Union

import aws_cdk.aws_iam as iam
import aws_cdk.aws_kinesis as kinesis
import aws_cdk.aws_kinesisfirehose as kinesisfirehose

# import aws_cdk.aws_logs as logs
import aws_cdk.aws_s3 as s3
from aws_cdk import Stack, aws_cloudwatch, Duration

# from aws_cdk import RemovalPolicy
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm, AlarmProps
from app.guest360_constructs.lambda_function import Guest360LambdaFunction
from app.src.reliability.utils import KinesisFirehoseName

logger = logging.getLogger(__name__)


class KinesisFirehoseBufferingHintsProps(TypedDict):
    """
    kinesis firehose buffering properties
    """

    unit_of_time: str  # SECONDS or MINUTES, which indicate the size allocated to each interval. Defaults to SECONDS.
    interval: int  # How often the unit time is polled to push new Firehose data to the target (S3). Defaults to 60.


class KinesisFirehoseDataTransformationProps(TypedDict):
    """
    kinesis firehose data transformation properties
    """

    enabled: bool
    lambda_properties: dict  # See lambda_function::LambdaFunctionProps|lambda_function::lambdaDockerProps


class KinesisFirehoseDynamicPartitionProps(TypedDict):
    """
    kinesis firehose dynamic partitioning props
    """

    enabled: bool
    keys: NotRequired[Dict[str, str]]


class KinesisFirehosePartitioningProps(TypedDict):
    """
    Kinesis firehose partitioning properties
    """

    dynamic: NotRequired[KinesisFirehoseDynamicPartitionProps]
    custom_keys: NotRequired[Dict[str, Union[str, None]]]  # Static keys to populate custom prefix


class FirehoseCloudWatchProps(TypedDict):
    """Kinesis Firehose CloudWatch Properties"""

    # period: int  # The period over which the specified statistic is applied. AWS Default: 5 (minutes)
    # evaluation_periods: int  # The number of periods over which data is compared to the specified threshold.
    # datapoints_to_alarm: int  # The number of datapoints that must be breaching to trigger the alarm.
    threshold: int  # The value against which the specified statistic is compared


@match_class_typing
class KinesisFirehoseProps(TypedDict):
    """
    Kinesis Firehose Properties
    """

    enabled: bool  # flag to enable or disable kinesis firehose
    bucket_name: str  # name of the bucket which will store the data from kinesis streams
    bucket: NotRequired[s3.Bucket]  # bucket which will store the data from kinesis streams
    buffering_hints: NotRequired[KinesisFirehoseBufferingHintsProps]  # See KinesisFirehoseBufferingHintsProps
    data_transformation: NotRequired[KinesisFirehoseDataTransformationProps]
    kinesis_stream: NotRequired[kinesis.Stream]  # kinesis stream will be the source from the kinesis firehose
    partitioning: NotRequired[
        KinesisFirehosePartitioningProps
    ]  # S3 partitioning props to define custom s3 prefix structure.
    stack_extension: NotRequired[str]  # Stack extension string name required for s3 partition prefix
    monitoring: NotRequired[
        dict[str, FirehoseCloudWatchProps]
    ]  # A map of metric key names, allowed values: [delivery_freshness, partition_count_exceeded], and FirehoseCloudWatchProps.


class InvalidMetricException(Exception):
    pass


class Guest360KinesisFirehose(Construct360):
    """
    Class for creating the kinesis firehose to deliver data to an S3 bucket
    May create a processing lambda if required and the kinesis firehose
    """

    @property
    def firehose_name(self) -> str:
        if self.var_kinesis_firehose_name is None:
            return ""
        else:
            return self.var_kinesis_firehose_name

    @property
    def data_transformation_lambda(self) -> Guest360LambdaFunction:
        return self.firehose_processing_lambda

    def __init__(self, scope: Construct360, construct_id: str, props: KinesisFirehoseProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.var_kinesis_firehose_name = None

        # Check that props matches proper input structure
        KinesisFirehoseProps(props)

        # The Kinesis Firehose will be deployed if the 'kinesis_firehose/enabled' is True.
        if not props["enabled"]:
            return

        account_id = Stack.of(self).account

        region = Stack.of(self).region.lower()
        prefix = self.node.try_get_context("prefix").lower()

        naming_prefix = f"{prefix}-{construct_id}"

        the_kinesis_stream = props["kinesis_stream"]
        var_kinesis_stream_name = the_kinesis_stream.stream_name

        self.var_firehose_processing_lambda_name = f"{construct_id}-fh-lambda"

        self.var_kinesis_firehose_name = KinesisFirehoseName(naming_prefix, "fhose").name()

        firehose_role_name = "FHToS3"

        # Get the bucket to use as a destination
        if props.get("bucket") is None:
            bucket_row = list(filter(lambda x: props["bucket_name"] in x["bucket_name"], props["static_buckets"]))[0]
            the_s3_bucket = bucket_row["bucket"]
        else:
            the_s3_bucket = props["bucket"]

        kms_s3 = the_s3_bucket.encryption_key

        #################
        # Firehose Role
        #################
        if region == "us-east-1":
            """
            With roles being global
            Only create kinesis firehose ca roles if region is us-east-1
            """
            self.firehose_role = Guest360IamRole(
                self,
                construct_id=firehose_role_name,
                props={
                    "role_name": f"{construct_id}-{firehose_role_name}",
                    "assumed_by": iam.CompositePrincipal(iam.ServicePrincipal("firehose.amazonaws.com")),
                    "description": "Firehose access role Service Principal",
                },
            ).role

        else:
            self.firehose_role = Guest360IamRole.from_role_name(
                self, f"{construct_id}-{firehose_role_name}", f"{construct_id}-{firehose_role_name}", mutable=True
            )

        self.firehose_role_arn = self.firehose_role.role_arn
        # Add Kinesis Stream permissions to the firehose role
        the_kinesis_stream.grant_read(self.firehose_role)
        # Add S3 permissions to the firehose role
        the_s3_bucket.grant_read_write(self.firehose_role)
        the_kinesis_stream.grant_read(
            iam.CompositePrincipal(
                iam.ServicePrincipal("firehose.amazonaws.com"),
                iam.ServicePrincipal("streams.metrics.cloudwatch.amazonaws.com"),
            )
        )

        processors_properties = []
        processing_configuration = kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(enabled=False)

        ###################
        # Lambda Processing
        ###################

        firehose_role_lambda_policies = []
        self.firehose_processing_lambda = None
        if props.get("data_transformation", {}).get("lambda_properties"):
            # deep copy data_transformation to normalize and accept all parameters that guest360_lambda allows
            lambda_props = copy.deepcopy(props["data_transformation"]["lambda_properties"])
            lambda_props["function_name"] = f"{construct_id}-fh-lambda"
            lambda_props["description"] = "Firehose Data Processing Lambda"

            self.firehose_processing_lambda = Guest360LambdaFunction(
                self,
                self.var_firehose_processing_lambda_name,
                props=lambda_props,
            )
            lambda_assume_role_policy = self.firehose_processing_lambda.function.role.assume_role_policy
            # add firehose service principal to lambda execution role trust firehose assumes the lambda execution role
            # then performs InvokeFunction on itself
            lambda_assume_role_policy.add_statements(
                iam.PolicyStatement(
                    principals=[iam.ServicePrincipal("firehose.amazonaws.com")],
                    actions=["sts:AssumeRole"],
                )
            )
            self.firehose_processing_lambda.function.role.add_to_policy(
                iam.PolicyStatement(
                    actions=[
                        "lambda:InvokeFunction",
                        "lambda:GetFunction",
                        "lambda:GetFunctionConfiguration",
                    ],
                    effect=iam.Effect.ALLOW,
                    resources=[
                        f"arn:aws:lambda:{region}:{account_id}:function:{self.firehose_processing_lambda.function_name}",
                        f"arn:aws:lambda:{region}:{account_id}:function:{self.firehose_processing_lambda.function_name}:*",
                    ],
                )
            )

            # Append lambda processor properties
            processors_properties.append(
                kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                    type="Lambda",
                    # the properties below are optional
                    parameters=[
                        kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                            parameter_name="LambdaArn",
                            parameter_value=self.firehose_processing_lambda.function.function_arn,
                        ),
                        kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                            parameter_name="RoleArn",
                            parameter_value=self.firehose_processing_lambda.function.role.role_arn,
                        ),
                    ],
                ),
            )
            # defines the processing configuration for Lambda and JQ to the kinesis Firehose
            processing_configuration = kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                enabled=props["data_transformation"]["enabled"],
                processors=processors_properties,
            )

            NagSuppressions.add_resource_suppressions(
                self.firehose_processing_lambda.function.role,
                [
                    {
                        "id": "AwsSolutions-IAM5",
                        "reason": "Allow execution of any lambda version of specified lambda arn",
                    },
                    {"id": "AwsSolutions-IAM4", "reason": "Allow lambda managed policies are ok."},
                ],
                True,
            )

        #################
        # Firehose Role
        #################

        # The GetFunctionConfiguration action is required to Kinesis Firehose.
        # The format resource must end with * without define version.

        firehose_policy_statements = [
            iam.PolicyStatement(
                actions=["kms:GenerateDataKey", "kms:Decrypt"],
                effect=iam.Effect.ALLOW,
                resources=[kms_s3.key_arn],
                conditions={
                    "StringEquals": {"kms:ViaService": f"s3.{region}.amazonaws.com"},
                    "StringLike": {
                        "kms:EncryptionContext:aws:s3:arn": [
                            "arn:aws:s3:::%FIREHOSE_POLICY_TEMPLATE_PLACEHOLDER%/*",
                            "arn:aws:s3:::%FIREHOSE_POLICY_TEMPLATE_PLACEHOLDER%",
                        ]
                    },
                },
            ),
            iam.PolicyStatement(
                actions=["logs:CreateLogGroup"],
                effect=iam.Effect.ALLOW,
                resources=[f"arn:aws:logs:{region}:{account_id}:*"],
            ),
            iam.PolicyStatement(
                actions=["kms:Decrypt"],
                effect=iam.Effect.ALLOW,
                resources=[f"arn:aws:kms:{region}:{account_id}:key/%FIREHOSE_POLICY_TEMPLATE_PLACEHOLDER%"],
                conditions={
                    "StringEquals": {"kms:ViaService": f"kinesis.{region}.amazonaws.com"},
                    "StringLike": {
                        "kms:EncryptionContext:aws:kinesis:arn": f"arn:aws:kinesis:{region}:{account_id}:stream/{var_kinesis_stream_name}"
                    },
                },
            ),
        ]

        firehose_policy_statements.extend(firehose_role_lambda_policies)

        firehose_execution_policy = iam.ManagedPolicy(
            self,
            id="KinesisFirehoseManagedPolicy",
            statements=firehose_policy_statements,
        )
        # Attach managed policy per region. self.firehose_role.add_managed_policy(firehose_execution_policy) -> Just works for  us-east-1
        firehose_execution_policy.attach_to_role(self.firehose_role)

        #################
        # NagSuppressions
        #################

        NagSuppressions.add_resource_suppressions(
            self.firehose_role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Browse only top level items in bucket",
                    "applies_to": f"[Resource::arn:aws:s3:::{the_s3_bucket.bucket_name}/*]",
                }
            ],
            True,
        )

        NagSuppressions.add_resource_suppressions(
            self.firehose_role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Access to Firehose logs based on template",
                    "applies_to": f"[Resource::arn:aws:logs:{region}:<AWS::AccountId>:log-group:%FIREHOSE_POLICY_TEMPLATE_PLACEHOLDER%:log-stream:*]",
                }
            ],
            True,
        )

        NagSuppressions.add_resource_suppressions(
            firehose_execution_policy,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Grant Write creates wildcard policy kms:GenerateDataKey* and kms:ReEncrypt*",
                },
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok."},
            ],
            True,
        )

        ######################
        # Dynamic Partitioning
        ######################

        s3_dynamic_partitioning: str = ""

        dynamic_partitioning_configuration = kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty(
            enabled=False
        )
        if props.get("partitioning", {}).get("dynamic"):
            partitioning = copy.deepcopy(props["partitioning"])
            if partitioning.get("dynamic").get("enabled"):
                # Evaluation of dynamic_keys
                dynamic_keys = partitioning.get("dynamic", {}).get("keys") or []

                # Default routing keys
                if not dynamic_keys:
                    dynamic_keys = {
                        "database": ".router_database",
                        "schema": ".router_schema",
                        "table": ".router_table",
                        "stream": ".stream",
                    }

                processor_parameter_value: str = ""
                for key, value in dynamic_keys.items():
                    s3_dynamic_partitioning += f"{key}=!{{partitionKeyFromQuery:{key}}}/"
                    processor_parameter_value += f"{key}: {value},"

                dynamic_partitioning_configuration = (
                    kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty(enabled=True)
                )
                processors_properties.append(
                    kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                        type="MetadataExtraction",
                        parameters=[
                            kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="MetadataExtractionQuery",
                                parameter_value=f"{{{processor_parameter_value}}}",
                            ),
                            kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="JsonParsingEngine", parameter_value="JQ-1.6"
                            ),
                        ],
                    )
                )

                # Multi record deaggregation processor
                processors_properties.append(
                    kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                        type="RecordDeAggregation",
                        parameters=[
                            kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="SubRecordType",
                                parameter_value="JSON",
                            )
                        ],
                    )
                )

                # Append delimiter
                processors_properties.append(
                    kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                        type="AppendDelimiterToRecord",
                        parameters=[
                            kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="Delimiter",
                                parameter_value="\\n",
                            )
                        ],
                    )
                )

                # JQ processing configuration for kinesis Firehose
                processing_configuration = kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                    enabled=True, processors=processors_properties
                )

        # Evaluation of custom partitioning prefixes
        s3_prefix: str = ""
        if props.get("partitioning", {}).get("custom_keys"):
            custom_keys = props["partitioning"]["custom_keys"]
            for key, value in custom_keys.items():
                if value is None:
                    s3_prefix += f"{key}/"
                else:
                    s3_prefix += f"{key}={value}/"

        # Default snowpipe prefix
        if not s3_prefix:
            s3_prefix = "snowpipe/"

        # Definition of S3 destination partition prefixes
        s3_destination_prefix = s3_prefix + s3_dynamic_partitioning + "!{timestamp:yyyy/MM/dd/HH}/"
        s3_error_destination_prefix = (
            s3_prefix + "Errors" + "/result=!{firehose:error-output-type}" + "/!{timestamp:yyyy/MM/dd/HH}/"
        )

        ##################
        # Kinesis Firehose
        ##################

        self.delivery_stream = kinesisfirehose.CfnDeliveryStream(
            self,
            self.var_kinesis_firehose_name,
            delivery_stream_name=self.var_kinesis_firehose_name,
            delivery_stream_type="KinesisStreamAsSource",
            kinesis_stream_source_configuration=kinesisfirehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty(
                kinesis_stream_arn=the_kinesis_stream.stream_arn,
                role_arn=self.firehose_role_arn,
            ),
            extended_s3_destination_configuration=kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(
                bucket_arn=the_s3_bucket.bucket_arn,
                buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                    interval_in_seconds=self._time_interval(
                        props.get("buffering_hints", {}).get("unit_of_time", "SECONDS"),
                        props.get("buffering_hints", {}).get("interval", 60),
                    )
                ),
                compression_format="GZIP",
                role_arn=self.firehose_role_arn,
                encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                    kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                        awskms_key_arn=kms_s3.key_arn
                    )
                ),
                cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                    enabled=True,
                    log_group_name=f"/aws/kinesisfirehose/{self.var_kinesis_firehose_name}",
                    log_stream_name="DestinationDelivery",
                ),
                processing_configuration=processing_configuration,
                dynamic_partitioning_configuration=dynamic_partitioning_configuration,
                prefix=s3_destination_prefix,
                error_output_prefix=s3_error_destination_prefix,
            ),
        )
        #################
        # NagSuppressions
        #################
        NagSuppressions.add_resource_suppressions(
            self.delivery_stream,
            [
                {
                    "id": "AwsSolutions-KDF1",
                    "reason": "Enabling encryption fails as it says it only supports DirectPut",
                    "applies_to": "[Resource::*]",
                },
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Enable managed policies for bucket stream notifications",
                },
            ],
            True,
        )

        ##########################################
        # Monitoring CloudWatch Metrics and Alarms
        ##########################################

        self._set_monitoring(props=props)

        ########################
        # Cloudwatch log groups
        ########################

        # cloudwatch logGroup for kinesis firehose - not used
        # loggroup = logs.LogGroup(self, f"{var_kinesis_firehose_name}-LogsLogGroup", log_group_name=f"/aws/kinesisfirehose/{var_kinesis_firehose_name}", removal_policy=RemovalPolicy.DESTROY, retention=logs.RetentionDays.ONE_MONTH)
        # cloudwatch logStream for backup delivery - not used
        # logslogstream = logs.LogStream(self, f"{var_kinesis_firehose_name}-LogStream-BackupDelivery", log_group=loggroup, log_stream_name="BackupDelivery", removal_policy=RemovalPolicy.DESTROY)
        # cloudwatch logStream for destination delivery - not used
        # logslogstream2 = logs.LogStream(self, f"{var_kinesis_firehose_name}-LogStream-DestinationDelivery", log_group=loggroup, log_stream_name="DestinationDelivery", removal_policy=RemovalPolicy.DESTROY)

        self.delivery_stream.node.add_dependency(self.firehose_role)

    def _time_interval(self, unit_of_time: str = "SECONDS", interval: int = 60) -> int:
        """Allows parameterization with defaults for how often a Firehose is buffering data to S3.

        Args:
            unit_of_time (str, optional): A unit of time is any particular time interval, used as a standard way of measuring or expressing duration. Accepts 'SECONDS' or 'MINUTES'. Defaults to 'SECONDS'.
            interval (int, optional): How often the unit_of_time is called for each buffer cycle. Defaults to 60.

        Raises:
            accepted_sizes ValueError: Can only use 'SECONDS' or 'MINUTES'.
            interval_in_seconds ValueError: The ultimate time in seconds of whatever the param inputs were.

        Returns:
            int: The time in whole seconds that will be exporting buffering data to s3.
        """
        # handling this for the get() method below
        if unit_of_time is None:
            unit_of_time = "SECONDS"
        if interval is None:
            interval = 60

        unit_of_time = unit_of_time.upper().strip()
        interval = int(interval)

        accepted_sizes = ["SECONDS", "MINUTES"]

        if unit_of_time not in accepted_sizes:
            raise ValueError("Constructed unit_of_time can only be in minutes or seconds.")

        # conversion of inputs to seconds
        if unit_of_time == accepted_sizes[0]:
            interval_in_seconds = interval
        elif unit_of_time == accepted_sizes[1]:
            interval_in_seconds = interval * 60

        if interval_in_seconds < 60 or interval_in_seconds > 900:
            raise ValueError(
                "Constructed interval_in_seconds has a valid Range: Minimum value of 60. Maximum value of 900."
            )

        return interval_in_seconds

    def _set_monitoring(self, props: KinesisFirehoseProps):
        """Function to configure default CloudWatch metrics and Guest360Alarm to Firehose resources"""

        # Define default metric settings
        default_monitoring = [
            {
                "metric_settings": {
                    "metric_name": "DeliveryToS3.DataFreshness",
                    "namespace": "Firehose",
                    "statistic": "Average",
                    "period": 5,  # Configurable
                    "dimensions_map": {
                        "DeliveryStreamName": self.firehose_name,
                    },
                },
                "alarm_props": {
                    "alarm_description": "WARNING Delivery to S3 Data Freshness Default Threshold Reached",
                    "evaluation_periods": 1,  # Configurable
                    "datapoints_to_alarm": 1,  # Configurable
                    "threshold": 900,  # unit Seconds (15') # Configurable
                },
            }
        ]

        # Validating dynamic partitioning enabled attribute
        dynamic_partitioning = False
        if props.get("partitioning", {}).get("dynamic"):
            partitioning = copy.deepcopy(props["partitioning"])
            if partitioning.get("dynamic").get("enabled"):
                dynamic_partitioning: bool = partitioning.get("dynamic").get("enabled")

        # Dynamic partitioning default metric and alarm
        if dynamic_partitioning:
            default_monitoring.append(
                {
                    "metric_settings": {
                        "metric_name": "PartitionCountExceeded",
                        "namespace": "Firehose",
                        "statistic": "Average",
                        "period": 5,  # Configurable
                        "dimensions_map": {
                            "DeliveryStreamName": self.firehose_name,
                        },
                    },
                    "alarm_props": {
                        "alarm_description": "WARNING PartitionCountExceeded Threshold Reached",
                        "evaluation_periods": 1,  # Configurable
                        "datapoints_to_alarm": 1,  # Configurable
                        "threshold": 1,  # unit Boolean # Configurable
                    },
                },
            )

        monitoring = default_monitoring

        # Custom monitoring definition
        if props.get("monitoring"):
            custom_monitoring = copy.deepcopy(props["monitoring"])

            for metric_key, custom_props in custom_monitoring.items():
                match metric_key:
                    case "delivery_freshness":
                        delivery_metric_settings = monitoring[0]["metric_settings"]
                        delivery_alarm_props = monitoring[0]["alarm_props"]

                        # Updating delivery_freshness metric settings
                        delivery_metric_settings["period"] = custom_props["period"]
                        custom_props.pop("period")

                        # Updating delivery_freshness alarm props
                        delivery_alarm_props.update(custom_props)

                    case "partition_count_exceeded" if dynamic_partitioning:
                        count_exceeded_metric_settings = monitoring[1]["metric_settings"]
                        count_exceeded_alarm_props = monitoring[1]["alarm_props"]

                        # Updating partition_count_exceeded metric settings
                        count_exceeded_metric_settings["period"] = custom_props["period"]
                        custom_props.pop("period")

                        # Updating partition_count_exceeded alarm props
                        count_exceeded_alarm_props.update(custom_props)

                    case _:
                        raise InvalidMetricException(f"Invalid metric {metric_key} supplied")

        # Define alarms
        for cw_alarm in monitoring:
            metric_settings = copy.deepcopy(cw_alarm["metric_settings"])
            alarm_props = copy.deepcopy(cw_alarm["alarm_props"])

            # Update period
            period = Duration.minutes(metric_settings["period"])
            metric_settings["period"] = period

            # Get IMetric
            metric = aws_cloudwatch.Metric(**metric_settings)

            # Update metric alarm
            alarm_props["metric"] = metric

            # Check alarm props
            AlarmProps(alarm_props)  # type: ignore

            # Define alarm
            Guest360Alarm(self, f"{self.firehose_name}-{metric.metric_name}", props=alarm_props)
