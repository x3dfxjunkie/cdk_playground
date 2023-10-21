"""Source Data Contract for XBMS  GRP_MSTR_REC_DLVR_SUM_ACTVY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS GRP_MSTR_REC_DLVR_SUM_ACTVY Data
    """

    GRP_MSTR_REC_DLVR_SUM_ACTVY_ID: int = Field(
        ...,
        alias="GRP_MSTR_REC_DLVR_SUM_ACTVY_ID",
        name="",
        description="",
        example=1021904,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_SORT_ACTVY_ID: Optional[int] = Field(
        None,
        alias="GRP_MSTR_REC_SORT_ACTVY_ID",
        name="",
        description="",
        example=3288,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_RES_FAC_ID: int = Field(
        ...,
        alias="GRP_MSTR_REC_RES_FAC_ID",
        name="",
        description="",
        example=503265,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_DLVR_FAC_ID: int = Field(
        ...,
        alias="GRP_MSTR_REC_DLVR_FAC_ID",
        name="",
        description="",
        example=1023211,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""Test 080""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2003-01-30 18:23:57""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""Test 080""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2006-05-12 20:05:41""",
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

    GMR_REDIR_INSTR_ACTVY_ID: Optional[int] = Field(
        None,
        alias="GMR_REDIR_INSTR_ACTVY_ID",
        name="",
        description="",
        example=1027774,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS GRP_MSTR_REC_DLVR_SUM_ACTVY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:48:44.893441""",
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
        example="""GRP_MSTR_REC_DLVR_SUM_ACTVY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=22076039316959,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWGrpMstrRecDlvrSumActvyModel(BaseModel):
    """
    Payload class for XBMS GRP_MSTR_REC_DLVR_SUM_ACTVY
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.GRP_MSTR_REC_DLVR_SUM_ACTVY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GRP_MSTR_REC_DLVR_SUM_ACTVY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
