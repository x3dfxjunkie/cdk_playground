"""Config file for all attributes to setup dynamodb table"""

from uuid import uuid4

table_attrs = [
    {
        "attr_def": [
            {"AttributeName": "node_id", "AttributeType": "S"},
        ],
        "key_schema": [
            {
                "AttributeName": "node_id",
                "KeyType": "HASH",
            }
        ],
    },
    {
        "attr_def": [
            {
                "AttributeName": "source_node",
                "AttributeType": "S",
            },
            {
                "AttributeName": "target_node",
                "AttributeType": "S",
            },
        ],
        "key_schema": [
            {
                "AttributeName": "source_node",
                "KeyType": "HASH",
            },
            {
                "AttributeName": "target_node",
                "KeyType": "RANGE",
            },
        ],
    },
    {
        "attr_def": [
            {
                "AttributeName": "type#id-PK",
                "AttributeType": "S",
            },
            {
                "AttributeName": "atomic_id",
                "AttributeType": "S",
            },
        ],
        "key_schema": [
            {
                "AttributeName": "type#id-PK",
                "KeyType": "HASH",
            }
        ],
        "global2ind": [
            {
                # IndexName used to be identity table but variable was not defined within this dictionary
                "IndexName": f"{str(uuid4())}_idx",
                "KeySchema": [{"AttributeName": "atomic_id", "KeyType": "HASH"}],
                "Projection": {"ProjectionType": "ALL"},
                "ProvisionedThroughput": {"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
            }
        ],
    },
    {
        "attr_def": [
            {
                "AttributeName": "atomic_id#event_name",
                "AttributeType": "S",
            },
            {"AttributeName": "event_time", "AttributeType": "N"},
        ],
        "key_schema": [
            {
                "AttributeName": "atomic_id#event_name",
                "KeyType": "HASH",
            },
            {"AttributeName": "event_time", "KeyType": "RANGE"},
        ],
    },
    {
        "attr_def": [
            {
                "AttributeName": "atomic_id",
                "AttributeType": "S",
            }
        ],
        "key_schema": [
            {
                "AttributeName": "atomic_id",
                "KeyType": "HASH",
            }
        ],
    },
]
