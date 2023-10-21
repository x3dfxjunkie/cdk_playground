"""Source Data Contract for XBMS  COST_CTR_CONFIG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS COST_CTR_CONFIG Data
    """

    COST_CTR_CONFIG_ID: int = Field(
        ...,
        alias="COST_CTR_CONFIG_ID",
        name="",
        description="",
        example=10002,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TXN_SRC_SYS_TX: str = Field(
        ...,
        alias="TXN_SRC_SYS_TX",
        name="",
        description="",
        example="""travel-plan-id""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_ID: Optional[int] = Field(
        None,
        alias="DSNY_FAC_ID",
        name="",
        description="",
        example=5822,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNTRY_ID: Optional[int] = Field(
        None,
        alias="CNTRY_ID",
        name="",
        description="",
        example=3453,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIP_INSD_FL: str = Field(
        ...,
        alias="SHIP_INSD_FL",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIP_OUTSD_FL: str = Field(
        ...,
        alias="SHIP_OUTSD_FL",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_CTR_ID: Optional[int] = Field(
        None,
        alias="COST_CTR_ID",
        name="",
        description="",
        example=10006,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WBS_ELMNT_ID: Optional[int] = Field(
        None,
        alias="WBS_ELMNT_ID",
        name="",
        description="",
        example=7306,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GNRL_LDGR_ID: Optional[int] = Field(
        None,
        alias="GNRL_LDGR_ID",
        name="",
        description="",
        example=10003,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""SEETN001""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1998-11-01 01:05:44""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""SEETN001""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2008-06-12 00:01:41""",
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
    Class for XBMS COST_CTR_CONFIG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:50:37.028336""",
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
        example="""COST_CTR_CONFIG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=43591959353606,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWCostCtrConfigModel(BaseModel):
    """
    Payload class for XBMS COST_CTR_CONFIG
    """

    class Config:
        """Payload Level Metadata"""

        title = "Cost Center Config"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = (
            """Reference table for cost center config and their attributes such as disney facility id."""  # optional
        )
        unique_identifier = ["data.COST_CTR_CONFIG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "COST_CTR_CONFIG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
