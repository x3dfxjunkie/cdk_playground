"""Source Data Contract for DREAMS Account Center Post Account SAP"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Account Center Post Account SAP Data"""

    acct_ctr_pst_acct_sap_id: int = Field(
        ...,
        alias="ACCT_CTR_PST_ACCT_SAP_ID",
        name="",
        description="",
        example=200001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_pst_acct_id: int = Field(
        ...,
        alias="ACCT_CTR_PST_ACCT_ID",
        name="",
        description="",
        example=100007,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_ref_id: int = Field(
        ...,
        alias="SAP_GL_REF_ID",
        name="",
        description="",
        example=55387,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_typ_nm: str = Field(
        ...,
        alias="TXN_TYP_NM",
        name="",
        description="",
        example="SALE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dflt_cfig_in: str = Field(
        ...,
        alias="DFLT_CFIG_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tx_exmpt_in: str = Field(
        ...,
        alias="TX_EXMPT_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-20T06:42:52.324Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SC5_SS1_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-03-24T18:55:43.792Z",
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


class DREAMSAccountingAcctCtrPsactSapModel(BaseModel):
    """Payload class for DREAMSAccountingAcctCtrPsactSapModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center Post Account SAP"
        stream_name = ""
        description = """This table has IDs and information related to the account center and the SAP post account"""
        unique_identifier = ["data.ACCT_CTR_PST_ACCT_SAP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACCT_CTR_PSACT_SAP"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
