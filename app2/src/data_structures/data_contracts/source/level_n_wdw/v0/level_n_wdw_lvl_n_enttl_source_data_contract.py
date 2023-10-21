"""Source Data Contract for Level-N LVL_N_ENTTL"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N LVL_N_ENTTL Data
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

    CNTNT_CACHE_ID: int = Field(
        ...,
        alias="CNTNT_CACHE_ID",
        name="",
        description="""""",
        example=8881337,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ISS_TYP_ID: int = Field(
        ...,
        alias="LVL_N_ISS_TYP_ID",
        name="",
        description="""""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TKT_VOID_TYP_CD: str = Field(
        ...,
        alias="TKT_VOID_TYP_CD",
        name="",
        description="""""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_PURCH_DT: datetime = Field(
        ...,
        alias="LVL_N_ENTTL_PURCH_DT",
        name="",
        description="""""",
        example="""2020-10-10 07:11:17""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_EXP_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_EXP_DT",
        name="",
        description="""""",
        example="""1974-01-21 19:40:36""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_SLS_PRICE: float = Field(
        ...,
        alias="LVL_N_ENTTL_SLS_PRICE",
        name="",
        description="""""",
        example=149.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_SLS_TAX: float = Field(
        ...,
        alias="LVL_N_ENTTL_SLS_TAX",
        name="",
        description="""""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ISS_RSN_TX: Optional[str] = Field(
        None,
        alias="LVL_N_ISS_RSN_TX",
        name="",
        description="""""",
        example="""Creating""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RSRT_RES_STRT_DT: Optional[datetime] = Field(
        None,
        alias="RSRT_RES_STRT_DT",
        name="",
        description="""""",
        example="""1979-03-09 18:27:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RSRT_RES_END_DT: Optional[datetime] = Field(
        None,
        alias="RSRT_RES_END_DT",
        name="",
        description="""""",
        example="""2017-05-30 07:51:51""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RSRT_RES_EXP_DT: Optional[datetime] = Field(
        None,
        alias="RSRT_RES_EXP_DT",
        name="",
        description="""""",
        example="""2014-06-18 19:51:58""",
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
        example="""1979-02-27 18:43:21""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""SFLNSAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2002-02-18 12:34:42""",
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

    LVL_N_ENTTL_TYP: Optional[str] = Field(
        None,
        alias="LVL_N_ENTTL_TYP",
        name="",
        description="""""",
        example="""Memory Maker Advance Purchase""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_EARND_PRICE: float = Field(
        ...,
        alias="LVL_N_ENTTL_EARND_PRICE",
        name="",
        description="""""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N LVL_N_ENTTL Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:37:53.034377""",
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
        example="""LVL_N_ENTTL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=56905701745706,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWLvlNEnttlModel(BaseModel):
    """
    Payload class for Level N LVL_N_ENTTL
    """

    class Config:
        """Payload Level Metadata"""

        title = "Level N Entitlement"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Captures details about the sale of a Level N Entitlement to a Guest, and identifies attributes such as a specific product and pricing."""  # optional
        unique_identifier = ["data.LVL_N_ENTTL_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LVL_N_ENTTL"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
