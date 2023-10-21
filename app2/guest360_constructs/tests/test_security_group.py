"""
Security Group Construct
"""
import pytest
import logging
import sys
import os
import yaml
import strongtyping
from aws_cdk.aws_ec2 import Vpc
from app.guest360_constructs.security_group import Guest360SecurityGroup
from app.guest360_constructs.tests.utils import print_template_on_debug

from aws_cdk import App, Stack, assertions, Token

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_CONTEXT = {"prefix": "lst-test_sg_something", "environment": "latest"}
ENVIRONMENT = {"region": "us-east-1", "account": "123456789"}
AWSSECURITYGROUP = "AWS::EC2::SecurityGroup"
DESCRIPTIONS_UDP1 = "from 10.171.98.0/23:443-443"
DESCRIPTIONS_UDP2 = "from 10.0.0.0/8:UDP 443-443"
DESCRIPTIONS_TCP1 = "from 10.255.0.0/16:443-443"

with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/../../configs/constants.yaml",
    mode="r",
    encoding="utf-8",
) as file:
    INTERNAL_IPS = yaml.safe_load(file)["disney_internal_cidr_blocks"]["ipv4"]
with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/../../configs/latest-environment.yaml",
    mode="r",
    encoding="utf-8",
) as file:
    VPC_CIDRS = yaml.safe_load(file)["networking"]["us-east-1"]["vpc"]["cidr"]
SPECIFIC_CIDR = f"{str(10)}.0.0.0/{str(8)}"


@pytest.fixture(name="stack")
def fixture_stack():
    app = App(context=TEST_CONTEXT)
    stack = Stack(app, env=ENVIRONMENT)
    yield stack


def test_security_group_created(stack):
    val = Guest360SecurityGroup(stack, "TestSecurityGroup", {"security_group_name": "foo"})
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(AWSSECURITYGROUP, 1)
    assert Token.is_unresolved(val.security_group_id)


def test_from_lookup_by_name(stack):
    from_security_group_name = Guest360SecurityGroup.from_lookup_by_name(
        stack, "testid", "foo", Vpc.from_lookup(stack, "vpc-123456")
    )
    assert from_security_group_name.security_group_id == "sg-12345678"


def test_from_lookup_by_id(stack):
    from_security_group_id = Guest360SecurityGroup.from_lookup_by_id(stack, "testid", "sg-12345678")
    assert from_security_group_id.security_group_id == "sg-12345678"


def test_security_group_ingress_bad_protocol(stack):
    with pytest.raises(ValueError) as exc:
        obj = {
            "security_group_name": "foo",
            "ingress_rules": [{"protocol": "HOPOPT", "from_port": 443, "to_port": 443, "vpc_only": True}],
        }
        Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    assert "Protocol not supported." in str(exc.value)


def test_security_group_ingress_bad_props(stack):
    with pytest.raises(strongtyping.strong_typing_utils.TypeMisMatch):
        obj = {
            "security_group_name": "foo",
            "ingress_rules": [{"protocol": "HOPOPT", "from_port": 443, "vpc_only": True}],
        }
        Guest360SecurityGroup(stack, "TestSecurityGroup", obj)


def test_internal_security_group_count(stack):
    assert len(INTERNAL_IPS) == 3


@pytest.mark.parametrize("traffic", ["ingress", "egress"])
def test_security_group_specific_cidr(stack, traffic):
    obj = {
        "security_group_name": "foo",
        f"{traffic}_rules": [{"protocol": "UDP", "from_port": 443, "to_port": 443, "cidr_block": SPECIFIC_CIDR}],
    }
    test = {
        f"SecurityGroup{traffic.capitalize()}": [
            {
                "CidrIp": SPECIFIC_CIDR,
                "Description": DESCRIPTIONS_UDP2,
                "FromPort": 443,
                "IpProtocol": "udp",
                "ToPort": 443,
            }
        ]
    }
    Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.has_resource_properties(AWSSECURITYGROUP, test)


def test_security_group_ingress_test_bad_cidr(stack):
    with pytest.raises(RuntimeError) as ex:
        obj = {
            "security_group_name": "foo",
            "ingress_rules": [{"protocol": "UDP", "from_port": 443, "to_port": 443, "cidr_block": "1000.0.0.0/8"}],
        }
        Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    assert 'Invalid IPv4 CIDR: "1000.0.0.0/8"' in str(ex.value)


@pytest.mark.parametrize("traffic", ["ingress", "egress"])
def test_security_group_one_rule(stack, traffic):
    obj = {
        "security_group_name": "foo",
        f"{traffic}_rules": [{"protocol": "TCP", "from_port": 443, "to_port": 443, "vpc_only": True}],
    }
    test = {
        f"SecurityGroup{traffic.capitalize()}": [
            {
                "CidrIp": VPC_CIDRS[0],
                "Description": DESCRIPTIONS_UDP1,
                "FromPort": 443,
                "IpProtocol": "tcp",
                "ToPort": 443,
            },
            {
                "CidrIp": VPC_CIDRS[1],
                "Description": DESCRIPTIONS_TCP1,
                "FromPort": 443,
                "IpProtocol": "tcp",
                "ToPort": 443,
            },
        ]
    }
    Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.has_resource_properties(AWSSECURITYGROUP, test)


@pytest.mark.parametrize("traffic", ["ingress", "egress"])
def test_security_group_two_rules(stack, traffic):
    obj = {
        "security_group_name": "foo",
        f"{traffic}_rules": [
            {"protocol": "TCP", "from_port": 443, "to_port": 443, "vpc_only": True},
            {"protocol": "TCP", "from_port": 80, "to_port": 80, "vpc_only": True},
        ],
    }
    test = {
        f"SecurityGroup{traffic.capitalize()}": [
            {
                "CidrIp": VPC_CIDRS[0],
                "Description": DESCRIPTIONS_UDP1,
                "FromPort": 443,
                "IpProtocol": "tcp",
                "ToPort": 443,
            },
            {
                "CidrIp": VPC_CIDRS[1],
                "Description": DESCRIPTIONS_TCP1,
                "FromPort": 443,
                "IpProtocol": "tcp",
                "ToPort": 443,
            },
            {
                "CidrIp": VPC_CIDRS[0],
                "Description": "from 10.171.98.0/23:80-80",
                "FromPort": 80,
                "IpProtocol": "tcp",
                "ToPort": 80,
            },
            {
                "CidrIp": VPC_CIDRS[1],
                "Description": "from 10.255.0.0/16:80-80",
                "FromPort": 80,
                "IpProtocol": "tcp",
                "ToPort": 80,
            },
        ]
    }
    Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.has_resource_properties(AWSSECURITYGROUP, test)


def test_security_group_egress_bad_protocol(stack):
    with pytest.raises(ValueError) as exc:
        obj = {
            "security_group_name": "foo",
            "egress_rules": [{"protocol": "OPTHOP", "from_port": 443, "to_port": 443, "vpc_only": True}],
        }
        Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    assert "Protocol not supported." in str(exc.value)


def test_security_group_egress_bad_props(stack):
    with pytest.raises(Exception):
        obj = {
            "security_group_name": "foo",
            "egress_rules": [{"protocol": "OPTHOP", "from_port": 443, "vpc_only": True}],
        }
        Guest360SecurityGroup(stack, "TestSecurityGroup", obj)


@pytest.mark.parametrize("traffic", ["egress", "ingress"])
def test_security_group_bad_ipv4_port(stack, traffic):
    with pytest.raises(ValueError) as ex:
        obj = {
            "security_group_name": "foo",
            f"{traffic}_rules": [{"protocol": "TCP", "from_port": 443, "to_port": 65536, "vpc_only": True}],
        }
        Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    assert "Ports out of range." in str(ex.value)


@pytest.mark.parametrize("traffic", ["ingress", "egress"])
def test_security_group_udp_port(stack, traffic):
    obj = {
        "security_group_name": "foo",
        f"{traffic}_rules": [{"protocol": "UDP", "from_port": 443, "to_port": 443, "vpc_only": True}],
    }
    test = {
        f"SecurityGroup{traffic.capitalize()}": [
            {
                "CidrIp": VPC_CIDRS[0],
                "Description": "from 10.171.98.0/23:UDP 443-443",
                "FromPort": 443,
                "IpProtocol": "udp",
                "ToPort": 443,
            },
            {
                "CidrIp": VPC_CIDRS[1],
                "Description": "from 10.255.0.0/16:UDP 443-443",
                "FromPort": 443,
                "IpProtocol": "udp",
                "ToPort": 443,
            },
        ]
    }
    Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.has_resource_properties(AWSSECURITYGROUP, test)


@pytest.mark.parametrize("traffic", ["egress", "ingress"])
def test_security_group_icmp_port(stack, traffic):
    obj = {
        "security_group_name": "foo",
        f"{traffic}_rules": [{"protocol": "ICMP", "from_port": -1, "to_port": -1, "vpc_only": True}],
    }
    test = {
        f"SecurityGroup{traffic.capitalize()}": [
            {
                "CidrIp": VPC_CIDRS[0],
                "Description": "from 10.171.98.0/23:ICMP Type 8",
                "FromPort": 8,
                "IpProtocol": "icmp",
                "ToPort": -1,
            },
            {
                "CidrIp": VPC_CIDRS[1],
                "Description": "from 10.255.0.0/16:ICMP Type 8",
                "FromPort": 8,
                "IpProtocol": "icmp",
                "ToPort": -1,
            },
        ]
    }
    Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.has_resource_properties(AWSSECURITYGROUP, test)


@pytest.mark.parametrize("traffic", ["egress", "ingress"])
def test_security_group_internal_cidrs(stack, traffic):
    obj = {
        "security_group_name": "foo",
        f"{traffic}_rules": [{"protocol": "UDP", "from_port": 443, "to_port": 443, "all_internal": True}],
    }
    test = {
        f"SecurityGroup{traffic.capitalize()}": [
            {
                "CidrIp": INTERNAL_IPS[0],
                "Description": DESCRIPTIONS_UDP2,
                "FromPort": 443,
                "IpProtocol": "udp",
                "ToPort": 443,
            },
            {
                "CidrIp": INTERNAL_IPS[1],
                "Description": "from 192.168.0.0/16:UDP 443-443",
                "FromPort": 443,
                "IpProtocol": "udp",
                "ToPort": 443,
            },
            {
                "CidrIp": INTERNAL_IPS[2],
                "Description": "from 172.16.0.0/12:UDP 443-443",
                "FromPort": 443,
                "IpProtocol": "udp",
                "ToPort": 443,
            },
        ]
    }
    Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.has_resource_properties(AWSSECURITYGROUP, test)


def test_security_group_egress_bad_rule(stack):
    with pytest.raises(ValueError) as ex:
        obj = {
            "security_group_name": "foo",
            "ingress_rules": [{"protocol": "OPTHOP", "from_port": 443, "to_port": 65536, "vpc_only": True}],
        }
        Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    assert "Ports out of range." in str(ex.value)


def test_security_group_ingress_egress(stack):
    obj = {
        "security_group_name": "foo",
        "ingress_rules": [{"protocol": "TCP", "from_port": 443, "to_port": 443, "vpc_only": True}],
        "egress_rules": [{"protocol": "TCP", "from_port": 443, "to_port": 443, "vpc_only": True}],
    }
    test = {
        "SecurityGroupIngress": [
            {
                "CidrIp": VPC_CIDRS[0],
                "Description": DESCRIPTIONS_UDP1,
                "FromPort": 443,
                "IpProtocol": "tcp",
                "ToPort": 443,
            },
            {
                "CidrIp": VPC_CIDRS[1],
                "Description": DESCRIPTIONS_TCP1,
                "FromPort": 443,
                "IpProtocol": "tcp",
                "ToPort": 443,
            },
        ],
        "SecurityGroupEgress": [
            {
                "CidrIp": VPC_CIDRS[0],
                "Description": DESCRIPTIONS_UDP1,
                "FromPort": 443,
                "IpProtocol": "tcp",
                "ToPort": 443,
            },
            {
                "CidrIp": VPC_CIDRS[1],
                "Description": DESCRIPTIONS_TCP1,
                "FromPort": 443,
                "IpProtocol": "tcp",
                "ToPort": 443,
            },
        ],
    }
    Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.has_resource_properties(AWSSECURITYGROUP, test)


def test_security_group_missing_key_to_port(stack):
    with pytest.raises(strongtyping.strong_typing_utils.TypeMisMatch):
        obj = {
            "security_group_name": "foo",
            "ingress_rules": [{"protocol": "TCP", "from_port": 443, "vpc_only": True}],
            "egress_rules": [{"protocol": "TCP", "from_port": 443, "to_port": 443, "vpc_only": True}],
        }
        Guest360SecurityGroup(stack, "TestSecurityGroup", obj)


def test_security_group_missing_key_to_protocol(stack):
    with pytest.raises(strongtyping.strong_typing_utils.TypeMisMatch):
        obj = {
            "security_group_name": "foo",
            "ingress_rules": [{"protocol": "TCP", "from_port": 443, "to_port": 443, "vpc_only": True}],
            "egress_rules": [{"from_port": 443, "to_port": 443, "vpc_only": True}],
        }
        Guest360SecurityGroup(stack, "TestSecurityGroup", obj)
