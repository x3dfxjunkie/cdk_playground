"""Source Data Contract for SnApp Attendance"""

from __future__ import annotations
from datetime import datetime, date
from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import GlobalSnAppHeader


class Total(BaseModel):
    """Class for Snapp Attendance Total"""

    key: str = Field(
        ...,
        alias="Key",
        name="Key",
        description="",
        example="APATT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    quantity: int = Field(
        ...,
        alias="Quantity",
        name="Quantity",
        description="",
        example=202,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AttendanceListItem(BaseModel):
    """AttendanceListItem"""

    code: str = Field(
        ...,
        alias="Code",
        name="Code",
        description="",
        example="LOC-WECTP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    totals: List[Total] = Field(
        ...,
        alias="Totals",
        name="Totals",
        description="",
    )


class Payload(BaseModel):
    """Payload"""

    attendance_list: List[AttendanceListItem] = Field(
        ...,
        alias="AttendanceList",
        name="Attendance List",
        description="",
    )
    date_time: datetime = Field(
        ...,
        alias="DateTime",
        name="DateTime",
        description="",
        example="2022-09-03T18:05:00.228+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fiscal_date: date = Field(
        ...,
        alias="FiscalDate",
        name="Fiscal Date",
        description="",
        example="2022-09-02",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reconcile: bool = Field(
        ...,
        alias="Reconcile",
        name="Reconcile",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    report_type: str = Field(
        ...,
        alias="ReportType",
        name="Report Type",
        description="",
        example="Location",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SnAppAttendanceModel(BaseModel):
    """SnAppAttendanceModel"""

    class Config:
        """SnAppAttendanceModel Config"""

        title = "SnApp Attendance"
        stream_name = ""
        description = "SnApp Attendance"
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = "SnApp.Attendance"

    header: GlobalSnAppHeader = Field(..., alias="Header", description="SnApp data metadata")
    payload: Payload = Field(..., alias="Payload", description="Data payload")
