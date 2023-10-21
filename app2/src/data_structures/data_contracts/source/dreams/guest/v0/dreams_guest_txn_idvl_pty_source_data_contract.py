"""Source Data Contract Template for txn_idvl_pty.json"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for txn_idvl_pty"""

    txn_idvl_pty_id: int = Field(
        ...,
        alias="TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=123041161,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    salut_cd: Optional[str] = Field(
        None,
        alias="SALUT_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sfx_cd: Optional[str] = Field(
        None,
        alias="SFX_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prmy_lang_cd: Optional[str] = Field(
        None,
        alias="PRMY_LANG_CD",
        name="",
        description="",
        example="eng",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    idvl_pty_actv_in: str = Field(
        ...,
        alias="IDVL_PTY_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    idvl_lst_nm: Optional[str] = Field(
        None,
        alias="IDVL_LST_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    idvl_fst_nm: Optional[str] = Field(
        None,
        alias="IDVL_FST_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    idvl_mid_nm: Optional[str] = Field(
        None,
        alias="IDVL_MID_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_idvl_pty_inactv_dts: Optional[datetime] = Field(
        None,
        alias="TXN_IDVL_PTY_INACTV_DTS",
        name="",
        description="",
        example="2023-07-13T23:04:29Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_nb: Optional[float] = Field(
        None,
        alias="AGE_NB",
        name="",
        description="",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pos_lst_nm_cd: Optional[float] = Field(
        None,
        alias="POS_LST_NM_CD",
        name="",
        description="",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fvrt_chrctr_nm: Optional[str] = Field(
        None,
        alias="FVRT_CHRCTR_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dvc_mbr_typ_nm: Optional[str] = Field(
        None,
        alias="DVC_MBR_TYP_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dcl_txfr_cd: Optional[str] = Field(
        None,
        alias="DCL_TXFR_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRT-DISNEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-13T13:42:28Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRT-DISNEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-13T13:42:28Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-13T11:34:21Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    incognito: Optional[str] = Field(
        None,
        alias="INCOGNITO",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGuestTxnIdvlPtyModel(BaseModel):
    """DREAMSGuestTxnIdvlPtyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Individual Party"
        stream_name = ""
        description = "Provides a transactional ID associated with an individual guest"  # optional
        unique_identifier = ["data.TXN_IDVL_PTY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_idvl_pty"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
