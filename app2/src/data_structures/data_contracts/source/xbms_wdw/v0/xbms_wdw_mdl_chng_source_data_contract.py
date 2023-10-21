"""Source Data Contract for XBMS  MDL_CHNG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS MDL_CHNG Data
    """

    MDL_CHNG_ID: int = Field(
        ...,
        alias="MDL_CHNG_ID",
        name="",
        description="",
        example=10411,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MDL_VRSN_ID: int = Field(
        ...,
        alias="MDL_VRSN_ID",
        name="",
        description="",
        example=10043,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTTY_NM: str = Field(
        ...,
        alias="ENTTY_NM",
        name="",
        description="",
        example="""Facility Request shipment Confirmation""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TBL_NM: str = Field(
        ...,
        alias="TBL_NM",
        name="",
        description="",
        example="""fac_req_shipmt_cnfirm""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTR_NM: str = Field(
        ...,
        alias="ATTR_NM",
        name="",
        description="",
        example="""n/a""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COL_NM: str = Field(
        ...,
        alias="COL_NM",
        name="",
        description="",
        example="""n/a""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHNG_DS: str = Field(
        ...,
        alias="CHNG_DS",
        name="",
        description="",
        example="""Table Created""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RSN_DS: str = Field(
        ...,
        alias="RSN_DS",
        name="",
        description="",
        example="""xBRC related tables""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REQ_DS: str = Field(
        ...,
        alias="REQ_DS",
        name="",
        description="",
        example="""xBMS Application Archietecture (Joey)""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""version_control_data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2001-07-09 00:06:54""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""version_control_data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1992-06-17 08:10:03""",
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
    Class for XBMS MDL_CHNG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:45:23.597850""",
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
        example="""MDL_CHNG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=79540077644618,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWMdlChngModel(BaseModel):
    """
    Payload class for XBMS MDL_CHNG
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.MDL_CHNG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "MDL_CHNG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
