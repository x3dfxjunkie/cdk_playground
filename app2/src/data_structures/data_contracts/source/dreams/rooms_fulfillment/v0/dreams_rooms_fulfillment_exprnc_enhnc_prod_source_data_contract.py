"""Source Data Contract Template for Dreams - Room Fulfillment Experience Enhancement Product"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for Dreams - Room Fulfillment Experience Enhancement Product Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2013-04-30T06:14:23Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="DBTeam",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_nm: str = Field(
        ...,
        alias="EXPRNC_ENHNC_NM",
        name="",
        description="",
        example="Bypass Front Desk",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_prod_end_dt: Optional[str] = Field(
        None,
        alias="EXPRNC_ENHNC_PROD_END_DT",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_prod_strt_dt: datetime = Field(
        ...,
        alias="EXPRNC_ENHNC_PROD_STRT_DT",
        name="",
        description="",
        example="2013-04-30T06:14:23Z",
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

    prge_dts: Optional[str] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=146370,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2013-04-30T09:09:46.229932Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="DMTeam",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    zero_price_in: str = Field(
        ...,
        alias="ZERO_PRICE_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentExprncEnhncProdModel(BaseModel):
    """Payload class for Dreams - Room Fulfillment Experience Enhancement Product Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Experience Enhancement Product"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.EXPRNC_ENHNC_NM", "data.PROD_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exprnc_enhnc_prod"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
