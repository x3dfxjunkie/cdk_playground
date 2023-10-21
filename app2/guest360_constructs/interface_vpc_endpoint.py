"""
Defines base construct and defaults for interface vpc_endpoint
"""
import os
from typing import List, TypedDict

from aws_cdk.aws_ec2 import InterfaceVpcEndpoint, Vpc, SubnetSelection, Subnet, InterfaceVpcEndpointService
from app.src.reliability.utils import StackName
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.security_group import Guest360SecurityGroup
from aws_cdk import Fn


@match_class_typing
class InterfaceVPCEndpointProps(TypedDict):
    """
    :prop service - The name of the endpoint service that we are connecting too
    ;prop reachable_from_dgn - Whether other services on the DGN need to find this service
    :prop security_groups - The security groups to associate with this interface VPC endpoint.
    :prop lookup_supported_azs - Limit to only those availability zones where the endpoint service can be created. Setting this to ‘true’ requires a lookup to be performed at synthesis time. Account and region must be set on the containing stack for this to work. Default: false
    :prop open - Whether to automatically allow VPC traffic to the endpoint. If enabled, all traffic to the endpoint from within the VPC will be automatically allowed. This is done based on the VPC’s CIDR range. Default: true
    :prop private_dns_enabled - Whether to associate a private hosted zone with the specified VPC. This allows you to make requests to the service using its default DNS hostname. Default: set by the instance of IInterfaceVpcEndpointService, or true if not defined by the instance of IInterfaceVpcEndpointService
    :prop security_groups - The security groups to associate with this interface VPC endpoint.
    """

    service: str
    reachable_from_dgn: bool
    security_groups: List[Guest360SecurityGroup]
    lookup_supported_azs: NotRequired[bool]
    open: NotRequired[bool]
    private_dns_enabled: NotRequired[bool]


class Guest360InterfaceVPCEndpoint(Construct360):
    """ """

    @property
    def vpc_endpoint(self):
        return self._vpc_endpoint

    @property
    def vpc_endpoint_id(self):
        return self._vpc_endpoint.vpc_endpoint_id

    @property
    def vpc_endpoint_url(self):
        return Fn.select(1, Fn.split(":", Fn.select(0, self._vpc_endpoint.vpc_endpoint_dns_entries), assumed_length=2))

    def __init__(self, scope: Construct360, construct_id: str, props: InterfaceVPCEndpointProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        InterfaceVPCEndpointProps(props)
        self.naming_prefix = f"{self._prefix}-{construct_id}"
        self.props_default = {"lookup_supported_azs": False}
        subnets = self._routable_subnets if props.pop("reachable_from_dgn") else self._nonroutable_subnets
        self.props_mandatory = {
            "vpc": Vpc.from_lookup(
                self,
                StackName(self.naming_prefix, "vpc").name(),
                vpc_id=self._vpc_id,
            ),
            "subnets": SubnetSelection(
                subnets=[Subnet.from_subnet_id(self, subnet["id"], subnet_id=subnet["id"]) for subnet in subnets]
            ),
            "security_groups": [sg.security_group for sg in props["security_groups"]],
            "service": InterfaceVpcEndpointService(props["service"]),
        }
        self.props_merged = self.props_default | props | self.props_mandatory
        self._vpc_endpoint = InterfaceVpcEndpoint(self, construct_id, **self.props_merged)
