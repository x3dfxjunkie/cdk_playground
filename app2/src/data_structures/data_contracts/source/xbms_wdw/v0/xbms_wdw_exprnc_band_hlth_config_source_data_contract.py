"""Source Data Contract for XBMS  EXPRNC_BAND_HLTH_CONFIG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_HLTH_CONFIG Data
    """

    EXPRNC_BAND_HLTH_CONFIG_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_HLTH_CONFIG_ID",
        name="",
        description="",
        example=10000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_HLTH_CONFIG_CD: str = Field(
        ...,
        alias="EXPRNC_BAND_HLTH_CONFIG_CD",
        name="",
        description="",
        example="""FULL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_HLTH_CONFIG_DS: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_HLTH_CONFIG_DS",
        name="",
        description="",
        example="""Full""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WKUP_CNTR_MIN_NB: Optional[int] = Field(
        None,
        alias="WKUP_CNTR_MIN_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WKUP_CNTR_MAX_NB: Optional[int] = Field(
        None,
        alias="WKUP_CNTR_MAX_NB",
        name="",
        description="",
        example=24,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HLTH_CONFIG_ACTV_IN: str = Field(
        ...,
        alias="HLTH_CONFIG_ACTV_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HLTH_CONFIG_RANK_NB: Optional[str] = Field(
        None,
        alias="HLTH_CONFIG_RANK_NB",
        name="",
        description="",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""XBMS_MIGRATION_62""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1980-11-19 07:34:06""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""Abhilasha Sinha""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2017-02-04 02:57:10""",
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

    GD_HLTH_IN: str = Field(
        ...,
        alias="GD_HLTH_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_HLTH_CONFIG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:46:51.030592""",
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
        example="""EXPRNC_BAND_HLTH_CONFIG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=26733285235058,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandHlthConfigModel(BaseModel):
    """
    Payload class for XBMS EXPRNC_BAND_HLTH_CONFIG
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_HLTH_CONFIG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXPRNC_BAND_HLTH_CONFIG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
