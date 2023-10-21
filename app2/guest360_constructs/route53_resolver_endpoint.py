"""
Defines base construct and defaults for Route53 DNS Resolver Inbound Endpoint
"""
import aws_cdk, os, yaml
from typing import TypedDict, Dict, Any
from typing_extensions import NotRequired
from app.guest360_constructs.construct_360 import Construct360
from aws_cdk import CfnTag
from strongtyping.strong_typing import match_class_typing
import aws_cdk.aws_route53resolver as route53resolver
from app.src.reliability.utils import StackName


@match_class_typing
class Route53ResolverEndpointProps(TypedDict):
    name: str
    security_group_ids: list[str]
    resolver_config_tag: NotRequired[
        str
    ]  # - will look up static ips in the environment config instead of just using the disney addressable ips
    tags: NotRequired[list[Dict[str, Any]]]

    # the following items are hard coded for now, but may be allowed in the future
    # direction: str  INBOUND Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:. - INBOUND : allows DNS queries to your VPC from your network - OUTBOUND : allows DNS queries from your VPC to your network
    # preferred_instance_type: NotRequired[str] #AWS::Route53Resolver::ResolverEndpoint.PreferredInstanceType.
    # resolver_endpoint_type: NotRequired[str] # The Resolver endpoint IP address type


class Guest360Route53ResolverEndpoint(Construct360):
    """ """

    def __init__(self, scope: Construct360, construct_id: str, props: Route53ResolverEndpointProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        Route53ResolverEndpointProps(props)
        stack = aws_cdk.Stack.of(self)
        environment = self.node.try_get_context("environment")
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/../configs/{environment}-environment.yaml",
            mode="r",
            encoding="utf-8",
        ) as file:
            environment_config = yaml.safe_load(file)
            if props.get("resolver_config_tag") is None:
                subnets_config = environment_config["networking"][stack.region]["subnets"]["private"]
                ip_addresses = [
                    route53resolver.CfnResolverEndpoint.IpAddressRequestProperty(subnet_id=subnet["id"])
                    for subnet in subnets_config
                ]
            elif (
                props.get("resolver_config_tag") is not None
                and environment_config["networking"][stack.region].get("resolvers") is not None
                and environment_config["networking"][stack.region]["resolvers"].get(props["resolver_config_tag"])
                is not None
            ):
                val = props.pop("resolver_config_tag")
                subnets_config = environment_config["networking"][stack.region]["resolvers"][val]
                ip_addresses = [
                    route53resolver.CfnResolverEndpoint.IpAddressRequestProperty(
                        subnet_id=subnet["SubnetId"], ip=subnet["Ip"]
                    )
                    for subnet in subnets_config
                ]
            elif environment_config["networking"][stack.region].get("resolvers") is None:
                raise ValueError("Resolver information is not set up in the environment configuration file")
            else:
                raise ValueError("resolver_config_tag not found")

        if props.get("tags") is not None:
            props["tags"] = [CfnTag(**tag) for tag in props["tags"]]
        self.props_default = {"direction": "INBOUND", "ip_addresses": ip_addresses, "resolver_endpoint_type": "IPV4"}
        self.props_merged = self.props_default | props
        self._route53_resolver_endpoint = route53resolver.CfnResolverEndpoint(self, construct_id, **self.props_merged)

    @property
    def resolver_endpoint_arn(self):
        return self._route53_resolver_endpoint.attr_arn
