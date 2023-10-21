from faker import Faker

fkr = Faker()
DDL_DF_DATA = [
    {"COLUMN_NAME": "col_1", "DATA_TYPE": "string", "EXAMPLE": "val_1"},
    {"COLUMN_NAME": "col_2", "DATA_TYPE": "integer", "EXAMPLE": 1},
    {"COLUMN_NAME": "col_3", "DATA_TYPE": "datetime", "EXAMPLE": None},
]
DDL_PK_DATA = [{"PRIMARY_KEY": "col_1"}]
PATCH_DATACLASS_GEN_DIR = "app.src.data_structures.utilities.ui.dataclass_generator"
UPDATE_TREE_DICT = {"lvl_1": {"lvl_2": "test_value"}}
JSON_SCHEMA = {
    "items": {
        "properties": {
            "arg_1": {"type": "str"},
            "arg_2": {"type": "str"},
            "arg_3": {"type": "str"},
        }
    }
}
DATA_DICT = {
    "lvl_1": [
        {"lvl_2": {"lvl_3": {"arg_1": "value_1_1", "arg_2": "value_2_1", "arg_3": "value_3_1"}}},
        {"lvl_2": {"lvl_3": {"arg_1": "value_1_2", "arg_2": "value_2_2", "arg_3": "value_3_2"}}},
        {"lvl_2": {"lvl_3": {"arg_1": "value_1_3", "arg_2": "value_2_3", "arg_3": "value_3_3"}}},
    ]
}
XML_DATA = """<servers>
    <server>
        <name>host1</name>
        <os>Linux</os>
        <interfaces>
            <interface>
                <name>em0</name>
                <ip_address>10.0.0.1</ip_address>
            </interface>
        </interfaces>
    </server>
</servers>"""
DB_FORM_DETAILS = {
    "host": "test.db",
    "port": 0000,
    "database": "Test",
    "db_type": "MariaDB",
    "source_name": "Test",
}
DB_AIRTABLE_DETAILS = {
    "fields": {
        "Connection Identifier": "Test Connection ID",
        "Hostname": "test.db",
        "Port": 0000,
        "Database Name": "Test",
        "RDBMS (from Source Pipeline)": ["MariaDB"],
    }
}
AIRTABLE_FILTER_COLUMN = [
    DB_AIRTABLE_DETAILS,
    DB_AIRTABLE_DETAILS,
    DB_AIRTABLE_DETAILS,
]
DB_MARIA_CONFIG = {
    "username": "test",
    "password": fkr.password(),
    "host": "test.db",
    "port": 6666,
    "database": "Test",
    "db_type": "MariaDB",
    "source_name": "Test",
    "schema_name": "Test",
}

DB_ORACLE_CONFIG = {
    "username": "test",
    "password": fkr.password(),
    "host": "test.db",
    "port": 6666,
    "database": "Test",
    "db_type": "ORACLE",
    "source_name": "Test",
    "service_name": "Test",
    "owner_name": "Test",
}

AWS_SESSION_DATA = {
    "Credentials": {
        "AccessKeyId": "123Test",
        "SecretAccessKey": fkr.password(),
        "SessionToken": "123Test",
    }
}

AWS_SECRET_MANAGER = {"SecretString": f'{{"username": "Test", "password": "{fkr.password()}"}}'}


DATA_CONTRACT = '''

from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Header(BaseModel):

    correlation_id: str = Field(
        ...,
        alias="CorrelationId",
        name="",
        description="",
        example="TEST1234-1234-TEST-1234-TEST12345678",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    data_commit_timestamp: datetime = Field(
        ...,
        alias="DataCommitTimestamp",
        name="",
        description="",
        example="2023-09-12T21:09:40.815+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    data_id: str = Field(
        ...,
        alias="DataId",
        name="",
        description="",
        example="TEST1234-1234-TEST-1234-TEST12345678",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )



class Payload(BaseModel):

    id: str = Field(
        ...,
        alias="Id",
        name="",
        description="",
        example="TEST1234-1234-TEST-1234-TEST12345678",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SnappEntitlementSourceDataContractSampleModel(BaseModel):
    class Config:
        """Payload Level Metadata"""

        title = "SnappEntitlementSourceDataContractSample"
        stream_name = ""
        description = "SnappEntitlementSourceDataContractSample"  # optional
        unique_identifier = [""]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    header: Header = Field(
        ...,
        alias="Header",
        name="",
        description="",
    )

    payload: Payload = Field(
        ...,
        alias="Payload",
        name="",
        description="",
    )

'''
