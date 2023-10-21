from aws_cdk import CfnResource
from cdk_nag import NagPack
from constructs import IConstruct
import pluginlib
import logging

logging.getLogger("pluginlib").propagate = False


class Guest360Rules(NagPack):
    """Custom cdk_nag pack for DPEP DPP Guest360

    This nag pack comprises of rules from GIS and Parks security.

    Typical usage example:

      self.aspects.add(Guest360Rules())
    """

    def __init__(self, *args) -> None:
        super().__init__(*args)
        self._pack_name = "Guest360Rules"
        self.loader = pluginlib.PluginLoader(modules=["app.guest360_aspects.rules"])
        self.plugins = self.loader.plugins

    def visit(self, node: IConstruct):
        if isinstance(node, CfnResource):
            for plugin in self.plugins.aspect:
                self._apply_rule(self.plugins.aspect[plugin](node))
