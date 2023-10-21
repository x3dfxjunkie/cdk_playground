"""Source Data Contract for XBMS  PKG_TMPLT_CONFIG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS PKG_TMPLT_CONFIG Data
    """

    PKG_TMPLT_CONFIG_ID: int = Field(
        ...,
        alias="PKG_TMPLT_CONFIG_ID",
        name="",
        description="",
        example=505301,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_TYP_CONFIG_ID: Optional[int] = Field(
        None,
        alias="PKG_CMPNT_TYP_CONFIG_ID",
        name="",
        description="",
        example=9000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRNT_PKG_CMPNT_ID: int = Field(
        ...,
        alias="PRNT_PKG_CMPNT_ID",
        name="",
        description="",
        example=504951,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHLD_PKG_CMPNT_ID: int = Field(
        ...,
        alias="CHLD_PKG_CMPNT_ID",
        name="",
        description="",
        example=504453,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_TMPLT_FOR_EA_CMPNT_CN: Optional[str] = Field(
        None,
        alias="PKG_TMPLT_FOR_EA_CMPNT_CN",
        name="",
        description="",
        example="""kTkUwqtCZjsWUybwUuNo""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_TMPLT_CONFIG_ACTV_IN: str = Field(
        ...,
        alias="PKG_TMPLT_CONFIG_ACTV_IN",
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
        example="""test100.user""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2021-11-01 20:37:55""",
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
        example="""1978-03-03 23:47:20""",
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
    Class for XBMS PKG_TMPLT_CONFIG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:43:00.818613""",
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
        example="""PKG_TMPLT_CONFIG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=78239930699074,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWPkgTmpltConfigModel(BaseModel):
    """
    Payload class for XBMS PKG_TMPLT_CONFIG
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.PKG_TMPLT_CONFIG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PKG_TMPLT_CONFIG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
