"""Source Data Contract Template for RES_PASSENGER"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_PASSENGER Data
    """

    ENDORSED_PASSENGER_NO: Optional[int] = Field(
        None,
        alias="ENDORSED_PASSENGER_NO",
        name="",
        description="""If the passenger uses an endorsed passport, the number of the passenger who endorse this passenger_x000D_
(e.g. if a child is endorsed by one of parents, the number of the parent).""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VISA_REQ: Optional[str] = Field(
        None,
        alias="VISA_REQ",
        name="",
        description="""Specifies whether VISA is required or not_x000D_
Required - 1, Not required - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LEAD: str = Field(
        ...,
        alias="LEAD",
        name="",
        description="""A flag indicating that the passenger is the lead passenger ( value is '1' ) or not ( value is '0' )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEND_VISA_APP_TO_LEAD: str = Field(
        ...,
        alias="SEND_VISA_APP_TO_LEAD",
        name="",
        description="""Specifies whether VISA application is sent to lead passenger_x000D_
Sent - 1, Not sent - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2002-02-13 17:57:51""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ELIGIBLE_INSURANCE: Optional[str] = Field(
        None,
        alias="ELIGIBLE_INSURANCE",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRAVEL_STATUS: Optional[str] = Field(
        None,
        alias="TRAVEL_STATUS",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=27640745,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PASSENGER_NO: int = Field(
        ...,
        alias="PASSENGER_NO",
        name="",
        description="""Passnger number of the details entered passenger""",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROFILE_ID: Optional[int] = Field(
        None,
        alias="PROFILE_ID",
        name="",
        description="""The system  generated id of the H2H profile""",
        example=47468518,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TYPE: str = Field(
        ...,
        alias="TYPE",
        name="",
        description="""The availbility type (1 = Available 2 = Free Sell)""",
        example="""C""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTE: Optional[str] = Field(
        None,
        alias="NOTE",
        name="",
        description="""The note of Special Rate""",
        example="""zSAobEZTnyGQCYBPdsLL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PER_PERSON_PRICE: float = Field(
        ...,
        alias="PER_PERSON_PRICE",
        name="",
        description="""Per person price including tax_x000D_
""",
        example=601.66,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PER_PERSON_TAX: float = Field(
        ...,
        alias="PER_PERSON_TAX",
        name="",
        description="""TAX APPROPRIATED FOR THIS PERSON FROM THE BOOKING""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACTIVE_FOR_BOOKING: str = Field(
        ...,
        alias="ACTIVE_FOR_BOOKING",
        name="",
        description="""Specifies whether the passenger is active with respect to the booking""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ASSISTANCE: str = Field(
        ...,
        alias="ASSISTANCE",
        name="",
        description="""YES = 'Y' NO  = 'N' DONT KNOW = 'D'""",
        example="""X""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECORD_MED_COND: str = Field(
        ...,
        alias="RECORD_MED_COND",
        name="",
        description="""YES = 'Y' NO  = 'N' DONT KNOW = 'D'""",
        example="""X""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CRITICAL_MED_CONDITION: str = Field(
        ...,
        alias="CRITICAL_MED_CONDITION",
        name="",
        description="""A flag indicating whether this passenger has critical medical conditions_x000D_
Y - has critical medical condition_x000D_
N - no critical medical condition_x000D_
D - don't know_x000D_
X - not applicable""",
        example="""X""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    THIRD_PARTY_INSURANCE: str = Field(
        ...,
        alias="THIRD_PARTY_INSURANCE",
        name="",
        description="""Specifies whether the insurance is third party or not_x000D_
Third party- 1, Not third party- 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OPTIONAL_INSURANCE: str = Field(
        ...,
        alias="OPTIONAL_INSURANCE",
        name="",
        description="""Specifies whether the insurance is optional or not_x000D_
Optional- 1, Not optional - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_FOR_BOOKING: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_FOR_BOOKING",
        name="",
        description="""A flag to indicate whether the passenger use the primary passport for the booking or not.""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUB_TYPE: Optional[str] = Field(
        None,
        alias="SUB_TYPE",
        name="",
        description="""1 = TYPE1 (GET % OR AMOUNT IN DISCOUNT BEFORE SPECIFIC BOOKING DATE),_x000D_
2 = TYPE2 (NON CALCULATED DESCRIPTION)_x000D_
3 = TYPE3 ((GET % OR AMOUNT IN DISCOUNT  BASED ON BOOKING TO DEPARTURE DURATION)""",
        example="""C""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REFUSE_INSURANCE: Optional[str] = Field(
        None,
        alias="REFUSE_INSURANCE",
        name="",
        description="""Specifies whether to refuse the insurance or not_x000D_
Refuse - 1, Not refuse - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PASSENGER_CATEGORY: Optional[str] = Field(
        None,
        alias="PASSENGER_CATEGORY",
        name="",
        description="""Category of the passenger_x000D_
P - Passenger_x000D_
A - Adult_x000D_
C - Child_x000D_
I - Infant""",
        example="""P""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRST_NIGHT_STREET: Optional[str] = Field(
        None,
        alias="FIRST_NIGHT_STREET",
        name="",
        description="""The street specified for the APIS information of the passenger.""",
        example="""ZVDAFDFsVfSmJskQMmla""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRST_NIGHT_COUNTRY: Optional[str] = Field(
        None,
        alias="FIRST_NIGHT_COUNTRY",
        name="",
        description="""The TravelBox code of the country defined for the APIS information of the passenger""",
        example="""wmYsaxUTLVfGunDQKbYK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRST_NIGHT_STATE: Optional[str] = Field(
        None,
        alias="FIRST_NIGHT_STATE",
        name="",
        description="""The TravelBox code of the state defined for the APIS information of the passenger""",
        example="""MXeVGMNIktbaFssraOxz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRST_NIGHT_CITY: Optional[str] = Field(
        None,
        alias="FIRST_NIGHT_CITY",
        name="",
        description="""The TravelBox code of the city defined for the APIS information of the passenger""",
        example="""hymUUaOvreaIrCFTZeui""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRST_NIGHT_POST_CODE: Optional[str] = Field(
        None,
        alias="FIRST_NIGHT_POST_CODE",
        name="",
        description="""The postcode defined for the APIS information of the passenger""",
        example="""bmmomCdWUsERWbiCJqBv""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENDORSED_PP_FOR_BOOKING: Optional[str] = Field(
        None,
        alias="ENDORSED_PP_FOR_BOOKING",
        name="",
        description="""A flag indicating that the passenger uses an endorsed passport (e.g. a child uses one of the parent's passport).""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_PASSENGER Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:52:06.771496""",
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
        example="""RES_PASSENGER""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=85176463245674,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResPassengerModel(BaseModel):
    """
    Payload class for TravelBox RES_PASSENGER
    """

    class Config:
        """Payload Level Metadata"""

        title = "Booking Passenger"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This is the main table maintaining the mapping between the passenger profile and the booking."""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.PASSENGER_NO",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_PASSENGER"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
