import logging
import sys
from aws_cdk import Aspects
from aws_cdk.assertions import Annotations, Template
from aws_cdk.aws_iam import Effect, PolicyStatement, PolicyDocument, Role, ServicePrincipal
from app.guest360_aspects.guest360_nagpack import Guest360Rules
from app.guest360_constructs.iam_role import Guest360IamRole

LOGGER = logging.getLogger(__name__)
STREAMHANDLER = logging.StreamHandler(sys.stdout)
FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
STREAMHANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(STREAMHANDLER)
STACK_NAME = "TestStack"
ROLE_NAME = "TestRole"
INLINE_POLICY_NAME = "TestInlinePolicy"
ACTIONS = "ec2:DescribeInstances"
VPC_CONDITION = "aws:sourceVpc"
VPCE_CONDITION = "aws:sourceVpce"
SVC_PRINCIPAL = "ec2.amazonaws.com"
RESOURCES = "arn:aws:ec2:us-east1:123456790:instance/i-0e5ba91a94f99f4b6"
IAM110 = "Guest360Rules-IAM110: IAM roles should have conditions to allow rights to requests that originate from within the vpc. This is a warning\n"


def test_g360_iam_role_construct_with_source_vpc(singlestack, constants):
    policy_stmts = [
        PolicyStatement(
            effect=Effect.ALLOW,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {f"{VPC_CONDITION}": "vpc-12345678"}},
        ),
    ]

    Guest360IamRole(
        singlestack,
        ROLE_NAME,
        props={
            "assumed_by": ServicePrincipal(SVC_PRINCIPAL),
            "description": "Test IAM Role",
            "inline_policies": {INLINE_POLICY_NAME: PolicyDocument(statements=policy_stmts)},
        },
    )

    # Apply our custom nag pack
    Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    # LOGGER.debug(json.dumps(template.to_json(), indent=2))

    annotations = Annotations.from_stack(singlestack)
    annotations.has_no_warning(f"/{STACK_NAME}/{ROLE_NAME}/Resource", IAM110)

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSIAMROLE"], 1)


def test_g360_iam_role_construct_with_source_vpce(singlestack, constants):
    policy_stmts = [
        PolicyStatement(
            effect=Effect.ALLOW,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {f"{VPCE_CONDITION}": "vpc-1111111"}},
        ),
    ]

    Guest360IamRole(
        singlestack,
        ROLE_NAME,
        props={
            "assumed_by": ServicePrincipal(SVC_PRINCIPAL),
            "description": "Test IAM Role",
            "inline_policies": {INLINE_POLICY_NAME: PolicyDocument(statements=policy_stmts)},
        },
    )

    # Apply our custom nag pack
    Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    # LOGGER.debug(json.dumps(template.to_json(), indent=2))

    annotations = Annotations.from_stack(singlestack)
    annotations.has_no_warning(f"/{STACK_NAME}/{ROLE_NAME}/Resource", IAM110)

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSIAMROLE"], 1)


def test_g360_iam_role_construct_with_source_vpc_err_str(singlestack, constants):
    policy_stmts = [
        PolicyStatement(
            effect=Effect.ALLOW,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {"aws:sourceVpcrr": "vpc-12345678"}},
        ),
    ]

    Role(
        scope=singlestack,
        id=ROLE_NAME,
        inline_policies={INLINE_POLICY_NAME: PolicyDocument(statements=policy_stmts)},
        assumed_by=ServicePrincipal(SVC_PRINCIPAL),
    )

    # Apply our custom nag pack
    Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    # LOGGER.debug(json.dumps(template.to_json(), indent=2))

    annotations = Annotations.from_stack(singlestack)
    annotations.has_warning(f"/{STACK_NAME}/{ROLE_NAME}/Resource", IAM110)

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSIAMROLE"], 1)


def test_g360_iam_role_construct_with_source_vpc_deny(singlestack, constants):
    policy_stmts = [
        PolicyStatement(
            effect=Effect.DENY,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {f"{VPC_CONDITION}": "vpc-22222222"}},
        ),
    ]

    Role(
        scope=singlestack,
        id=ROLE_NAME,
        inline_policies={INLINE_POLICY_NAME: PolicyDocument(statements=policy_stmts)},
        assumed_by=ServicePrincipal(SVC_PRINCIPAL),
    )

    # Apply our custom nag pack
    Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    # LOGGER.debug(json.dumps(template.to_json(), indent=2))

    annotations = Annotations.from_stack(singlestack)
    annotations.has_warning(f"/{STACK_NAME}/{ROLE_NAME}/Resource", IAM110)

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSIAMROLE"], 1)


def test_g360_iam_role_construct_with_multiple_statements_pass(singlestack, constants):
    policy_stmts = [
        PolicyStatement(
            effect=Effect.DENY,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {f"{VPC_CONDITION}": "vpc-33333333"}},
        ),
        PolicyStatement(
            effect=Effect.ALLOW,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {f"{VPC_CONDITION}": "vpc-4444444"}},
        ),
        PolicyStatement(
            effect=Effect.DENY,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {f"{VPC_CONDITION}": "vpc-15555555"}},
        ),
    ]

    Role(
        scope=singlestack,
        id=ROLE_NAME,
        inline_policies={INLINE_POLICY_NAME: PolicyDocument(statements=policy_stmts)},
        assumed_by=ServicePrincipal(SVC_PRINCIPAL),
    )

    # Apply our custom nag pack
    Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    # LOGGER.debug(json.dumps(template.to_json(), indent=2))

    annotations = Annotations.from_stack(singlestack)
    annotations.has_no_warning(f"/{STACK_NAME}/{ROLE_NAME}/Resource", IAM110)

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSIAMROLE"], 1)


def test_g360_iam_role_construct_with_multiple_statements_fail(singlestack, constants):
    policy_stmts = [
        PolicyStatement(
            effect=Effect.DENY,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {f"{VPC_CONDITION}": "vpc-637494645"}},
        ),
        PolicyStatement(
            effect=Effect.DENY,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {f"{VPCE_CONDITION}": "vpc-29464463"}},
        ),
        PolicyStatement(
            effect=Effect.DENY,
            actions=[ACTIONS],
            resources=[RESOURCES],
            conditions={"StringEquals": {f"{VPCE_CONDITION}": "vpc-983243647"}},
        ),
    ]

    Role(
        scope=singlestack,
        id=ROLE_NAME,
        inline_policies={INLINE_POLICY_NAME: PolicyDocument(statements=policy_stmts)},
        assumed_by=ServicePrincipal(SVC_PRINCIPAL),
    )

    # Apply our custom nag pack
    Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    # LOGGER.debug(json.dumps(template.to_json(), indent=2))

    annotations = Annotations.from_stack(singlestack)
    annotations.has_warning(f"/{STACK_NAME}/{ROLE_NAME}/Resource", IAM110)

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSIAMROLE"], 1)


def test_g360_iam_role_construct_nosourcevpc(singlestack, constants):
    policy_stmts = [
        PolicyStatement(
            effect=Effect.ALLOW,
            actions=[ACTIONS],
            resources=[RESOURCES],
        ),
    ]

    Role(
        scope=singlestack,
        id=ROLE_NAME,
        inline_policies={INLINE_POLICY_NAME: PolicyDocument(statements=policy_stmts)},
        assumed_by=ServicePrincipal("eks.amazonaws.com"),
    )

    # Apply our custom nag pack
    Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    # LOGGER.debug(json.dumps(template.to_json(), indent=2))

    # Ensure the synth causes the expected error
    annotations = Annotations.from_stack(singlestack)
    annotations.has_warning(f"/{STACK_NAME}/{ROLE_NAME}/Resource", IAM110)

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSIAMROLE"], 1)


def test_non_vpc_origin_policy(singlestack, constants):
    """Test role with wildcard permission in inline policy."""

    policy_stmts = [
        PolicyStatement(
            effect=Effect.ALLOW, actions=["s3:GetObject*"], resources=["arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"]
        ),
    ]

    Role(
        scope=singlestack,
        id=ROLE_NAME,
        inline_policies={INLINE_POLICY_NAME: PolicyDocument(statements=policy_stmts)},
        assumed_by=ServicePrincipal("eks.amazonaws.com"),
    )

    # Apply our custom nag pack
    Aspects.of(singlestack).add(Guest360Rules())

    # Synth the app
    template = Template.from_stack(singlestack)
    # LOGGER.debug(json.dumps(template.to_json(), indent=2))

    # Ensure the synth causes the expected error
    annotations = Annotations.from_stack(singlestack)
    annotations.has_warning(f"/{STACK_NAME}/{ROLE_NAME}/Resource", IAM110)

    # Ensure we have the expected count and params
    template.resource_count_is(constants["AWSIAMROLE"], 1)
