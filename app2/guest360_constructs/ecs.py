"""
Defines base construct and defaults for Guest360's ECR Repositories
"""
import builtins
import logging
import os
from abc import ABC
from typing import Any, Dict, List, Optional, Sequence, TypedDict, Union

import aws_cdk
import jsii
import yaml
from app.guest360_constructs.security_group import Guest360SecurityGroup
from app.guest360_constructs.ecr_repository import Guest360ECRRepository
from app.src.reliability import utils
from aws_cdk import aws_cloudwatch, aws_ec2, aws_ecs, aws_iam
from cdk_nag import NagSuppressions
from constructs import Construct
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

logger = logging.getLogger(__name__)


@match_class_typing
class ECSClusterProps(TypedDict):
    """
    ECSCluster Properties
    """

    vpc: Union[
        str, jsii._reference_map.InterfaceDynamicProxy
    ]  # – The VPC id where your ECS instances will be running or your ENIs will be deployed. Default to Vpc in Environment
    container_insights: NotRequired[
        bool
    ]  # – Forced to True CloudWatch Container Insights will be enabled for the cluster. Override: True Container Insights will be disabled for this cluster.
    capacity: NotRequired[
        Union[aws_ecs.AddCapacityOptions, Dict[str, Any]]
    ]  # – The ec2 capacity to add to the cluster. Default: - no EC2 capacity will be added, you can use addCapacity to add capacity later.
    cluster_name: NotRequired[str]  # – The name for the cluster. Default: CloudFormation-generated name
    default_cloud_map_namespace: NotRequired[
        Union[aws_ecs.CloudMapNamespaceOptions, Dict[str, Any]]
    ]  # – The service discovery namespace created in this cluster. Default: - no service discovery namespace created, you can use addDefaultCloudMapNamespace to add a default service discovery namespace later.
    enable_fargate_capacity_providers: NotRequired[
        bool
    ]  # – Whether to enable Fargate Capacity Providers. Default: false
    execute_command_configuration: NotRequired[
        Union[aws_ecs.ExecuteCommandConfiguration, Dict[str, Any]]
    ]  # – The execute command configuration for the cluster. Default: - no configuration will be provided.


class Guest360ECSCluster(aws_ecs.Cluster):
    """
    Define a ECS Cluster with Guest360 defaults.
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *args,
        props: dict = None,
        **kwargs,
    ):
        # Check that props matches proper input structure
        self._props = props
        if props is None:
            self._props = {**kwargs}

        self._environment = scope.node.try_get_context("environment")
        self._region = aws_cdk.Stack.of(scope).region.lower()
        self._prefix = scope.node.try_get_context("prefix")
        self._naming_prefix = f"{self._prefix}-{construct_id}"
        self._override_props = {"container_insights": True}
        self._default_props = {}

        ECSClusterProps(self._props)
        # ensure vpc is converted from string to IVpc or environment vpc Ivpc is returned
        self._props["vpc"] = self._get_vpc(scope, construct_id, self._props.get("vpc"))
        # convert cluster_name into helix name if provided
        if self._props.get("cluster_name"):
            self._props["cluster_name"] = utils.ECSClusterName(self._naming_prefix, self._props["cluster_name"]).name()

        self._props = self._default_props | self._props | self._override_props

        logger.debug("Guest360ECSCluster: props=%s", self._props)
        super().__init__(
            scope=scope,
            id=construct_id,
            **self._props,
        )

    def _get_vpc(self, scope: Construct, construct_id: str, vpc_id: str) -> Optional[aws_ec2.IVpc]:
        vpc = aws_ec2.Vpc.from_lookup(scope, f"{construct_id}-vpc", vpc_id=vpc_id)
        return vpc


@match_class_typing
class FargateServiceProps(TypedDict):
    """
    FargateService Properties
    """

    cluster: Union[
        jsii._reference_map.InterfaceDynamicProxy, aws_ecs.Cluster
    ]  # – The name of the cluster that hosts the service. - Any because typedict cannot check instance types and is checked by underlying cdk
    task_definition: aws_ecs.TaskDefinition  # – The task definition to use for tasks in the service. [disable-awslint:ref-via-interface]
    subnet_type: str  # – subnet type from environment config (non-routable,private)
    service_name: str  # – The name of the service.

    security_groups: NotRequired[
        Union[Sequence[aws_ec2.ISecurityGroup], Dict[str, Any], None]
    ]  # – The security groups to associate with the service. If you do not specify a security group, a new security group is created. Default: - A new security group is created.
    platform_version: NotRequired[
        aws_ecs.FargatePlatformVersion
    ]  # – The platform version on which to run your service. If one is not specified, the LATEST platform version is used by default. For more information, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide. Default: Latest
    capacity_provider_strategies: NotRequired[
        Union[aws_ecs.CapacityProviderStrategy, Dict[str, Any]]
    ]  # – A list of Capacity Provider strategies used to place a service. Default: - undefined
    circuit_breaker: NotRequired[
        Union[aws_ecs.DeploymentCircuitBreaker, Dict[str, Any]]
    ]  # – Whether to enable the deployment circuit breaker. If this property is defined, circuit breaker will be implicitly enabled. Default: create a DeploymentCircuitBreaker
    cloud_map_options: NotRequired[
        Union[aws_ecs.CloudMapOptions, Dict[str, Any], None]
    ]  # – The options for configuring an Amazon ECS service to use service discovery. Default: - AWS Cloud Map service discovery is not enabled.
    deployment_alarms: NotRequired[
        Union[aws_ecs.DeploymentAlarmConfig, Dict[str, Any]]
    ]  # – The alarm(s) to monitor during deployment, and behavior to apply if at least one enters a state of alarm during the deployment or bake time. Default: - No alarms will be monitored during deployment.
    deployment_controller: NotRequired[
        Union[aws_ecs.DeploymentController, Dict[str, Any]]
    ]  # – Specifies which deployment controller to use for the service. For more information, see Amazon ECS Deployment Types Default: - Rolling update (ECS)
    desired_count: NotRequired[
        Union[int, float, None]
    ]  # – The desired number of instantiations of the task definition to keep running on the service. Default: - When creating the service, default is 1; when updating the service, default uses the current task number.
    enable_ecs_managed_tags: NotRequired[
        bool
    ]  # – Specifies whether to enable Amazon ECS managed tags for the tasks within the service. For more information, see Tagging Your Amazon ECS Resources Default: true
    enable_execute_command: NotRequired[
        bool
    ]  # – Whether to enable the ability to execute into a container. Default: - false
    health_check_grace_period: NotRequired[
        aws_cdk.Duration
    ]  # – The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started. Default: - defaults to 60 seconds if at least one load balancer is in-use and it is not already set
    max_healthy_percent: NotRequired[
        Union[int, float, None]
    ]  # – The maximum number of tasks, specified as a percentage of the Amazon ECS service’s DesiredCount value, that can run in a service during a deployment. Default: - 100 if daemon, otherwise 200
    min_healthy_percent: NotRequired[
        Union[int, float, None]
    ]  # – The minimum number of tasks, specified as a percentage of the Amazon ECS service’s DesiredCount value, that must continue to run and remain healthy during a deployment. Default: - 0 if daemon, otherwise 50
    propagate_tags: NotRequired[
        Union[aws_ecs.PropagatedTagSource, None]
    ]  # – Specifies whether to propagate the tags from the task definition or the service to the tasks in the service. Valid values are: PropagatedTagSource.SERVICE, PropagatedTagSource.TASK_DEFINITION or PropagatedTagSource.NONE Default: PropagatedTagSource.NONE
    service_connect_configuration: NotRequired[
        Union[aws_ecs.ServiceConnectProps, Dict[str, Any], None]
    ]  # – Configuration for Service Connect. Default: No ports are advertised via Service Connect on this service, and the service cannot make requests to other services via Service Connect.


class Guest360FargateService(aws_ecs.FargateService):
    """
    Define a ECS Fargate Service with Guest360 defaults.
    """

    @property
    def service_name(self) -> str:
        return self._props.get("service_name")

    @property
    def vpc_id(self) -> str:
        return self._vpc_id

    @property
    def vpc_subnets(self) -> aws_ec2.SubnetSelection:
        return self._props.get("vpc_subnets")

    @property
    def security_groups(self) -> Sequence[aws_ec2.SecurityGroup]:
        return self._props.get("security_groups")

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *args,
        props: dict = None,
        **kwargs,
    ):
        # Check that props matches proper input structure
        self._props = props
        if props is None:
            self._props = {**kwargs}

        self._environment = scope.node.try_get_context("environment")
        self._region = aws_cdk.Stack.of(scope).region.lower()
        self._prefix = scope.node.try_get_context("prefix")
        self._naming_prefix = f"{self._prefix}-{construct_id}"
        # set defaults, props, and overrides merge
        self._override_props = {"assign_public_ip": False}
        self._default_props = {
            "enable_ecs_managed_tags": True,
            "enable_execute_command": False,
        }

        FargateServiceProps(self._props)
        self._props["vpc_subnets"] = self._get_subnets(scope, construct_id, self._props["subnet_type"])
        # pop the custom key vpc_subnet_type out of dict
        self._props.pop("subnet_type", None)
        # get vpc_id from cluster
        self._vpc_id = self._props["cluster"].vpc
        # convert service_name into helix name if provided
        if self._props.get("service_name"):
            self._props["service_name"] = utils.FargateServiceName(
                self._naming_prefix, self._props["service_name"]
            ).name()

        self._props = self._default_props | self._props | self._override_props
        logger.debug("Guest360FargateService: props=%s", self._props)
        super().__init__(
            scope=scope,
            id=construct_id,
            **self._props,
        )

    def _get_subnets(self, scope: Construct, construct_id: str, subnet_type: str) -> aws_ec2.SubnetSelection:
        # This should be in a library but alas it is not so here we go
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/../configs/{self._environment}-environment.yaml",
            mode="r",
        ) as file:
            environment_config = yaml.safe_load(file)
        try:
            environment_subnets = environment_config["networking"][self._region]["subnets"][subnet_type]
            logger.debug("environment_subnets=%s", environment_subnets)
        except builtins.KeyError:
            raise builtins.AttributeError(f"subnet_type {subnet_type} not found in environment")
        service_subnets = aws_cdk.aws_ec2.SubnetSelection(
            subnets=[
                aws_cdk.aws_ec2.Subnet.from_subnet_id(
                    scope=scope, id=f"{construct_id}-{subnet_id}", subnet_id=subnet_id["id"]
                )
                for subnet_id in environment_subnets
            ]
        )
        return service_subnets


@match_class_typing
class FargateTaskDefinitionProps(TypedDict):
    """
    ecs task definition props
    """

    cpu: str  # – The number of cpu units used by the task. If you are using the EC2 launch type, this field is optional and any value can be used. If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 8192 (8 vCPU) - Available memory values: Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB) 16384 (16 vCPU) - Available memory values: Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB) Default: - CPU units are not specified.
    execution_role: Union[
        jsii._reference_map.InterfaceDynamicProxy, aws_iam.Role
    ]  # – The name of the IAM task execution role that grants the ECS agent permission to call AWS APIs on your behalf. The role will be used to retrieve container images from ECR and create CloudWatch log groups. Default: - An execution role will be automatically created if you use ECR images in your task definition.
    memory_mib: str  # – The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU) 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU) 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU) Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU) Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU) Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB) - Available cpu values: 8192 (8 vCPU) Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB) - Available cpu values: 16384 (16 vCPU) Default: - Memory used by task is not specified.
    task_role: Union[
        jsii._reference_map.InterfaceDynamicProxy, aws_iam.Role
    ]  # – The name of the IAM role that grants containers in the task permission to call AWS APIs on your behalf. Default: - A task role is automatically created for you.
    log_prefix: str  # - Log prefix to use for cloudwatch log stream

    ephemeral_storage_gib: NotRequired[
        Union[int, float, None]
    ]  # – The amount (in GiB) of ephemeral storage to be allocated to the task. Only supported in Fargate platform version 1.4.0 or later. Default: - Undefined, in which case, the task will receive 20GiB ephemeral storage.
    inference_accelerators: NotRequired[
        Sequence[Union[aws_ecs.InferenceAccelerator, Dict[str, Any]]]
    ]  # – The inference accelerators to use for the containers in the task. Not supported in Fargate. Default: - No inference accelerators.
    runtime_platform: NotRequired[
        Union[aws_ecs.RuntimePlatform, Dict[str, Any], None]
    ]  # – The operating system that your task definitions are running on. A runtimePlatform is supported only for tasks using the Fargate launch type. Default: - Undefined.
    family: NotRequired[
        str
    ]  # – The name of a family that this task definition is registered to. A family groups multiple versions of a task definition. Default: - Automatically generated name.
    proxy_configuration: NotRequired[
        aws_ecs.ProxyConfiguration
    ]  # – The configuration details for the App Mesh proxy. Default: - No proxy configuration.
    volumes: NotRequired[
        Sequence[Union[aws_ecs.Volume, Dict[str, Any]]]
    ]  # – The list of volume definitions for the task. For more information, see Task Definition Parameter Volumes. Default: - No volumes are passed to the Docker daemon on a container instance.


class Guest360FargateTaskDefinitionABC(ABC, aws_ecs.TaskDefinition):
    @staticmethod
    def convert_env_to_str(env: dict) -> Dict[str, str]:
        """Function to convert all values in dictionary to strings
        Args:
            env (dict): Environment variables for ECS task to convert to strings
        Returns:
            dict[str]: Correctly formated environment variables or None if there is not a env var
        """
        return {key: str(value) for key, value in env.items()} if env is not None else env

    def add_container(self, *args, **kwargs):
        # override the default add_container to force cw logging and other standards for containers
        if kwargs.get("logging") is None:
            kwargs["logging"] = aws_ecs.AwsLogDriver(stream_prefix=f"{self._log_prefix}")
        # now call the super class with the overriden parameters
        kwargs["environment"] = self.convert_env_to_str(kwargs.get("environment", {}))
        super().add_container(*args, **kwargs)


class Guest360FargateTaskDefinition(Guest360FargateTaskDefinitionABC):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *args,
        props: dict = None,
        **kwargs,
    ):
        # check that the props matches the proper input structure
        self._props = props
        if self._props is None:
            self._props = {**kwargs}

        self._environment = scope.node.try_get_context("environment")
        self._prefix = scope.node.try_get_context("prefix")
        self._naming_prefix = f"{self._prefix}-{construct_id}"
        self._region = aws_cdk.Stack.of(scope).region.lower()

        FargateTaskDefinitionProps(**self._props)
        self._log_prefix = self._props.pop("log_prefix", "")

        self._override_props = {
            "compatibility": aws_ecs.Compatibility.FARGATE,
            "network_mode": aws_ecs.NetworkMode.AWS_VPC,
        }
        self._default_props = {}

        self._props = self._default_props | self._props | self._override_props
        logger.debug("Guest360FargateTaskDefinition: _log_prefix=%s", self._log_prefix)
        logger.debug("Guest360FargateTaskDefinition: props=%s", self._props)
        super().__init__(
            scope=scope,
            id=construct_id,
            **self._props,
        )

        # nags
        NagSuppressions.add_resource_suppressions(
            self,
            [
                {
                    "id": "AwsSolutions-ECS2",
                    "reason": "Allow Environment Variables to be passed into ECS",
                }
            ],
            True,
        )


@match_class_typing
class FargateTaskDefinitionOtelProps(TypedDict):
    """
    ecs task definition props
    NOTE this has copied fields from FargateTaskDefinitionProps due to an issue with match_class_typing and subclassing.
        match_class_typing fails to do any typechecks the class is subclassed.
    """

    cpu: str  # – The number of cpu units used by the task. If you are using the EC2 launch type, this field is optional and any value can be used. If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 8192 (8 vCPU) - Available memory values: Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB) 16384 (16 vCPU) - Available memory values: Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB) Default: - CPU units are not specified.
    execution_role: Union[
        jsii._reference_map.InterfaceDynamicProxy, aws_iam.Role
    ]  # – The name of the IAM task execution role that grants the ECS agent permission to call AWS APIs on your behalf. The role will be used to retrieve container images from ECR and create CloudWatch log groups. Default: - An execution role will be automatically created if you use ECR images in your task definition.
    memory_mib: str  # – The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU) 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU) 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU) Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU) Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU) Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB) - Available cpu values: 8192 (8 vCPU) Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB) - Available cpu values: 16384 (16 vCPU) Default: - Memory used by task is not specified.
    task_role: Union[
        jsii._reference_map.InterfaceDynamicProxy, aws_iam.Role
    ]  # – The name of the IAM role that grants containers in the task permission to call AWS APIs on your behalf. Default: - A task role is automatically created for you.
    log_prefix: str  # - Log prefix to use for cloudwatch log stream

    ephemeral_storage_gib: NotRequired[
        Union[int, float, None]
    ]  # – The amount (in GiB) of ephemeral storage to be allocated to the task. Only supported in Fargate platform version 1.4.0 or later. Default: - Undefined, in which case, the task will receive 20GiB ephemeral storage.
    inference_accelerators: NotRequired[
        Sequence[Union[aws_ecs.InferenceAccelerator, Dict[str, Any]]]
    ]  # – The inference accelerators to use for the containers in the task. Not supported in Fargate. Default: - No inference accelerators.
    runtime_platform: NotRequired[
        Union[aws_ecs.RuntimePlatform, Dict[str, Any], None]
    ]  # – The operating system that your task definitions are running on. A runtimePlatform is supported only for tasks using the Fargate launch type. Default: - Undefined.
    family: NotRequired[
        str
    ]  # – The name of a family that this task definition is registered to. A family groups multiple versions of a task definition. Default: - Automatically generated name.
    proxy_configuration: NotRequired[
        aws_ecs.ProxyConfiguration
    ]  # – The configuration details for the App Mesh proxy. Default: - No proxy configuration.
    volumes: NotRequired[
        Sequence[Union[aws_ecs.Volume, Dict[str, Any]]]
    ]  # – The list of volume definitions for the task. For more information, see Task Definition Parameter Volumes. Default: - No volumes are passed to the Docker daemon on a container instance.
    otel_repository_name: NotRequired[str]  # - override default otel repository name
    otel_tag: NotRequired[str]  # - override default otel image tag
    otel_ports: NotRequired[list[int]]  # - override list of otel ports
    otel_environment: NotRequired[dict]  # - dictionary of environment variables for otel


class Guest360FargateTaskDefinitionOtel(Guest360FargateTaskDefinition):
    otel_repository_name = "otel/otel_sidecar"
    otel_tag = "v0.31.x"
    otel_ports = [55679, 4317, 13133]

    def __init__(self, scope, construct_id, *args, props: dict = None, **kwargs):
        # check that the props matches the proper input structure
        props = props
        if props is None:
            props = {**kwargs}

        self._environment = scope.node.try_get_context("environment")
        self._prefix = scope.node.try_get_context("prefix")
        self._naming_prefix = f"{self._prefix}-{construct_id}"
        self._region = aws_cdk.Stack.of(scope).region.lower()
        # FargateTaskDefinitionOtelProps(props)
        self.otel_environment = {"AWS_REGION": self._region}
        # populate the default values if not provided and pop off of temporary props to send to super
        otel_keys = ["otel_repository_name", "otel_tag", "otel_ports", "otel_environment"]
        otel_props = {key: props.pop(key, getattr(self, key)) for key in otel_keys}

        super().__init__(scope, construct_id, *args, **kwargs)
        # add the otel_props now that the super call has created self._props
        self._props.update(otel_props)
        self._props["otel_envionment"] = self.otel_environment | self._props.get("otel_environment", {})
        logger.debug("Guest360FargateTaskDefinitionOtel props=%s", self._props)

        ### Creating OTEL Image, which will be used in every service ###
        otel_sidecar_portmappings = [
            aws_cdk.aws_ecs.PortMapping(container_port=port) for port in self._props["otel_ports"]
        ]

        otel_repository = Guest360ECRRepository.from_repository_name(
            self,
            "otel-repository",
            repository_name=f"guest360/{self._props['otel_repository_name']}",
        )

        otel_image = aws_cdk.aws_ecs.ContainerImage.from_ecr_repository(
            repository=otel_repository, tag=self._props["otel_tag"]
        )

        self.add_container(
            "otel-sidecar",
            image=otel_image,
            container_name="otel-adot-collector",
            environment=self.convert_env_to_str(self._props["otel_environment"]),
            port_mappings=[aws_ecs.PortMapping(container_port=port) for port in self._props["otel_ports"]],
        )
