"""Source Data Contract Template for SnApp Media"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import List, Optional

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import (
    GlobalSnAppHeader,
)


class AccessAreaListItem(BaseModel):
    access_area_account_code: str = Field(
        ...,
        alias="AccessAreaAccountCode",
        name="",
        description="",
        example="ACC-WMKGA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    access_area_account_id: str = Field(
        ...,
        alias="AccessAreaAccountId",
        name="",
        description="",
        example="88888888-CCCC-8888-CCCC-88888888B64F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    access_area_account_name: str = Field(
        ...,
        alias="AccessAreaAccountName",
        name="",
        description="",
        example="MK GA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Payload(BaseModel):
    access_area_list: List[AccessAreaListItem] = Field(
        ...,
        alias="AccessAreaList",
        name="",
        description="",
    )

    controller_workstation_code: Optional[str] = Field(
        None,
        alias="ControllerWorkstationCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    controller_workstation_id: Optional[str] = Field(
        None,
        alias="ControllerWorkstationId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    controller_workstation_name: Optional[str] = Field(
        None,
        alias="ControllerWorkstationName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    license_id: int = Field(
        ...,
        alias="LicenseId",
        name="",
        description="",
        example=1241,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_account_code: str = Field(
        ...,
        alias="LocationAccountCode",
        name="",
        description="",
        example="LOC-WMKTP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_account_id: str = Field(
        ...,
        alias="LocationAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA0EB0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_account_name: str = Field(
        ...,
        alias="LocationAccountName",
        name="",
        description="",
        example="MAGIC KINGDOM THEME PARK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operationg_area_account_code: str = Field(
        ...,
        alias="OperationgAreaAccountCode",
        name="",
        description="",
        example="SMKAC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operationg_area_account_id: str = Field(
        ...,
        alias="OperationgAreaAccountId",
        name="",
        description="",
        example="99999999-DDDD-9999-DDDD-99999999E43E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operationg_area_account_name: str = Field(
        ...,
        alias="OperationgAreaAccountName",
        name="",
        description="",
        example="Magic Kingdom Access Control",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_channel_id: Optional[str] = Field(
        None,
        alias="SaleChannelId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    station_serial: Optional[str] = Field(
        None,
        alias="StationSerial",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_category_code: str = Field(
        ...,
        alias="WorkstationCategoryCode",
        name="",
        description="",
        example="CAT128",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_category_name: str = Field(
        ...,
        alias="WorkstationCategoryName",
        name="",
        description="",
        example="@Lookup.EntityType.AccessPoint",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_code: str = Field(
        ...,
        alias="WorkstationCode",
        name="",
        description="",
        example="MK265MX000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_name: str = Field(
        ...,
        alias="WorkstationName",
        name="",
        description="",
        example="Magic Kingdom Mobile 265",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_type_code: int = Field(
        ...,
        alias="WorkstationTypeCode",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_type_name: str = Field(
        ...,
        alias="WorkstationTypeName",
        name="",
        description="",
        example="Access Point",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SnAppWorkstationModel(BaseModel):
    """Payload class for SnAppWorkstationModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SnApp Workstation"
        stream_name = ""
        description = """"""
        unique_identifier = ["Payload.WorkstationCode"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = ["SnApp.Media.Assign", "SnApp.Media.Disable", "SnApp.Media.Enabled"]

    header: GlobalSnAppHeader = Field(
        ...,
        alias="Header",
        name="",
        description="",
    )

    payload: Payload = Field(
        ...,
        alias="Payload",
        name="",
        description="",
    )
