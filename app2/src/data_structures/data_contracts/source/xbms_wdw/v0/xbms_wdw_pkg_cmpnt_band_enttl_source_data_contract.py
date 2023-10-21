"""Source Data Contract for XBMS  PKG_CMPNT_BAND_ENTTL"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS PKG_CMPNT_BAND_ENTTL Data
    """

    PKG_CMPNT_BAND_ENTTL_ID: int = Field(
        ...,
        alias="PKG_CMPNT_BAND_ENTTL_ID",
        name="",
        description="",
        example=505000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ENTTL_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_ENTTL_ID",
        name="",
        description="",
        example=10028,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_ID: int = Field(
        ...,
        alias="PKG_CMPNT_ID",
        name="",
        description="",
        example=504452,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DFLT_PKG_CMPNT_IN: str = Field(
        ...,
        alias="DFLT_PKG_CMPNT_IN",
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
        example="""1986-11-06 05:07:56""",
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
        example="""2008-06-24 05:25:19""",
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

    PKG_CMPNT_BAND_ENTTL_TYP_ID: Optional[int] = Field(
        None,
        alias="PKG_CMPNT_BAND_ENTTL_TYP_ID",
        name="",
        description="",
        example=10001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_ID: Optional[int] = Field(
        None,
        alias="DSNY_FAC_ID",
        name="",
        description="",
        example=503951,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ARVL_STRT_DT: Optional[datetime] = Field(
        None,
        alias="ARVL_STRT_DT",
        name="",
        description="",
        example="""1979-09-27 21:44:06""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ARVL_END_DT: Optional[datetime] = Field(
        None,
        alias="ARVL_END_DT",
        name="",
        description="",
        example="""1980-04-03 20:26:49""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ST_ID: Optional[int] = Field(
        None,
        alias="ST_ID",
        name="",
        description="",
        example=8447,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS PKG_CMPNT_BAND_ENTTL Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:43:31.955752""",
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
        example="""PKG_CMPNT_BAND_ENTTL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=17000845468968,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWPkgCmpntBandEnttlModel(BaseModel):
    """
    Payload class for XBMS PKG_CMPNT_BAND_ENTTL
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.PKG_CMPNT_BAND_ENTTL_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PKG_CMPNT_BAND_ENTTL"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
