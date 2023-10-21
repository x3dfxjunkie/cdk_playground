"""Source Data Contract for Level-N LVL_N_LNK_RL"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N LVL_N_LNK_RL Data
    """

    LVL_N_LNK_ID: str = Field(
        ...,
        alias="LVL_N_LNK_ID",
        name="",
        description="""""",
        example="""2C91808279F8D8540179F8D8BD2A0007""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_RL_ID: int = Field(
        ...,
        alias="LVL_N_RL_ID",
        name="",
        description="""""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""f-sflnsmd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""2013-11-20 20:39:09""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""f-sflnsmd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""1986-08-17 05:00:34""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LGCL_DEL_IN: str = Field(
        ...,
        alias="LGCL_DEL_IN",
        name="",
        description="""""",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N LVL_N_LNK_RL Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:37:57.500119""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    record_type: str = Field(
        ...,
        alias="record-type",
        name="",
        description="""Type of record""",
        example="""data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operation: str = Field(
        ...,
        alias="operation",
        name="",
        description="""Type of operation [insert, delete, update]""",
        example="""update""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="",
        description="""Partition key""",
        example="""schema-table""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    schema_name: str = Field(
        ...,
        alias="schema-name",
        name="",
        description="""Name of schema""",
        example="""SFLNSMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""LVL_N_LNK_RL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=79663921072582,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWLvlNLnkRlModel(BaseModel):
    """
    Payload class for Level N LVL_N_LNK_RL
    """

    class Config:
        """Payload Level Metadata"""

        title = "Level N Link Role"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Describes the various roles for individuals that are participating in a transaction. A party may perform multiple roles. Roles are shared by multiple people. The same party could be a guest, mother of the bride, group contact, DVC owner and shareholder and more. For Memory Maker, examples are Participant, Non Participant"""  # optional
        unique_identifier = ["data.LVL_N_LNK_ID", "data.LVL_N_RL_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LVL_N_LNK_RL"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
