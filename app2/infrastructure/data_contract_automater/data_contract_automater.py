"""
File containing code for the guest360 automater stack
"""

import logging
import os
import sys
from pathlib import Path
from typing import List, Dict, cast

import aws_cdk
from aws_cdk import Stack, Tags
from cdk_nag import NagSuppressions
import yaml

from app.infrastructure.ingestion.ingestion import Ingestion
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.ingestion.data_contract_automater import DataContractAutomater
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from app.infrastructure.workstream_stack import WorkstreamStack


logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Auto-Mater | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class DataContractAutomaterStack(WorkstreamStack):
    """
    Stack definition for the auto-mater stack.
    """

    def __init__(self, scope: Stack, construct_id: str, ingestion_stack: Ingestion, **kwargs) -> None:
        """Initialization method for ingestion class
        Args:
            scope (Construct360): scope for stack
            construct_id (str): ID of construct for naming purposes
            environment_config (dict): environment configuration details
        """
        super().__init__(scope, construct_id, **kwargs)

        environment = self.node.try_get_context("environment").lower()
        region_name = Stack.of(self).region.lower()

        Tags.of(self).add("prefix", self.prefix)

        """
        Automater Role
        """

        # Grab networking information from global environment config
        env_config_path = f"{self.project_dir}/app/configs/{environment}-environment.yaml"
        with open(
            env_config_path,
            mode="r",
            encoding="utf-8",
        ) as file:
            environment_config = yaml.safe_load(file)
            vpc_endpoints: List[Dict[str, str]] = environment_config["networking"][region_name]["endpoints"]
            api_gateway_vpc_endpoint = next(
                filter(lambda endpoint: endpoint["service_name"] == "execute-api", vpc_endpoints)
            )
            vpc_endpoint = aws_cdk.aws_ec2.InterfaceVpcEndpoint.from_interface_vpc_endpoint_attributes(
                self, "api_gateway_endpoint", port=443, vpc_endpoint_id=api_gateway_vpc_endpoint["id"]
            )

        data_contract_automater = DataContractAutomater(
            self, "data-contract-automater", {"vpc_endpoints": [vpc_endpoint]}
        )

        raw_bucket = Guest360S3Bucket.from_ssm(
            cast(Construct360, self), "bucket", ingestion_stack.stack_name, f"{ingestion_stack.construct_id}-raw"
        )
        raw_bucket.bucket.grant_read(data_contract_automater.automater_role)

        NagSuppressions.add_resource_suppressions(
            data_contract_automater,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "allow read access to raw bucket.",
                }
            ],
            True,
        )
