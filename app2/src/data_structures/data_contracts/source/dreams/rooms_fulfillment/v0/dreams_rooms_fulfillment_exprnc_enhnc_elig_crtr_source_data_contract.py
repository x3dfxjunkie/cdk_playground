"""Source Data Contract Template for Dreams - Room Fulfillment Experience Enhancement Eligibility Criteria"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for Dreams - Room Fulfillment Experience Enhancement Eligibility Criteria Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2016-05-30T06:14:22Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="fakeu001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    crtr_usg_lvl_nm: str = Field(
        ...,
        alias="CRTR_USG_LVL_NM",
        name="",
        description="",
        example="Travel Component",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    elig_crtr_nm: str = Field(
        ...,
        alias="ELIG_CRTR_NM",
        name="",
        description="",
        example="Product",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_crtr_end_dt: Optional[str] = Field(
        None,
        alias="EXPRNC_ENHNC_CRTR_END_DT",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_crtr_strt_dt: datetime = Field(
        ...,
        alias="EXPRNC_ENHNC_CRTR_STRT_DT",
        name="",
        description="",
        example="2016-05-30T06:14:22Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_crtr_vl: str = Field(
        ...,
        alias="EXPRNC_ENHNC_CRTR_VL",
        name="",
        description="",
        example="Accommodation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_nm: str = Field(
        ...,
        alias="EXPRNC_ENHNC_NM",
        name="",
        description="",
        example="Straight To Park",
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2016-05-30T06:14:22Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="fakeu001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentExprncEnhncEligCrtrModel(BaseModel):
    """Payload class for Dreams - Room Fulfillment Experience Enhancement Eligibility Criteria Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Experience Enhancement Eligibility Criteria"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.EXPRNC_ENHNC_NM", "data.ELIG_CRTR_NM", "data.EXPRNC_ENHNC_CRTR_VL"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exprnc_enhnc_elig_crtr"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
