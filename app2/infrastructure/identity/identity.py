"""
Identity library
"""
import os
import yaml

from aws_cdk import Stack

from app.guest360_constructs.identity.identity_graph import IdentityGraph
from app.guest360_constructs.identity.keyring_table import KeyringTable
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream
from app.infrastructure.workstream_stack import WorkstreamStack
from aws_cdk import Duration, aws_kinesis


class Identity(WorkstreamStack):
    """
    Infrastructure Identity
    """

    keyring_table: KeyringTable

    identity_graph: IdentityGraph

    def __init__(self, scope: Stack, construct_id: str, environment_config: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)  # type: ignore
        environment = self.node.try_get_context("environment")
        environment_config["unused"] = "unused"

        directory = os.path.dirname(os.path.realpath(__file__))
        try:
            with open(
                f"{directory}/configs/{environment}-identity.yaml", "r", encoding="utf-8"
            ) as identity_config_yaml:
                processing_config = yaml.safe_load(identity_config_yaml)
        except FileNotFoundError:
            with open(f"{directory}/configs/local-identity.yaml", "r", encoding="utf-8") as processing_config_yaml:
                processing_config = yaml.safe_load(processing_config_yaml)

        # Keyring table:
        identity_table_name = processing_config["identity-table-name"]

        # TODO: Delete Code After Prod Deploy
        # Used because delete and update operations
        # We should definitely have a global prefix
        # Delete is not a big deal because of the future dataloader
        suffix = environment

        self.keyring_table = KeyringTable(self, "keyring_table", {"table_name": f"{identity_table_name}-{suffix}"})  # type: ignore

        # Graph tables:
        identity_nodes_table_name = processing_config["identity-nodes-table-name"]
        identity_edges_table_name = processing_config["identity-edges-table-name"]

        self.identity_graph = IdentityGraph(
            self,  # type: ignore
            "identity_graph",
            {
                "node_table_name": f"{identity_nodes_table_name}-{suffix}",
                "edge_table_name": f"{identity_edges_table_name}-{suffix}",
            },
        )

        # Identity Notification Stream
        identity_kinesis_stream_name = processing_config["identity-kinesis-stream-name"]

        kinesis_identity_stream_props = {
            "retention_period": Duration.hours(24),
            "stream_mode": aws_kinesis.StreamMode.ON_DEMAND
            # In order for stage to be moved to provisioned, it needs to be done so by moving the shard count to 2 instead of 1, and later to 1.
            if environment in ("stage", "load", "prod") else aws_kinesis.StreamMode.PROVISIONED,
            "shard_count": None if environment in ("stage", "load", "prod") else 1,
            "stream_name": identity_kinesis_stream_name,
        }

        self.identity_notification_stream = Guest360KinesisDatastream(
            self, construct_id=identity_kinesis_stream_name, props=kinesis_identity_stream_props  # type: ignore
        )

        self.keyring_table.export_ssm()

        self.identity_graph.export_ssm()
