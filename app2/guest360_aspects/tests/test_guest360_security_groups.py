import json
import logging
import sys
import aws_cdk
from app.guest360_aspects.guest360_nagpack import Guest360Rules
from aws_cdk.assertions import Annotations, Template

LOGGER = logging.getLogger(__name__)
STREAMHANDLER = logging.StreamHandler(sys.stdout)
FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
STREAMHANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(STREAMHANDLER)
CFSTACKPATH = "/TestStack/TestPHZ/Resource"
INGRESS = "SecurityGroupIngress"

def test_aspect_default_params(stack, constants):
    """Test with a security group that should be valid."""

    vpc = aws_cdk.aws_ec2.Vpc(
        stack, "TestVPC", ip_addresses=aws_cdk.aws_ec2.IpAddresses.cidr(constants["TESTCIDRBLOCK"])
    )

    default_sg = aws_cdk.aws_ec2.SecurityGroup(
        scope=stack,
        id="TestSecurityGroup",
        vpc=vpc,
        allow_all_outbound=True, #NOSONAR
        description="Test SG",
    )

    # Create a valid security group ingress rule
    default_sg.add_ingress_rule(
        peer=aws_cdk.aws_ec2.Peer.ipv4(vpc.vpc_cidr_block),
        connection=aws_cdk.aws_ec2.Port.tcp(443),
        description="Local HTTPS",
    )

    # Apply our custom nag pack
    aws_cdk.Aspects.of(stack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(stack)
    LOGGER.debug(json.dumps(template.to_json(), indent=2))

    # Ensure the synth causes the expected error
    annotations = Annotations.from_stack(stack)
    annotations.has_no_error(
        "/TestStack/TestSecurityGroup/Resource",
        "Guest360Rules-EC23: The Security Group allows for wide port ranges for inbound access.\n",
    )

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSSECURITYGROUP"], 1)
    template.has_resource_properties(
        constants["AWSSECURITYGROUP"],
        {
            INGRESS: [{"ToPort": 443}], #NOSONAR
            INGRESS: [{"FromPort": 443}], #NOSONAR
        },
    )


def test_aspect_bad_port_range(singlestack, constants):
    """Test with an ingress rule that has more than a single port."""

    vpc = aws_cdk.aws_ec2.Vpc(
        singlestack, "TestVPC", ip_addresses=aws_cdk.aws_ec2.IpAddresses.cidr(constants["TESTCIDRBLOCK"])
    )

    default_sg = aws_cdk.aws_ec2.SecurityGroup(
        scope=singlestack,
        id="TestSecurityGroup",
        vpc=vpc,
        allow_all_outbound=True, #NOSONAR
        description="Test SG",
    )

    # Create an ivalid security group ingress rule
    default_sg.add_ingress_rule(
        peer=aws_cdk.aws_ec2.Peer.ipv4(vpc.vpc_cidr_block),
        connection=aws_cdk.aws_ec2.Port.all_tcp(),
        description="Wide Open TCP",
    )

    # Apply our custom nag pack
    aws_cdk.Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    LOGGER.debug(json.dumps(template.to_json(), indent=2))

    # Ensure the synth causes the expected error
    annotations = Annotations.from_stack(singlestack)
    annotations.has_error(
        "/TestStack/TestSecurityGroup/Resource",
        "Guest360Rules-EC23: The Security Group allows for wide port ranges for inbound access.\n",
    )

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSSECURITYGROUP"], 1)
    template.has_resource_properties(
        constants["AWSSECURITYGROUP"],
        {
            INGRESS: [{"ToPort": 65535}], #NOSONAR
            INGRESS: [{"FromPort": 0}], #NOSONAR
        },
    )
