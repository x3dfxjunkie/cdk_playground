"""Source Data Contract for Level-N LVL_N_ENTTL_LNK"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N LVL_N_ENTTL_LNK Data
    """

    LVL_N_ENTTL_ID: int = Field(
        ...,
        alias="LVL_N_ENTTL_ID",
        name="",
        description="""""",
        example=215051,
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

    LVL_N_LNK_ID: str = Field(
        ...,
        alias="LVL_N_LNK_ID",
        name="",
        description="""""",
        example="""8AB2A36448572220014857241A7E0009""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_LNK_STRT_DT: datetime = Field(
        ...,
        alias="LVL_N_ENTTL_LNK_STRT_DT",
        name="",
        description="""""",
        example="""2020-03-26 19:47:13""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_LNK_END_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_ENTTL_LNK_END_DT",
        name="",
        description="""""",
        example="""1998-08-01 07:13:20""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""SFLNSAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""2013-06-24 12:02:08""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""PM41076""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""1987-02-26 14:57:45""",
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
    Class for Level N LVL_N_ENTTL_LNK Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:38:09.847429""",
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
        example="""LVL_N_ENTTL_LNK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=21935345778980,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWLvlNEnttlLnkModel(BaseModel):
    """
    Payload class for Level N LVL_N_ENTTL_LNK
    """

    class Config:
        """Payload Level Metadata"""

        title = "Level N Entitlement Link"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Associates the Memory Maker Guest with his entitlement(s). A guest is allowed to have more than one entitlement, and an entitlement is allowed to have more than one Guest."""  # optional
        unique_identifier = [
            "data.LVL_N_ENTTL_ID",
            "data.LVL_N_RL_ID",
            "data.LVL_N_LNK_ID",
            "data.LVL_N_ENTTL_LNK_STRT_DT",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LVL_N_ENTTL_LNK"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
