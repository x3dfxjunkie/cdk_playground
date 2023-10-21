"""Source Data Contract Template for CANCELLATION_SCHEME"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CANCELLATION_SCHEME Data
    """

    CANCEL_SCHEME_ID: int = Field(
        ...,
        alias="CANCEL_SCHEME_ID",
        name="",
        description="""Cancellation scheme ID of the rule""",
        example=4440,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CANCELLATION_REF: str = Field(
        ...,
        alias="CANCELLATION_REF",
        name="",
        description="""referance for the cancellation scheme""",
        example="""CARNOCXL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PER_PERSON_CHARGE: Optional[float] = Field(
        None,
        alias="PER_PERSON_CHARGE",
        name="",
        description="""The flight booking  cancellation charge per person""",
        example=94591.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_DAYS: Optional[int] = Field(
        None,
        alias="MAX_DAYS",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHARGE_TYPE: Optional[str] = Field(
        None,
        alias="CHARGE_TYPE",
        name="",
        description="""P = PERCENTAGE, A = AMOUNT""",
        example="""A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_TYPE: Optional[str] = Field(
        None,
        alias="PRODUCT_TYPE",
        name="",
        description="""Other Cost applicable Product Type Code""",
        example="""CAR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""Alamo - No cancellation fee""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CARGE_CATEGORY: str = Field(
        ...,
        alias="CARGE_CATEGORY",
        name="",
        description="""charge category of the cancellation scheme_x000D_
Addition of charge 1 and charge 2 = 'A'_x000D_
Maximum of charge 1 and charge 2 = 'M' """,
        example="""A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NO_SHOW_CHARGE: Optional[float] = Field(
        None,
        alias="NO_SHOW_CHARGE",
        name="",
        description="""If the cancellation date has passed departure date, the_x000D_
amount specified here will be taken as the charge for_x000D_
the cancellation""",
        example=942.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NO_SHOW_TYPE: str = Field(
        ...,
        alias="NO_SHOW_TYPE",
        name="",
        description="""NO show charge type_x000D_
FIXED = 'F'_x000D_
AMOUNT = 'A'_x000D_
PERCENTAGE = 'P'_x000D_
NIGHT = 'N'""",
        example="""P""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTIFY_IN_RES: str = Field(
        ...,
        alias="NOTIFY_IN_RES",
        name="",
        description="""whether this is notify in the reservation client or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEP_DATE_BASED: str = Field(
        ...,
        alias="DEP_DATE_BASED",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_BASED_DATE: Optional[str] = Field(
        None,
        alias="ITEM_BASED_DATE",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CANCELLATION_SCHEME Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:38.269904""",
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
        example="""TBX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""CANCELLATION_SCHEME""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=14436706258402,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCancellationSchemeModel(BaseModel):
    """
    Payload class for TravelBox CANCELLATION_SCHEME
    """

    class Config:
        """Payload Level Metadata"""

        title = "Cancellation Scheme"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Contains user defined cancellation scheme details. Set up at Cancellation scheme main panel in Suplier Client"""  # optional
        unique_identifier = ["data.CANCEL_SCHEME_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CANCELLATION_SCHEME"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
