"""Source Data Contract for DREAMS Function Type"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Function Type Data"""

    fnc_typ_id: int = Field(
        ...,
        alias="FNC_TYP_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fnc_typ_nm: str = Field(
        ...,
        alias="FNC_TYP_NM",
        name="",
        description="",
        example="Check Request",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fnc_typ_cd: str = Field(
        ...,
        alias="FNC_TYP_CD",
        name="",
        description="",
        example="AA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fnc_typ_strt_dt: datetime = Field(
        ...,
        alias="FNC_TYP_STRT_DT",
        name="",
        description="",
        example="2007-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fnc_typ_end_dt: datetime = Field(
        ...,
        alias="FNC_TYP_END_DT",
        name="",
        description="",
        example="2099-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fnc_typ_dspl_seq_nb: int = Field(
        ...,
        alias="FNC_TYP_DSPL_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="QC24297_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-03-30T11:34:19.809Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingFncTypModel(BaseModel):
    """Payload class for DREAMSAccountingFncTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Function Type"
        stream_name = ""
        description = """List of types of Functions that are associated to convention or group reservations: ie: Setup & Teardown Charge
Exhibit Space Rental
Refrigerator Rental
Risers/Flipcharts
Magic Kingdom Tour
Saute Chef/Carver Charge
Ticket Sales
Massage
Golf
Hospitality Room
Bar Refresh
Package Bar
Breakfast, Lunch, Dinner
Business Center"""
        unique_identifier = ["data.FNC_TYP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FNC_TYP"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
