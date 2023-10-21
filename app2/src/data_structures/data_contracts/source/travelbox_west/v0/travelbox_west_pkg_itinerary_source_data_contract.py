"""Source Data Contract Template for PKG_ITINERARY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox PKG_ITINERARY Data
    """

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1975-07-18 18:16:10""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HOTEL_ELEMENT_NO: int = Field(
        ...,
        alias="HOTEL_ELEMENT_NO",
        name="",
        description="""NaN""",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_BKG_TO_DEP_DAYS: Optional[int] = Field(
        None,
        alias="MAX_BKG_TO_DEP_DAYS",
        name="",
        description="""NaN""",
        example=4648,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEST_CITY_CODE: Optional[str] = Field(
        None,
        alias="DEST_CITY_CODE",
        name="",
        description="""Deprecated""",
        example="""hIffeVqiaEhWWRgBRuQQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION_OVERRIDE: Optional[str] = Field(
        None,
        alias="COMMISSION_OVERRIDE",
        name="",
        description="""Specifies whether the commission rate is overriden for supplement""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    THRESHOLD: Optional[str] = Field(
        None,
        alias="THRESHOLD",
        name="",
        description="""Deprecated""",
        example="""EXACT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION: Optional[float] = Field(
        None,
        alias="COMMISSION",
        name="",
        description="""The commission percentage recieved by the tour operator""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALC_PAX_BASE: Optional[int] = Field(
        None,
        alias="CALC_PAX_BASE",
        name="",
        description="""Setup at Departure tab of Dates node of the package. Used to determine_x000D_
the group size of the contract for which are defined as group rate contracts.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEP_DATE_EXIST: Optional[str] = Field(
        None,
        alias="DEP_DATE_EXIST",
        name="",
        description="""deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PUSH_SALES_EXIST: Optional[str] = Field(
        None,
        alias="PUSH_SALES_EXIST",
        name="",
        description="""A flag indicating whether Push Sales Exist or not._x000D_
1 - Exist_x000D_
0 - Not Exist.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SPECIAL_OFFER_EXIST: Optional[str] = Field(
        None,
        alias="SPECIAL_OFFER_EXIST",
        name="",
        description="""A flag indicating whether Special Offers Exist or not._x000D_
1 - Exist_x000D_
0 - Not Exist.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BLACKOUT_EXIST: Optional[str] = Field(
        None,
        alias="BLACKOUT_EXIST",
        name="",
        description="""A flag indicating a blackout exists""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EBR_DISCOUNT_EXIST: Optional[str] = Field(
        None,
        alias="EBR_DISCOUNT_EXIST",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VISA_EXIST: Optional[str] = Field(
        None,
        alias="VISA_EXIST",
        name="",
        description="""A flag indicating whether Visa Exist or not._x000D_
1 - Exist_x000D_
0 - Not Exist.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CMS_CODE: Optional[str] = Field(
        None,
        alias="CMS_CODE",
        name="",
        description="""User defined CMS code which is taken as parameter values for tb_code, tb_itin, tb_pricegrid in package, itinerary and price grid respectively in the CMS URL which refers from travelbox to CMS. If this value is not defined the system will take package code, itinerary code and price grid name as default value of above variables.""",
        example="""AELNPsvHXZtheVWJYzZo""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITI_DEST_CITY: Optional[str] = Field(
        None,
        alias="ITI_DEST_CITY",
        name="",
        description="""TravelBox City Code of the Itinerary destination city""",
        example="""ANA""",
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

    TOUR_REGION: Optional[str] = Field(
        None,
        alias="TOUR_REGION",
        name="",
        description="""The TravelBox Tourist Region code for the Package. Tourist Region for the package is decided by an internal logic.""",
        example="""fqJjyllkFVcHMKitBiCF""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_ID: Optional[int] = Field(
        None,
        alias="SUPPLIER_ID",
        name="",
        description="""Not in DSN Scope""",
        example=29923,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CENTERS: Optional[int] = Field(
        None,
        alias="CENTERS",
        name="",
        description="""Deprecated""",
        example=1727,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESORT: Optional[str] = Field(
        None,
        alias="RESORT",
        name="",
        description="""The foreign Key which refers the field CODE of the ACT_ABSORPTION table""",
        example="""DISNEY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_BKG_TO_DEP_DAYS: Optional[int] = Field(
        None,
        alias="MIN_BKG_TO_DEP_DAYS",
        name="",
        description="""Required minimum number of days between the booking date and departure date""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_ID: int = Field(
        ...,
        alias="PACKAGE_ID",
        name="",
        description="""The foreign key which refers the field PACKAGE_ID of the table PKG_HOLIDAY""",
        example=13713,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITINERARY_NO: int = Field(
        ...,
        alias="ITINERARY_NO",
        name="",
        description="""The foreign key which refers the field ITINERARY_NO of the table PKG_ITINERARY""",
        example=51,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""51 ITN [17N]""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Itinerary [17 nights] FALCH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NIGHTS: int = Field(
        ...,
        alias="NIGHTS",
        name="",
        description="""This is 1 since the rates are for a day.""",
        example=17,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATUS: int = Field(
        ...,
        alias="STATUS",
        name="",
        description="""The TravelBox code of the status of the contract""",
        example=503,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAGE: int = Field(
        ...,
        alias="STAGE",
        name="",
        description="""The TravelBox code of the stage of the contract""",
        example=50301,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AVERAGE_MARGIN: Optional[float] = Field(
        None,
        alias="AVERAGE_MARGIN",
        name="",
        description="""Deprecated""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAGE_REASON: Optional[str] = Field(
        None,
        alias="STAGE_REASON",
        name="",
        description="""The TravelBox name of the reason for the stage of the contract""",
        example="""BanFJgrUkynhmypmyiIz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTRA_STAYS_ONLY: str = Field(
        ...,
        alias="EXTRA_STAYS_ONLY",
        name="",
        description="""A flag indicating whether Flex Parameters are enabled or not allowing user to define the applicable itineraries._x000D_
1 - Flex Parameters are enabled_x000D_
0 - Flex Parameters are not enabled""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_STAGE: str = Field(
        ...,
        alias="PACKAGE_STAGE",
        name="",
        description="""A flag indicating whether Stage and Status of the package are applied automatically or not.""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_PAX: Optional[int] = Field(
        None,
        alias="MIN_PAX",
        name="",
        description="""If this is a group based contract, the minimum number of pax for which the rates are applied""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_PAX: Optional[int] = Field(
        None,
        alias="MAX_PAX",
        name="",
        description="""If this is a group based contract, the maximum number of pax for which the rates are applied""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VARIATION_CODE: Optional[str] = Field(
        None,
        alias="VARIATION_CODE",
        name="",
        description="""Deprecated""",
        example="""oplMnMRezajoYgtxhzUG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VARIATION_NO: Optional[int] = Field(
        None,
        alias="VARIATION_NO",
        name="",
        description="""The system generated number of the variation""",
        example=3773,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SET_NO: int = Field(
        ...,
        alias="SET_NO",
        name="",
        description="""The numeric index within the scheme""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HOTEL_CODE: Optional[str] = Field(
        None,
        alias="HOTEL_CODE",
        name="",
        description="""When an Itinerary contains an Accommadation Item, the suppliear code of the item is saved in this field. The value is saved in the Itinerary level, so it provides faster access. """,
        example="""FALCH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox PKG_ITINERARY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:21.556801""",
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
        example="""PKG_ITINERARY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=12544599795671,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestPkgItineraryModel(BaseModel):
    """
    Payload class for TravelBox PKG_ITINERARY
    """

    class Config:
        """Payload Level Metadata"""

        title = "Package Itinerary"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Details such as package_id, Itinerary_no, name and code of the itinerary are stored.
Itineraries are setup at the itineraries node of the package tree"""  # optional
        unique_identifier = ["data.PACKAGE_ID", "data.ITINERARY_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PKG_ITINERARY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
