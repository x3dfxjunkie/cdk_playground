"""Source Data Contract for Dreams Folio Scheduled Events Transaction"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Scheduled Events Transaction Data"""

    se_txn_id: int = Field(
        ...,
        alias="SE_TXN_ID",
        name="",
        description="",
        example=33021298,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    se_txn_typ_nm: str = Field(
        ...,
        alias="SE_TXN_TYP_NM",
        name="",
        description="",
        example="PAYMENT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    se_loc_nm: str = Field(
        ...,
        alias="SE_LOC_NM",
        name="",
        description="",
        example="10",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    se_op_usr_id_cd: str = Field(
        ...,
        alias="SE_OP_USR_ID_CD",
        name="",
        description="",
        example="WDPRO1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    se_op_rl_nm: str = Field(
        ...,
        alias="SE_OP_RL_NM",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    se_txn_ref_id: int = Field(
        ...,
        alias="SE_TXN_REF_ID",
        name="",
        description="",
        example=1563773386,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    se_bank_out_in: str = Field(
        ...,
        alias="SE_BANK_OUT_IN",
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
        example="WDPRO1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T10:38:55.276000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T10:38:55.276000Z",
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
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-06-09T10:38:55.276000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioSeTxnModel(BaseModel):
    """Payload class for DREAMSFolioSeTxnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Scheduled Events Transaction"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.SE_TXN_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SE_TXN"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
