"""Source Data Contract for XBMS  EXPRNC_BAND_IDVL_REQ"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_IDVL_REQ Data
    """

    EXPRNC_BAND_REQ_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_ID",
        name="",
        description="",
        example=713900,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_ID: int = Field(
        ...,
        alias="RES_ID",
        name="",
        description="",
        example=708400,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RSRT_SHIPMT_DSNY_FAC_ID: Optional[int] = Field(
        None,
        alias="RSRT_SHIPMT_DSNY_FAC_ID",
        name="",
        description="",
        example=503250,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIP_IMDT_REQ_IN: str = Field(
        ...,
        alias="SHIP_IMDT_REQ_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_HLD_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_HLD_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURR_REQ_HLD_RSN_ID: Optional[int] = Field(
        None,
        alias="CURR_REQ_HLD_RSN_ID",
        name="",
        description="",
        example=5693,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STERLING_ID: Optional[str] = Field(
        None,
        alias="STERLING_ID",
        name="",
        description="",
        example="""eNVYlQtDeCYzCAQuFllk""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_IDVL_REQ Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:49:35.158326""",
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
        example="""EXPRNC_BAND_IDVL_REQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=22207903846244,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandIdvlReqModel(BaseModel):
    """
    Payload class for XBMS EXPRNC_BAND_IDVL_REQ
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_REQ_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXPRNC_BAND_IDVL_REQ"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
