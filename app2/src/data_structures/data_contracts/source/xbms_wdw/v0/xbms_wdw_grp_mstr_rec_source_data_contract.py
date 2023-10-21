"""Source Data Contract for XBMS  GRP_MSTR_REC"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS GRP_MSTR_REC Data
    """

    GRP_MSTR_REC_ID: int = Field(
        ...,
        alias="GRP_MSTR_REC_ID",
        name="",
        description="",
        example=502500,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_NB: str = Field(
        ...,
        alias="GRP_NB",
        name="",
        description="",
        example="""04216""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_NM: Optional[str] = Field(
        None,
        alias="GRP_NM",
        name="",
        description="",
        example="""ANGEL GROUP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_CREATE_DT: datetime = Field(
        ...,
        alias="GRP_CREATE_DT",
        name="",
        description="",
        example="""1999-06-15 10:16:24""",
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
        example="""1997-12-14 22:32:05""",
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
        example="""2010-08-09 20:52:22""",
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

    GRP_NM_OVRD_IN: str = Field(
        ...,
        alias="GRP_NM_OVRD_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DFLT_EXPRNC_BAND_DSNY_PROD_ID: Optional[int] = Field(
        None,
        alias="DFLT_EXPRNC_BAND_DSNY_PROD_ID",
        name="",
        description="",
        example=3533,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REDIR_SHIPMT_TO_RSRT: str = Field(
        ...,
        alias="REDIR_SHIPMT_TO_RSRT",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_EXST_REQ_IN: str = Field(
        ...,
        alias="UPDT_EXST_REQ_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GMR_ORD_PROC_PARAM_VAL: Optional[int] = Field(
        None,
        alias="GMR_ORD_PROC_PARAM_VAL",
        name="",
        description="",
        example=9604,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS GRP_MSTR_REC Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:48:33.110812""",
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
        example="""GRP_MSTR_REC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=45867015979222,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWGrpMstrRecModel(BaseModel):
    """
    Payload class for XBMS GRP_MSTR_REC
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.GRP_MSTR_REC_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GRP_MSTR_REC"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
