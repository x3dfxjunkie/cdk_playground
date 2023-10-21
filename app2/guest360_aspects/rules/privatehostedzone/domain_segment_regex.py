import jsii, re
from aws_cdk import CfnResource
from cdk_nag import NagRuleCompliance
from app.guest360_aspects.rules.rule_base import Guest360ValidatorBase


class Guest360Validator(Guest360ValidatorBase):
    _alias_ = "PHZ103"
    _version_ = "1.0.0"

    def __init__(self, node: CfnResource) -> None:
        super().__init__(node)

    def rule(self, node) -> NagRuleCompliance:
        if isinstance(node, CfnResource) and node.cfn_resource_type == "AWS::Route53::HostedZone":
            """
            Individual domain segments checks
            #  Can begin and end with a number or letter only (no check)
            #  Can contain hyphens, a-z, A-Z, 0-9 (no check)
            #  1 - 63 chars allowed (check)
            """
            domain_name = node.name if node.name[-1:] != "." else node.name[0:-1]
            segment_validator = re.compile(r"^[a-z0-9]([a-z-0-9-]{0,61}[a-z0-9])?$", re.IGNORECASE)
            if not all(segment_validator.match(segment) for segment in domain_name.split(".")):
                return NagRuleCompliance.NON_COMPLIANT
        return NagRuleCompliance.COMPLIANT

    @property
    def explanation(self) -> str:
        return "DNS rules are complicated.  Overall Domain Check(2) Must be at least 1 character and must be less than 255.  For each individual sub-domain segment Check (3) Can begin and end with a number or letter only.  Can contain hyphens, a-z, A-Z, 0-9.  1 - 63 chars allowed"

    @property
    def rule_suffix_override(self) -> str:
        return "PHZ103"

    @property
    def info(self) -> str:
        return "Domain Name Segments must match regex expression -> ^[a-z0-9]([a-z-0-9-]{0,61}[a-z0-9])?$"
