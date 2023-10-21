"""
Logic for Guest360's base construct for KMS Keys
"""
from typing import Optional, TypedDict

import aws_cdk
from app.guest360_constructs.construct_360 import Construct360
from strongtyping.strong_typing import match_class_typing


@match_class_typing
class Guest360KMSKeyProps(TypedDict):
    """
    Properties class for strongtyping
    """

    alias: str
    description: Optional[str]
    enable: Optional[bool]
    pending_window: Optional[aws_cdk.Duration]
    removal_policy: Optional[aws_cdk.RemovalPolicy]


class Guest360KMSKey(Construct360):
    """Guest360 Construct for KMS Keys.
    This includes some hard-coded values, as well as some overrideable defaults.
    Required props:
        {
            "alias": string,
        }
    Optional props:
        {
            "description": string  # Description of the key.
            "enabled": bool  # Enable or disable this key. Defaults to True.
            "pending_window": aws_cdk.Duration  # How long a key is pending delete before it's gone for good. Latest defaults to None, otherwise 14 days.
            "removal_policy": aws_cdk.RemovalPolicy  # destroy with the stack or not. Latest default to DESTROY, otherwise RETAIN.
        }
    Usage:
        Guest360KMSKey(self, f"{self.stack_name}-encryption-key",
                        {
                            'alias': f"{stack_name}-encryption-key-alias",
                        })
    """

    @property
    def key(self):
        return self._key

    def __init__(self, scope: Construct360, construct_id: str, props: Guest360KMSKeyProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        Guest360KMSKeyProps(props)

        self.environment = self.node.try_get_context("environment")
        self.stack_name = self.node.try_get_context("stack_name")
        prefix = self.node.try_get_context("prefix")

        self.props_default = {
            "description": "Encrypting Data",
            "enabled": True,
            "pending_window": aws_cdk.Duration.days(7) if self.environment != "prod" else None,
            "removal_policy": aws_cdk.RemovalPolicy.RETAIN
            if self.environment == "prod"
            else aws_cdk.RemovalPolicy.DESTROY,
        }

        self.props_dict = {1: self.props_default, 2: props}
        self.props_merged = {**self.props_dict[1], **self.props_dict[2]}

        default_policy = aws_cdk.aws_iam.PolicyDocument(
            statements=[
                aws_cdk.aws_iam.PolicyStatement(
                    actions=["kms:Describe*", "kms:Get*", "kms:List*", "kms:Decrypt"]
                    if self.environment != "prod"
                    else ["kms:Describe*", "kms:Get*", "kms:List*"],
                    principals=[aws_cdk.aws_iam.AccountRootPrincipal()],
                    resources=["*"],
                )
            ]
        )

        self._key = aws_cdk.aws_kms.Key(
            self,
            f"{prefix}-{construct_id}-{props['alias']}",
            # alias=props['alias'],  # Leaving this in for future re-use.
            admins=[aws_cdk.aws_iam.AccountRootPrincipal()],
            description=self.props_merged["description"],
            enable_key_rotation=True,
            enabled=self.props_merged["enabled"],
            pending_window=self.props_merged["pending_window"],
            policy=default_policy,
            removal_policy=self.props_merged["removal_policy"],
        )

        self._key.grant_encrypt(aws_cdk.aws_iam.AccountRootPrincipal())
