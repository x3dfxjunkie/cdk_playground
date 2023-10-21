"""Source Data Contract for XBMS  RES_SEG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS RES_SEG Data
    """

    RES_SEG_ID: int = Field(
        ...,
        alias="RES_SEG_ID",
        name="",
        description="",
        example=712800,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_ID: int = Field(
        ...,
        alias="DSNY_FAC_ID",
        name="",
        description="",
        example=503279,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_SEG_BEGIN_DT: datetime = Field(
        ...,
        alias="RES_SEG_BEGIN_DT",
        name="",
        description="",
        example="""2004-12-16 07:15:50""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_SEG_END_DT: datetime = Field(
        ...,
        alias="RES_SEG_END_DT",
        name="",
        description="",
        example="""1971-08-04 05:06:00""",
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
        example="""1970-01-18 13:32:03""",
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
        example="""2019-01-15 15:50:53""",
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

    TRVL_PLAN_SEG_ID: str = Field(
        ...,
        alias="TRVL_PLAN_SEG_ID",
        name="",
        description="",
        example="""442511722766""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRVL_CMPNT_ID: str = Field(
        ...,
        alias="TRVL_CMPNT_ID",
        name="",
        description="",
        example="""837396349""",
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

    TRVL_CMPNT_STS_ID: int = Field(
        ...,
        alias="TRVL_CMPNT_STS_ID",
        name="",
        description="",
        example=10002,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_TM_ID: Optional[int] = Field(
        None,
        alias="GRP_MSTR_REC_TM_ID",
        name="",
        description="",
        example=3773,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_SEG_PKG_CD: Optional[str] = Field(
        None,
        alias="RES_SEG_PKG_CD",
        name="",
        description="",
        example="""wJKFDYBpOqsICutDpEUS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_SEG_PKG_PROD_ID: Optional[int] = Field(
        None,
        alias="RES_SEG_PKG_PROD_ID",
        name="",
        description="",
        example=1213,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_SEG_PKG_DS: Optional[str] = Field(
        None,
        alias="RES_SEG_PKG_DS",
        name="",
        description="",
        example="""ltVweUTZEsHBekuuJddK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_SEG_SPCL_OFFER_IN: str = Field(
        ...,
        alias="RES_SEG_SPCL_OFFER_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS RES_SEG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:50:05.525999""",
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
        example="""RES_SEG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=41467908601395,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWResSegModel(BaseModel):
    """
    Payload class for XBMS RES_SEG
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.RES_SEG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_SEG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
