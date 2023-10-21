"""utilities for tests: setup_dynamo db
"""

import boto3
from app.src.data_structures.tests.utils.configs.setup_dynamodb_table_configs import table_attrs


def setup_dynamodb(
    identity_table_name,
    identity_nodes_table_name,
    identity_edges_table_name,
    profile_table_name,
    event_table_name,
    identity_notification_stream,
    create_table=False,
):
    """function will setup dynamo db and create table if create_table is set to True"""

    client = boto3.client("dynamodb")
    kinesis_client = boto3.client("kinesis")

    # table creation had to be set up like this because sonarqube would not pass the explicit cdk
    # because of repetitive code. Non variable attributes were added to a dictionary and variables
    # were kept within the scope of this function i.e table_names
    table_names = [
        identity_nodes_table_name,
        identity_edges_table_name,
        identity_table_name,
        event_table_name,
        profile_table_name,
    ]
    for table_attr, table_name in zip(table_attrs, table_names):
        kwargs = {
            "AttributeDefinitions": table_attr["attr_def"],
            "KeySchema": table_attr["key_schema"],
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
            "TableName": table_name,
        }
        if table_attr.get("global2ind", None) is not None:
            kwargs["GlobalSecondaryIndexes"] = table_attr["global2ind"]
        client.create_table(**kwargs)

    kinesis_client.create_stream(StreamName=identity_notification_stream, ShardCount=1)

    if create_table:
        table = boto3.resource("dynamodb").Table(identity_table_name)
        table.put_item(Item={"type#id-PK": "swid#{abcde}", "atomic_id": "12345"})
