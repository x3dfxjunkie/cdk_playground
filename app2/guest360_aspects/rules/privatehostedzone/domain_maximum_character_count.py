from aws_cdk import CfnResource
from cdk_nag import NagRuleCompliance
from app.guest360_aspects.rules.rule_base import Guest360ValidatorBase


class Guest360Validator(Guest360ValidatorBase):
    _alias_ = "PHZ102"
    _version_ = "1.0.0"

    def __init__(self, node: CfnResource) -> None:
        super().__init__(node)

    def rule(self, node) -> NagRuleCompliance:
        """Check PHZ for Domain Name Length Compliance"""
        if isinstance(node, CfnResource) and node.cfn_resource_type == "AWS::Route53::HostedZone":
            domain_name = node.name if node.name[-1:] != "." else node.name[0:-1]
            if len(domain_name) > 253:
                return NagRuleCompliance.NON_COMPLIANT
        return NagRuleCompliance.COMPLIANT

    @property
    def explanation(self) -> str:
        return "DNS rules are complicated.  Overall Domain Check(2) Must be at least 1 character and must be less than 255.  For each individual sub-domain segment Check (3) Can begin and end with a number or letter only.  Can contain hyphens, a-z, A-Z, 0-9.  1 - 63 chars allowed"

    @property
    def rule_suffix_override(self) -> str:
        return "PHZ102"

    @property
    def info(self) -> str:
        return "Domain Name must be less than 253 characters"
