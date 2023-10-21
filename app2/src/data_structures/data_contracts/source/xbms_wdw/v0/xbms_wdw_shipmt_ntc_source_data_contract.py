"""Source Data Contract for XBMS  SHIPMT_NTC"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS SHIPMT_NTC Data
    """

    SHIPMT_NTC_ID: int = Field(
        ...,
        alias="SHIPMT_NTC_ID",
        name="",
        description="",
        example=521600,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_NB: str = Field(
        ...,
        alias="SHIPMT_NB",
        name="",
        description="",
        example="""10023""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PO_ID: int = Field(
        ...,
        alias="PO_ID",
        name="",
        description="",
        example=505150,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_NTC_SHIP_DT: datetime = Field(
        ...,
        alias="SHIPMT_NTC_SHIP_DT",
        name="",
        description="",
        example="""2008-10-09 13:09:20""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_NTC_EXPECT_DLVR_DT: datetime = Field(
        ...,
        alias="SHIPMT_NTC_EXPECT_DLVR_DT",
        name="",
        description="",
        example="""2018-10-09 09:21:16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""XBANDAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2009-01-14 05:45:30""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""XBANDAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2004-04-13 06:04:16""",
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

    ADV_SHIPMT_NTFCTN_FILE_NM: Optional[str] = Field(
        None,
        alias="ADV_SHIPMT_NTFCTN_FILE_NM",
        name="",
        description="",
        example="""2_5_1680_1_env2.xml""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SAP_UPDT_STS_ID: Optional[int] = Field(
        None,
        alias="SAP_UPDT_STS_ID",
        name="",
        description="",
        example=3847,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MTRL_DOC_NB: Optional[str] = Field(
        None,
        alias="MTRL_DOC_NB",
        name="",
        description="",
        example="""sntEWmgLbTvkPGwmqEgU""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLMT_LOC_ID: Optional[int] = Field(
        None,
        alias="FFLMT_LOC_ID",
        name="",
        description="",
        example=7827,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS SHIPMT_NTC Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:44:06.310441""",
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
        example="""SHIPMT_NTC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=92003306233926,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWShipmtNtcModel(BaseModel):
    """
    Payload class for XBMS SHIPMT_NTC
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.SHIPMT_NTC_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "SHIPMT_NTC"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
