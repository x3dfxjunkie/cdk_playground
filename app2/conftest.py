import pytest
from aws_cdk import App, Stack

ENVIRONMENT_VARIABLES = {"region": "us-east-1", "account": "123456789"}
ENVIRONMENTS = [
    {"long_env": "latest", "short_env": "lst"},
    {"long_env": "stage", "short_env": "stg"},
    {"long_env": "load", "short_env": "lod"},
    {"long_env": "prod", "short_env": "prd"},
    {"long_env": "local", "short_env": "lcl"},
]


def rtn_context(long_env, short_env):
    return {"prefix": f"{short_env}-test_something", "environment": long_env}


def rtn_test_context(long_env, short_env):
    return {"prefix": f"{short_env}-test_something", "environment": f"test-{long_env}"}


@pytest.fixture(name="stack", params=ENVIRONMENTS)
def fixture_stack(request):
    app = App(context=rtn_context(**request.param))
    stack = Stack(app, env=ENVIRONMENT_VARIABLES)
    yield stack


@pytest.fixture(name="teststack", params=ENVIRONMENTS)
def fixture_test_stack(request):
    app = App(context=rtn_test_context(**request.param))
    stack = Stack(app, env=ENVIRONMENT_VARIABLES)
    yield stack


@pytest.fixture(name="singlestack")
def fixture_single_stack():
    app = App(context={"prefix": "lst-test", "environment": "latest"})
    stack = Stack(app, "TestStack", env={"region": "us-east-1", "account": "123456789"})
    yield stack


@pytest.fixture(name="constants")
def constants():
    obj = {
        "AWSHOSTEDZONE": "AWS::Route53::HostedZone",
        "AWSRECORDSET": "AWS::Route53::RecordSet",
        "AWSRESOLVER": "AWS::Route53Resolver::ResolverEndpoint",
        "AWSSECURITYGROUP": "AWS::EC2::SecurityGroup",
        "AWSVPCENDPOINT": "AWS::EC2::VPCEndpoint",
        "AWSCLOUDMAP": "AWS::ServiceDiscovery::PrivateDnsNamespace",
        "TESTCIDRBLOCK": f"172.16{'.0'*2}/16",
        "AWSVPCENDPOINTSVC": "AWS::EC2::VPCEndpointService",
        "AWSLAMBDAFUNCTION": "AWS::Lambda::Function",
        "AWSDBINSTANCE": "AWS::RDS::DBInstance",
        "AWSDBSUBNETGROUP": "AWS::RDS::DBSubnetGroup",
        "AWSKMSKEY": "AWS::KMS::Key",
        "AWSIAMROLE": "AWS::IAM::Role",
        "AWSCWALARM": "AWS::CloudWatch::Alarm",
    }
    return obj
