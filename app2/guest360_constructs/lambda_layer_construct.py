"""Lambda Layer Construct
"""
#!/usr/bin/env python3
import os
from pathlib import Path
from typing import List, TypedDict

import aws_cdk
from aws_cdk import RemovalPolicy, aws_lambda
from strongtyping.strong_typing import match_class_typing

from app.guest360_constructs.construct_360 import Construct360


@match_class_typing
class LambdaLayerProps(TypedDict):
    layer_name: str  # Name of the lambda layer
    cross_account_access: bool  # True/False if cross-account-access required
    cross_account_id: List[str]  # aws account ids for ca access
    code: str  # code path for lambda layer app code
    description: str  # description of lambda layer functionality
    compatible_runtimes: aws_cdk.aws_lambda.Runtime


class Guest360LambdaLayer(Construct360):
    """Class for lambda layer construct

    Args:
        Construct: aws_cdk construct
    """

    @property
    def lambda_layer(self):
        return self.layer

    def __init__(self, scope: Construct360, construct_id: str, props: dict, **kwargs) -> None:
        """Construct to create lambda layer

        Args:
            scope (Construct):
            construct_id (str): Construct ID
            props (dict): Configurations for Lambda Layer - see LambdaLayerProps TypedDict
        """

        super().__init__(scope, construct_id, **kwargs)

        prefix = self.node.try_get_context("prefix").lower()

        # Type check lambda layer props
        lambda_layer_props = props["lambda_layer"]

        LambdaLayerProps(lambda_layer_props)

        stack_path = str(Path(os.getcwd()).parents[0])
        var_layer_name = f"{prefix}-{lambda_layer_props['layer_name']}"

        self.layer = aws_lambda.LayerVersion(
            self,
            self.pass_id,
            layer_version_name=var_layer_name,
            code=aws_lambda.Code.from_asset(f"{stack_path}/{lambda_layer_props['code']}"),
            description=lambda_layer_props["description"],
            compatible_runtimes=[lambda_layer_props["compatible_runtimes"]],
            removal_policy=RemovalPolicy.DESTROY,
        )

        # grant layer access across a list of accounts
        if lambda_layer_props["cross_account_access"]:
            for account in lambda_layer_props["cross_account_id"]:
                self.layer.add_permission("remote-account-grant", account_id=account)
