"""Source Data Contract for XBMS  RES_GST"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS RES_GST Data
    """

    GST_ID: int = Field(
        ...,
        alias="GST_ID",
        name="",
        description="",
        example=938700,
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

    EXPRNC_BAND_LNK_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_LNK_ID",
        name="",
        description="",
        example=964800,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRMY_GST_IN: str = Field(
        ...,
        alias="PRMY_GST_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_FRST_NM: Optional[str] = Field(
        None,
        alias="GST_FRST_NM",
        name="",
        description="",
        example="""kbrmZLsVIuGZEsEztdRq""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_LST_NM: Optional[str] = Field(
        None,
        alias="GST_LST_NM",
        name="",
        description="",
        example="""cCZjXzFWsYhdZHLQujcc""",
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
        example="""1993-06-20 12:14:53""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""f-xbandapp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2009-07-14 10:05:44""",
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

    AP_EXP_DT: Optional[datetime] = Field(
        None,
        alias="AP_EXP_DT",
        name="",
        description="",
        example="""2019-07-29 08:44:38""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_ENTTL_OVRD_IN: str = Field(
        ...,
        alias="GST_ENTTL_OVRD_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DVC_MBR_IN: str = Field(
        ...,
        alias="DVC_MBR_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AP_TKT_ID: Optional[str] = Field(
        None,
        alias="AP_TKT_ID",
        name="",
        description="",
        example="""TfCSwSpGNdOtXvxhDVnH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AP_TKT_CD: Optional[str] = Field(
        None,
        alias="AP_TKT_CD",
        name="",
        description="",
        example="""iMGzodTfVgZVYGOVbopo""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AP_TKT_CONFIG_DS: Optional[str] = Field(
        None,
        alias="AP_TKT_CONFIG_DS",
        name="",
        description="",
        example="""NegXqCNKZmKwJsKtoBDP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACTV_GST_IN: str = Field(
        ...,
        alias="ACTV_GST_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_FRST_NM_UPPER: Optional[str] = Field(
        None,
        alias="gst_frst_nm_upper",
        name="",
        description="",
        example="""TeYvkpkGgYhPcgmowpTI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_LST_NM_UPPER: Optional[str] = Field(
        None,
        alias="gst_lst_nm_upper",
        name="",
        description="",
        example="""jUDAoEtSKRjRWSERmlTz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCOG_REQ_ID: Optional[int] = Field(
        None,
        alias="INCOG_REQ_ID",
        name="",
        description="",
        example=9252,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS RES_GST Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:48:01.120224""",
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
        example="""RES_GST""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=48889883574258,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWResGstModel(BaseModel):
    """
    Payload class for XBMS RES_GST
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.GST_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_GST"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
