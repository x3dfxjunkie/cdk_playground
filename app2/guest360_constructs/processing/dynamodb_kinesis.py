""" DynamoDB Kinesis """
import os
from pathlib import Path
import aws_cdk
import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
import aws_cdk.aws_kinesis as kinesis
import aws_cdk.aws_lambda as aws_lambda
from aws_cdk import Duration
from aws_cdk.aws_lambda_event_sources import KinesisEventSource
from cdk_nag import NagSuppressions
from app.guest360_constructs.lambda_function import LambdaFunctionProps, Guest360LambdaFunction
from app.guest360_constructs.construct_360 import Construct360


class DynamodbKinesisConstruct(Construct360):
    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        stream_name: str,
        days_retention: int,
        environment_config: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        region_name = environment_config["region"]

        # fix me these have circular dependency issues/hard codings
        msk_tls_port = 9094

        stack_name = self.node.try_get_context("stack_name")
        stack_path = str(Path(os.getcwd()).parents[0])
        stack = aws_cdk.Stack.of(self)

        vpc = ec2.Vpc.from_lookup(
            stack,
            "VPC",
            vpc_id=environment_config["networking"][region_name]["vpc"]["id"]
            # This imports the default VPC but you can also
            # specify a 'vpcName' or 'tags'.
        )

        subnets = vpc.select_subnets(
            subnet_filters=[
                ec2.SubnetFilter.by_ids(
                    [
                        subnet["id"]
                        for subnet in environment_config["networking"][region_name]["subnets"]["non-routable"]
                    ]
                ),
            ]
        )

        # cannot dynamically reference this due to being a construct this should be pulled from cfn output or ssm
        # msk_sg = ec2.SecurityGroup.from_lookup_by_name(stack, "msk_sg", security_group_name=msk_sg_name, vpc=vpc)
        # create lambda vpc security group to tunnel between lambda_sg and msk_sg
        # lambda_sg_name = f"{stack_name}-DataServicesMSKLambdaProducerSecurityGroup"
        # lambda_sg = ec2.SecurityGroup(
        #     self,
        #     id="DataServicesMSKLambdaProducerSecurityGroup",
        #     security_group_name=lambda_sg_name,
        #     vpc=vpc,
        #     allow_all_outbound=False,
        # )
        # lambda_sg.add_egress_rule(
        #     ec2.Peer.any_ipv4(),
        #     ec2.Port.tcp(msk_tls_port),
        #     description="msk_producer to msk via tcp port and security group tunnel",
        # )

        dynamodb.Table(
            self,
            "lightning-lane-profile",
            partition_key={"name": "atomicId", "type": dynamodb.AttributeType.STRING},
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,
        )

        stream_to_load = kinesis.Stream(
            self,
            stream_name,
            stream_name=stream_name,
            retention_period=Duration.days(days_retention),
            stream_mode=kinesis.StreamMode.ON_DEMAND,
        )

        ddb_target_table = dynamodb.Table(
            self,
            "TargetTable",
            partition_key=dynamodb.Attribute(name="atomic_id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            kinesis_stream=stream_to_load,
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,
        )

        lambda_consumer = Guest360LambdaFunction(
            self,
            "CONSUMER",
            LambdaFunctionProps(
                function_name="CONSUMER",
                description="Example Lambda to consume events from Kinesis.",
                runtime=aws_lambda.Runtime.PYTHON_3_9,
                code=aws_lambda.Code.from_asset(
                    f"{stack_path}/bazel-bin/app/src/data_service/msk_producer/lambda_archive.zip"
                ),
                handler="lambda_function.lambda_handler",
                environment={
                    "ssm_config_path": f"/{stack_name}/data-services/msk/cluster-arn",
                    "msk_role": f"arn:aws:iam::{stack.account}:role/DataServicesMSKClientRole",
                    "security_protocol": "SASL_SSL",
                    "sasl_mechanism": "SCRAM-SHA-512",
                    # fixme - bootstrap_servers should not be hard coded (cannot do botolookup due to vpc endpoint config)
                    # os.environ["DATA_SERVICES_MSK_BOOTSTRAP_SERVERS"],
                    "bootstrap_servers": "b-1.lstguest360dataservic.5nds5f.c19.kafka.us-east-1.amazonaws.com:9096,b-2.lstguest360dataservic.5nds5f.c19.kafka.us-east-1.amazonaws.com:9096,b-3.lstguest360dataservic.5nds5f.c19.kafka.us-east-1.amazonaws.com:9096",
                    "secret_name": "AmazonMSK_DataServicesMSKClusterSecret",
                },
                vpc=vpc,
                vpc_subnets=ec2.SubnetSelection(
                    subnets=[ec2.Subnet.from_subnet_id(stack, subnet, subnet) for subnet in subnets.subnet_ids]
                ),
                allow_public_subnet=True,
                # security_groups=[lambda_sg],
                timeout=aws_cdk.Duration.seconds(300),
            ),
        ).function

        lambda_consumer.add_event_source(
            KinesisEventSource(
                stream_to_load,
                batch_size=100,  # default
                starting_position=aws_lambda.StartingPosition.TRIM_HORIZON,
            )
        )
        stream_to_load.grant_read(lambda_consumer)

        lambda_consumer_execution_policy_statements = [
            iam.PolicyStatement(
                **{
                    "effect": iam.Effect.ALLOW,
                    "actions": [
                        "ssm:GetParameter",
                        "ssm:GetParameters",
                        "ssm:GetParametersByPath",
                    ],
                    "resources": [
                        f"arn:aws:ssm:{stack.region}:{stack.account}:parameter/{stack_name}/data-services/msk/cluster-arn"
                    ],
                }
            ),
            iam.PolicyStatement(
                **{
                    "effect": iam.Effect.ALLOW,
                    "actions": ["sts:AssumeRole"],
                    "resources": [f"arn:aws:iam::{stack.account}:role/DataServicesMSKClientRole"],
                }
            ),
            iam.PolicyStatement(
                **{
                    "effect": iam.Effect.ALLOW,
                    "actions": [
                        "secretsmanager:GetSecretValue",
                        "secretsmanager:DescribeSecret",
                    ],
                    "resources": [
                        f"arn:aws:secretsmanager:{stack.region}:{stack.account}:secret:AmazonMSK_DataServicesMSKClusterSecret-??????",
                    ],
                }
            ),
            iam.PolicyStatement(
                **{
                    "effect": iam.Effect.ALLOW,
                    "actions": [
                        "kms:Decrypt",
                        "kms:DescribeKey",
                    ],
                    "resources": [
                        f"arn:aws:kms:{stack.region}:{stack.account}:alias/{stack_name}-DataServicesMSKClusterKMSKey"
                    ],
                }
            ),
        ]  # TODO - update hard coded arns to params

        lambda_consumer_execution_policy = iam.ManagedPolicy(
            self,
            id="DataServiceKinesisConsumerManagedPolicy",
            statements=lambda_consumer_execution_policy_statements,
        )

        lambda_consumer.role.add_managed_policy(lambda_consumer_execution_policy)

        NagSuppressions.add_resource_suppressions(
            lambda_consumer.role,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "This is a CDK created role, which uses AWS managed policy, but uses least priviledge policies automatically.",
                }
            ],
            True,
        )
