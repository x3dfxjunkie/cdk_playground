"""Source Data Contract Template for CHRG_GRP.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for CHRG_GRP"""

    chrg_grp_sts_nm: str = Field(
        ...,
        alias="CHRG_GRP_STS_NM",
        name="",
        description="",
        example="Earned",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_ds: Optional[str] = Field(
        None,
        alias="CHRG_GRP_DS",
        name="",
        description="",
        example="From Booking",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_strt_dts: datetime = Field(
        ...,
        alias="CHRG_GRP_STRT_DTS",
        name="",
        description="",
        example="2023-06-10T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_end_dts: datetime = Field(
        ...,
        alias="CHRG_GRP_END_DTS",
        name="",
        description="",
        example="2023-06-17T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_acct_ctr_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_dlgt_sml_bal_wrtoff_in: str = Field(
        ...,
        alias="GRP_DLGT_SML_BAL_WRTOFF_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDW-MDX-IOS-",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-10T11:37:43.785000Z",
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
    chrg_grp_actv_in: str = Field(
        ...,
        alias="CHRG_GRP_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_id: int = Field(
        ...,
        alias="CHRG_GRP_ID",
        name="",
        description="",
        example=975171530,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_typ_nm: str = Field(
        ...,
        alias="CHRG_GRP_TYP_NM",
        name="",
        description="",
        example="Node",
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
        example="2023-04-11T21:29:06.692000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_fac_id: Optional[int] = Field(
        None,
        alias="TXN_FAC_ID",
        name="",
        description="",
        example=80010400,
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
    auth_pin_encrpt_hash_vl: Optional[str] = Field(
        None,
        alias="AUTH_PIN_ENCRPT_HASH_VL",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioChrgGrpModel(BaseModel):
    """Payload class for DREAMSFolioChrgGrpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Group"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CHRG_GRP_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG_GRP"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
