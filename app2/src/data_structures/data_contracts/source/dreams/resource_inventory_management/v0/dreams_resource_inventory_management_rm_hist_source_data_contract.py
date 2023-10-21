"""Source Data Contract for Dreams Resource Inventory Management Room History"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Resource Inventory Management Room History"""

    arvl_dts: Optional[datetime] = Field(
        None,
        alias="ARVL_DTS",
        name="",
        description="",
        example="2023-07-29T11:01:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-29T11:09:32.871000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MCGAE004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dprt_dts: Optional[datetime] = Field(
        None,
        alias="DPRT_DTS",
        name="",
        description="",
        example="2023-07-29T11:01:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=80010383,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    hskp_sts_nm: Optional[str] = Field(
        None,
        alias="HSKP_STS_NM",
        name="",
        description="",
        example="DIRTY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_sts_nm: Optional[str] = Field(
        None,
        alias="INVTRY_STS_NM",
        name="",
        description="",
        example=" ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ocpncy_sts_nm: Optional[str] = Field(
        None,
        alias="OCPNCY_STS_NM",
        name="",
        description="",
        example="OCCUPIED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prmy_gst_nm: Optional[str] = Field(
        None,
        alias="PRMY_GST_NM",
        name="",
        description="",
        example="CLOSED_FLOOR - Pre Inspection \u2013 724",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_hist_actn_ds: str = Field(
        ...,
        alias="RM_HIST_ACTN_DS",
        name="",
        description="",
        example="CHECKIN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_hist_id: int = Field(
        ...,
        alias="RM_HIST_ID",
        name="",
        description="",
        example=543136809,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_id_vl: str = Field(
        ...,
        alias="RM_ID_VL",
        name="",
        description="",
        example="9832",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    shr_in: str = Field(
        ...,
        alias="SHR_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-29T11:09:32.871000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MCGAE004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_ref_vl: Optional[str] = Field(
        None,
        alias="TC_REF_VL",
        name="",
        description="",
        example="12096785159",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tp_ref_vl: Optional[str] = Field(
        None,
        alias="TP_REF_VL",
        name="",
        description="",
        example="753194655163",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_id_vl: Optional[str] = Field(
        None,
        alias="GRP_ID_VL",
        name="",
        description="",
        example="TW02256764",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_hist_cmt_tx: Optional[str] = Field(
        None,
        alias="RM_HIST_CMT_TX",
        name="",
        description="",
        example="TRANSFER",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_typ_nm: Optional[str] = Field(
        None,
        alias="SCH_TYP_NM",
        name="",
        description="",
        example="",
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


class DREAMSResourceInventoryManagementRmHistModel(BaseModel):
    """Payload Class for Dreams Resource Inventory Management Room History"""

    class Config:
        """Payload Level Metadata"""

        title = "Room History"
        stream_name = ""
        description = """This table tracks the history of the physical rooms in every resort. The occupancy and housekeeping status updates, etc."""
        unique_identifier = ["data.RM_HIST_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rm_hist"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
