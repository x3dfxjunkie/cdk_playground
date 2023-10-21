"""
Interface VPC Endpoint Construct
"""
import logging
import sys
from app.guest360_constructs.vpc_endpoint_service import Guest360VPCEndpointService
from app.guest360_constructs.tests.utils import print_template_on_debug
from aws_cdk.aws_ec2 import VpcEndpointService, Vpc, IpAddresses
from aws_cdk.aws_iam import ArnPrincipal

import aws_cdk.aws_elasticloadbalancingv2 as elbv2
from aws_cdk import assertions, Token, Stack

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TESTCIDRBLOCK = f"172.16{'.0'*2}/16"


def test_vpc_endpoint_service_created(singlestack, constants):
    VPC = Vpc(singlestack, "TestVPC", ip_addresses=IpAddresses.cidr(TESTCIDRBLOCK))
    load_balancer = elbv2.NetworkLoadBalancer(singlestack, "TestNLB", vpc=VPC)
    val = Guest360VPCEndpointService(
        singlestack,
        "testendpointservice",
        props={"allowed_principals": [], "vpc_endpoint_service_load_balancers": [load_balancer]},
    )
    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSVPCENDPOINTSVC"], 1)

    assert type(val.vpc_endpoint_service) == VpcEndpointService
    assert Token.is_unresolved(val.vpc_endpoint_service_id)
    assert type(Stack.of(singlestack).resolve(val.vpc_endpoint_service_name)) == dict


def test_vpc_endpoint_service_pass_two_lb(singlestack, constants):
    VPC = Vpc(singlestack, "TestVPC", ip_addresses=IpAddresses.cidr(TESTCIDRBLOCK))
    load_balancer_1 = elbv2.NetworkLoadBalancer(singlestack, "TestNLB1", vpc=VPC)
    load_balancer_2 = elbv2.NetworkLoadBalancer(singlestack, "TestNLB2", vpc=VPC)
    val = Guest360VPCEndpointService(
        singlestack,
        "testendpointservice",
        props={
            "vpc_endpoint_service_load_balancers": [load_balancer_1, load_balancer_2],
        },
    )
    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSVPCENDPOINTSVC"], 1)

    assert type(val.vpc_endpoint_service) == VpcEndpointService
    assert Token.is_unresolved(val.vpc_endpoint_service_id)
    assert type(Stack.of(singlestack).resolve(val.vpc_endpoint_service_name)) == dict


def test_vpc_endpoint_service_pass_allowed_principal(singlestack, constants):
    VPC = Vpc(singlestack, "TestVPC", ip_addresses=IpAddresses.cidr(TESTCIDRBLOCK))
    load_balancer_1 = elbv2.NetworkLoadBalancer(singlestack, "TestNLB1", vpc=VPC)
    load_balancer_2 = elbv2.NetworkLoadBalancer(singlestack, "TestNLB2", vpc=VPC)
    val = Guest360VPCEndpointService(
        singlestack,
        "testendpointservice",
        props={
            "allowed_principals": [ArnPrincipal("arn:aws:iam::123456789012:root")],
            "vpc_endpoint_service_load_balancers": [load_balancer_1, load_balancer_2],
        },
    )
    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSVPCENDPOINTSVC"], 1)

    assert type(val.vpc_endpoint_service) == VpcEndpointService
    assert Token.is_unresolved(val.vpc_endpoint_service_id)
    assert type(Stack.of(singlestack).resolve(val.vpc_endpoint_service_name)) == dict


def test_vpc_endpoint_service_pass_all_params(singlestack, constants):
    VPC = Vpc(singlestack, "TestVPC", ip_addresses=IpAddresses.cidr(TESTCIDRBLOCK))
    load_balancer_1 = elbv2.NetworkLoadBalancer(singlestack, "TestNLB1", vpc=VPC)
    load_balancer_2 = elbv2.NetworkLoadBalancer(singlestack, "TestNLB2", vpc=VPC)
    val = Guest360VPCEndpointService(
        singlestack,
        "testendpointservice",
        props={
            "allowed_principals": [ArnPrincipal("arn:aws:iam::123456789012:root")],
            "acceptance_required": False,
            "vpc_endpoint_service_load_balancers": [load_balancer_1, load_balancer_2],
        },
    )
    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSVPCENDPOINTSVC"], 1)

    assert type(val.vpc_endpoint_service) == VpcEndpointService
    assert Token.is_unresolved(val.vpc_endpoint_service_id)
    assert type(Stack.of(singlestack).resolve(val.vpc_endpoint_service_name)) == dict
