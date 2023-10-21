"""Source Data Contract for Level-N LVL_N_ENTTL_TYP_SITE_ASSC"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N LVL_N_ENTTL_TYP_SITE_ASSC Data
    """

    LVL_N_ENTTL_TYP_SITE_ASSC_ID: int = Field(
        ...,
        alias="LVL_N_ENTTL_TYP_SITE_ASSC_ID",
        name="",
        description="""""",
        example=1,
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

    SITE: Optional[str] = Field(
        None,
        alias="SITE",
        name="",
        description="""""",
        example="""WDW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_TYP_SITE_ASSC_DS: Optional[str] = Field(
        None,
        alias="LVL_N_ENTTL_TYP_SITE_ASSC_DS",
        name="",
        description="""""",
        example="""Prearrival Memory Maker""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USE_ID: Optional[str] = Field(
        None,
        alias="CREATE_USE_ID",
        name="",
        description="""""",
        example="""SYS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USE_DTS: Optional[datetime] = Field(
        None,
        alias="CREATE_USE_DTS",
        name="",
        description="""""",
        example="""1982-04-28 15:41:30""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: Optional[str] = Field(
        None,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""SYS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: Optional[datetime] = Field(
        None,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""1978-02-23 01:23:58""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N LVL_N_ENTTL_TYP_SITE_ASSC Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:38:18.682425""",
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
        example="""LVL_N_ENTTL_TYP_SITE_ASSC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=78641948621521,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWLvlNEnttlTypSiteAsscModel(BaseModel):
    """
    Payload class for Level N LVL_N_ENTTL_TYP_SITE_ASSC
    """

    class Config:
        """Payload Level Metadata"""

        title = "Level N Entitlement Type Site Association"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = (
            """Reference table that provides the entitlement types, site (WDW or DLR), and description."""  # optional
        )
        unique_identifier = ["data.LVL_N_ENTTL_TYP_SITE_ASSC_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LVL_N_ENTTL_TYP_SITE_ASSC"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
