"""
Logic for Guest360's base construct for KMS Keys
"""
import os
from typing import Optional, TypedDict, Union

import yaml
import aws_cdk
from aws_cdk import Duration, RemovalPolicy, Stack, Tags, aws_iam, aws_kms
from strongtyping.strong_typing import match_class_typing

from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import KmsKeyAliasName


@match_class_typing
class Guest360KMSKeyProps(TypedDict):
    """
    Properties class for strongtyping
    """

    alias: Optional[str]
    description: Optional[str]
    enable: Optional[bool]
    pending_window: Optional[Duration]
    removal_policy: Optional[RemovalPolicy]
    tags_for_read: Optional[dict]


class Guest360KMSKey(aws_kms.Key):
    """Guest360 Construct for KMS Keys.
    This includes some hard-coded values, as well as some overrideable defaults.
    Optional props:
        {
            "alias": string,
            "description": string  # Description of the key.
            "enabled": bool  # Enable or disable this key. Defaults to True.
            "pending_window": Duration  # How long a key is pending delete before it's gone for good. Latest defaults to None, otherwise 14 days.
            "removal_policy": RemovalPolicy  # destroy with the stack or not. Latest default to DESTROY, otherwise RETAIN.
            "tags_for_read": dict  # Key/value pairs for tags that must match for decrypt access.
        }
    Usage:
        Guest360KMSKey(self, f"{self.stack_name}-encryption-key",
                        {
                            'alias': f"{stack_name}-encryption-key-alias",
                            "tags_for_read": {"foo": "bar"},
                        })
    """

    def __init__(
        self, scope: Construct360, construct_id: str, props: Union[dict, Guest360KMSKeyProps] = {}, **kwargs
    ) -> aws_kms.Key:
        self._set_environment(scope)
        self._check_and_process_props(props)
        super().__init__(scope, construct_id, **self.props_merged, **kwargs)
        self._default_policy()
        self._enable_tag_access()

    def _set_environment(self, scope: Construct360) -> None:
        """Set some environment info"""
        self._stack = Stack.of(scope)
        self._environment = scope.node.try_get_context("environment")
        self._stack_path = scope.node.try_get_context("stack_path")
        self._prefix = scope.node.try_get_context("prefix")

    def _check_and_process_props(self, props: Union[dict, Guest360KMSKeyProps]) -> None:
        """Validate props and set defaults"""
        Guest360KMSKeyProps(props)

        filename = os.path.splitext(os.path.split(__file__)[1])[0]
        with open(
            f"{self._stack_path}/app/configs/constructs/{filename}.yaml", "r", encoding="UTF-8"
        ) as file:
            key_defaults = yaml.safe_load(file)

        self.props_default = key_defaults["defaults"] | key_defaults.get(self._environment, {})
        self.props_default["pending_window"] = eval(self.props_default["pending_window"], {"aws_cdk": aws_cdk}, {})
        self.props_default["removal_policy"] = eval(self.props_default["removal_policy"], {"aws_cdk": aws_cdk}, {})
        self.props_default["policy"] = eval(self.props_default["policy"], {"aws_cdk": aws_cdk}, {})

        if "alias" in props:
            props["alias"] = KmsKeyAliasName(self._prefix, props["alias"]).name()

        if "tags_for_read" in props:
            self._tags_for_read = props.pop("tags_for_read")

        self.props_merged = self.props_default | props

        aws_iam.PolicyDocument.validate_for_resource_policy(self.props_merged["policy"])

    def _default_policy(self) -> None:
        """Assign default permissions to the key."""
        self.grant_admin(aws_iam.AccountRootPrincipal())
        self.grant_admin(aws_iam.ArnPrincipal(f"arn:aws:iam::{self._stack.account}:role/WDPR-CLAIMANT"))
        self.grant_encrypt(aws_iam.AccountRootPrincipal())
        self._policy.validate_for_resource_policy()

    def _enable_tag_access(self) -> None:
        """Enable tag-based access"""
        try:
            statements = []
            for key, value in self._tags_for_read.items():
                Tags.of(self).add(key, value, priority=300)
                statements.append(
                    aws_iam.PolicyStatement(
                        actions=[
                            "kms:Decrypt",
                        ],
                        effect=aws_iam.Effect.ALLOW,
                        principals=[aws_iam.AccountRootPrincipal()],
                        resources=["*"],
                        conditions={"StringEquals": {f"aws:PrincipalTag/{key}": "${aws:ResourceTag/%s}" % key}},
                    )
                )
                statements.append(
                    aws_iam.PolicyStatement(
                        actions=[
                            "kms:Decrypt",
                        ],
                        effect=aws_iam.Effect.DENY,
                        principals=[aws_iam.AccountRootPrincipal()],
                        resources=["*"],
                        conditions={"Null": {f"aws:PrincipalTag/{key}": "true"}},
                    )
                )

            aws_iam.PolicyDocument(
                assign_sids=True, minimize=True, statements=statements
            ).validate_for_resource_policy()
            for statement in statements:
                self.add_to_resource_policy(statement)

        except AttributeError:
            pass
