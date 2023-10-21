from aws_cdk import CfnResource, Stack
from cdk_nag import NagRuleCompliance, NagRules
from app.guest360_aspects.rules.rule_base import Guest360ValidatorBase


class Guest360Validator(Guest360ValidatorBase):
    _alias_ = "EC23"
    _version_ = "1.0.0"

    """Check all security groups for port ranges instead of individual ports.

    In the spirit of least access, Guest360 is maintaining a policy of opening
    TCP ports in a methodical fashion. With that in mind, port ranges are discouraged.

    Typical usage example:

      cdk_nag.NagPack._apply_rule(Guest360SGPortRule(node)
    """

    def __init__(self, node: CfnResource) -> None:
        super().__init__(node)

    def rule(self, node) -> NagRuleCompliance:
        """Check security group ingress rules for toPort and fromPort parity.

        If toPort and fromPort are equal, return NagRuleCompliance.COMPLIANT.
        Otherwise, return NagRuleCompliance.NON_COMPLIANT.

        Args:
            node: aws_cdk.CfnResource CloudFormation resource object

        Returns:
            cdk_nag.NagRuleCompliance

        Raises:
            None
        """
        if (
            isinstance(node, CfnResource)
            and node.cfn_resource_type == "AWS::EC2::SecurityGroup"
            and Stack.of(node).resolve(node.security_group_ingress) is not None
        ):
            for rule in Stack.of(node).resolve(node.security_group_ingress):
                resolved_rule = Stack.of(node).resolve(rule)
                resolved_port_from = (
                    NagRules.resolve_if_primitive(node, resolved_rule["fromPort"])
                    if resolved_rule.get("fromPort") is not None
                    else None
                )
                resolved_port_to = (
                    NagRules.resolve_if_primitive(node, resolved_rule["toPort"])
                    if resolved_rule.get("toPort") is not None
                    else None
                )
                if resolved_port_from != None and resolved_port_to != None and resolved_port_to != resolved_port_from:
                    return NagRuleCompliance.NON_COMPLIANT
        return NagRuleCompliance.COMPLIANT

    @property
    def explanation(self) -> str:
        return "Large port ranges, when open, expose instances to unwanted attacks. More than that, they make traceability of vulnerabilities very difficult. For instance, your web servers may only require 80 and 443 ports to be open, but not all. One of the most common mistakes observed is when  all ports for 0.0.0.0/0 range are open in a rush to access the instance. EC2 instances must expose only to those ports enabled on the corresponding security group level."

    @property
    def rule_suffix_override(self) -> str:
        return "EC23"

    @property
    def info(self) -> str:
        return "The Security Group allows for wide port ranges for inbound access."
