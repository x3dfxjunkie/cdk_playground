"""Source Data Contract for Level-N LVL_N_PROD_CONFIG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N LVL_N_PROD_CONFIG Data
    """

    LVL_N_PROD_CONFIG_ID: int = Field(
        ...,
        alias="LVL_N_PROD_CONFIG_ID",
        name="",
        description="""""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNTNT_CACHE_ID: int = Field(
        ...,
        alias="CNTNT_CACHE_ID",
        name="",
        description="""""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_PROD_CONFIG_ACTN_TYP_NM: str = Field(
        ...,
        alias="LVL_N_PROD_CONFIG_ACTN_TYP_NM",
        name="",
        description="""""",
        example="""Adding Guest""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_PROD_CONFIG_PRD_NM: str = Field(
        ...,
        alias="LVL_N_PROD_CONFIG_PRD_NM",
        name="",
        description="""""",
        example="""Planned Arrival Date""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_CONFIG_STRT_DY_NB: int = Field(
        ...,
        alias="LVL_N_CONFIG_STRT_DY_NB",
        name="",
        description="""""",
        example=-10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_CONFIG_END_DY_NB: int = Field(
        ...,
        alias="LVL_N_CONFIG_END_DY_NB",
        name="",
        description="""""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""admin""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""2005-11-04 05:35:54""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""admin""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""1979-04-12 10:09:11""",
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
    Class for Level N LVL_N_PROD_CONFIG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:37:16.562516""",
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
        example="""LVL_N_PROD_CONFIG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=42747107590448,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWLvlNProdConfigModel(BaseModel):
    """
    Payload class for Level N LVL_N_PROD_CONFIG
    """

    class Config:
        """Payload Level Metadata"""

        title = "Level N Product Configuration"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Reference table for product configuration ID and their action type name and period name.  Source table has only one row and not further populated since 2012."""  # optional
        unique_identifier = ["data.LVL_N_PROD_CONFIG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LVL_N_PROD_CONFIG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
