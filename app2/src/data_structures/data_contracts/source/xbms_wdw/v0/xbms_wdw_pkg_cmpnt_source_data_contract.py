"""Source Data Contract for XBMS  PKG_CMPNT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS PKG_CMPNT Data
    """

    PKG_CMPNT_ID: int = Field(
        ...,
        alias="PKG_CMPNT_ID",
        name="",
        description="",
        example=10087,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_TYP_ID: int = Field(
        ...,
        alias="PKG_CMPNT_TYP_ID",
        name="",
        description="",
        example=500000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_NM: str = Field(
        ...,
        alias="PKG_CMPNT_NM",
        name="",
        description="",
        example="""NEW INCREDIBLE2""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AVAIL_TO_GST_IN: str = Field(
        ...,
        alias="AVAIL_TO_GST_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_ACTV_FR_DT: Optional[datetime] = Field(
        None,
        alias="PKG_CMPNT_ACTV_FR_DT",
        name="",
        description="",
        example="""1987-05-19 14:55:34""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_ACTV_UNTIL_DT: Optional[datetime] = Field(
        None,
        alias="PKG_CMPNT_ACTV_UNTIL_DT",
        name="",
        description="",
        example="""1972-12-18 13:25:47""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_MIN_CPCTY_CN: Optional[str] = Field(
        None,
        alias="PKG_CMPNT_MIN_CPCTY_CN",
        name="",
        description="",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_MAX_CPCTY_CN: Optional[str] = Field(
        None,
        alias="PKG_CMPNT_MAX_CPCTY_CN",
        name="",
        description="",
        example="""5""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_ACTV_IN: str = Field(
        ...,
        alias="PKG_CMPNT_ACTV_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""REFERENCE_DATA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1981-06-09 01:18:16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""test100.user""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1990-02-13 16:37:01""",
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
    Class for XBMS PKG_CMPNT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:46:28.563294""",
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
        example="""PKG_CMPNT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=18243853513745,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWPkgCmpntModel(BaseModel):
    """
    Payload class for XBMS PKG_CMPNT
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.PKG_CMPNT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PKG_CMPNT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
