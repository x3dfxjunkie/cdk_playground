"""
Interface VPC Endpoint Construct
"""
import logging
import sys
from app.guest360_constructs.interface_vpc_endpoint import Guest360InterfaceVPCEndpoint
from app.guest360_constructs.security_group import Guest360SecurityGroup
from app.guest360_constructs.tests.utils import print_template_on_debug
from aws_cdk.aws_ec2 import InterfaceVpcEndpoint
from aws_cdk import assertions, Token, Stack

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


def test_vpc_endpoint_created(stack, constants):
    default_sg = Guest360SecurityGroup(stack, "sg", {"security_group_name": "test_sg"})
    val = Guest360InterfaceVPCEndpoint(
        stack,
        "testendpoint",
        props={"service": "com.foo.foo", "reachable_from_dgn": False, "security_groups": [default_sg]},
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSVPCENDPOINT"], 1)
    template.has_resource_properties(
        constants["AWSVPCENDPOINT"],
        {"SubnetIds": [subnet["id"] for subnet in val._nonroutable_subnets]},
    )
    template.has_resource_properties(constants["AWSVPCENDPOINT"], {"VpcEndpointType": "Interface"})
    template.has_resource_properties(constants["AWSVPCENDPOINT"], {"PrivateDnsEnabled": False})
    assert type(val.vpc_endpoint) == InterfaceVpcEndpoint
    assert Token.is_unresolved(val.vpc_endpoint_id)


def test_vpc_endpoint_created_open_false(stack, constants):
    default_sg = Guest360SecurityGroup(stack, "sg", {"security_group_name": "test_sg"})
    IVPCE = Guest360InterfaceVPCEndpoint(
        stack,
        "testendpoint",
        props={"service": "com.foo.foo", "reachable_from_dgn": False, "security_groups": [default_sg], "open": False},
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSVPCENDPOINT"], 1)
    template.has_resource_properties(
        constants["AWSVPCENDPOINT"],
        {"SubnetIds": [subnet["id"] for subnet in IVPCE._nonroutable_subnets]},
    )
    template.has_resource_properties(constants["AWSVPCENDPOINT"], {"VpcEndpointType": "Interface"})
    template.has_resource_properties(constants["AWSVPCENDPOINT"], {"PrivateDnsEnabled": False})
    template.resource_count_is(constants["AWSSECURITYGROUP"], 1)
    template.has_resource_properties(
        constants["AWSSECURITYGROUP"],
        {
            "SecurityGroupEgress": [
                {
                    "CidrIp": "255.255.255.255/32",
                    "Description": "Disallow all traffic",
                    "FromPort": 252,
                    "IpProtocol": "icmp",
                    "ToPort": 86,
                }
            ]
        },
    )
