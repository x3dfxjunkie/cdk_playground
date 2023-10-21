"""
Module to facilitate the logic for looking up various IDs and returning an atomic_id.
"""
from __future__ import annotations

from typing import Optional, List
import importlib
import json
import time
from functools import reduce

from app.src.data_structures.profiles import profile
from app.src.data_structures.identity.identity import IdentityNode, IdentityEdge, IdentityGraph
from app.src.data_structures.events.base_event import BaseEvent

from .dynamodb_datastore import DynamoDBDatastore


class Lookup:
    """
    Top level class to return atomic ids given any id from a particular domain.

    Implements the strategy pattern for retrieving from a datastore.
    """

    def __init__(self, datastore):
        self._datastore = datastore

    def profile_lookup(self, atomic_id) -> profile.Profile:
        """
        Given a domain, check to see if the domain is valid then retrieve the key.
        """
        return self._get_profile_from_atomic_id(atomic_id)

    def get_events_from_profile(self, atomic_id: str, event_start_time, event_end_time):
        event_start_time_unixtime = int(time.mktime(event_start_time.timetuple()) * 1000)
        event_end_time_unixtime = int(time.mktime(event_end_time.timetuple()) * 1000)
        return self._datastore.get_events(
            atomic_id, "lightning_lane", event_start_time_unixtime, event_end_time_unixtime
        )

    def _get_profile_from_atomic_id(self, atomic_id):
        """
        Given a swid, construct a composite key and retrieve the atomic id.
        """
        key = f"{atomic_id}"
        return self._datastore.fetch_profile(key)

    def atomic_id_lookup(self, domain, identifier) -> str:
        """
        Given a domain, check to see if the domain is valid then retrieve the key.
        """
        return self._get_atomic_id(domain, identifier)

    def fetch_or_create_atomic_id(self, domain, identifier) -> str:
        return self._get_or_create_atomic_id(domain, identifier)

    def link_identity(self, first_domain: str, first_identifier: str, second_domain: str, second_identifier: str):
        """Given two identifiers, link both of them to a single atomic_id.
        If there is already an association between these two, propogate the atomic_id from the second_identifier to the first_identifier

        Args:
            first_identifier (str): The first identifier you want to link.
            second_identifier (str): The second identifier you want to link.
        """
        self._datastore.link_identity(first_domain, first_identifier, second_domain, second_identifier)

    def unlink_identity(self, domain: str, identifier: str):
        """Given an atomic_id and an identifier, remove the identifier from the identity graph and keyring.

        Args:
            atomic_id (str): atomic_id of the identity you want to remove an identifier from.
            identifier (str): The identifier you want to remove.
        """
        self._datastore.unlink_identity(f"{domain}#{identifier}")

    def get_identity_node(self, domain: str, identifier: str) -> Optional[IdentityNode]:
        """Method which returns an identity graph node.

        Args:
            domain (str): Domain of the identity component
            identifier (str): Identifier related to the identity component

        Returns:
            identity.IdentityNode: An identity node from the identity graph.
        """
        return self._datastore.get_identity_node(domain, identifier)

    def get_identity_edges(self, source_node: IdentityNode) -> List[IdentityEdge]:
        """Method which returns a list of edges given a source identity node.

        Args:
            source_node (IdentityNode): The source node you want to get every connection of.

        Returns:
            Optional[List[IdentityEdge]]: A list of edges associated with the source node.
        """
        return self._datastore.get_identity_edges(source_node)

    def get_identity_graph(self) -> IdentityGraph:
        """Returns all nodes and edges in the graph.

        Returns:
            TypedDict[List[IdentityNode], List[IdentityEdge]]: A collection of nodes and edges.
        """
        return self._datastore.get_identity_graph()

    def _get_atomic_id(self, domain, identifier):
        """
        Given a swid, construct a composite key and retrieve the atomic id.
        """
        return self._datastore.fetch_atomic_id(domain, identifier)

    def _get_or_create_atomic_id(self, domain, identifier):
        """
        Given a swid, construct a composite key and retrieve the atomic id.
        """
        return self._datastore.fetch_or_create_atomic_id(domain, identifier)


class DynamoDBLookupFactory:
    """
    Construct a DynamoDB backed lookup class.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_dynamodb_lookup(
        dynamodb_resource,
        kinesis_client,
        profile_table_name=None,
        events_table_name=None,
        identity_table_name=None,
        identity_nodes_table_name=None,
        identity_edges_table_name=None,
        identity_notification_stream_name=None,
    ) -> Lookup:
        dynamodb_datastore = DynamoDBDatastore(
            dynamodb_resource=dynamodb_resource,
            kinesis_client=kinesis_client,
            identity_table_name=identity_table_name,
            identity_nodes_table_name=identity_nodes_table_name,
            identity_edges_table_name=identity_edges_table_name,
            profile_table_name=profile_table_name,
            events_table_name=events_table_name,
            identity_notification_stream_name=identity_notification_stream_name,
        )
        dynamodb_lookup = Lookup(dynamodb_datastore)
        return dynamodb_lookup


class EventDeserializer:
    """Deserializes Raw Events from dynamo"""

    @staticmethod
    def get_event_from_dynamo(raw_event: dict) -> BaseEvent:
        try:
            event_json = json.loads(raw_event["event"]["S"])

            class_name = str(event_json.get("className"))
            # convert pascal class name into snake case
            file = reduce(lambda x, y: x + ("_" if y.isupper() else "") + y, class_name).lower()
            module = importlib.import_module(f"app.src.data_structures.events.{file}")
            event_class_obj = getattr(module, class_name)

            # call the schema loads for the detected class
            event_object = event_class_obj.schema().loads(json.dumps(event_json))
        except (ModuleNotFoundError, ImportError) as error:
            raise ValueError(f"Could not import {class_name}") from error
        except (KeyError, ValueError, json.decoder.JSONDecodeError) as error:
            raise ValueError("Failed to deserialize event from dynamo") from error
        return event_object
