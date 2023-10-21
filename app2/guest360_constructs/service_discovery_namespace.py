"""
Defines base construct and defaults for aws cloud map
"""
import aws_cdk
from typing import TypedDict
from app.guest360_constructs.construct_360 import Construct360
from aws_cdk import aws_servicediscovery as service_discovery
from aws_cdk.aws_servicediscovery import PrivateDnsNamespace
from strongtyping.strong_typing import match_class_typing
from app.src.reliability.utils import StackName


@match_class_typing
class ServiceDiscoveryNamespaceRule(TypedDict):
    """
    :prop name => name of the namespace
    """

    name: str


class Guest360ServiceDiscoveryNamespace(Construct360):
    """
    Also referred to as aws cloud map - AWS Cloud Map is a fully managed service that you can use to create and maintain a map of the backend services and resources that your applications depend on.
    This creates a hosted zone that allows services to talk to each other with local aliases
    Guest360ServiceDiscoveryNamespace(stack, "<construct_id>", {"name": "<zone_name>})

    """

    def __init__(self, scope: Construct360, construct_id: str, props: ServiceDiscoveryNamespaceRule, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        ServiceDiscoveryNamespaceRule(props)
        self.naming_prefix = f"{self._prefix}-{construct_id}"
        props["name"] = f'{self.naming_prefix}-{props["name"]}'
        self._vpc = aws_cdk.aws_ec2.Vpc.from_lookup(
            self, StackName(self.naming_prefix, "vpc").name(), vpc_id=self._vpc_id
        )
        self.props_default = {"vpc": self._vpc}
        self.props_merged = self.props_default | props
        self._namespace = PrivateDnsNamespace(self, construct_id, **self.props_merged)

    @property
    def namespace_hosted_zone_id(self):
        return self._namespace.namespace_hosted_zone_id

    @property
    def namespace(self):
        return self._namespace

    @property
    def private_dns_namespace_name(self):
        return self._namespace.private_dns_namespace_name

    @classmethod
    def from_lookup_by_name(cls, *args, **kwargs) -> PrivateDnsNamespace:
        """
        namespace_arn (str)  Namespace ARN for the Namespace.
        namespace_id (str)  Namespace Id for the Namespace.
        namespace_name (str)  A name for the Namespace.
        """
        return service_discovery.namespace.from_private_dns_namespace_attributes(*args, **kwargs)
