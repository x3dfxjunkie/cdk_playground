"""Source Data Contract for DREAMS Natural Post Item Configuration"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Natural Post Item Configuration Data"""

    natr_pst_item_config_id: int = Field(
        ...,
        alias="NATR_PST_ITEM_CONFIG_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_item_id: int = Field(
        ...,
        alias="PST_ITEM_ID",
        name="",
        description="",
        example=20228,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_acct_ctr_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    natr_pst_item_config_strt_dt: datetime = Field(
        ...,
        alias="NATR_PST_ITEM_CONFIG_STRT_DT",
        name="",
        description="",
        example="1999-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    natr_pst_item_config_end_dt: Optional[datetime] = Field(
        None,
        alias="NATR_PST_ITEM_CONFIG_END_DT",
        name="",
        description="",
        example="1999-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_st_nm: str = Field(
        ...,
        alias="PST_ST_NM",
        name="",
        description="",
        example="Earned",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_typ_nm: str = Field(
        ...,
        alias="FOLIO_TYP_NM",
        name="",
        description="",
        example="INDIVIDUAL",
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
        example="2010-01-20T06:28:38.945Z",
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
        example="2010-05-26T13:36:24.545Z",
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


class DREAMSAccountingNatrPitmConfigModel(BaseModel):
    """Payload class for DREAMSAccountingNatrPitmConfigModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Natural Post Item Configuration"
        stream_name = ""
        description = """Configures the Post Items, Source Account Center ID and Folio type for the Natural accounts"""
        unique_identifier = ["data.NATR_PST_ITEM_CONFIG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "NATR_PITM_CONFIG"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
