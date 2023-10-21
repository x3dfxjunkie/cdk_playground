"""Source Data Contract for XBMS  EXPRNC_BAND_REQ_STS"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_REQ_STS Data
    """

    EXPRNC_BAND_REQ_STS_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_STS_ID",
        name="",
        description="",
        example=10000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_STS_CTGY_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_STS_CTGY_ID",
        name="",
        description="",
        example=10007,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_STS_CD: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_STS_CD",
        name="",
        description="",
        example="""NOT_SENT_TO_FULFILLMENT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_STS_DS: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_STS_DS",
        name="",
        description="",
        example="""No orders for the Request have been sent to the Fulfillment Vendor""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""reference_data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2014-02-02 15:37:50""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""reference_data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2009-04-14 10:57:40""",
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
    Class for XBMS EXPRNC_BAND_REQ_STS Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:45:58.826735""",
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
        example="""EXPRNC_BAND_REQ_STS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=24729342661011,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandReqStsModel(BaseModel):
    """
    Payload class for XBMS EXPRNC_BAND_REQ_STS
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_REQ_STS_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXPRNC_BAND_REQ_STS"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
