"""Source Data Contract for GAM WDW Affiliation"""
from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class AffiliationIdItem(BaseModel):
    """Data class that represents the affiliation IDs from sources"""

    id: Optional[str] = Field(
        None,
        alias="id",
        name="Affiliation ID Value",
        description="Key value from origin source system, related to the affiliation",
        example="801150015104773833",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: Optional[str] = Field(
        None,
        alias="type",
        name="Affiliation ID Type",
        description="Key type from origin source system, related to the affiliation",
        example="ENTITLEMENT-ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Guest(BaseModel):
    """Data class that represents the Guest details"""

    guest_id_type: str = Field(
        ...,
        alias="guestIdType",
        name="Guest Identifier Type",
        description="Guest ID type -  SWID, GUID etc that the affiliation is linked to",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_id_value: str = Field(
        ...,
        alias="guestIdValue",
        name="Guest Identifier Value",
        description="Guest ID value that the affiliation is linked to",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class Affiliation(BaseModel):
    """Data class that represents the Affiliation details"""

    class Config:
        """Class Level Metadata"""

        alias = "affiliation"

    id: str = Field(
        ...,
        alias="id",
        name="Affiliation ID from GAM",
        description="Unique affiliation ID assigned in GAM",
        example="18266323",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    category: str = Field(
        ...,
        alias="category",
        name="Affiliation Category",
        description="Category of the Guest affiliation, as defined by GAM",
        example="AnnualPass",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Affiliation Type",
        description="Type of the Guest affiliation, as defined by GAM",
        example="Deluxe Annual Passport",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="Affiliation Subtype",
        description="Subtype of the Guest affiliation, as defined by GAM",
        example="DELUXE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validity_start_date: datetime = Field(
        ...,
        alias="validityStartDate",
        name="Validity Start Date",
        description="Start datetime of the affiliation",
        example="2023-01-17T05:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validity_end_date: Optional[datetime] = Field(
        None,
        alias="validityEndDate",
        name="Validity End Date",
        description="End datetime of the affiliation",
        example="2030-12-31T05:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="status",
        name="Affiliation Status",
        description="Status of the affiliation",
        example="ACTIVE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    affiliation_ids: List[AffiliationIdItem] = Field(
        ...,
        alias="affiliationIds",
        name="Affiliation IDs",
        description="Keys from the source system, related to the affiliation",
    )
    guest: Guest = Field(
        ...,
        alias="guest",
        name="Guest ID Info",
        description="Details of the Guest that the affiliation is tied to",
    )
    description: Optional[str] = Field(
        None,
        alias="description",
        name="Affiliation Description",
        description="Affiliation description, provided by GAM",
        example="CAST GUEST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source: Optional[str] = Field(
        None,
        alias="source",
        name="Original Source",
        description="Origin source of the affiliation",
        example="SNAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    renewable: Optional[bool] = Field(
        None,
        alias="renewable",
        name="Affiliation Renewable Indicator",
        description="Indicates whether the affiliation/pass can be renewed",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GAMWDWAffiliationModel(BaseModel):
    """Payload class for GAMWDWAffiliationModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM WDW Affiliation"
        stream_name = "gam-kinesis-affil-affiliation-guest360-wdw"
        description = """Affiliations of WDW Guests, as received and derived in GAM"""
        unique_identifier = ["affiliation.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"  # optional
        key_path_value = "AFFILIATION"  # optional

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always AFFILIATION",
        example="AFFILIATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the affiliation was created new or updated or removed from GAM",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="Event timestamp",
        description="Timestamp of the event generated by GAM",
        example="2023-03-29T12:57:49Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    affiliation: Affiliation = Field(
        ...,
        alias="affiliation",
        name="Affiliation Details",
        description="Affiliation details that include the category, type etc.",
    )
