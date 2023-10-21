"""Source Data Contract for Level-N LVL_N_AP_DTLS"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N LVL_N_AP_DTLS Data
    """

    LVL_N_ENTTL_ID: int = Field(
        ...,
        alias="LVL_N_ENTTL_ID",
        name="",
        description="""""",
        example=4404348,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AP_ENTTL_ID: str = Field(
        ...,
        alias="AP_ENTTL_ID",
        name="",
        description="""""",
        example="""967329188302003""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AP_STRT_DT: Optional[datetime] = Field(
        None,
        alias="AP_STRT_DT",
        name="",
        description="""""",
        example="""2005-08-10 09:58:13""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AP_END_DT: Optional[datetime] = Field(
        None,
        alias="AP_END_DT",
        name="",
        description="""""",
        example="""1989-03-02 05:57:08""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AP_TKT_CD: Optional[str] = Field(
        None,
        alias="AP_TKT_CD",
        name="",
        description="""""",
        example="""AAqzsoNkrcMvlgnfUQlf""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AP_TKT_TYP: Optional[str] = Field(
        None,
        alias="AP_TKT_TYP",
        name="",
        description="""""",
        example="""wkXBdtADpTNKfPUOqHak""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MM_TKT_CD: Optional[str] = Field(
        None,
        alias="MM_TKT_CD",
        name="",
        description="""""",
        example="""THbFMXrfxzITYOdllTyc""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: Optional[datetime] = Field(
        None,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""1986-05-03 19:32:07""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: Optional[datetime] = Field(
        None,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""1975-12-19 13:16:54""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: Optional[str] = Field(
        None,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""SFLNSAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: Optional[str] = Field(
        None,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""SFLNSAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N LVL_N_AP_DTLS Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:37:13.973487""",
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
        example="""LVL_N_AP_DTLS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=86079930632155,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWLvlNApDtlsModel(BaseModel):
    """
    Payload class for Level N LVL_N_AP_DTLS
    """

    class Config:
        """Payload Level Metadata"""

        title = "Level N Annual Passholder Details"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Provides annual passholder details for Level N entitlement such as ticket codes and types (gold, platinum, etc.)"""  # optional
        unique_identifier = ["data.LVL_N_ENTTL_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LVL_N_AP_DTLS"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
