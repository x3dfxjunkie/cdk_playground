"""Source Data Contract for DREAMS Charge Account Charge Group"""


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Charge Account Charge Group Data"""

    auth_pin_encrpt_hash_vl: Optional[str] = Field(
        None,
        alias="AUTH_PIN_ENCRPT_HASH_VL",
        name="",
        description="",
        example="AAAaaAAAAAAAAaaAAAAaaAAAaaAAAAAAAA+A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_id: int = Field(
        ...,
        alias="CHRG_GRP_ID",
        name="",
        description="",
        example=983378339,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_sts_nm: str = Field(
        ...,
        alias="CHRG_GRP_STS_NM",
        name="",
        description="",
        example="UnEarned",
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
    chrg_grp_ds: str = Field(
        ...,
        alias="CHRG_GRP_DS",
        name="",
        description="",
        example="Disney's Beach Club Resort Sun Feb 04 00:00:00 EST 2024 - Fri Feb 09 00:00:00 EST 2024 3YGGC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_strt_dts: datetime = Field(
        ...,
        alias="CHRG_GRP_STRT_DTS",
        name="",
        description="",
        example="2024-02-04T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_end_dts: datetime = Field(
        ...,
        alias="CHRG_GRP_END_DTS",
        name="",
        description="",
        example="2024-02-09T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_fac_id: Optional[int] = Field(
        None,
        alias="TXN_FAC_ID",
        name="",
        description="",
        example=80010389,
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
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="STEEW010",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T17:18:34.860000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="STEEW010",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T17:18:34.860000Z",
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


class DREAMSChargeAccountChrgGrpModel(BaseModel):
    """Payload class for DREAMSChargeAccountChrgGrpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "CREAMS Charge Account Charge Group"
        stream_name = ""
        description = ""
        unique_identifier = ["data.CHRG_GRP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "chrg_grp"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
