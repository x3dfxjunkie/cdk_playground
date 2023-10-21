"""Source Data Contract for XBMS  DSNY_FAC"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS DSNY_FAC Data
    """

    DSNY_FAC_ID: int = Field(
        ...,
        alias="DSNY_FAC_ID",
        name="",
        description="",
        example=503250,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_ID: Optional[int] = Field(
        None,
        alias="ADDR_ID",
        name="",
        description="",
        example=724270,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_TYP_ID: int = Field(
        ...,
        alias="DSNY_FAC_TYP_ID",
        name="",
        description="",
        example=10004,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIP_CTCT_ID: Optional[int] = Field(
        None,
        alias="SHIP_CTCT_ID",
        name="",
        description="",
        example=503600,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FAC_ID: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_NM: str = Field(
        ...,
        alias="DSNY_FAC_NM",
        name="",
        description="",
        example="""Bay Lake Tower at Disney's Contemporary Resort""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_AVAIL_FOR_BULK_ORD_IN: str = Field(
        ...,
        alias="DSNY_FAC_AVAIL_FOR_BULK_ORD_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_FOR_RCV_GST_ORD_IN: Optional[str] = Field(
        None,
        alias="DSNY_FAC_FOR_RCV_GST_ORD_IN",
        name="",
        description="",
        example="""Y""",
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
        example="""2013-01-13 22:38:43""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""Will Mcknight""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2015-06-07 20:07:27""",
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

    RL_ASGN_FAC_IN: str = Field(
        ...,
        alias="RL_ASGN_FAC_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RTL_LOC_IN: str = Field(
        ...,
        alias="RTL_LOC_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_SHORT_NM: Optional[str] = Field(
        None,
        alias="DSNY_FAC_SHORT_NM",
        name="",
        description="",
        example="""JqwYhdIqIaofzlQIjapH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_CTR_ID: Optional[int] = Field(
        None,
        alias="COST_CTR_ID",
        name="",
        description="",
        example=502500,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BUS_AREA_ID: Optional[int] = Field(
        None,
        alias="BUS_AREA_ID",
        name="",
        description="",
        example=1006600,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GNRL_LDGR_ID: Optional[int] = Field(
        None,
        alias="GNRL_LDGR_ID",
        name="",
        description="",
        example=500650,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WBS_ELMNT_ID: Optional[int] = Field(
        None,
        alias="WBS_ELMNT_ID",
        name="",
        description="",
        example=1082050,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTO_RCV_IN: str = Field(
        ...,
        alias="AUTO_RCV_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SAP_GOODS_ISSUE_SKIP_RSN_ID: Optional[int] = Field(
        None,
        alias="SAP_GOODS_ISSUE_SKIP_RSN_ID",
        name="",
        description="",
        example=1098,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS DSNY_FAC Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:44:18.828642""",
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
        example="""DSNY_FAC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=41182725298742,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWDsnyFacModel(BaseModel):
    """
    Payload class for XBMS DSNY_FAC
    """

    class Config:
        """Payload Level Metadata"""

        title = "Disney Facility"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Reference table for Disney facilities in XBMS and corresponding address, facility type, shipping contact, enterprise facility id, and facility name."""  # optional
        unique_identifier = ["data.DSNY_FAC_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "DSNY_FAC"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
