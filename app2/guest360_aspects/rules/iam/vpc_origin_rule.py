from aws_cdk import CfnResource
from cdk_nag import NagRuleCompliance, NagMessageLevel
from app.guest360_aspects.rules.rule_base import Guest360ValidatorBase


class Guest360Validator(Guest360ValidatorBase):
    _alias_ = "IAM110"
    _version_ = "1.0.0"

    def rule(self, node) -> NagRuleCompliance:
        """Check role statement for vpc origin conditions:
        # aws:SourceVpce key to specify the endpoint
        # aws:SourceVPC key to specify the VPC
        """
        # apply the rule only if the resource is of type AWS::IAM::Role. All other case return as compliant
        if isinstance(node, CfnResource) and node.cfn_resource_type == "AWS::IAM::Role":
            policy_docs_json = []
            for doc in node.policies:
                policy_docs_json.append(doc.policy_document.to_json())
        else:
            return NagRuleCompliance.COMPLIANT
        for doc_json in policy_docs_json:
            for statement in doc_json["Statement"]:
                # apply the rule only for Effect = Allow
                if (
                    (statement["Effect"] is not None)
                    and (statement["Effect"] == "Allow")
                    and ("Condition" in statement)
                ):
                    conditions = statement["Condition"]
                    if "StringEquals" in conditions and (
                        "aws:sourceVpce" in conditions["StringEquals"] or "aws:sourceVpc" in conditions["StringEquals"]
                    ):
                        # returns compliant if above strings are present in condition for Effect=Allow
                        return NagRuleCompliance.COMPLIANT
                    # returns non compliant if above strings are not present in condition for Effect=Allow
                    return NagRuleCompliance.NON_COMPLIANT
        # returns non compliant if policy json is empty
        return NagRuleCompliance.NON_COMPLIANT

    @property
    def explanation(self) -> str:
        return "IAM roles should have conditions to allow rights to requests that originate from within the vpc. This is a warning"

    @property
    def rule_suffix_override(self) -> str:
        return "IAM110"

    @property
    def info(self) -> str:
        return "IAM roles should have conditions to allow rights to requests that originate from within the vpc. This is a warning"

    @property
    def level(self) -> NagMessageLevel:
        return NagMessageLevel.WARN
