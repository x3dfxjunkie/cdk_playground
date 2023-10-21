"""Source Data Contract for Dreams Profile Srvc"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from datetime import date, datetime


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-12T11:44:11Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mxmo_item_nb: Optional[str] = Field(
        None,
        alias="MXMO_ITEM_NB",
        name="",
        description="",
        example="999999",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkup_rqd_in: str = Field(
        ...,
        alias="PKUP_RQD_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[date] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2011-05-17",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: Optional[int] = Field(
        None,
        alias="PROD_ID",
        name="",
        description="",
        example=124455,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    srvc_id: int = Field(
        ...,
        alias="SRVC_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    srvc_typ_nm: str = Field(
        ...,
        alias="SRVC_TYP_NM",
        name="",
        description="",
        example="Delivery",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2011-05-17T09:24:44.191000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSProfileSrvcModel(BaseModel):
    """Payload class for DREAMSProfileSrvcModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Service"
        stream_name = ""
        description = ""
        unique_identifier = ["data.SRVC_ID"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "srvc"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
