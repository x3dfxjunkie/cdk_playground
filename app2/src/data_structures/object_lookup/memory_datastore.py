"""
This is a concrete implemetnation of a datastore.

Designed for only testing purposes.
"""
from typing import Optional, List

import app.src.data_structures.profiles.profile as profile
import app.src.data_structures.identity.identity as identity
import app.src.data_structures.events.lightning_lane_event as ll_event
from app.src.data_structures.object_lookup.datastore import Datastore


class MemoryDatastore(Datastore):
    """
    Implementation of a Datastore intended for testing.
    """

    def __init__(self):
        self._kvstore = {}

    def fetch_profile(self, atomic_id: str) -> Optional[profile.Profile]:
        """
        Return an atomic id given a key.
        """
        profile_json = self._kvstore.get(atomic_id)
        if profile_json is None:
            return None
        return profile.Profile.schema().loads(profile_json)

    def add_keyvalue(self, key: str, val: profile.Profile):
        """
        Add a key to the keystore.
        This is intended to help populate a datastore for testing.
        """
        self._kvstore[key] = val

    def get_events(self, atomic_id: str, event_type: str, event_start_time: int, event_end_time: int, limit: int = 100) -> Optional[List[ll_event.LightningLaneEvent]]:
        pass

    def fetch_atomic_id(self, domain: str, identifier: str) -> Optional[str]:
        """
        Return an atomic id given a key.
        """
        key = f"{domain}#{identifier}"
        return self._kvstore.get(key)

    def link_identity(self, first_domain: str, first_identifier: str, second_domain: str, second_identifier: str):
        """Given two identifiers, link both of them to a single atomic_id.
        If there is already an association between these two, throw an exception.

        Args:
            first_identifier (str): The first identifier you want to link.
            second_identifier (str): The second identifier you want to link.
        """
        print("link_identity not yet implemented")

    def unlink_identity(self, atomic_id: str, identifier: str):
        """Given an atomic_id and an identifier, remove the identifier from the identity graph and keyring.

        Args:
            atomic_id (str): atomic_id of the identity you want to remove an identifier from.
            identifier (str): The identifier you want to remove.
        """
        print("unlink_identity not yet implemented")

    def get_identity_node(self, domain: str, identifier: str) -> Optional[identity.IdentityNode]:
        """Method which returns an identity graph node.

        Args:
            domain (str): Domain of the identity component
            identifier (str): Identifier related to the identity component

        Returns:
            identity.IdentityNode: An identity node from the identity graph.
        """
        return None

    def get_identity_edges(self, source_node: identity.IdentityNode) -> List[identity.IdentityEdge]:
        """Method which returns a list of edges given a source identity node.

        Args:
            source_node (IdentityNode): The source node you want to get every connection of.

        Returns:
            Optional[List[IdentityEdge]]: A list of edges associated with the source node.
        """
        return []

    def get_identity_graph(self) -> identity.IdentityGraph:
        """Returns all nodes and edges in the graph.

        Returns:
            TypedDict[List[IdentityNode], List[IdentityEdge]]: A collection of nodes and edges.
        """
        return identity.IdentityGraph([], [])

    def _create_atomic_id(self, domain, identifier):
        key = f"{domain}#{identifier}"
        atomic_id = self._generate_atomic_id()
        self._kvstore[key] = atomic_id

    def get_known_domains(self) -> list:
        """
        Return a list of valid domains.
        """
        return ["swid"]
