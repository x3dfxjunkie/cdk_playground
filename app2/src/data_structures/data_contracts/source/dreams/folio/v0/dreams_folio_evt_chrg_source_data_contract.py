"""Source Data Contract Template for EVT_CHRG.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for EVT_CHRG"""

    evt_chrg_id: int = Field(
        ...,
        alias="EVT_CHRG_ID",
        name="",
        description="",
        example=3409183741,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fnc_typ_id: int = Field(
        ...,
        alias="FNC_TYP_ID",
        name="",
        description="",
        example=29,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rpt_ctgy_id: int = Field(
        ...,
        alias="RPT_CTGY_ID",
        name="",
        description="",
        example=47,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    evt_id: Optional[int] = Field(
        None,
        alias="EVT_ID",
        name="",
        description="",
        example=16,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    evt_dt: datetime = Field(
        ...,
        alias="EVT_DT",
        name="",
        description="",
        example="2023-06-12T07:30:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    evt_loc_nm: Optional[str] = Field(
        None,
        alias="EVT_LOC_NM",
        name="",
        description="",
        example="Salons 1-5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    blk_cd: Optional[str] = Field(
        None,
        alias="BLK_CD",
        name="",
        description="",
        example="1234567899",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-13T03:41:01Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rtrv_ref_nb: Optional[str] = Field(
        None,
        alias="RTRV_REF_NB",
        name="",
        description="",
        example="A760d97d2e3b",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioEvtChrgModel(BaseModel):
    """Payload class for DREAMSFolioEvtChrgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Event Charge"
        stream_name = ""
        description = "This table holds Charges that are related to Events which are related to Group/Convention guests"  # optional
        unique_identifier = ["data.EVT_CHRG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "EVT_CHRG"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
