"""Source Data Contract for XBMS  CHRCTR_GRP"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS CHRCTR_GRP Data
    """

    BRAND_TYP_ID: Optional[int] = Field(
        None,
        alias="BRAND_TYP_ID",
        name="",
        description="",
        example=128,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHRCTR_CD: str = Field(
        ...,
        alias="CHRCTR_CD",
        name="",
        description="",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHRCTR_GRP_NM: str = Field(
        ...,
        alias="CHRCTR_GRP_NM",
        name="",
        description="",
        example="""Pride""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHRCTR_TYP_ID: int = Field(
        ...,
        alias="CHRCTR_TYP_ID",
        name="",
        description="",
        example=7,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHRCTR_BIN_VAL: Optional[str] = Field(
        None,
        alias="CHRCTR_BIN_VAL",
        name="",
        description="",
        example="""000000111""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1992-10-02 06:07:07""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""babus010""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1984-01-14 01:03:46""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""babus010""",
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
    Class for XBMS CHRCTR_GRP Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:47:15.784494""",
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
        example="""CHRCTR_GRP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=19662900460418,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWChrctrGrpModel(BaseModel):
    """
    Payload class for XBMS CHRCTR_GRP
    """

    class Config:
        """Payload Level Metadata"""

        title = "Character Group"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Reference table for brand types and their character groups such as Marvel, DVC, Princess, Run Disney, Polynesian Village, etc."""  # optional
        unique_identifier = ["data.CHRCTR_CD"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CHRCTR_GRP"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
