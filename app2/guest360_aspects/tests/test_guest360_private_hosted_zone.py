import json, pytest
import logging
import sys
import aws_cdk
from aws_cdk import App, Stack
from app.guest360_aspects.guest360_nagpack import Guest360Rules
from aws_cdk.assertions import Annotations, Template

LOGGER = logging.getLogger(__name__)
STREAMHANDLER = logging.StreamHandler(sys.stdout)
FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
STREAMHANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(STREAMHANDLER)
CFSTACKPATH = "/TestStack/TestPHZ/Resource"
ERROR_MSG = "Guest360Rules-PHZ103: Domain Name Segments must match regex expression -> ^[a-z0-9]([a-z-0-9-]{0,61}[a-z0-9])?$\n"

def test_aspect_bad_dns_name(singlestack, constants):
    """Test with a bad dns name and see if it handles it"""

    vpc = aws_cdk.aws_ec2.Vpc(
        singlestack, "TestVPC", ip_addresses=aws_cdk.aws_ec2.IpAddresses.cidr(constants["TESTCIDRBLOCK"])
    )
    # create an invalid domain
    aws_cdk.aws_route53.PrivateHostedZone(scope=singlestack, id="TestPHZ", vpc=vpc, zone_name="#.com")

    # Apply our custom nag pack
    aws_cdk.Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    LOGGER.debug(json.dumps(template.to_json(), indent=2))

    # Ensure the synth causes the expected error
    annotations = Annotations.from_stack(singlestack)
    annotations.has_error(
        CFSTACKPATH,
        ERROR_MSG
    )

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSHOSTEDZONE"], 1)
    template.has_resource_properties(constants["AWSHOSTEDZONE"], {"Name": "#.com."})

def test_aspect_bad_dns_name1(singlestack, constants):
    """Test with a bad dns name and see if it handles it"""

    vpc = aws_cdk.aws_ec2.Vpc(
        singlestack, "TestVPC", ip_addresses=aws_cdk.aws_ec2.IpAddresses.cidr(constants["TESTCIDRBLOCK"])
    )
    # create an invalid domain
    aws_cdk.aws_route53.PrivateHostedZone(scope=singlestack, id="TestPHZ", vpc=vpc, zone_name="a$aaaa.com")

    # Apply our custom nag pack
    aws_cdk.Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    LOGGER.debug(json.dumps(template.to_json(), indent=2))

    # Ensure the synth causes the expected error
    annotations = Annotations.from_stack(singlestack)
    annotations.has_error(
        CFSTACKPATH,
        ERROR_MSG,
    )
    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSHOSTEDZONE"], 1)
    template.has_resource_properties(constants["AWSHOSTEDZONE"], {"Name": "a$aaaa.com."})


def test_aspect_small_dns_name(singlestack, constants):
    """Test with a bad dns name and see if it handles it"""

    vpc = aws_cdk.aws_ec2.Vpc(
        singlestack, "TestVPC", ip_addresses=aws_cdk.aws_ec2.IpAddresses.cidr(constants["TESTCIDRBLOCK"])
    )
    # create an invalid domain
    aws_cdk.aws_route53.PrivateHostedZone(scope=singlestack, id="TestPHZ", vpc=vpc, zone_name="m")

    # Apply our custom nag pack
    aws_cdk.Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    LOGGER.debug(json.dumps(template.to_json(), indent=2))

    # Ensure the synth causes the expected error
    annotations = Annotations.from_stack(singlestack)
    annotations.has_error(CFSTACKPATH, "Guest360Rules-PHZ101: Domain Name must be at least 1 character\n")
    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSHOSTEDZONE"], 1)
    template.has_resource_properties(constants["AWSHOSTEDZONE"], {"Name": "m."})
