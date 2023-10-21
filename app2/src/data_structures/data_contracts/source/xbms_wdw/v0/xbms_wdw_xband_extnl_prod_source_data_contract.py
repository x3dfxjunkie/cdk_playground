"""Source Data Contract for XBMS  XBAND_EXTNL_PROD"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS XBAND_EXTNL_PROD Data
    """

    XBAND_EXTNL_PROD_ID: int = Field(
        ...,
        alias="XBAND_EXTNL_PROD_ID",
        name="",
        description="",
        example=1076388,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_PROD_SRC_SYS_NTV_ID: str = Field(
        ...,
        alias="EXTNL_PROD_SRC_SYS_NTV_ID",
        name="",
        description="",
        example="""1231231231""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_PROD_TXN_SRC_SYS_TX: str = Field(
        ...,
        alias="EXTNL_PROD_TXN_SRC_SYS_TX",
        name="",
        description="",
        example="""productId""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_PROD_STRT_DTS: Optional[datetime] = Field(
        None,
        alias="EXTNL_PROD_STRT_DTS",
        name="",
        description="",
        example="""1996-05-11 05:59:13""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_PROD_END_DTS: Optional[datetime] = Field(
        None,
        alias="EXTNL_PROD_END_DTS",
        name="",
        description="",
        example="""1974-11-28 22:50:34""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_PROD_CREATE_STRT_DTS: Optional[datetime] = Field(
        None,
        alias="EXTNL_PROD_CREATE_STRT_DTS",
        name="",
        description="",
        example="""1971-05-30 10:35:08""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_PROD_CREATE_END_DTS: Optional[datetime] = Field(
        None,
        alias="EXTNL_PROD_CREATE_END_DTS",
        name="",
        description="",
        example="""1972-03-09 06:20:38""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    XBAND_ENTTL_PROD_ASSC_ACTV_IN: str = Field(
        ...,
        alias="XBAND_ENTTL_PROD_ASSC_ACTV_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""rajal003""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1982-01-11 13:46:41""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_IN: Optional[str] = Field(
        None,
        alias="GROUP_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""XBMSEDCMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2003-05-03 04:14:52""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LGCL_DEL_IN: str = Field(
        ...,
        alias="LGCL_DEL_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DUAL_ORDER: Optional[str] = Field(
        None,
        alias="DUAL_ORDER",
        name="",
        description="",
        example="""XgmTufStyaeahorsgYlw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FAC_ID: Optional[int] = Field(
        None,
        alias="FAC_ID",
        name="",
        description="",
        example=4599,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS XBAND_EXTNL_PROD Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:51:50.554806""",
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
        example="""XBMSEDCMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""XBAND_EXTNL_PROD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=28655062616525,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWXbandExtnlProdModel(BaseModel):
    """
    Payload class for XBMS XBAND_EXTNL_PROD
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.XBAND_EXTNL_PROD_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "XBAND_EXTNL_PROD"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
