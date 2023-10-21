"""Source Data Contract for DREAMS Offset Post Group Configuration"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Offset Post Group Configuration Data"""

    ofst_pst_grp_config_id: int = Field(
        ...,
        alias="OFST_PST_GRP_CONFIG_ID",
        name="",
        description="",
        example=100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ofst_pst_grp_id: int = Field(
        ...,
        alias="OFST_PST_GRP_ID",
        name="",
        description="",
        example=100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ofst_pst_grp_config_strt_dt: datetime = Field(
        ...,
        alias="OFST_PST_GRP_CONFIG_STRT_DT",
        name="",
        description="",
        example="1999-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ofst_pst_grp_config_end_dt: datetime = Field(
        ...,
        alias="OFST_PST_GRP_CONFIG_END_DT",
        name="",
        description="",
        example="2099-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_id: Optional[int] = Field(
        None,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=366854,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_typ_id: int = Field(
        ...,
        alias="REV_TYP_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_id: Optional[int] = Field(
        None,
        alias="PROD_ID",
        name="",
        description="",
        example=53828,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_id: Optional[int] = Field(
        None,
        alias="PKG_ID",
        name="",
        description="",
        example=54089,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_chan_id: Optional[str] = Field(
        None,
        alias="PKG_CHAN_ID",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    allow_sspns_in: str = Field(
        ...,
        alias="ALLOW_SSPNS_IN",
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
        example="2010-05-24T19:49:46.446Z",
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
        example="2010-05-24T19:49:46.446Z",
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
    folio_typ_nm: Optional[str] = Field(
        None,
        alias="FOLIO_TYP_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingOfstPgrpConfigModel(BaseModel):
    """Payload class for DREAMSAccountingOfstPgrpConfigModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Offset Post Group Configuration"
        stream_name = ""
        description = """Configures the Post Groups, Revenue Class ID, Revenue Type Code, Product ID and PKG ID if applicable for the Offset accounts"""
        unique_identifier = ["data.OFST_PST_GRP_CONFIG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "OFST_PGRP_CONFIG"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
