import os

import aws_cdk
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_kms as kms
from aws_cdk import aws_logs
from aws_cdk import aws_msk as msk
from aws_cdk import aws_secretsmanager as secretsmanager
from aws_cdk import aws_ssm as ssm
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360

# TODO - temp constant for revision.  Eventually update to pass into construct or config file based.
CLUSTER_CONFIG_REVISION = 1


class MSK(Construct360):
    def __init__(
        self,
        scope: Construct360,
        id: str,
        environment_config: dict,
        msk_cluster_config: dict,
        secret_rotation_days=180,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)
        account_id = environment_config["account"]
        region_name = environment_config["region"]

        stack_name = self.node.try_get_context("stack_name")
        stack = aws_cdk.Stack.of(self)
        vpc = ec2.Vpc.from_lookup(
            stack,
            "VPC",
            vpc_id=environment_config["networking"][region_name]["vpc"]["id"]
            # This imports the default VPC but you can also
            # specify a 'vpcName' or 'tags'.
        )

        msk_cluster_configuration_name = f"{stack_name}-DataServicesMSKClusterConfig"
        msk_cluster_name = f"{stack_name}-DataServicesMSKCluster"
        msk_broker_log_group_name = f"/aws/kafka/{msk_cluster_name}/broker"

        self.msk_cluster_security_group = ec2.SecurityGroup(
            self,
            id="DataServicesMSKClusterSecurityGroup",
            security_group_name="DataServicesMSKClusterSecurityGroup",
            vpc=vpc,
        )

        self.msk_broker_cloudwatch = aws_logs.LogGroup(
            self,
            id="DataServicesMskBrokerLogs",
            log_group_name=msk_broker_log_group_name,
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,
            retention=aws_logs.RetentionDays.THREE_DAYS,
        )

        # TODO -
        # #Run cdk deploy once first, then update value below, uncomment, and run again (due to not being able to pass vars accross constructs):
        # msk_producer_sg_id = "sg-0a9d4426a9df9c10f" #Update to MSK producer sec group ID after deployment.
        # self.msk_cluster_security_group.add_ingress_rule(
        #     ec2.Peer.security_group_id(security_group_id=msk_producer_sg_id),
        #     ec2.Port.tcp(msk_tls_port),
        #     description="Allow msk_producer lambda sg"
        # )

        for allowed_cidr in msk_cluster_config["allowed-cidrs"]:
            for consumer_port in msk_cluster_config["consumer-ports"]:
                self.msk_cluster_security_group.add_ingress_rule(
                    ec2.Peer.ipv4(allowed_cidr),
                    ec2.Port.tcp(consumer_port["port"]),
                    description=f'Allow consumer {consumer_port["type"]} for port {consumer_port["port"]} for cidr {allowed_cidr}',
                )

        msk_cluster_configuration = msk.CfnConfiguration(
            self,
            "DataServicesMSKClusterConfig",
            name=msk_cluster_configuration_name,
            server_properties="auto.create.topics.enable=true",
        )

        # TODO - make properties config based
        msk_cluster_properties = {
            "cluster_name": f"{stack_name}-DataServicesMSKCluster",
            "kafka_version": msk_cluster_config["kafka-version"],
            "number_of_broker_nodes": msk_cluster_config["number-of-broker-nodes"],
            "broker_node_group_info": msk.CfnCluster.BrokerNodeGroupInfoProperty(
                instance_type=msk_cluster_config["instance-type"],
                client_subnets=[subnet["id"] for subnet in environment_config["networking"][region_name]["subnets"]["private"]],
                security_groups=[
                    self.msk_cluster_security_group.security_group_id,
                ],
                storage_info=msk.CfnCluster.StorageInfoProperty(ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(volume_size=msk_cluster_config["volume-size"])),
            ),
            "client_authentication": msk.CfnCluster.ClientAuthenticationProperty(
                sasl=msk.CfnCluster.SaslProperty(
                    iam=msk.CfnCluster.IamProperty(enabled=True),
                    scram=msk.CfnCluster.ScramProperty(enabled=True),
                ),
                unauthenticated=msk.CfnCluster.UnauthenticatedProperty(enabled=False),
            ),
            "configuration_info": msk.CfnCluster.ConfigurationInfoProperty(
                arn=msk_cluster_configuration.attr_arn,
                revision=1,
            ),
            "logging_info": msk.CfnCluster.LoggingInfoProperty(
                broker_logs=msk.CfnCluster.BrokerLogsProperty(
                    cloud_watch_logs=msk.CfnCluster.CloudWatchLogsProperty(
                        enabled=True,
                        log_group=msk_broker_log_group_name,
                    )
                )
            ),
        }

        self.msk_cluster = msk.CfnCluster(
            self,
            id="DataServicesMSKCluster",
            **msk_cluster_properties,
        )

        encryption_key = kms.Key(
            self,
            "DataServicesMSKClusterKMSKey",
            enable_key_rotation=True,
            alias=f"{stack_name}-DataServicesMSKClusterKMSKey",
        )

        templated_username = secretsmanager.Secret(
            self,
            "AmazonMSK_DataServicesMSKClusterTemplatedUsername",
            generate_secret_string=secretsmanager.SecretStringGenerator(secret_string_template="{}", generate_string_key="username"),
        )

        templated_password = secretsmanager.Secret(
            self,
            "AmazonMSK_DataServicesMSKClusterTemplatedPassword",
            generate_secret_string=secretsmanager.SecretStringGenerator(secret_string_template="{}", generate_string_key="password"),
        )

        secret = secretsmanager.Secret(
            self,
            "AmazonMSK_DataServicesMSKClusterSecret",
            secret_name="AmazonMSK_DataServicesMSKClusterSecret",
            secret_object_value={
                "username": templated_username.secret_value_from_json("username"),
                "password": templated_password.secret_value_from_json("password"),
            },
            encryption_key=encryption_key,
        )

        # secret.add_rotation_schedule("DataServicesMSKClusterSCRAMSecretRotationSchedule", automatically_after=aws_cdk.Duration.days(secret_rotation_days), hosted_rotation=None,)
        msk_scram_secret = msk.CfnBatchScramSecret(
            self,
            "DataServicesMSKClusterSCRAMSecret",
            cluster_arn=self.msk_cluster.attr_arn,
            # the properties below are optional
            secret_arn_list=[
                secret.secret_full_arn,
            ],
        )

        msk_cluster_ssm_arn = ssm.StringParameter(
            self,
            "DataServicesMSKClusterARN",
            parameter_name=f"/{stack_name}/data-services/msk/cluster-arn",
            string_value=self.msk_cluster.attr_arn,
        )

        NagSuppressions.add_resource_suppressions(
            templated_username,
            [
                {
                    "id": "AwsSolutions-SMG4",
                    "reason": "Have backlog story to add lambda rotator",
                }
            ],
            True,
        )
        NagSuppressions.add_resource_suppressions(
            templated_password,
            [
                {
                    "id": "AwsSolutions-SMG4",
                    "reason": "Have backlog story to add lambda rotator",
                }
            ],
            True,
        )
        NagSuppressions.add_resource_suppressions(
            secret,
            [
                {
                    "id": "AwsSolutions-SMG4",
                    "reason": "Have backlog story to add lambda rotator",
                }
            ],
            True,
        )

        # msk_client_policy_statements = [
        #     iam.PolicyStatement(
        #         **{
        #             "effect": iam.Effect.ALLOW,
        #             "actions": [
        #                 "kafka-cluster:Connect",
        #                 "kafka-cluster:AlterCluster",
        #                 "kafka-cluster:DescribeCluster",
        #             ],
        #             "resources": [
        #                 self.msk_cluster.attr_arn,
        #             ],
        #         }
        #     ),
        #     iam.PolicyStatement(
        #         **{
        #             "effect": iam.Effect.ALLOW,
        #             "actions": [
        #                 "kafka-cluster:*Topic*",
        #                 "kafka-cluster:WriteData",
        #                 "kafka-cluster:ReadData",
        #             ],
        #             "resources": [
        #                 f"arn:aws:kafka:{region_name}:{account_id}:topic/{self.msk_cluster.cluster_name}/*"
        #             ],
        #         }
        #     ),
        #     iam.PolicyStatement(
        #         **{
        #             "effect": iam.Effect.ALLOW,
        #             "actions": [
        #                 "kafka-cluster:AlterGroup",
        #                 "kafka-cluster:DescribeGroup",
        #             ],
        #             "resources": [
        #                 f"arn:aws:kafka:{region_name}:{account_id}:group/{self.msk_cluster.cluster_name}/*"
        #             ],
        #         }
        #     ),
        # ]

        # msk_client_policy = iam.ManagedPolicy(
        #     self,
        #     id="DataServicesMSKClientPolicy",
        #     statements=msk_client_policy_statements,
        # )

        # msk_client_role = iam.Role(
        #     self,
        #     id="DataServicesMSKClientRole",
        #     role_name="DataServicesMSKClientRole",
        #     assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        # )

        # msk_client_role.add_managed_policy(msk_client_policy)

        # ec2_instance_profile = iam.CfnInstanceProfile(
        #     self,
        #     "DataServicesMSKClientInstanceProfile",
        #     roles=[
        #         msk_client_role.role_name,
        #     ],
        # )
