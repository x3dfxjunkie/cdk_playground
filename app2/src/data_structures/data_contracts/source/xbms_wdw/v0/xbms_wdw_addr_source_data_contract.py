"""Source Data Contract for XBMS ADDR"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS ADDR Data
    """

    ADDR_ID: int = Field(
        ...,
        alias="ADDR_ID",
        name="",
        description="",
        example=14509,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNTRY_ID: Optional[int] = Field(
        None,
        alias="CNTRY_ID",
        name="",
        description="",
        example=10374,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_1_TX: Optional[str] = Field(
        None,
        alias="ADDR_1_TX",
        name="",
        description="",
        example="""96 i eWViR ei""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_2_TX: Optional[str] = Field(
        None,
        alias="ADDR_2_TX",
        name="",
        description="",
        example="""YMCYaXYupY pWuuYpiXWu pYuiYa658""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_3_TX: Optional[str] = Field(
        None,
        alias="ADDR_3_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_4_TX: Optional[str] = Field(
        None,
        alias="ADDR_4_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_CTY_NM: Optional[str] = Field(
        None,
        alias="ADDR_CTY_NM",
        name="",
        description="",
        example="""Orlando""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_ST_NM: Optional[str] = Field(
        None,
        alias="ADDR_ST_NM",
        name="",
        description="",
        example="""NC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_PSTL_CD: Optional[str] = Field(
        None,
        alias="ADDR_PSTL_CD",
        name="",
        description="",
        example="""85726-8881""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_RCPNT_PHN_NB: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_RCPNT_PHN_NB",
        name="",
        description="",
        example="""34567967890""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""reference-data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1997-08-05 08:38:10""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""test071@disney.com""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1972-08-20 03:31:25""",
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

    EXPRNC_BAND_RCPNT_NM: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_RCPNT_NM",
        name="",
        description="",
        example="""FZEkrGWOMTqlJaXeHMYN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_RCPNT_PHN_EXT_NB: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_RCPNT_PHN_EXT_NB",
        name="",
        description="",
        example="""zDKafDxVzaOHCqXSKwrZ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCOG_REQ_ID: Optional[int] = Field(
        None,
        alias="INCOG_REQ_ID",
        name="",
        description="",
        example=337,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS ADDR Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:46:40.935914""",
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
        example="""ADDR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=22029135643648,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWAddrModel(BaseModel):
    """
    Payload class for XBMS ADDR
    """

    class Config:
        """Payload Level Metadata"""

        title = "Address"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Contains addresses for xband recipients."""  # optional
        unique_identifier = ["data.ADDR_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ADDR"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
