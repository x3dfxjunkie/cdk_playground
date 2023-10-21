"""Source Data Contract for DREAMS Post Group"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Post Group Data"""

    pst_grp_id: int = Field(
        ...,
        alias="PST_GRP_ID",
        name="",
        description="",
        example=1001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_nm: str = Field(
        ...,
        alias="PST_GRP_NM",
        name="",
        description="",
        example="Accounts Receivable Whsl Pkg Adjustment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_actv_in: str = Field(
        ...,
        alias="PST_GRP_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_tax_dtrmnt_in: str = Field(
        ...,
        alias="PST_GRP_TAX_DTRMNT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_dspl_seq_nb: int = Field(
        ...,
        alias="PST_GRP_DSPL_SEQ_NB",
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
        example="SC4_SS_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-03-02T02:42:00.023Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SC5a_S2P_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-05-24T18:10:58.195Z",
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


class DREAMSAccountingPstGrpModel(BaseModel):
    """Payload class for DREAMSAccountingPstGrpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Post Group"
        stream_name = ""
        description = """Post Group names associated to Post Group IDs"""
        unique_identifier = ["data.PST_GRP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PST_GRP"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
