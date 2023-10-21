"""Source Data Contract for Dreams Price Package Category Product"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Price Package Category Product"""

    cmpnt_prod_id: int = Field(
        ...,
        alias="CMPNT_PROD_ID",
        name="",
        description="",
        example=23383,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2012-11-27T09:07:45.466300Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
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

    pkg_ctgy_prod_id: int = Field(
        ...,
        alias="PKG_CTGY_PROD_ID",
        name="",
        description="",
        example=11557923,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_ctgy_prod_sell_in: str = Field(
        ...,
        alias="PKG_CTGY_PROD_SELL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_id: int = Field(
        ...,
        alias="PKG_PROD_CLS_ID",
        name="",
        description="",
        example=514902,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-10T14:58:46.221222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_grid_id: int = Field(
        ...,
        alias="PRICE_GRID_ID",
        name="",
        description="",
        example=398316,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2012-11-27T09:07:45.466300Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePkgCtgyProdTModel(BaseModel):
    """Payload class for DREAMSPricePkgCtgyProdTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Package Category Product"
        stream_name = ""
        description = "This table holds Package Product Class ID, Price Grid ID and Component Product ID that is related to a specific Package"  # optional
        unique_identifier = ["data.PKG_CTGY_PROD_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PKG_CTGY_PROD_ID_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
