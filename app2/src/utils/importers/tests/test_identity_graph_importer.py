"""Test suite for identity graph importer.
"""
import pytest
import os
from pathlib import Path
from datetime import datetime
import app.src.utils.importers.importer as graph_importer

stack_path = str(Path(os.getcwd()))

def test_import_dynamodb_s3_does_not_exist(spark_session):
    with pytest.raises(graph_importer.GraphImportException):
        graph_importer.import_identity_graph_from_s3(spark_session, "/this_is_a_bad_path")


def test_import_dynamodb_s3_path_does_not_contain_edges_or_nodes(spark_session):
    with pytest.raises(graph_importer.GraphImportException):
        graph_importer.import_identity_graph_from_s3(spark_session, f"{stack_path}/app/tools/test_data")


def test_import_dynamodb_graph_bad_schema(spark_session):
    with pytest.raises(Exception):
        graph_importer.import_identity_graph_from_s3(
            spark_session, f"{stack_path}/app/src/utils/importers/tests/data/identity_graph_dynamodb_streams_bad_schema"
        )


def test_import_dyanmodb_to_graphframe(spark_session):
    graph = graph_importer.import_identity_graph_from_s3(
        spark_session, f"{stack_path}/app/src/utils/importers/tests/data/identity_graph_dynamodb_streams"
    )

    in_degrees = graph.inDegrees.collect()
    pagerank_results = graph.pageRank(resetProbability=0.01, maxIter=20).vertices.collect()

    assert in_degrees[0].inDegree == 1
    assert round(pagerank_results[0].pagerank) == 2


def test_import_dyanmodb_to_graphframe_point_in_time(spark_session):
    snapshot_datetime = datetime.fromtimestamp(1679580674)
    graph = graph_importer.import_identity_graph_from_s3(
        spark_session, f"{stack_path}/app/src/utils/importers/tests/data/identity_graph_dynamodb_streams", snapshot_datetime
    )

    in_degrees = graph.inDegrees.collect()
    pagerank_results = graph.pageRank(resetProbability=0.01, maxIter=20).vertices.collect()

    assert len(in_degrees) == 2
    assert in_degrees[0].inDegree == 1
    assert round(pagerank_results[0].pagerank) == 1


def test_import_raw_dynamo_nodes_to_nodes_df(spark_session):
    raw_nodes = spark_session.read.json(f"{stack_path}/app/src/utils/importers/tests/data/identity_graph_dynamodb_streams/nodes")
    clean_nodes = graph_importer.dynamo_to_nodes(spark_session, raw_nodes)
    nodes = clean_nodes.collect()
    assert len(nodes) == 6
    assert nodes[0]["id"] == "device_id#device_id_1"


def test_import_raw_dynamo_nodes_point_in_time_two_nodes(spark_session):
    raw_nodes = spark_session.read.json(f"{stack_path}/app/src/utils/importers/tests/data/identity_graph_dynamodb_streams/nodes")
    snapshot_datetime = datetime.fromtimestamp(1679580674)
    clean_nodes = graph_importer.dynamo_to_nodes(spark_session, raw_nodes, snapshot_datetime)
    nodes = clean_nodes.collect()
    assert len(nodes) == 2
    assert nodes[0]["id"] == "swid#swid_1"


def test_import_raw_dynamo_nodes_point_in_time_empty(spark_session):
    raw_nodes = spark_session.read.json(f"{stack_path}/app/src/utils/importers/tests/data/identity_graph_dynamodb_streams/nodes")
    snapshot_datetime = datetime.fromtimestamp(1679580676)
    clean_nodes = graph_importer.dynamo_to_nodes(spark_session, raw_nodes, snapshot_datetime)
    nodes = clean_nodes.collect()
    assert len(nodes) == 0


def test_import_raw_dyanmo_edges_df(spark_session):
    raw_edges = spark_session.read.json(f"{stack_path}/app/src/utils/importers/tests/data/identity_graph_dynamodb_streams/edges")
    clean_edges = graph_importer.dynamo_to_edges(spark_session, raw_edges)
    edges = clean_edges.collect()
    assert len(edges) == 10


def test_import_raw_dyanmo_edges_df_point_in_time_two_edges(spark_session):
    raw_edges = spark_session.read.json(f"{stack_path}/app/src/utils/importers/tests/data/identity_graph_dynamodb_streams/edges")
    snapshot_datetime = datetime.fromtimestamp(1679580674)
    clean_edges = graph_importer.dynamo_to_edges(spark_session, raw_edges, snapshot_datetime)
    edges = clean_edges.collect()
    assert len(edges) == 2


def test_import_raw_dyanmo_edges_df_point_in_time_zero_edges(spark_session):
    raw_edges = spark_session.read.json(f"{stack_path}/app/src/utils/importers/tests/data/identity_graph_dynamodb_streams/edges")
    snapshot_datetime = datetime.fromtimestamp(1679580676)
    clean_edges = graph_importer.dynamo_to_edges(spark_session, raw_edges, snapshot_datetime)
    edges = clean_edges.collect()
    assert len(edges) == 0
