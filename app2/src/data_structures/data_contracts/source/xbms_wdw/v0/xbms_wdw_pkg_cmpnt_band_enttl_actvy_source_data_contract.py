"""Source Data Contract for XBMS  PKG_CMPNT_BAND_ENTTL_ACTVY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS PKG_CMPNT_BAND_ENTTL_ACTVY Data
    """

    PKG_CMPNT_BAND_ENTTL_ACTVY_ID: int = Field(
        ...,
        alias="PKG_CMPNT_BAND_ENTTL_ACTVY_ID",
        name="",
        description="",
        example=1232260,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ENTTL_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_ENTTL_ID",
        name="",
        description="",
        example=1023371,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_ID: int = Field(
        ...,
        alias="PKG_CMPNT_ID",
        name="",
        description="",
        example=505850,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ARVL_STRT_DT: Optional[datetime] = Field(
        None,
        alias="ARVL_STRT_DT",
        name="",
        description="",
        example="""1992-01-05 07:16:43""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ARVL_END_DT: Optional[datetime] = Field(
        None,
        alias="ARVL_END_DT",
        name="",
        description="",
        example="""2021-11-12 11:42:46""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_BAND_ENTTL_DEL_IN: str = Field(
        ...,
        alias="PKG_CMPNT_BAND_ENTTL_DEL_IN",
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
        example="""Nanda Venugopal""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1990-10-13 15:41:56""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""Nanda Venugopal""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2003-07-28 21:20:23""",
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

    PKG_CMPNT_BAND_ENTTL_TYP_ID: Optional[int] = Field(
        None,
        alias="PKG_CMPNT_BAND_ENTTL_TYP_ID",
        name="",
        description="",
        example=10000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS PKG_CMPNT_BAND_ENTTL_ACTVY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:43:42.382486""",
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
        example="""PKG_CMPNT_BAND_ENTTL_ACTVY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=27546482905826,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWPkgCmpntBandEnttlActvyModel(BaseModel):
    """
    Payload class for XBMS PKG_CMPNT_BAND_ENTTL_ACTVY
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.PKG_CMPNT_BAND_ENTTL_ACTVY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PKG_CMPNT_BAND_ENTTL_ACTVY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
