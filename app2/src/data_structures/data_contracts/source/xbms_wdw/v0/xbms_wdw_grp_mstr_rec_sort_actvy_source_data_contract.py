"""Source Data Contract for XBMS  GRP_MSTR_REC_SORT_ACTVY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS GRP_MSTR_REC_SORT_ACTVY Data
    """

    GRP_MSTR_REC_SORT_ACTVY_ID: int = Field(
        ...,
        alias="GRP_MSTR_REC_SORT_ACTVY_ID",
        name="",
        description="",
        example=1010508,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_ID: int = Field(
        ...,
        alias="GRP_MSTR_REC_ID",
        name="",
        description="",
        example=1023915,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_SORT_TYP_ID: int = Field(
        ...,
        alias="GRP_MSTR_REC_SORT_TYP_ID",
        name="",
        description="",
        example=10020,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_SORT_ARVL_STRT_DT: Optional[datetime] = Field(
        None,
        alias="GRP_MSTR_REC_SORT_ARVL_STRT_DT",
        name="",
        description="",
        example="""1985-05-04 20:06:17""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_SORT_ARVL_END_DT: Optional[datetime] = Field(
        None,
        alias="GRP_MSTR_REC_SORT_ARVL_END_DT",
        name="",
        description="",
        example="""2007-10-28 14:07:32""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_SORT_DEL_IN: str = Field(
        ...,
        alias="GRP_MSTR_REC_SORT_DEL_IN",
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
        example="""Preethi Ponnuchamy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1985-03-24 07:34:17""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""Preethi Ponnuchamy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1978-04-28 09:31:17""",
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
    Class for XBMS GRP_MSTR_REC_SORT_ACTVY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:44:49.288634""",
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
        example="""GRP_MSTR_REC_SORT_ACTVY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=68047423822586,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWGrpMstrRecSortActvyModel(BaseModel):
    """
    Payload class for XBMS GRP_MSTR_REC_SORT_ACTVY
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.GRP_MSTR_REC_SORT_ACTVY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GRP_MSTR_REC_SORT_ACTVY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
