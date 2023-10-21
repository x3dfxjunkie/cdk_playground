"""
Logic to connect and handle DynamoDB requests.
"""
import json
import uuid
from typing import Optional, List, Union
from datetime import datetime

from boto3.dynamodb.conditions import Key

import app.src.data_structures.events.lightning_lane_event as ll_event
from app.src.data_structures.identity import identity
from app.src.data_structures.profiles import profile
from app.src.data_structures.object_lookup.datastore import Datastore

from aws_lambda_powertools import Logger
from opentelemetry import trace

logging = Logger(service=__name__)
trace.get_tracer_provider()
tracer = trace.get_tracer(__name__)


class DynamoDBDatastore(Datastore):
    """
    Concrete implementation of Datastore using DynamoDB as a backend.
    """

    @tracer.start_as_current_span("init_datastore")
    def __init__(
        self,
        dynamodb_resource,
        kinesis_client,
        identity_table_name=None,
        identity_nodes_table_name=None,
        identity_edges_table_name=None,
        profile_table_name=None,
        events_table_name=None,
        identity_notification_stream_name=None,
    ):
        client = dynamodb_resource.meta.client

        identity_tablename = identity_table_name
        identity_nodes_tablename = identity_nodes_table_name
        identity_edges_tablename = identity_edges_table_name
        profile_tablename = profile_table_name
        events_tablename = events_table_name

        self._setup_aws_resources(
            dynamodb_resource,
            kinesis_client,
            identity_notification_stream_name,
            identity_tablename,
            identity_nodes_tablename,
            identity_edges_tablename,
            profile_tablename,
            events_tablename,
        )

    def _setup_aws_resources(
        self,
        dynamodb_resource,
        kinesis_client,
        identity_notification_stream_name,
        identity_tablename,
        identity_nodes_tablename,
        identity_edges_tablename,
        profile_tablename,
        events_tablename,
    ):
        self.kinesis_client = kinesis_client
        self.identity_notification_stream_name = identity_notification_stream_name

        identity_dynamo_table = dynamodb_resource.Table(identity_tablename)
        self._identity_dynamo_table = identity_dynamo_table

        identity_nodes_dynamo_table = dynamodb_resource.Table(identity_nodes_tablename)
        self._identity_nodes_dynamo_table = identity_nodes_dynamo_table

        identity_edges_dynamo_table = dynamodb_resource.Table(identity_edges_tablename)
        self._identity_edges_dynamo_table = identity_edges_dynamo_table

        profile_dynamo_table = dynamodb_resource.Table(profile_tablename)
        self._profile_dynamo_table = profile_dynamo_table

        events_dynamo_table = dynamodb_resource.Table(events_tablename)
        self._events_dynamo_table = events_dynamo_table

    @tracer.start_as_current_span("fetch_profile")
    def fetch_profile(self, atomic_id: str) -> Optional[profile.Profile]:
        """
        Given a business key in DynamoDB, fetch the atomic_id that
        is associated with that business key.
        """
        response = self._profile_dynamo_table.get_item(Key={"atomic_id": atomic_id})
        item = response.get("Item")
        if item is None:
            return None
        json_profile = item.get("profile")
        if json_profile is None:
            return None
        guest_profile = profile.Profile.schema().loads(json_profile)
        return guest_profile

    @tracer.start_as_current_span("get_events")
    def get_events(
        self, atomic_id: str, event_type: str, event_start_time: int, event_end_time: int, limit: int = 100
    ) -> Optional[List[ll_event.LightningLaneEvent]]:
        condition = Key("atomic_id#event_name").eq(atomic_id + "#" + event_type) & Key("event_time").between(
            event_start_time, event_end_time
        )
        response = self._events_dynamo_table.query(
            KeyConditionExpression=condition, ConsistentRead=True, ScanIndexForward=False, Limit=limit
        )
        lightning_lane_events: List[ll_event.LightningLaneEvent] = [
            ll_event.LightningLaneEvent.from_json(item["event"]) for item in response["Items"]
        ]
        return lightning_lane_events

    @tracer.start_as_current_span("fetch_or_create_atomic_id")
    def fetch_or_create_atomic_id(self, domain: str, identifier: str) -> Optional[str]:
        # Add a node to the id graph if doesn't exist.

        atomic_id = super().fetch_or_create_atomic_id(domain, identifier)
        if self.get_identity_node(domain, identifier) is None:
            self.create_identity_node(domain, identifier, atomic_id)
        return atomic_id

    @tracer.start_as_current_span("fetch_atomic_id")
    def fetch_atomic_id(self, domain: str, identifier: str) -> Optional[str]:
        """
        Given a business key in DynamoDB, fetch the atomic_id that
        is associated with that business key.
        """
        key = f"{domain}#{identifier}"
        response = self._identity_dynamo_table.get_item(Key={"type#id-PK": key}, ConsistentRead=True)
        item = response.get("Item")
        if item is not None:
            atomic_id = item["atomic_id"]
        else:
            atomic_id = None
        return atomic_id

    @tracer.start_as_current_span("_create_atomic_id")
    def _create_atomic_id(self, domain, identifier, connection_type="dynamic") -> Optional[str]:
        atomic_id = self._generate_atomic_id()
        key = f"{domain}#{identifier}"
        self._identity_dynamo_table.put_item(
            Item={"type#id-PK": key, "atomic_id": atomic_id, "connection_type": connection_type}
        )
        return atomic_id

    def get_known_domains(self) -> list:
        """
        Return list of valid business key domains.
        """
        return ["swid", "ealinkid"]

    @tracer.start_as_current_span("link_identity")
    def link_identity(self, first_domain: str, first_identifier: str, second_domain: str, second_identifier: str):
        """Given two identifiers, link both of them to a single atomic_id.
        If there is already an association between these two, throw an exception.

        Args:
            first_identifier (str): The first identifier you want to link.
            second_identifier (str): The second identifier you want to link.
        """
        key_1 = f"{first_domain}#{first_identifier}"
        key_2 = f"{second_domain}#{second_identifier}"

        atomic_id_1 = self.fetch_atomic_id(first_domain, first_identifier)
        atomic_id_2 = self.fetch_atomic_id(second_domain, second_identifier)
        # If neither key has been added, create an atomic_id and link them.
        if atomic_id_1 is None and atomic_id_2 is None:
            atomic_id_1 = self._create_atomic_id(first_domain, first_identifier, connection_type="explicit")
            self._identity_dynamo_table.put_item(
                Item={"type#id-PK": key_2, "atomic_id": atomic_id_1, "connection_type": "explicit"}
            )

            # Update identity nodes with potentially new atomic_ids
            self.create_identity_node(first_domain, first_identifier, atomic_id_1)
            self.create_identity_node(second_domain, second_identifier, atomic_id_1)

            # Add two edges for undirected graph
            identity_edge_1 = identity.IdentityEdge(
                source_node=key_2, target_node=key_1, active=True, created_date=datetime.now(), deactivated_date=None
            )
            identity_edge_2 = identity.IdentityEdge(
                source_node=key_1, target_node=key_2, active=True, created_date=datetime.now(), deactivated_date=None
            )
            with self._identity_edges_dynamo_table.batch_writer() as batch:
                batch.put_item(
                    Item={"source_node": key_2, "target_node": key_1, "identity_edge": identity_edge_1.to_json()}
                )
                batch.put_item(
                    Item={"source_node": key_1, "target_node": key_2, "identity_edge": identity_edge_2.to_json()}
                )
            return
        # If only one of the atomic_ids do not exist, link the identity component to existing atomic_id
        if atomic_id_1 is None:
            self._identity_dynamo_table.put_item(
                Item={"type#id-PK": key_1, "atomic_id": atomic_id_2, "connection_type": "explicit"}
            )

            # Update identity nodes with potentially new atomic_ids
            self.create_identity_node(first_domain, first_identifier, atomic_id_2)
            self.create_identity_node(second_domain, second_identifier, atomic_id_2)

            # Add two edges for undirected graph
            identity_edge_1 = identity.IdentityEdge(
                source_node=key_2, target_node=key_1, active=True, created_date=datetime.now(), deactivated_date=None
            )
            identity_edge_2 = identity.IdentityEdge(
                source_node=key_1, target_node=key_2, active=True, created_date=datetime.now(), deactivated_date=None
            )
            with self._identity_edges_dynamo_table.batch_writer() as batch:
                batch.put_item(
                    Item={"source_node": key_2, "target_node": key_1, "identity_edge": identity_edge_1.to_json()}
                )
                batch.put_item(
                    Item={"source_node": key_1, "target_node": key_2, "identity_edge": identity_edge_2.to_json()}
                )
            return
        if atomic_id_2 is None:
            self._identity_dynamo_table.put_item(
                Item={"type#id-PK": key_2, "atomic_id": atomic_id_1, "connection_type": "explicit"}
            )

            # Update identity nodes with potentially new atomic_ids
            self.create_identity_node(first_domain, first_identifier, atomic_id_1)
            self.create_identity_node(second_domain, second_identifier, atomic_id_1)

            # Add two edges for undirected graph
            identity_edge_1 = identity.IdentityEdge(
                source_node=key_2, target_node=key_1, active=True, created_date=datetime.now(), deactivated_date=None
            )
            identity_edge_2 = identity.IdentityEdge(
                source_node=key_1, target_node=key_2, active=True, created_date=datetime.now(), deactivated_date=None
            )
            with self._identity_edges_dynamo_table.batch_writer() as batch:
                batch.put_item(
                    Item={"source_node": key_2, "target_node": key_1, "identity_edge": identity_edge_1.to_json()}
                )
                batch.put_item(
                    Item={"source_node": key_1, "target_node": key_2, "identity_edge": identity_edge_2.to_json()}
                )
            return
        # If both atomic_ids are equal, there is nothing to do for the keyring, but a connection should still be made.
        if atomic_id_1 == atomic_id_2:
            # Update identity nodes with potentially new atomic_ids
            self.create_identity_node(first_domain, first_identifier, atomic_id_1)
            self.create_identity_node(second_domain, second_identifier, atomic_id_1)

            # Add two edges for undirected graph
            identity_edge_1 = identity.IdentityEdge(
                source_node=key_2, target_node=key_1, active=True, created_date=datetime.now(), deactivated_date=None
            )
            identity_edge_2 = identity.IdentityEdge(
                source_node=key_1, target_node=key_2, active=True, created_date=datetime.now(), deactivated_date=None
            )
            with self._identity_edges_dynamo_table.batch_writer() as batch:
                batch.put_item(
                    Item={"source_node": key_2, "target_node": key_1, "identity_edge": identity_edge_1.to_json()}
                )
                batch.put_item(
                    Item={"source_node": key_1, "target_node": key_2, "identity_edge": identity_edge_2.to_json()}
                )
            return
        if atomic_id_1 != atomic_id_2:
            self.unlink_identity(key_2)
            self._identity_dynamo_table.put_item(
                Item={"type#id-PK": key_2, "atomic_id": atomic_id_1, "connection_type": "explicit"}
            )
            self._notify_split_event(atomic_id_2, atomic_id_1)

            # Update identity nodes with potentially new atomic_ids
            self.create_identity_node(first_domain, first_identifier, atomic_id_1)
            self.create_identity_node(second_domain, second_identifier, atomic_id_1)

            # Add two edges for undirected graph
            identity_edge_1 = identity.IdentityEdge(
                source_node=key_2, target_node=key_1, active=True, created_date=datetime.now(), deactivated_date=None
            )
            identity_edge_2 = identity.IdentityEdge(
                source_node=key_1, target_node=key_2, active=True, created_date=datetime.now(), deactivated_date=None
            )
            with self._identity_edges_dynamo_table.batch_writer() as batch:
                batch.put_item(
                    Item={"source_node": key_2, "target_node": key_1, "identity_edge": identity_edge_1.to_json()}
                )
                batch.put_item(
                    Item={"source_node": key_1, "target_node": key_2, "identity_edge": identity_edge_2.to_json()}
                )
            self._notify_merge_event(atomic_id_2, atomic_id_1)
            return

    @tracer.start_as_current_span("unlink_identity")
    def unlink_identity(self, identifier: str):
        """Given an atomic_id and an identifier, remove the identifier from the identity graph and keyring.

        Args:
            atomic_id (str): atomic_id of the identity you want to remove an identifier from.
            identifier (str): The identifier you want to remove.
        """
        self._identity_dynamo_table.delete_item(Key={"type#id-PK": identifier})

    @tracer.start_as_current_span("create_identity_node")
    def create_identity_node(self, domain: str, identifier: str, atomic_id: Union[str, None]):
        new_identity_node = identity.IdentityNode(domain, identifier, atomic_id)
        new_identity_node_dynamodb = {}
        new_identity_node_dynamodb["node_id"] = f"{domain}#{identifier}"
        new_identity_node_dynamodb["identity_node"] = new_identity_node.to_json()
        self._identity_nodes_dynamo_table.put_item(Item=new_identity_node_dynamodb)

    @tracer.start_as_current_span("get_identity_node")
    def get_identity_node(self, domain: str, identifier: str) -> Optional[identity.IdentityNode]:
        """Method which returns an identity graph node.

        Args:
            domain (str): Domain of the identity component
            identifier (str): Identifier related to the identity component

        Returns:
            identity.IdentityNode: An identity node from the identity graph.
        """
        key = f"{domain}#{identifier}"
        response = self._identity_nodes_dynamo_table.get_item(Key={"node_id": key})
        item = response.get("Item")
        if item is None:
            return None
        json_identity_node = item.get("identity_node")
        if json_identity_node is None:
            return None
        identity_node = identity.IdentityNode.schema().loads(json_identity_node)
        return identity_node

    @tracer.start_as_current_span("get_identity_edges")
    def get_identity_edges(self, source_node: identity.IdentityNode) -> List[identity.IdentityEdge]:
        """Method which returns a list of edges given a source identity node.

        Args:
            source_node (IdentityNode): The source node you want to get every connection of.

        Returns:
            Optional[List[IdentityEdge]]: A list of edges associated with the source node.
        """
        hash_key = f"{source_node.domain}#{source_node.identifier}"
        response = self._identity_edges_dynamo_table.query(
            # Return all of the elements (target_node) given a source node. Sort key is implicitly returning all.
            KeyConditionExpression=Key("source_node").eq(hash_key)
        )
        edges_list: List[identity.IdentityEdge] = [
            identity.IdentityEdge.schema().loads(item.get("identity_edge")) for item in response["Items"]
        ]
        return edges_list

    @tracer.start_as_current_span("get_identity_graph")
    def get_identity_graph(self) -> identity.IdentityGraph:
        """Returns all nodes and edges in the graph.

        Returns:
            IdentityGraph: A collection of nodes and edges.
        """
        nodes = self._get_all_nodes()
        edges = self._get_all_edges()
        return identity.IdentityGraph(nodes, edges)

    @tracer.start_as_current_span("_get_all_nodes")
    def _get_all_nodes(self):
        response = self._identity_nodes_dynamo_table.scan()
        nodes: List[identity.IdentityNode] = [
            identity.IdentityNode.schema().loads(item["identity_node"]) for item in response["Items"]
        ]
        return nodes

    @tracer.start_as_current_span("_get_all_edges")
    def _get_all_edges(self):
        response = self._identity_edges_dynamo_table.scan()
        edges: List[identity.IdentityEdge] = [
            identity.IdentityEdge.schema().loads(item["identity_edge"]) for item in response["Items"]
        ]
        return edges

    @tracer.start_as_current_span("_notify_merge_event")
    def _notify_merge_event(self, old_atomic_id, new_atomic_id):
        try:
            self.kinesis_client.put_record(
                StreamName=self.identity_notification_stream_name,
                Data=json.dumps(f"{old_atomic_id} and {new_atomic_id} have merged, pull latest identity components."),
                PartitionKey=str(uuid.uuid4()),
            )
        except Exception as e:
            raise e

    @tracer.start_as_current_span("_notify_split_event")
    def _notify_split_event(self, first_atomic_id, second_atomic_id):
        try:
            self.kinesis_client.put_record(
                StreamName=self.identity_notification_stream_name,
                Data=json.dumps(
                    f"{first_atomic_id} has split into {second_atomic_id}, pull latest identity components."
                ),
                PartitionKey=str(uuid.uuid4()),
            )
        except Exception as e:
            raise e
