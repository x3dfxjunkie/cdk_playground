"""
Testing of Domain Record Types
"""
import pytest
import logging
import sys
from aws_cdk.aws_ec2 import Vpc, IpAddresses
from aws_cdk.aws_route53 import PrivateHostedZone, RecordTarget
from app.guest360_constructs.route53_domain_record_types import Guest360Route53CnameRecord, Guest360Route53ARecord
from app.guest360_constructs.tests.utils import print_template_on_debug

from aws_cdk import App, Stack, assertions, Token

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_CONTEXT = {"prefix": "lst-test_sg_something", "environment": "latest"}
ENVIRONMENT = {"region": "us-east-1", "account": "123456789"}
AWSRECORDSET = "AWS::Route53::RecordSet"
ZONENAME = "bar.com"
DOMAINNAME = "example.com"
CIDR_BLOCK = f"172.16{'.0'*2}/16"
TEST_ADDRESS = str("1." * 4)[:-1]
print(TEST_ADDRESS)


@pytest.fixture(name="stack")
def fixture_stack():
    app = App(context=TEST_CONTEXT)
    stack = Stack(app, env=ENVIRONMENT)
    yield stack


def test_cname_domain_name_record(stack):
    """Tests Required Parameters to domain root"""
    VPC = Vpc(stack, "TestVPC", ip_addresses=IpAddresses.cidr(CIDR_BLOCK))
    PHZ = PrivateHostedZone(scope=stack, id="TestPHZ", vpc=VPC, zone_name=ZONENAME)
    Guest360Route53CnameRecord(stack, "TestCName1", props={"domain_name": f"xxx.{DOMAINNAME}", "zone": PHZ})
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(AWSRECORDSET, 1)
    template.has_resource_properties(AWSRECORDSET, {"Name": f"{ZONENAME}.", "ResourceRecords": [f"xxx.{DOMAINNAME}"]})


def test_cname_domain_name_two_records(stack):
    """Tests optional subdomain Parameters to two different domain roots"""
    VPC = Vpc(stack, "TestVPC", ip_addresses=IpAddresses.cidr(CIDR_BLOCK))
    PHZ = PrivateHostedZone(scope=stack, id="TestPHZ", vpc=VPC, zone_name="bar.com")
    Guest360Route53CnameRecord(
        stack, "TestCName1", props={"domain_name": f"xxx.{DOMAINNAME}", "record_name": "foo", "zone": PHZ}
    )
    Guest360Route53CnameRecord(
        stack, "TestCName2", props={"domain_name": f"yyy.{DOMAINNAME}", "record_name": "bar", "zone": PHZ}
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(AWSRECORDSET, 2)
    template.has_resource_properties(
        AWSRECORDSET, {"Name": f"foo.{ZONENAME}.", "ResourceRecords": [f"xxx.{DOMAINNAME}"]}
    )
    template.has_resource_properties(
        AWSRECORDSET, {"Name": f"bar.{ZONENAME}.", "ResourceRecords": [f"yyy.{DOMAINNAME}"]}
    )


def test_cname_domain_name_record_with_ip(stack):
    """Tests whether an IP address can sneak in"""
    with pytest.raises(ValueError) as exc:
        VPC = Vpc(stack, "TestVPC", ip_addresses=IpAddresses.cidr(CIDR_BLOCK))
        PHZ = PrivateHostedZone(scope=stack, id="TestPHZ", vpc=VPC, zone_name=ZONENAME)
        Guest360Route53CnameRecord(stack, "TestCName1", props={"domain_name": TEST_ADDRESS, "zone": PHZ})
    assert "CNAME records require a FQDN not an ip address" in str(exc.value)


def test_a_domain_name_record(stack):
    """Tests Required Parameters to domain root"""
    VPC = Vpc(stack, "TestVPC", ip_addresses=IpAddresses.cidr(CIDR_BLOCK))
    PHZ = PrivateHostedZone(scope=stack, id="TestPHZ", vpc=VPC, zone_name=ZONENAME)
    Guest360Route53ARecord(
        stack, "TestAName1", props={"target": RecordTarget.from_ip_addresses(TEST_ADDRESS), "zone": PHZ}
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(AWSRECORDSET, 1)
    template.has_resource_properties(AWSRECORDSET, {"Name": f"{ZONENAME}.", "ResourceRecords": [TEST_ADDRESS]})


def test_a_domain_name_two_records(stack):
    """Tests optional subdomain Parameters to two different domain roots"""
    VPC = Vpc(stack, "TestVPC", ip_addresses=IpAddresses.cidr(CIDR_BLOCK))
    PHZ = PrivateHostedZone(scope=stack, id="TestPHZ", vpc=VPC, zone_name=ZONENAME)
    Guest360Route53ARecord(
        stack, "TestAName1", props={"target": RecordTarget.from_values(TEST_ADDRESS), "record_name": "foo", "zone": PHZ}
    )
    Guest360Route53ARecord(
        stack, "TestAName2", props={"target": RecordTarget.from_values(TEST_ADDRESS), "record_name": "bar", "zone": PHZ}
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(AWSRECORDSET, 2)
    template.has_resource_properties(AWSRECORDSET, {"Name": f"foo.{ZONENAME}.", "ResourceRecords": [TEST_ADDRESS]})
    template.has_resource_properties(AWSRECORDSET, {"Name": f"bar.{ZONENAME}.", "ResourceRecords": [TEST_ADDRESS]})


def test_a_domain_name_record_with_domain(stack):
    """Tests whether it will look up values - Note this should fail but there isn't a way here to handle this because of alias"""
    VPC = Vpc(stack, "TestVPC", ip_addresses=IpAddresses.cidr(CIDR_BLOCK))
    PHZ = PrivateHostedZone(scope=stack, id="TestPHZ", vpc=VPC, zone_name=ZONENAME)
    Guest360Route53ARecord(stack, "TestAName1", props={"target": RecordTarget.from_values("google.com"), "zone": PHZ})
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(AWSRECORDSET, 1)
    template.has_resource_properties(AWSRECORDSET, {"Name": f"{ZONENAME}.", "ResourceRecords": ["google.com"]})
