"""
Defines base construct and defaults for vpc_endpoint service
"""
from typing import List, TypedDict

# from aws_cdk import Duration, aws_ec2
from aws_cdk.aws_ec2 import VpcEndpointService
from aws_cdk.aws_elasticloadbalancingv2 import NetworkLoadBalancer
from aws_cdk.aws_iam import ArnPrincipal
from app.src.reliability.utils import StackName
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired
from app.guest360_constructs.construct_360 import Construct360
from aws_cdk import CfnOutput, Stack, Fn


@match_class_typing
class VPCEndpointServiceProps(TypedDict):
    """
    :prop vpc_endpoint_service_load_balancers - One or more load balancers to host the VPC Endpoint Service
    :prop acceptance_required - Whether requests from service consumers to connect to the service through an endpoint must be accepted. Default: true
    :prop allowed_principals – IAM users, IAM roles, or AWS accounts to allow inbound connections from. These principals can connect to your service using VPC endpoints. Takes a list of one or more ArnPrincipal. Default: - no principals
    :prop contributor_insights - Not supported in cdk version 2.93.0 – Indicates whether to enable the built-in Contributor Insights rules provided by AWS PrivateLink. Default: false
    """

    vpc_endpoint_service_load_balancers: List[NetworkLoadBalancer]
    allowed_principals: NotRequired[List[ArnPrincipal]]
    acceptance_req: NotRequired[bool]


class Guest360VPCEndpointService(Construct360):
    """Guest360 Construct for VPC Endpoint service
        Defines base construct and defaults for VPCEndpointService
        New class expects list of load balancers, allowed principals in the props
        Will be leveraging the methods available in cdk lib for VPCEndpointService  construct
    https://myjira.disney.com/browse/GUEST360-4085
    """

    @property
    def vpc_endpoint_service(self):
        return self._vpc_endpoint_service

    @property
    def vpc_endpoint_service_id(self):
        return self._vpc_endpoint_service.vpc_endpoint_service_id

    @property
    def vpc_endpoint_service_name(self):
        return self._vpc_endpoint_service.vpc_endpoint_service_name

    def __init__(self, scope: Construct360, construct_id: str, props: VPCEndpointServiceProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        VPCEndpointServiceProps(props)
        prefix = self.node.try_get_context("prefix")
        self.naming_prefix = f"{prefix}-{construct_id}"
        self.props_default = {
            "acceptance_required": True,
            "allowed_principals": [],
        }
        self.props_mandatory = {
            "vpc_endpoint_service_load_balancers": list(props["vpc_endpoint_service_load_balancers"]),
        }
        self.props_merged = self.props_default | props | self.props_mandatory
        self._vpc_endpoint_service = VpcEndpointService(self, construct_id, **self.props_merged)
