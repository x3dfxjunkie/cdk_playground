"""
Module for abstract classes defining methods for implementing datastores.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, List
import uuid

import app.src.data_structures.profiles.profile as profile
import app.src.data_structures.events.lightning_lane_event as ll_event
import app.src.data_structures.identity.identity as identity


class Datastore(ABC):
    """
    Abstract class needed to implement datastore operations.
    """

    @abstractmethod
    def fetch_profile(self, atomic_id: str) -> Optional[profile.Profile]:
        """
        Fetch a profile given an atomic id.
        """

    @abstractmethod
    def get_events(self, atomic_id: str, event_type: str, event_start_time: int, event_end_time: int, limit: int = 100) -> Optional[List[ll_event.LightningLaneEvent]]:
        """
        Returns list of events associated with atomic_id
        """

    @abstractmethod
    def fetch_atomic_id(self, domain: str, identifier: str) -> str:
        """
        Fetch an atomic ID given a key.
        """

    @abstractmethod
    def get_known_domains(self) -> list:
        """
        Get a list of known key domains.
        """

    def fetch_or_create_atomic_id(self, domain: str, identifier: str) -> Optional[str]:
        """
        Fetch an atomic ID given a key or create a new atomic ID if none found.
        """
        atomic_id = self.fetch_atomic_id(domain, identifier)
        if atomic_id is None:
            atomic_id = self._create_atomic_id(domain, identifier)
        return atomic_id

    def _generate_atomic_id(self) -> str:
        return str(uuid.uuid4())

    @abstractmethod
    def _create_atomic_id(self, domain: str, identifier: str):
        """
        Create an atomic id given a key.
        """

    @abstractmethod
    def link_identity(self, first_identifier: str, second_identifier: str):
        """Given two identifiers, link both of them to a single atomic_id.
        If there is already an association between these two, throw an exception.

        Args:
            first_identifier (str): The first identifier you want to link.
            second_identifier (str): The second identifier you want to link.
        """

    @abstractmethod
    def unlink_identity(self, identifier: str):
        """Given an atomic_id and an identifier, remove the identifier from the identity graph and keyring.

        Args:
            atomic_id (str): atomic_id of the identity you want to remove an identifier from.
            identifier (str): The identifier you want to remove.
        """

    @abstractmethod
    def get_identity_node(self, key: str) -> identity.IdentityNode:
        """Method which returns an identity graph node.

        Args:
            domain (str): Domain of the identity component
            identifier (str): Identifier related to the identity component

        Returns:
            identity.IdentityNode: An identity node from the identity graph.
        """

    @abstractmethod
    def get_identity_edges(self, source_node: identity.IdentityNode) -> List[identity.IdentityEdge]:
        """Method which returns a list of edges given a source identity node.

        Args:
            source_node (IdentityNode): The source node you want to get every connection of.

        Returns:
            Optional[List[IdentityEdge]]: A list of edges associated with the source node.
        """

    @abstractmethod
    def get_identity_graph(self) -> identity.IdentityGraph:
        """Returns all nodes and edges in the graph.

        Returns:
            TypedDict[List[IdentityNode], List[IdentityEdge]]: A collection of nodes and edges.
        """
