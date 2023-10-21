"""
Logic for Guest360's base construct for ECS
"""
import os
from copy import deepcopy
from typing import Dict, List, Tuple, TypedDict, Union

import aws_cdk
import yaml
from aws_cdk import Duration, aws_cloudwatch, aws_iam
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.cloudwatch_alarm import AlarmProps, Guest360Alarm
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.ecr_repository import Guest360ECRRepository
from app.guest360_constructs.iam_role import Guest360IamRole, IAMProps
from app.guest360_constructs.s3_bucket import Guest360S3Bucket, S3Props
from app.src.reliability.utils import (
    ContainerName,
    ECRRepoName,
    ECSClusterName,
    FargateServiceName,
    RoleName,
    SecurityGroupName,
    StackName,
)
from app.guest360_constructs.alarm_utils import create_alarm_for_incoming_log_traffic


class VPCProps(TypedDict):
    """VPC Properties"""

    vpc_id: Union[str, None]  # ID of VPC to use for ECS
    allowlist: Dict[str, Dict]  # List of SG ingress and egress rules (all outbound allowed)
    is_default: bool  # Whether or not the vpc is the default vpc
    blocklist: NotRequired[Dict[str, Dict]]  # List of Network ACL rules (for potential explicit denies)


class ServiceProps(TypedDict):
    """Service Properties"""

    service_name: str  # The name to be used for the container task
    repository_name: NotRequired[str]  # The repository name name for the specific service
    environment: Dict[str, str]  # Dictionary of environment variables to pass to ECS Instance
    desired_count: int = 1  # The desired count for task of each service
    cloudmap: bool  # Enable the cloudmap service
    command: List[str] = None  # command to execute on task


class CloudWatchProps(TypedDict):
    """
    Metrics Settings and Guest360Alarm AlarmProps definitions
    """

    cpu_alarm: dict  # CPUUtilization - Guest360 Alarm properties. This should be AlarmProps type, just FYI
    memory_alarm: dict  # MemoryUtilization - Guest360 Alarm properties. This should be AlarmProps type, just FYI
    metric_period: int  # The period over which the specified statistic is applied. AWS Default: 5 (minutes)
    metric_statistic: str  # Allowed values: “Minimum”,“Maximum”,“Average”,“Sum”,“SampleCount - AWS Default: Average


@match_class_typing
class ECSConsumerProps(TypedDict):
    """ECS Consumer Properties"""

    secret_name: str  # AWS Secrets Manager Secret Name
    s3: Dict  # S3 Props for message failure bucket - this should be S3Props, just FYI
    memory_mib: Union[str, int]  # Memory needed for ECS container
    cpu_limitmb: Union[str, int]  # Limit in MB used by cpu's
    services: List[Union[Tuple[str, ServiceProps], Dict]]  # Services - list of ecs service and container details
    iam: Dict  # Props for IAM construct - this should be IamPops, just FYI. See Guest360IAM Construct for more details.
    networking: NotRequired[VPCProps]  # Props for VPC - includes VPC_ID
    monitoring: NotRequired[CloudWatchProps]  # Cloudwatch metrics and Guest360Alarm props


class Sidecar(TypedDict):
    registry_repository_name: NotRequired[str]  # The name to be used for the container task
    image_tag: NotRequired[str]  # The name of the image tag to use
    tag: str  # The name to be used for the sidecar container
    environment: Dict[str, str]  # Dictionary of environment variables to pass to ECS Instance
    port_mappings: Dict[str, str]  # Dictionary of environment variables to pass to ECS Instance


class Guest360ECS(Construct360):
    """
    Class defining Guest360's base construct for ECS
    """

    @property
    def fargate_services(self) -> List[aws_cdk.aws_ecs.FargateService]:
        return self.services

    def __init__(self, scope: Construct360, construct_id: str, props: ECSConsumerProps, **kwargs) -> None:
        """Construct to create an ECS Fargate Construct
        Args:
            scope (Construct360)
            construct_id (str): Construct ID
            props (dict): Configurations for Messaging ECS Cluster - see ECSConsumerProps TypedDict
            **kwargs: Description
        """

        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        # Imported props need to be checked apart
        S3Props(props["s3"])
        IAMProps(props["iam"])
        ECSConsumerProps(props)

        stack = aws_cdk.Stack.of(self)
        environment = self.node.try_get_context("environment")
        region_name = aws_cdk.Stack.of(self).region.lower()
        prefix = self.node.try_get_context("prefix")
        global_prefix = self.node.try_get_context("prefix_global")
        self.naming_prefix = f"{prefix}-{construct_id}"

        self.cloudmap = {}
        # Grab networking information from global environment config
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/../configs/{environment}-environment.yaml",
            mode="r",
            encoding="utf-8",
        ) as file:
            environment_config = yaml.safe_load(file)
            subnets_config = environment_config["networking"][stack.region]["subnets"]["non-routable"]
            vpc_config = environment_config["networking"][stack.region]["vpc"]["id"]
            subnet_id_list: List[str] = []
            subnet_cidr_list: List[str] = []

            for subnet in subnets_config:
                subnet_id_list.append(subnet["id"])
                subnet_cidr_list.append(subnet["cidr"])

        # Grab the VPC from lookup
        vpc = aws_cdk.aws_ec2.Vpc.from_lookup(self, StackName(self.naming_prefix, "vpc").name(), vpc_id=vpc_config)

        # Grab subnets
        service_subnets = aws_cdk.aws_ec2.SubnetSelection(
            subnets=[
                aws_cdk.aws_ec2.Subnet.from_subnet_id(scope=self, id=f"{prefix}-{subnet_id}", subnet_id=subnet_id)
                for subnet_id in subnet_id_list
            ]
        )

        # Create the security group to be used by the fargate service
        self.sg_group = aws_cdk.aws_ec2.SecurityGroup(
            self,
            StackName(self.naming_prefix, "ecs-sg").name(),
            security_group_name=SecurityGroupName(self.naming_prefix, "ecs-sg").name(),
            vpc=vpc,
            allow_all_outbound=True,
        )

        # Route ports for containers, as well as add ingress rules for security group
        networking_props = props["networking"]

        ingress: Dict[str, List[Union[int, str]]] = networking_props["allowlist"]["ingress"]

        self.set_ingress_rules(ingress)

        self.port_mappings = [aws_cdk.aws_ecs.PortMapping(container_port=x) for x in list(set(ingress["ports"]))]
        # self.port_mappings.append(port_map)
        # get unique port_mappings

        # Create the ECS cluster using the naming convention and ensuring cloudwatch container insights
        # are enabled for cdk synth pass
        self.cluster = aws_cdk.aws_ecs.Cluster(
            self, ECSClusterName(self.naming_prefix, "fargate-cluster").name(), container_insights=True, vpc=vpc
        )

        # Create the IAM Roles used for ECS Cluster or grab the existing roles if region is not us-east-1
        iam_props = props["iam"]

        if region_name == "us-east-1":
            # The execution role is used by ECS to create services and grab the ECR image
            iam_execution_props = deepcopy(iam_props)
            iam_execution_props["role_name"] = f"{iam_execution_props['role_name']}-execution"
            self.ecs_execution_role = Guest360IamRole(
                self, StackName(global_prefix, iam_execution_props["role_name"]).name(), iam_execution_props
            )

        # Since IAM is global -
        # if region is us-west-2 assume the roles have already been created and avoid creating them again.
        else:
            self.ecs_execution_role = aws_iam.Role.from_role_name(
                self,
                StackName(global_prefix, f"{iam_props['role_name']}-execution").name(),
                role_name=RoleName(global_prefix, f'{iam_props["role_name"]}-execution').name(),
                mutable=True,
            )

        # Use given information in order to find the static ECR repository to use
        # in order to get the images for the container
        ecr_props: Dict[str, str] = props["ecr"]
        default_ecr_name: str = ecr_props["repository_name"]  # Grab AWS Secret from secrets manager
        default_ecr_repository = self._get_ecr_repository(stack, construct_id, environment, default_ecr_name)

        if environment == "local":
            secret = aws_cdk.aws_secretsmanager.Secret(
                stack,
                StackName(self.naming_prefix, f'{props["secret_name"]}-sm').name(),
                secret_name=props["secret_name"],
            )
            secret.add_rotation_schedule(
                "RotationSchedule", hosted_rotation=aws_cdk.aws_secretsmanager.HostedRotation.mysql_single_user()
            )

        self.secret = aws_cdk.aws_secretsmanager.Secret.from_secret_name_v2(
            stack, StackName(self.naming_prefix, "sm").name(), secret_name=props["secret_name"]
        )

        # Grant ECS role access to read secret
        self.secret.grant_read(self.ecs_execution_role.role)

        self.asset_bucket = Guest360S3Bucket(
            self, StackName(self.naming_prefix, "consumer-failure-bucket").name(), region_name, props["s3"]
        )

        self.task_definitions: List[aws_cdk.aws_ecs.TaskDefinition] = []
        self.services: List[aws_cdk.aws_ecs.FargateService] = []

        self.task_roles = {}

        ### Creating OTEL Image, which will be used in every service ###
        otel_repository_name = ecr_props.get("otel_repository_name", "otel/otel_sidecar")
        ports = [55679, 4317, 13133]  # TODO: should this go in the ingestion config too?
        otel_sidecar_portmappings = [aws_cdk.aws_ecs.PortMapping(container_port=port) for port in ports]

        otel_repository = Guest360ECRRepository.from_repository_name(
            stack,
            "otel-repository",
            repository_name=f"guest360/{otel_repository_name}",
        )

        otel_image = aws_cdk.aws_ecs.ContainerImage.from_ecr_repository(
            repository=otel_repository, tag=ecr_props.get("otel_tag", "v0.31.x")  # TODO do something about hardcoding
        )

        otel_environment = {"AWS_REGION": region_name}

        # Loop through provided services creating services in the cluster to read from messengers
        for service in props["services"]:
            service_name = service["service_name"]
            sidecar = service.get("sidecar")

            # Use given information in order to find the static ECR repository to use
            # in order to get the images for the container
            ecr_repository = (
                default_ecr_repository
                if service.get("repository_name") is None
                else self._get_ecr_repository(stack, construct_id, environment, service.get("repository_name"))
            )

            # The task role is used by the individual tasks to make amazon API calls
            iam_task_props = deepcopy(iam_props)
            iam_task_props["role_name"] = f'{iam_task_props["role_name"]}-{service_name}'
            ecs_task_role = Guest360IamRole(
                self, StackName(global_prefix, iam_task_props["role_name"]).name(), iam_task_props
            )

            self.task_roles[service_name] = ecs_task_role
            NagSuppressions.add_resource_suppressions(
                ecs_task_role.role,
                [
                    {
                        "id": "AwsSolutions-IAM5",
                        "reason": "Grant Write creates wildcard policy kms:GenerateDataKey* and kms:ReEncrypt*",
                    }
                ],
                True,
            )

            # ensure environment variable name matches bucket name
            # validate the case when a service have not a environment config
            self.asset_bucket.bucket.grant_read_write(ecs_task_role.role)

            # grant the ability for the task role to read from secrets manager
            self.secret.grant_read(ecs_task_role.role)

            ## Grant the task roles permission to publish traces to aws xray
            ecs_task_role.role.add_to_policy(
                aws_iam.PolicyStatement(actions=["xray:PutTraceSegments", "xray:PutTelemetryRecords"], resources=["*"])
            )

            # Create the task definition for ECS and suppress complaints
            task_definition = aws_cdk.aws_ecs.TaskDefinition(
                self,
                StackName(self.naming_prefix, f"{service_name}-task-definition").name(),
                execution_role=self.ecs_execution_role.role,
                task_role=ecs_task_role.role,
                memory_mib=str(props["memory_mib"]),
                cpu=str(props["cpu_limitmb"]),
                compatibility=aws_cdk.aws_ecs.Compatibility.FARGATE,
            )
            self.task_definitions.append(task_definition)
            NagSuppressions.add_resource_suppressions(
                task_definition,
                [
                    {
                        "id": "AwsSolutions-ECS2",
                        "reason": "Allow Environment Variables to be passed into ECS",
                    }
                ],
                True,
            )

            # ensure environment variable name matches bucket name
            # validate the case when a service have not a environment config
            if service["environment"] is not None:
                service["environment"]["FAILED_MSG_BUCKET_NAME"] = self.asset_bucket.bucket.bucket_name

            # Add the container to the task, configuring logging and port mappings and passing on
            # environment variables
            container = task_definition.add_container(
                StackName(self.naming_prefix, f"{service_name}-consumer").name(),
                image=aws_cdk.aws_ecs.ContainerImage.from_ecr_repository(
                    repository=ecr_repository, tag=service["image_tag"]
                ),
                container_name=ContainerName(self.naming_prefix, f"{service_name}-consumer").name(),
                environment=self.convert_env_to_str(service["environment"]),
                logging=aws_cdk.aws_ecs.AwsLogDriver(stream_prefix=f"{service_name}-log"),
                port_mappings=self.port_mappings,
                command=service["command"] if service.get("command") is not None else [],
            )

            self._create_sidecar_container(
                sidecar=sidecar,
                task_definition=task_definition,
                default_ecr_repository=default_ecr_repository,
                service_name=service_name,
                naming_prefix=self.naming_prefix,
            )

            # Add open telemetry sidecar for every service
            task_definition.add_container(
                StackName(self.naming_prefix, f"{service_name}-otel-sidecar").name(),
                image=otel_image,
                container_name=ContainerName(self.naming_prefix, f"{service_name}-otel-sidecar").name(),
                environment=self.convert_env_to_str(otel_environment),
                logging=aws_cdk.aws_ecs.AwsLogDriver(stream_prefix="otel-sidecar-log"),
                port_mappings=otel_sidecar_portmappings,
            )
            # Start fargate service using security group created above
            fargate_service = aws_cdk.aws_ecs.FargateService(
                self,
                StackName(self.naming_prefix, f"{service_name}-FS").name(),
                cluster=self.cluster,
                task_definition=task_definition,
                service_name=FargateServiceName(self.naming_prefix, f"{service_name}-FS").name(),
                security_groups=[self.sg_group],
                vpc_subnets=service_subnets,
                circuit_breaker=aws_cdk.aws_ecs.DeploymentCircuitBreaker(rollback=True),
                desired_count=service["desired_count"],
            )
            self.services.append(fargate_service)

            # add cloudmap service

            self._set_cloudmap(vpc, service, container, service_name, fargate_service)

            # Monitoring
            self._set_monitoring(service_name, props)

            default_alarms = [
                {
                    "metric": aws_cloudwatch.Metric(
                        namespace="ECS/ContainerInsights",
                        metric_name="RunningTaskCount",
                        statistic=aws_cloudwatch.Statistic.SUM.value,
                        unit=aws_cloudwatch.Unit.COUNT,
                        period=Duration.minutes(1),
                    ),
                    "evaluation_periods": 1,
                    "threshold": 1,
                    "alarm_description": "WARNING RunningTaskCount is less than 1. Possible Unhealthy/Failing Container.",
                    "datapoints_to_alarm": 1,
                    "comparison_operator": aws_cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
                    "alarm_actions_disabled": False,
                },
            ]
            if environment == "prod":
                # conditionally add an alarm based on environment, as the lower environments don't get as much traffic
                # A more robust alarming mechanism is a topic for discussion in https://myjira.disney.com/browse/GUEST360-4401
                log_group_name = container.log_driver_config.options["awslogs-group"]
                period_in_minutes = 5
                default_alarms.append(create_alarm_for_incoming_log_traffic(log_group_name, period_in_minutes))

            self._set_cloudwatch_alarms(default_alarms, service_name)

        # Add suppressions
        NagSuppressions.add_resource_suppressions(
            self.ecs_execution_role.role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Grant Write creates wildcard policy kms:GenerateDataKey* and kms:ReEncrypt*",
                }
            ],
            True,
        )

    def _create_sidecar_container(self, sidecar, task_definition, default_ecr_repository, service_name, naming_prefix):
        if sidecar is not None:
            sidecar_port_mappings = [
                aws_cdk.aws_ecs.PortMapping(container_port=port) for port in set(sidecar["port_mappings"])
            ]

            if sidecar["registry_repository_name"] is None:
                sidecar_ecr_image = aws_cdk.aws_ecs.ContainerImage.from_ecr_repository(
                    repository=default_ecr_repository,
                    tag=sidecar["image_tag"],
                )
            else:
                sidecar_ecr_image = aws_cdk.aws_ecs.ContainerImage.from_registry(
                    name=sidecar["registry_repository_name"]
                )

            container_name = ContainerName(naming_prefix, f"{service_name}-sidecar").name()
            log_stream_prefix = f"{service_name}-sidecar-log"

            task_definition.add_container(
                StackName(naming_prefix, f"{service_name}-sidecar").name(),
                image=sidecar_ecr_image,
                container_name=container_name,
                environment=self.convert_env_to_str(sidecar["environment"]),
                logging=aws_cdk.aws_ecs.AwsLogDriver(stream_prefix=log_stream_prefix),
                port_mappings=sidecar_port_mappings,
            )

    def _set_cloudwatch_alarms(self, default_alarms: list, service_name: str):
        for cw_alarm in default_alarms:
            Guest360Alarm(
                self,
                f"{service_name}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )

    def set_ingress_rules(self, ingress):
        ingress_rules = [(cidr, port) for cidr in ingress["cidrs"] for port in ingress["ports"]]

        for ingress_rule in ingress_rules:
            self.sg_group.add_ingress_rule(
                peer=aws_cdk.aws_ec2.Peer.ipv4(ingress_rule[0]),
                connection=aws_cdk.aws_ec2.Port.tcp(ingress_rule[1]),
                description=f"ingress-{ingress_rule[0]}-{ingress_rule[1]}",
            )

    def _set_cloudmap(self, vpc, service, container, service_name, fargate_service):
        if "cloudmap" in service and service["cloudmap"]:
            cloudmap = aws_cdk.aws_servicediscovery.PrivateDnsNamespace(
                self, StackName(self.naming_prefix, "namespace").name(), name=self.naming_prefix, vpc=vpc
            )

            fargate_service.enable_cloud_map(
                cloud_map_namespace=cloudmap,
                container=container,
                name=service_name,
            )
            self.cloudmap[service_name] = cloudmap

    def convert_env_to_str(self, env: dict) -> Dict[str, str]:
        """Function to convert all values in dictionary to strings
        Args:
            env (dict): Environment variables for ECS task to convert to strings
        Returns:
            dict[str]: Correctly formated environment variables or None if there is not a env var
        """

        return {key: str(value) for key, value in env.items()} if env is not None else None

    def format_registry_name(self, repo_name: str, image_tag: str) -> str:
        """Function to correctly format the ECR Registry name given the repo name and tag
        Args:
            repo_name (str): Name of the ECR Repository
            image_tag (str): The Tag of the ECR Image to use
        Returns:
            str: Correctly formatted ECR Registry name
        """
        return f"ECR/{repo_name}:{image_tag}"

    def _set_monitoring(self, service_name: str, props: ECSConsumerProps):
        """Function to configure CloudWatch Metrics and set CloudWatch Guest360Alarm to ECS Services
        Args:
            service_name (str) : Name of the service to monitor
            props (ECSConsumerProps) : ECS Consumer Properties
        """
        if props.get("monitoring") is None:
            return

        monitoring_props = props["monitoring"]

        # Metric settings
        metrics_settings = {
            "dimensions_map": {
                "ServiceName": FargateServiceName(self.naming_prefix, f"{service_name}-FS").name(),
                "ClusterName": self.cluster.cluster_name,
            },
            "statistic": monitoring_props["metric_statistic"],
            "period": aws_cdk.Duration.minutes(monitoring_props["metric_period"]),
        }

        # Define CPU Utilization and Memory Utilization metrics
        cpu_utilization_metric = self.cluster.metric_cpu_utilization(**metrics_settings)
        memory_utilization_metric = self.cluster.metric_memory_utilization(**metrics_settings)

        # Alarm props
        cpu_alarm_props = monitoring_props["cpu_alarm"]
        memory_alarm_props = monitoring_props["memory_alarm"]

        # Update alarm props metric
        cpu_alarm_props["metric"] = cpu_utilization_metric
        memory_alarm_props["metric"] = memory_utilization_metric

        # Alarms props checks
        AlarmProps(cpu_alarm_props)
        AlarmProps(memory_alarm_props)

        # Alarms definition
        self.cpu_ecs_alarm = Guest360Alarm(self, f"{service_name}-CPUUtilization", props=cpu_alarm_props)
        self.memory_ecs_alarm = Guest360Alarm(self, f"{service_name}-MemoryUtilization", props=memory_alarm_props)

    def _get_ecr_repository(self, stack: aws_cdk.Stack, construct_id: str, environment: str, ecr_name: str):
        if environment == "local":
            ecr_name = ECRRepoName(self.naming_prefix, f"{ecr_name}-ECR-REPO").name()

        ecr_repository = Guest360ECRRepository.from_repository_name(
            stack, StackName(self.naming_prefix, f"{ecr_name}-ecr").name(), repository_name=ecr_name
        )

        # Grant our ecs execution role the ability to pull images from ECR
        if hasattr(self.ecs_execution_role, "role"):
            ecr_repository.grant_pull(self.ecs_execution_role.role)
        else:
            raise ValueError(
                "Construct with name"
                f"{construct_id}-roler-execution is already defined (Hint: Do not use the same for multi-region)"
            )

        return ecr_repository
