"""Source Data Contract Template for CMP_COMPANY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CMP_COMPANY Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""WDTC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Walt Disney Travel Company""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS: Optional[str] = Field(
        None,
        alias="ADDRESS",
        name="",
        description="""Address of the credit card holder for credit card batch payment""",
        example="""190 Center Street Promenade""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_CODE: Optional[str] = Field(
        None,
        alias="POST_CODE",
        name="",
        description="""Postal code of the credit card holder for credit card batch payment""",
        example="""92805""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REGISTRATION_NO: Optional[str] = Field(
        None,
        alias="REGISTRATION_NO",
        name="",
        description="""The main registration number of the company""",
        example="""crrLsgbUhvrmhsSwcKJF""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TIME_ZONE: Optional[str] = Field(
        None,
        alias="TIME_ZONE",
        name="",
        description="""The time zone of the accommodation""",
        example="""PST""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BASE_CURRENCY: Optional[str] = Field(
        None,
        alias="BASE_CURRENCY",
        name="",
        description="""Base currency code at multy currency and it is a foregin key which refers to the filed CODE of the CURRENCY table""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_EXEMPT: Optional[str] = Field(
        None,
        alias="TAX_EXEMPT",
        name="",
        description="""A flag indicating whether the contract is excempt from tax ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_OVERRIDE: Optional[str] = Field(
        None,
        alias="TAX_OVERRIDE",
        name="",
        description="""A flag indicating whether the tax is overriden at the contract ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: Optional[str] = Field(
        None,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""ANA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATE: Optional[str] = Field(
        None,
        alias="STATE",
        name="",
        description="""State of the given credit card details address""",
        example="""CA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTRY: Optional[str] = Field(
        None,
        alias="COUNTRY",
        name="",
        description="""The TravelBox code of the country for which the rule is defined""",
        example="""US""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MERCHENT_FEE_NOT_APPLIED: str = Field(
        ...,
        alias="MERCHENT_FEE_NOT_APPLIED",
        name="",
        description="""Flag to indicate if a merchant fee is added to the credit card payments for bookings done through the company._x000D_
1 - merchant fee is not added._x000D_
0 - merchent fee is added. """,
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BIT_VALUE: Optional[int] = Field(
        None,
        alias="BIT_VALUE",
        name="",
        description="""The system generated bit value of the brand""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GDS_PHONE_NO: Optional[str] = Field(
        None,
        alias="GDS_PHONE_NO",
        name="",
        description="""Phone number which should be sent to the GDS and recorded in the PNR""",
        example="""714-520-5001""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CMP_COMPANY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:43:44.662081""",
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
        example="""CMP_COMPANY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=65721593567800,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCmpCompanyModel(BaseModel):
    """
    Payload class for TravelBox CMP_COMPANY
    """

    class Config:
        """Payload Level Metadata"""

        title = "Company"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This is the table for travelbox company details. Set up under 'Company' in 'General' tab of Set up Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CMP_COMPANY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
