"""Source Data Contract Template for CME WDW Ticket Code Mapping"""

from __future__ import annotations

from datetime import datetime, date
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    access_code: str = Field(
        ...,
        alias="access_code",
        name="",
        description="",
        example="3LFK4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    add_ons: str = Field(
        ...,
        alias="add_ons",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_group: str = Field(
        ...,
        alias="age_group",
        name="",
        description="",
        example="C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    blockout_calendar_id: Optional[str] = Field(
        None,
        alias="blockout_calendar_id",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    calendar_id: str = Field(
        ...,
        alias="calendar_id",
        name="",
        description="",
        example="ThemePark",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_on: datetime = Field(
        ...,
        alias="created_on",
        name="",
        description="",
        example="2023-08-18T14:28:16Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_usr: str = Field(
        ...,
        alias="created_usr",
        name="",
        description="",
        example="AAAAA111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date: date = Field(
        ...,
        alias="end_date",
        name="",
        description="",
        example="2023-12-15",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    has_blockout: int = Field(
        ...,
        alias="has_blockout",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    inventory_category: str = Field(
        ...,
        alias="inventory_category",
        name="",
        description="",
        example="TICKET",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_updated: datetime = Field(
        ...,
        alias="last_updated",
        name="",
        description="",
        example="2023-08-18T14:28:16Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    num_days: int = Field(
        ...,
        alias="num_days",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    park_access_type: str = Field(
        ...,
        alias="park_access_type",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pgm_name: str = Field(
        ...,
        alias="pgm_name",
        name="",
        description="",
        example="TBD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_category: str = Field(
        ...,
        alias="product_category",
        name="",
        description="",
        example="ThemePark",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_type: str = Field(
        ...,
        alias="product_type",
        name="",
        description="",
        example="ThemePark",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    retl_sls_desc: str = Field(
        ...,
        alias="retl_sls_desc",
        name="",
        description="",
        example="FL Resident 3-Day Disney Weekday Magic Ticket w/ Water Park and Sports Option 3-9",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tckt_category_type: str = Field(
        ...,
        alias="tckt_category_type",
        name="",
        description="",
        example="FL Weekday Magic Water Park & Sports",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tckt_sub_type_name: str = Field(
        ...,
        alias="tckt_sub_type_name",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code: str = Field(
        ...,
        alias="ticket_code",
        name="",
        description="",
        example="3LFK4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_description: str = Field(
        ...,
        alias="ticket_description",
        name="",
        description="",
        example="FL Resident 3-Day Disney Weekday Magic Ticket w/ Water Park and Sports Option 3-9",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_type_name: str = Field(
        ...,
        alias="ticket_type_name",
        name="",
        description="",
        example="1 Park with OGA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_usr: str = Field(
        ...,
        alias="updated_usr",
        name="",
        description="",
        example="AAAAA111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEWDWTicketCodeMappingModel(BaseModel):
    """Payload class for CMEWDWTicketCodeMappingModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Ticket Code Mapping"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.ticket_code"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ticket_code_mapping"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
