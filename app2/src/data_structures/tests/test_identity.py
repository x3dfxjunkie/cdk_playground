"""
Tests for identity functions and methods
"""
# Disable pylint redefinition of name: that is how fixtures work.
# pylint: disable=W0621
import boto3
import pytest
from moto import mock_dynamodb, mock_kinesis

from app.src.data_structures.object_lookup import dynamodb_datastore, lookup
from app.src.data_structures.tests.utils.setup_dynamodb import setup_dynamodb
from app.src.data_structures.identity import identity


@pytest.fixture(scope="module")
def identity_datastore():
    resource = boto3.resource("dynamodb")
    kinesis_client = boto3.client("kinesis")
    yield dynamodb_datastore.DynamoDBDatastore(
        resource,
        kinesis_client,
        identity_table_name="identity",
        identity_nodes_table_name="identity_nodes",
        identity_edges_table_name="identity_edges",
        profile_table_name="profile",
        events_table_name="events",
        identity_notification_stream_name="identity_notification_stream",
    )


@mock_dynamodb
@mock_kinesis
def test_link_identities_same_domain_none_exists(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")

    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    atomic_id_from_swid_1 = identity_engine.atomic_id_lookup("swid", "swid_1")
    atomic_id_from_swid_2 = identity_engine.atomic_id_lookup("swid", "swid_2")
    assert atomic_id_from_swid_1 is not None
    assert atomic_id_from_swid_1 is not None
    assert atomic_id_from_swid_1 == atomic_id_from_swid_2


@mock_dynamodb
@mock_kinesis
def test_link_identities_same_domain_one_exists(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")
    identity_engine = lookup.Lookup(identity_datastore)
    # Create the first identity atomic_id first
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    # Create the second identity atomic_id first
    identity_engine.fetch_or_create_atomic_id("swid", "swid_4")
    identity_engine.link_identity("swid", "swid_3", "swid", "swid_4")
    atomic_id_from_swid_1 = identity_engine.atomic_id_lookup("swid", "swid_1")
    atomic_id_from_swid_2 = identity_engine.atomic_id_lookup("swid", "swid_2")
    assert atomic_id_from_swid_1 is not None
    assert atomic_id_from_swid_2 is not None
    assert atomic_id_from_swid_1 == atomic_id_from_swid_2


@mock_dynamodb
@mock_kinesis
def test_link_identities_same_domain_atomic_id_exists(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")
    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    identity_engine.fetch_or_create_atomic_id("swid", "swid_4")
    identity_engine.link_identity("swid", "swid_3", "swid", "swid_4")
    atomic_id_from_swid_1 = identity_engine.atomic_id_lookup("swid", "swid_1")
    atomic_id_from_swid_2 = identity_engine.atomic_id_lookup("swid", "swid_2")
    atomic_id_from_swid_3 = identity_engine.atomic_id_lookup("swid", "swid_3")
    atomic_id_from_swid_4 = identity_engine.atomic_id_lookup("swid", "swid_4")
    assert atomic_id_from_swid_1 is not None
    assert atomic_id_from_swid_2 is not None
    assert atomic_id_from_swid_3 is not None
    assert atomic_id_from_swid_4 is not None
    assert atomic_id_from_swid_1 == atomic_id_from_swid_2
    assert atomic_id_from_swid_3 == atomic_id_from_swid_4


@mock_dynamodb
@mock_kinesis
def test_link_identities_same_domain_link_exists_same_atomic_id(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")
    identity_engine = lookup.Lookup(identity_datastore)
    atomic_id_1 = identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    atomic_id_2 = identity_engine.fetch_or_create_atomic_id("swid", "swid_2")
    assert atomic_id_1 != atomic_id_2
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    atomic_id_1 = identity_engine.atomic_id_lookup("swid", "swid_1")
    atomic_id_2 = identity_engine.atomic_id_lookup("swid", "swid_2")
    assert atomic_id_1 == atomic_id_2


@mock_dynamodb
@mock_kinesis
def test_link_identities_same_domain_link_exists_diff_atomic_ids(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")
    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    atomic_id_1 = identity_engine.atomic_id_lookup("swid", "swid_1")
    atomic_id_2 = identity_engine.atomic_id_lookup("swid", "swid_2")
    assert atomic_id_1 == atomic_id_2


@mock_dynamodb
@mock_kinesis
def test_identity_node_created(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")
    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_node = identity_engine.get_identity_node("swid", "swid_1")
    assert isinstance(identity_node, identity.IdentityNode)
    assert identity_node.identifier == "swid_1"


@mock_dynamodb
@mock_kinesis
def test_identity_node_two_created(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")

    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    identity_node_1 = identity_engine.get_identity_node("swid", "swid_1")
    identity_node_2 = identity_engine.get_identity_node("swid", "swid_2")
    assert identity_node_1 is not None
    assert identity_node_2 is not None


@mock_dynamodb
@mock_kinesis
def test_identity_edges_returns_empty_list(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")
    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_node = identity_engine.get_identity_node("swid", "swid_1")
    edges = []
    if identity_node is not None:
        edges = identity_engine.get_identity_edges(identity_node)
    assert len(edges) == 0


@mock_dynamodb
@mock_kinesis
def test_identity_edges_returns_list_one_object(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")

    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_node = identity_engine.get_identity_node("swid", "swid_1")
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    edges = []
    if identity_node is not None:
        edges = identity_engine.get_identity_edges(identity_node)
    assert len(edges) == 1


@mock_dynamodb
@mock_kinesis
def test_identity_edges_returns_list_two_objects(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")

    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_node = identity_engine.get_identity_node("swid", "swid_1")
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_3")
    edges = []
    if identity_node is not None:
        edges = identity_engine.get_identity_edges(identity_node)
    assert len(edges) == 2


@mock_dynamodb
@mock_kinesis
def test_identity_edges_returns_list_two_objects_three_linked_to_same_atomic_id(identity_datastore):
    """Create a chain of assosiated IDs and ensure the chain lengths and atomic_ids are expected."""
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")

    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_2")
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_3")
    identity_engine.link_identity("swid", "swid_2", "swid", "swid_4")
    identity_node_1 = identity_engine.get_identity_node("swid", "swid_1")
    identity_node_2 = identity_engine.get_identity_node("swid", "swid_2")
    edges_1 = []
    edges_2 = []
    if identity_node_1 is not None:
        edges_1 = identity_engine.get_identity_edges(identity_node_1)
    if identity_node_2 is not None:
        edges_2 = identity_engine.get_identity_edges(identity_node_2)

    atomic_id_1 = identity_engine.atomic_id_lookup("swid", "swid_1")
    atomic_id_2 = identity_engine.atomic_id_lookup("swid", "swid_2")
    atomic_id_3 = identity_engine.atomic_id_lookup("swid", "swid_3")
    atomic_id_4 = identity_engine.atomic_id_lookup("swid", "swid_4")
    assert len(edges_1) == 2
    assert len(edges_2) == 2
    assert atomic_id_1 == atomic_id_2 == atomic_id_3 == atomic_id_4


@mock_dynamodb
@mock_kinesis
def test_identity_complicated_edges_still_results_in_two_atomic_ids(identity_datastore):
    """Create a chain of assosiated IDs and ensure the chain lengths and atomic_ids are expected."""
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")
    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_engine.fetch_or_create_atomic_id("swid", "swid_2")

    identity_engine.link_identity("swid", "swid_1", "swid", "swid_3")
    identity_engine.link_identity("swid", "swid_2", "swid", "swid_4")

    atomic_id_1 = identity_engine.atomic_id_lookup("swid", "swid_1")
    atomic_id_2 = identity_engine.atomic_id_lookup("swid", "swid_2")
    atomic_id_3 = identity_engine.atomic_id_lookup("swid", "swid_3")
    atomic_id_4 = identity_engine.atomic_id_lookup("swid", "swid_4")

    assert atomic_id_1 == atomic_id_3
    assert atomic_id_2 == atomic_id_4

    # This should result in an atomic_id that is shared between swid1, 3, and 4
    identity_engine.link_identity("swid", "swid_1", "swid", "swid_4")

    atomic_id_1 = identity_engine.atomic_id_lookup("swid", "swid_1")
    atomic_id_2 = identity_engine.atomic_id_lookup("swid", "swid_2")
    atomic_id_3 = identity_engine.atomic_id_lookup("swid", "swid_3")
    atomic_id_4 = identity_engine.atomic_id_lookup("swid", "swid_4")

    assert atomic_id_1 == atomic_id_3 == atomic_id_4
    assert atomic_id_2 != atomic_id_1

    identity_node_1 = identity_engine.get_identity_node("swid", "swid_1")
    identity_node_2 = identity_engine.get_identity_node("swid", "swid_2")
    identity_node_3 = identity_engine.get_identity_node("swid", "swid_3")
    identity_node_4 = identity_engine.get_identity_node("swid", "swid_4")

    edges_1 = identity_engine.get_identity_edges(identity_node_1)
    edges_2 = identity_engine.get_identity_edges(identity_node_2)
    edges_3 = identity_engine.get_identity_edges(identity_node_3)
    edges_4 = identity_engine.get_identity_edges(identity_node_4)

    # Identity Node 1 and 4 should still have two connections, even though the atomic_id has changed.
    # DISCUSS: We need to confirm that this is the desired behavior, or if we want to invalidate connections that had prior atomic_ids.
    assert len(edges_1) == 2
    assert len(edges_4) == 2
    assert len(edges_2) == 1
    assert len(edges_3) == 1


@mock_dynamodb
@mock_kinesis
def test_get_identity_graph(identity_datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")
    identity_engine = lookup.Lookup(identity_datastore)
    identity_engine.fetch_or_create_atomic_id("swid", "swid_1")
    identity_engine.fetch_or_create_atomic_id("swid", "swid_2")

    identity_engine.link_identity("swid", "swid_1", "swid", "swid_3")
    identity_engine.link_identity("swid", "swid_2", "swid", "swid_4")

    graph = identity_engine.get_identity_graph()

    assert graph is not None
    assert len(graph.edges) == 4
    assert len(graph.nodes) == 4
