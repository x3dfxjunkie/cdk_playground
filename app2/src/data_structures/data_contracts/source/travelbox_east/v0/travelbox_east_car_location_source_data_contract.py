"""Source Data Contract Template for CAR_LOCATION"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CAR_LOCATION Data
    """

    LOCATION_ID: int = Field(
        ...,
        alias="LOCATION_ID",
        name="",
        description="""Location id is saved when the module configuration_x000D_
'STORE_LOCATION_ID' is enabled, otherwise_x000D_
-1""",
        example=33578,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_ID: int = Field(
        ...,
        alias="SUPPLIER_ID",
        name="",
        description="""Not in DSN Scope""",
        example=29980,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCATION_TYPE: str = Field(
        ...,
        alias="LOCATION_TYPE",
        name="",
        description="""Car location type code as defined in car setup""",
        example="""DEPO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""JAXT71""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""JACKSONVILLE INTL AIRPORT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS: Optional[str] = Field(
        None,
        alias="ADDRESS",
        name="",
        description="""Address of the credit card holder for credit card batch payment""",
        example="""JACKSONVILLE INTL AIRPORT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: Optional[str] = Field(
        None,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""JAX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATE: Optional[str] = Field(
        None,
        alias="STATE",
        name="",
        description="""State of the given credit card details address""",
        example="""FL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ZIP_CODE: Optional[str] = Field(
        None,
        alias="ZIP_CODE",
        name="",
        description="""The zip code of the location""",
        example="""32218""",
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

    REGION: Optional[str] = Field(
        None,
        alias="REGION",
        name="",
        description="""The TravelBox code of the region where the airport is located""",
        example="""NAM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PHONE: Optional[str] = Field(
        None,
        alias="PHONE",
        name="",
        description="""Phone number associated with the location""",
        example="""(904) 741-4428""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FAX: Optional[str] = Field(
        None,
        alias="FAX",
        name="",
        description="""Fax number associated with the location""",
        example="""yOujfSseZEHKdgfSIIbL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EMAIL: Optional[str] = Field(
        None,
        alias="EMAIL",
        name="",
        description="""The email address of the user""",
        example="""JpMksmjdxeMFdbDQVVDH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEASONAL_OPENING: str = Field(
        ...,
        alias="SEASONAL_OPENING",
        name="",
        description="""Specifies whether opening hours of a location are seasonal._x000D_
Then  particular location will be available only during the specific season_x000D_
Seasonal - 1, Not seasonal - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IMAGE_PATH: Optional[str] = Field(
        None,
        alias="IMAGE_PATH",
        name="",
        description="""The path on which the main image is saved""",
        example="""KsfgDCjjstOGqmmdYHxC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IMAGE_WIDTH: int = Field(
        ...,
        alias="IMAGE_WIDTH",
        name="",
        description="""The width of the main image""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IMAGE_HEIGHT: int = Field(
        ...,
        alias="IMAGE_HEIGHT",
        name="",
        description="""The height of the main image""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURRENCY: str = Field(
        ...,
        alias="CURRENCY",
        name="",
        description="""The TravelBox code of the currency in which the board basis fares are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUT_OF_HOUR_CHARGE: Optional[float] = Field(
        None,
        alias="OUT_OF_HOUR_CHARGE",
        name="",
        description="""The out of hour charge that is applicable to the location""",
        example=15296.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ERRATA_GROUP: Optional[int] = Field(
        None,
        alias="ERRATA_GROUP",
        name="",
        description="""Refers to the errata_group_id of errata_group table when user adds Free Text Conditions in contract level.  The option is available in 'Free Text Conditions' node in contract.""",
        example=276760,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PICKUP_PROCEDURE: Optional[str] = Field(
        None,
        alias="PICKUP_PROCEDURE",
        name="",
        description="""The description on the pickup procedure associated with location""",
        example="""KEoNiOQukusMdVLEzsgD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DROPOFF_PROCEDURE: Optional[str] = Field(
        None,
        alias="DROPOFF_PROCEDURE",
        name="",
        description="""The description on the dropoff procedure associated with location""",
        example="""NFsdVMVAjuUXcMEOvESW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_LOCATION: str = Field(
        ...,
        alias="DEFAULT_LOCATION",
        name="",
        description="""whether this is the group default location or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE: Optional[str] = Field(
        None,
        alias="LATITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example="""pQSHcSMLhuBXTBoyFyuR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE: Optional[str] = Field(
        None,
        alias="LONGITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example="""fHGQVkLLJgJrinGcENFh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIRPORT: Optional[str] = Field(
        None,
        alias="AIRPORT",
        name="",
        description="""Departure airport's code""",
        example="""JAX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: datetime = Field(
        ...,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""2021-07-25 11:35:00""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACTIVE: str = Field(
        ...,
        alias="ACTIVE",
        name="",
        description="""Whether 3D secure filter is active or not""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WEB_ENABLE: str = Field(
        ...,
        alias="WEB_ENABLE",
        name="",
        description="""Specifies whether the location is enabled for web_x000D_
Enabled - 1, Not enabled - 0""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESTINATION_ID: Optional[int] = Field(
        None,
        alias="DESTINATION_ID",
        name="",
        description="""System generated - auto incrementing id to identify the ledger destination""",
        example=2581,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    H2H_ID: Optional[int] = Field(
        None,
        alias="H2H_ID",
        name="",
        description="""Not in DSN Scope""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATED_BY: Optional[int] = Field(
        None,
        alias="CREATED_BY",
        name="",
        description="""A Foreign key which refers to the field USER_ID of the ADM_USER table""",
        example=15075,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATED_ON: Optional[datetime] = Field(
        None,
        alias="CREATED_ON",
        name="",
        description="""Created date time""",
        example="""2019-03-20 14:28:06""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=15097,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VERIFIED_BY: Optional[int] = Field(
        None,
        alias="VERIFIED_BY",
        name="",
        description="""The user id of the user who has done the verification of the location""",
        example=2518,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VERIFIED_ON: Optional[datetime] = Field(
        None,
        alias="VERIFIED_ON",
        name="",
        description="""The date and time of the verification of the location""",
        example="""2016-04-01 10:59:35""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IMPORTED_BY: Optional[int] = Field(
        None,
        alias="IMPORTED_BY",
        name="",
        description="""Deprecated""",
        example=1481,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IMPORTED_ON: Optional[datetime] = Field(
        None,
        alias="IMPORTED_ON",
        name="",
        description="""Deprecated""",
        example="""2005-11-13 13:14:50""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OPERATOR: Optional[str] = Field(
        None,
        alias="OPERATOR",
        name="",
        description="""Deprecated""",
        example="""pRbOOgLUmJoKIcoYIPWg""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCATION_GROUP_CODE: Optional[str] = Field(
        None,
        alias="LOCATION_GROUP_CODE",
        name="",
        description="""Code of the location group, a particular location is associated with""",
        example="""vjQpXyYnmdTkGwiUJnsw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CAR_LOCATION Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:50:21.496971""",
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
        example="""CAR_LOCATION""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=53002220892833,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastCarLocationModel(BaseModel):
    """
    Payload class for TravelBox CAR_LOCATION
    """

    class Config:
        """Payload Level Metadata"""

        title = "Car Location"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """Different locations available which can be used as pickup or drop off locations for a particular supplier, This can be setup from the Car module -> setup -> Location menu item -> new Location dialog"""  # optional
        unique_identifier = ["data.LOCATION_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CAR_LOCATION"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
