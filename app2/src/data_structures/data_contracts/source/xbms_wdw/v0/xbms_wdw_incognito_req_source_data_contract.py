"""Source Data Contract for XBMS  INCOGNITO_REQ"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS INCOGNITO_REQ Data
    """

    REQ_ID: int = Field(
        ...,
        alias="REQ_ID",
        name="",
        description="",
        example=10000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MESSAGE_ID: int = Field(
        ...,
        alias="MESSAGE_ID",
        name="",
        description="",
        example=34561,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVENT_SEQ_NO: int = Field(
        ...,
        alias="EVENT_SEQ_NO",
        name="",
        description="",
        example=34562,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TASK_ID: int = Field(
        ...,
        alias="TASK_ID",
        name="",
        description="",
        example=34563,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PERSONAL_DATA_REQUEST_ID: int = Field(
        ...,
        alias="PERSONAL_DATA_REQUEST_ID",
        name="",
        description="",
        example=34564,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORIGIN_SYS: Optional[str] = Field(
        None,
        alias="ORIGIN_SYS",
        name="",
        description="",
        example="""ANONYMIZER""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVENT_TIME: Optional[datetime] = Field(
        None,
        alias="EVENT_TIME",
        name="",
        description="",
        example="""1996-10-18 05:30:31""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVENT_TYPE: Optional[str] = Field(
        None,
        alias="EVENT_TYPE",
        name="",
        description="",
        example="""RTF""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOOK_UP_IDS: Optional[str] = Field(
        None,
        alias="LOOK_UP_IDS",
        name="",
        description="",
        example="""'345090801'""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCOG: Optional[str] = Field(
        None,
        alias="INCOG",
        name="",
        description="",
        example="""LcwJpNSoHUXQobfANcUd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOGS: Optional[str] = Field(
        None,
        alias="LOGS",
        name="",
        description="",
        example="""Done insert incognito_req = 10000. Done drop and create tmp_exprnc_band_lnkIDs. inserted 0 tmp_exprnc_band_lnkIDs by look up by tgid. inserted 3 tmp_exprnc_band_lnkIDs by look up by TPID. inserted 3 tmp_exprnc_band_lnkIDs by look up by TSID. Done drop and recreate temp identifiers. inserted 4 identifiers. """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMENTS: Optional[str] = Field(
        None,
        alias="COMMENTS",
        name="",
        description="",
        example="""sLtAPXWPOdbOGwZYqYXq""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: Optional[datetime] = Field(
        None,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2023-04-16 16:47:31""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: Optional[datetime] = Field(
        None,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2006-03-01 13:23:01""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    USR_ID: Optional[str] = Field(
        None,
        alias="USR_ID",
        name="",
        description="",
        example="""f-xbandapp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS INCOGNITO_REQ Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:48:41.321805""",
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
        example="""INCOGNITO_REQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=26874105098987,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWIncognitoReqModel(BaseModel):
    """
    Payload class for XBMS INCOGNITO_REQ
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.REQ_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "INCOGNITO_REQ"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
