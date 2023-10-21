import os
import app.src.processing.historical.batch as batch
import app.src.processing.realtime.module.domains.gam.identity_processor as identity_processor
import app.src.data_structures.object_lookup.lookup as lookup
import app.src.data_structures.object_lookup.dynamodb_datastore as dynamodb_datastore
import mock
import moto
import boto3
import csv


def get_sample_dlr_data():
    batches = []
    row_count = 0
    batch_size = 10
    with open(f"{os.path.dirname(__file__)}/gam_dlr_historical_sample.csv", encoding="utf-8-sig") as csvfile:
        dlrhistorical = csv.DictReader(csvfile)
        batch = []
        for row in dlrhistorical:
            row_to_append = (row["SOURCE_DATA_OBJECT"],)
            batch.append(row_to_append)
            if row_count % batch_size == 0:
                batches.append(batch.copy())
                batch = []
            row_count = row_count + 1
    return batches


@mock.patch(
    "app.src.processing.historical.batch.HistoricalGAMLoader.fetch_historical_data_records",
    return_value=get_sample_dlr_data(),
)
@mock.patch("app.src.data_structures.object_lookup")
@moto.mock_dynamodb
@moto.mock_kinesis
def test_batch_source_snowflake_dne(mock_fetch_historical_records, mock_identity_processor):
    event_table_name = "guest360-ea-test"
    gam_table_name = "gam"
    identity_table_name = "identity"
    identity_nodes_table_name = "identity_nodes"
    identity_edges_table_name = "identity_edges"
    profile_table_name = "profile_lookup"
    identity_notification_stream_name = "identity_notification"
    dynamodb_resource = boto3.resource("dynamodb")
    kinesis_client = boto3.client("kinesis")
    setup_dynamodb(
        identity_table_name=identity_table_name,
        identity_nodes_table_name=identity_nodes_table_name,
        identity_edges_table_name=identity_edges_table_name,
        event_table_name=event_table_name,
        profile_table_name=profile_table_name,
        identity_notification_stream=identity_notification_stream_name,
    )
    datastore = dynamodb_datastore.DynamoDBDatastore(
        dynamodb_resource=dynamodb_resource,
        kinesis_client=kinesis_client,
        identity_table_name=identity_table_name,
        identity_nodes_table_name=identity_nodes_table_name,
        identity_edges_table_name=identity_edges_table_name,
        events_table_name=event_table_name,
        profile_table_name=profile_table_name,
        identity_notification_stream_name=identity_notification_stream_name,
    )
    lookup_engine = lookup.Lookup(datastore)
    processor = identity_processor.IdentityProcessor(
        dynamo_resource=dynamodb_resource,
        kinesis_client=kinesis_client,
        event_table_name=event_table_name,
        identity_table_name=identity_table_name,
        identity_nodes_table_name=identity_nodes_table_name,
        identity_edges_table_name=identity_edges_table_name,
        profile_table_name=profile_table_name,
        identity_notification_stream_name=identity_notification_stream_name,
    )
    loader = batch.HistoricalGAMLoader(processor, "n/a", "n/a", "n/a", "n/a", "n/a", "n/a")
    loader.work()
    graph = lookup_engine.get_identity_graph()

    assert len(graph.edges) == 1648
    assert len(graph.nodes) == 729


def setup_dynamodb(
    identity_table_name,
    identity_nodes_table_name,
    identity_edges_table_name,
    profile_table_name,
    event_table_name,
    identity_notification_stream,
):
    client = boto3.client("dynamodb")
    kinesis_client = boto3.client("kinesis")
    client.create_table(
        AttributeDefinitions=[
            {"AttributeName": "node_id", "AttributeType": "S"},
        ],
        KeySchema=[
            {
                "AttributeName": "node_id",
                "KeyType": "HASH",
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
        TableName=identity_nodes_table_name,
    )
    client.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "source_node",
                "AttributeType": "S",
            },
            {
                "AttributeName": "target_node",
                "AttributeType": "S",
            },
        ],
        KeySchema=[
            {
                "AttributeName": "source_node",
                "KeyType": "HASH",
            },
            {
                "AttributeName": "target_node",
                "KeyType": "RANGE",
            },
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
        TableName=identity_edges_table_name,
    )
    client.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "type#id-PK",
                "AttributeType": "S",
            },
            {
                "AttributeName": "atomic_id",
                "AttributeType": "S",
            },
        ],
        KeySchema=[
            {
                "AttributeName": "type#id-PK",
                "KeyType": "HASH",
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
        GlobalSecondaryIndexes=[
            {
                "IndexName": f"{identity_table_name}_idx",
                "KeySchema": [{"AttributeName": "atomic_id", "KeyType": "HASH"}],
                "Projection": {"ProjectionType": "ALL"},
                "ProvisionedThroughput": {"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
            }
        ],
        TableName=identity_table_name,
    )

    client.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "atomic_id#event_name",
                "AttributeType": "S",
            },
            {"AttributeName": "event_time", "AttributeType": "N"},
        ],
        KeySchema=[
            {
                "AttributeName": "atomic_id#event_name",
                "KeyType": "HASH",
            },
            {"AttributeName": "event_time", "KeyType": "RANGE"},
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
        TableName=event_table_name,
    )
    client.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "atomic_id",
                "AttributeType": "S",
            }
        ],
        KeySchema=[
            {
                "AttributeName": "atomic_id",
                "KeyType": "HASH",
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
        TableName=profile_table_name,
    )

    kinesis_client.create_stream(StreamName=identity_notification_stream, ShardCount=1)
