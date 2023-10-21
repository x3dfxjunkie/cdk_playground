import pluginlib, jsii, logging
from aws_cdk import CfnResource
from cdk_nag import IApplyRule, NagMessageLevel, NagRuleCompliance

logging.getLogger("pluginlib").propagate = False


@pluginlib.Parent("aspect")
@jsii.implements(IApplyRule)
class Guest360ValidatorBase:
    """Base Class to reduce duplication"""

    def __init__(self, node: CfnResource) -> None:
        self._node = node

    @property
    def node(self) -> CfnResource:
        return self._node

    @property
    def level(self) -> NagMessageLevel:
        return NagMessageLevel.ERROR

    def rule(self, node) -> NagRuleCompliance:  # NOSONAR
        raise NotImplementedError

    @property
    @pluginlib.abstractmethod
    def explanation(self) -> str:  # NOSONAR
        raise NotImplementedError

    @property
    @pluginlib.abstractmethod
    def rule_suffix_override(self) -> str:  # NOSONAR
        raise NotImplementedError

    @property
    @pluginlib.abstractmethod
    def info(self) -> str:  # NOSONAR
        raise NotImplementedError
