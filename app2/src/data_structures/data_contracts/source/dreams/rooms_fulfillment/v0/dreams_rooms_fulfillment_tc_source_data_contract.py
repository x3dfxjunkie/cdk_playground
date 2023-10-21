"""Source Data Contract for DREAMS Travel Component"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Travel Component Data"""

    tc_id: int = Field(
        ...,
        alias="TC_ID",
        name="",
        description="",
        example=32106233623,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_typ_nm: str = Field(
        ...,
        alias="TC_TYP_NM",
        name="",
        description="",
        example="ComponentTravelComponent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_grp_nb: int = Field(
        ...,
        alias="TC_GRP_NB",
        name="",
        description="",
        example=653140846959,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=7280453,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_id: int = Field(
        ...,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=366837,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_strt_dts: datetime = Field(
        ...,
        alias="TC_STRT_DTS",
        name="",
        description="",
        example="2023-06-10T09:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_end_dts: datetime = Field(
        ...,
        alias="TC_END_DTS",
        name="",
        description="",
        example="2023-06-10T09:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_bk_dts: datetime = Field(
        ...,
        alias="TC_BK_DTS",
        name="",
        description="",
        example="2023-05-20T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_slct_in: str = Field(
        ...,
        alias="TC_SLCT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_typ_nm: Optional[str] = Field(
        None,
        alias="PROD_TYP_NM",
        name="",
        description="",
        example="RESERVABLE_RESOURCE_COMPONENT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comnctn_chan_id: int = Field(
        ...,
        alias="COMNCTN_CHAN_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sls_chan_id: int = Field(
        ...,
        alias="SLS_CHAN_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_id: Optional[int] = Field(
        None,
        alias="FAC_ID",
        name="",
        description="",
        example=90002464,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_sts_nm: str = Field(
        ...,
        alias="TRVL_STS_NM",
        name="",
        description="",
        example="Booked",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    upgrd_typ_nm: str = Field(
        ...,
        alias="UPGRD_TYP_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_chrg_in: str = Field(
        ...,
        alias="TC_CHRG_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    asgn_own_id: Optional[int] = Field(
        None,
        alias="ASGN_OWN_ID",
        name="",
        description="",
        example=340589011,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_invtry_in: str = Field(
        ...,
        alias="TC_INVTRY_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    srvc_prd_id: Optional[int] = Field(
        None,
        alias="SRVC_PRD_ID",
        name="",
        description="",
        example=19630921,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-20T19:55:24Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-05-20T19:55:46Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prnt_tc_id: Optional[int] = Field(
        None,
        alias="PRNT_TC_ID",
        name="",
        description="",
        example=32106233622,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_chkin_dts: Optional[datetime] = Field(
        None,
        alias="TC_CHKIN_DTS",
        name="",
        description="",
        example="2023-05-20T19:55:47.238000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    blk_cd: Optional[str] = Field(
        None,
        alias="BLK_CD",
        name="",
        description="",
        example="01851",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_pty_id: Optional[int] = Field(
        None,
        alias="TRVL_AGCY_PTY_ID",
        name="",
        description="",
        example=89815,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    upgrd_tc_id: Optional[int] = Field(
        None,
        alias="UPGRD_TC_ID",
        name="",
        description="",
        example=22087357659,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentTcModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentTcModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Travel Component"
        stream_name = ""
        description = "This table holds information about the detailed parts, items, components of the reservation and/or the package ie: AccommodationComponent, Service, PackageTravelComponent, AdmissionComponent, ComponentTravelComponent"  # optional
        unique_identifier = ["data.TC_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tc"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
