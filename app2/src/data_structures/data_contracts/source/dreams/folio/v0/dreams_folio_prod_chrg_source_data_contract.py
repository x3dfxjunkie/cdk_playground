"""Source Data Contract for Dreams Folio Product Charge"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Product Charge Data"""

    chrg_id: int = Field(
        ...,
        alias="CHRG_ID",
        name="",
        description="",
        example=3425562269,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_mkt_pkg_id: Optional[int] = Field(
        None,
        alias="CHRG_MKT_PKG_ID",
        name="",
        description="",
        example=161916684,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    comctn_chan_nm: Optional[str] = Field(
        None,
        alias="COMCTN_CHAN_NM",
        name="",
        description="",
        example="Contact Center",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-23T09:44:26.412000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="TbxSyncUser",
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

    ovrd_prod_chrg_in: str = Field(
        ...,
        alias="OVRD_PROD_CHRG_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2011-01-26T01:41:32.803Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_cd: Optional[str] = Field(
        None,
        alias="PROD_CD",
        name="",
        description="",
        example="SA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chrg_upgrd_typ_nm: str = Field(
        ...,
        alias="PROD_CHRG_UPGRD_TYP_NM",
        name="",
        description="",
        example="Original",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_ds: Optional[str] = Field(
        None,
        alias="PROD_DS",
        name="",
        description="",
        example="Standard Room - SA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=115834,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_typ_nm: str = Field(
        ...,
        alias="PROD_TYP_NM",
        name="",
        description="",
        example="AccommodationProduct",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sls_chan_nm: Optional[str] = Field(
        None,
        alias="SLS_CHAN_NM",
        name="",
        description="",
        example="Internal and External WholeSaler",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trvl_agt_id: Optional[int] = Field(
        None,
        alias="TRVL_AGT_ID",
        name="",
        description="",
        example=111504,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-23T09:44:26.412000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="TbxSyncUser",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioProdChrgModel(BaseModel):
    """Payload class for DREAMSFolioProdChrgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Product Charge"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CHRG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PROD_CHRG"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
