"""Module containing base class for guest360 constructs
"""
import hashlib, functools
from pathlib import Path

from constructs import Construct


class Construct360(Construct):
    """Intermediate base class between raw CDK Construct and rest of Guest360 implementations. Used to add default
    behavior to any children."""

    this_file_path = Path(__file__)
    app_dir = str(this_file_path.parents[1])
    project_dir = str(this_file_path.parents[2])

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        """Can be used add default behavior to all guest360 constructs. Same __init__ args as parent Construct class

        Args:
            scope (Construct): The scope in which to define this construct.
            construct_id (str): The scoped construct ID. Must be unique amongst siblings. If the ID includes a path separator (``/``), then it will be replaced by double dash ``--``.
        """
        self.pass_id = self.to_passing_id(construct_id)
        super().__init__(scope, self.pass_id, **kwargs)  # CDK Construct ids are curated in passing

    @classmethod
    def to_passing_id(cls, scope_id: str) -> str:
        """Prepares incomiing scope (stack or construct) id for reuse in in child constructs. Does not guarantee uniqueness of siblings.

        Args:
            scope_id (str): stack or construct id to be prepared for pass into the id of child construct

        Returns:
            str: s = (instantiating class name) + (one-way, 5 character alphanumeric hash)
        """
        construct_class_name = cls.__name__  # Name of class in which child construct is created
        scope_hash = hashlib.sha1(scope_id.encode()).hexdigest()[:5]  # Trimmed hash of scope-parent id
        return construct_class_name + scope_hash

    ##############################################
    ## Base Construct Properties
    @property
    def _stack(self):
        from aws_cdk import Stack

        return Stack.of(self)

    @_stack.setter
    def _stack(self, value):
        return value

    @property
    def _stack_name(self):
        return self.node.try_get_context("stack_name")

    @_stack_name.setter
    def _stack_name(self, value):
        return value

    @property
    def _environment(self):
        return self.node.try_get_context("environment")

    @_environment.setter
    def _environment(self, value):
        return value

    @property
    def _region(self):
        return self._stack.region

    @_region.setter
    def _region(self, value):
        return value

    @property
    def _prefix(self):
        return self.node.try_get_context("prefix")

    @_prefix.setter
    def _prefix(self, value):
        return value

    ##############################################
    ## Environment Specific Config File Properties
    @functools.cached_property
    def _environment_config_file(self):
        import yaml

        with open(
            f"{self.app_dir}/configs/{self._environment}-environment.yaml",
            mode="r",
            encoding="utf-8",
        ) as file:
            return yaml.safe_load(file)

    @property
    def _vpc_id(self):
        return self._environment_config_file["networking"][self._region]["vpc"]["id"]

    @property
    def _routable_subnets(self):
        return self._environment_config_file["networking"][self._region]["subnets"]["private"]

    @property
    def _nonroutable_subnets(self):
        return self._environment_config_file["networking"][self._region]["subnets"]["non-routable"]

    ##############################################
    ## Constant Config File Properties

    @functools.cached_property
    def _constants_config_file(self):
        import yaml

        with open(
            f"{self.app_dir}/configs/constants.yaml",
            mode="r",
            encoding="utf-8",
        ) as file:
            return yaml.safe_load(file)

    @property
    def _disney_internal_ipv4_cidr_blocks(self):
        return self._constants_config_file["disney_internal_cidr_blocks"]["ipv4"]

    @property
    def _account_numbers(self):
        return self._constants_config_file["account_ids"][self._environment]
