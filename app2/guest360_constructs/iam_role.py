"""
File for Guest360 base IAM Role construct
"""
from typing import TypedDict, Union

import aws_cdk
from app.src.reliability.utils import RoleName
from aws_cdk import Duration
from aws_cdk.aws_iam import (
    AnyPrincipal,
    ArnPrincipal,
    CompositePrincipal,
    ServicePrincipal,
    WebIdentityPrincipal,
    PrincipalWithConditions,
)
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from .construct_360 import Construct360


@match_class_typing
class IAMProps(TypedDict):
    assumed_by: Union[
        ServicePrincipal, CompositePrincipal, ArnPrincipal, WebIdentityPrincipal, AnyPrincipal, PrincipalWithConditions
    ]
    description: str
    max_session_duration: NotRequired[Duration]
    path: NotRequired[str]
    role_name: NotRequired[str]


class Guest360IamRole(Construct360):
    """Guest360 Construct for IAM Roles.

    This includes some hard-coded values, as well as some overrideable defaults.
    Required props:
        {
            "assumed_by": Union[ServicePrincipal, CompositePrincipal, ArnPrincipal],
            "description": string,
        }

    Optional props:
        {
            "max_session_duration": aws_cdk.Duration  # Time a session is valid for. Lowest value is 15 minutes, default is 1 hour.
            "path": string # Logical path of the role. Only used for filtering.
        }

    Usage:
        Guest360IamRole(self, f"{self.stack_name}-lambda-role",
                        {
                            'assumed_by': aws_iam.ServicePrincipal('lambda.amazonaws.com'),
                            'description': 'Lambda role for process.'
                        })
    """

    role: aws_cdk.aws_iam.Role

    def __init__(self, scope: Construct360, construct_id: str, props: IAMProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        IAMProps(props)

        prefix = self.node.try_get_context("prefix_global")

        self.props_default = {"max_session_duration": aws_cdk.Duration.hours(1), "path": "/"}
        if "description" not in props:
            raise ValueError("required field - description: str - missing")

        self.props_dict = {1: self.props_default, 2: props}
        self.props_merged = {**self.props_dict[1], **self.props_dict[2]}

        if "role_name" in self.props_merged:
            self.props_merged["role_name"] = RoleName(prefix, self.props_merged["role_name"]).name()

        self.role: aws_cdk.aws_iam.Role = aws_cdk.aws_iam.Role(
            scope=self,
            id=self.pass_id,
            **self.props_merged,
        )

    @classmethod
    def from_role_name(cls, scope, construct_id, role_name: str, *args, **kwargs) -> aws_cdk.aws_iam.IRole:
        prefix = scope.node.try_get_context("prefix_global")
        g360name = RoleName(prefix, role_name).name()
        return aws_cdk.aws_iam.Role.from_role_name(
            scope=scope, id=cls.to_passing_id(construct_id), role_name=g360name, *args, **kwargs
        )

    @classmethod
    def from_role_arn(cls, *args, **kwargs) -> aws_cdk.aws_iam.IRole:
        return aws_cdk.aws_iam.Role.from_role_arn(*args, **kwargs)
