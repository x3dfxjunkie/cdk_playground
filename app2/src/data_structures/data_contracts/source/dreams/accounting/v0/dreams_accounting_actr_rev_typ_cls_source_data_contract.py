"""Source Data Contract for DREAMS Account Center Revenue Type Class"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Account Center Revenue Type Class Data"""

    acct_ctr_rev_typ_cls_id: int = Field(
        ...,
        alias="ACCT_CTR_REV_TYP_CLS_ID",
        name="",
        description="",
        example=5001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_id: int = Field(
        ...,
        alias="ACCT_CTR_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_id: int = Field(
        ...,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=366927,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_grp_id: Optional[int] = Field(
        None,
        alias="TAX_GRP_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dflt_actr_rev_cls_in: str = Field(
        ...,
        alias="DFLT_ACTR_REV_CLS_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    actr_rev_cls_actv_in: str = Field(
        ...,
        alias="ACTR_REV_CLS_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    allow_man_pst_in: str = Field(
        ...,
        alias="ALLOW_MAN_PST_IN",
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
        example="MDMUPD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-03-17T16:28:00.110Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SC5_SS2Y_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-04-07T12:38:44.773Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rpt_ctgy_id: Optional[int] = Field(
        None,
        alias="RPT_CTGY_ID",
        name="",
        description="",
        example=124,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingActrRevTypClsModel(BaseModel):
    """Payload class for DREAMSAccountingActrRevTypClsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center Revenue Type Class"
        stream_name = ""
        description = """Associates the revenue class IDs to the Account Center IDs"""
        unique_identifier = ["data.ACCT_CTR_REV_TYP_CLS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACTR_REV_TYP_CLS"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
