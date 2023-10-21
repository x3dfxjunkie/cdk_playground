"""Source Data Contract for XBMS  EXPRNC_BAND_ENTTL_ACQ_TYP"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_ENTTL_ACQ_TYP Data
    """

    EXPRNC_BAND_ENTTL_ACQ_TYP_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_ENTTL_ACQ_TYP_ID",
        name="",
        description="",
        example=10000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ENTTL_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_ENTTL_ID",
        name="",
        description="",
        example=1026286,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TXN_SRC_SYS_TX: Optional[str] = Field(
        None,
        alias="TXN_SRC_SYS_TX",
        name="",
        description="",
        example="""dcl-travel-plan-id""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CUSTOMIZATION_END_DATE_INTERVAL: Optional[str] = Field(
        None,
        alias="CUSTOMIZATION_END_DATE_INTERVAL",
        name="",
        description="",
        example="""9""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""venun003""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1993-07-07 02:49:37""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""venun003""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1998-10-03 20:19:42""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOGICAL_DEL_IN: str = Field(
        ...,
        alias="LOGICAL_DEL_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_ENTTL_ACQ_TYP Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:46:11.510360""",
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
        example="""XBANDMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""EXPRNC_BAND_ENTTL_ACQ_TYP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=37361243267188,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandEnttlAcqTypModel(BaseModel):
    """
    Payload class for XBMS EXPRNC_BAND_ENTTL_ACQ_TYP
    """

    class Config:
        """Payload Level Metadata"""

        title = "Experience Band Entitlement Acquisition Type"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_ENTTL_ACQ_TYP_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXPRNC_BAND_ENTTL_ACQ_TYP"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
