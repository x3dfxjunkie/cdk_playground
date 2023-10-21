"""Source Data Contract for XBMS  EXPRNC_BAND_DSNY_PROD"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_DSNY_PROD Data
    """

    EXPRNC_BAND_DSNY_PROD_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_DSNY_PROD_ID",
        name="",
        description="",
        example=500000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_TYP_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_TYP_ID",
        name="",
        description="",
        example=10020,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_TOP_COLOR_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_TOP_COLOR_ID",
        name="",
        description="",
        example=10023,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_BOTTOM_COLOR_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_BOTTOM_COLOR_ID",
        name="",
        description="",
        example=10024,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ERLST_FFLMT_DY_CN: str = Field(
        ...,
        alias="EXPRNC_BAND_ERLST_FFLMT_DY_CN",
        name="",
        description="",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_SHIPMT_TO_RSRT_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_SHIPMT_TO_RSRT_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_PROD_AVAIL_FR_DTS: Optional[datetime] = Field(
        None,
        alias="EXPRNC_BAND_PROD_AVAIL_FR_DTS",
        name="",
        description="",
        example="""1984-02-11 12:49:59""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_PROD_AVAIL_TO_DTS: Optional[datetime] = Field(
        None,
        alias="EXPRNC_BAND_PROD_AVAIL_TO_DTS",
        name="",
        description="",
        example="""1983-11-14 20:14:25""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""reference_data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1983-09-11 11:43:15""",
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
        example="""2021-07-31 08:39:55""",
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

    AVAIL_TO_GST_ORD_EXTNL_PART_IN: str = Field(
        ...,
        alias="AVAIL_TO_GST_ORD_EXTNL_PART_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DFLT_FOR_GRP_IN: str = Field(
        ...,
        alias="DFLT_FOR_GRP_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AVAIL_TO_REORD_EXTNL_PART_IN: str = Field(
        ...,
        alias="AVAIL_TO_REORD_EXTNL_PART_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AVAIL_TO_GMR_EXTNL_PART_IN: str = Field(
        ...,
        alias="AVAIL_TO_GMR_EXTNL_PART_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_DSNY_PROD Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:49:03.307833""",
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
        example="""EXPRNC_BAND_DSNY_PROD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=10958623982043,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandDsnyProdModel(BaseModel):
    """
    Payload class for XBMS EXPRNC_BAND_DSNY_PROD
    """

    class Config:
        """Payload Level Metadata"""

        title = "Experience Band Disney Product"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_DSNY_PROD_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXPRNC_BAND_DSNY_PROD"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
