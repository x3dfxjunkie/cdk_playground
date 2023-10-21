"""Source Data Contract for DREAMS Account Center Post Item Expense Account"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Account Center Post Item Expense Account Data"""

    acct_ctr_pst_item_exp_acct_id: int = Field(
        ...,
        alias="ACCT_CTR_PST_ITEM_EXP_ACCT_ID",
        name="",
        description="",
        example=51,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    expns_acct_typ_nm: str = Field(
        ...,
        alias="EXPNS_ACCT_TYP_NM",
        name="",
        description="",
        example="COMMISSION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_acct_nb: str = Field(
        ...,
        alias="SAP_GL_ACCT_NB",
        name="",
        description="",
        example="0000699001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_cost_ctr_cd: str = Field(
        ...,
        alias="SAP_COST_CTR_CD",
        name="",
        description="",
        example="0005154189",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_co_cd: str = Field(
        ...,
        alias="SAP_CO_CD",
        name="",
        description="",
        example="1001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_bus_area_cd: str = Field(
        ...,
        alias="SAP_BUS_AREA_CD",
        name="",
        description="",
        example="138",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_pst_item_id: int = Field(
        ...,
        alias="ACCT_CTR_PST_ITEM_ID",
        name="",
        description="",
        example=6359,
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
        example="2010-04-22T15:55:49.813Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SC5a_S1_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-04-22T15:55:49.813Z",
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


class DREAMSAccountingActrPiExpAcctModel(BaseModel):
    """Payload class for DREAMSAccountingActrPiExpAcctModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center Post Item Expense Account"
        stream_name = ""
        description = """Ties together Post Item account with Post item Expense account. The only expense type as of 6/19/2023 is commission"""
        unique_identifier = ["data.ACCT_CTR_PST_ITEM_EXP_ACCT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACTR_PI_EXP_ACCT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
