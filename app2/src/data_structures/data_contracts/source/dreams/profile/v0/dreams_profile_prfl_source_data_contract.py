"""Source Data Contract for Dreams Profile"""


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams Profile Data"""

    prfl_id: int = Field(
        ...,
        alias="PRFL_ID",
        name="",
        description="",
        example=188400,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prfl_typ_nm: str = Field(
        ...,
        alias="PRFL_TYP_NM",
        name="",
        description="",
        example="Comment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prfl_actv_in: str = Field(
        ...,
        alias="PRFL_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prrty_dspl_in: str = Field(
        ...,
        alias="PRRTY_DSPL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prfl_val_cd: str = Field(
        ...,
        alias="PRFL_VAL_CD",
        name="",
        description="",
        example="CONTIX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prfl_val_ds: str = Field(
        ...,
        alias="PRFL_VAL_DS",
        name="",
        description="",
        example="Guest was issued (#) Contingency Tickets due to: ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="BULLN007",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-02T10:10:26.858000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="BULLN007",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-02T10:10:26.858000Z",
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
    extnl_ref_vl: Optional[str] = Field(
        None,
        alias="EXTNL_REF_VL",
        name="",
        description="",
        example="16",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSProfilePrflModel(BaseModel):
    """Payload class for DREAMSProfilePrflModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Profile"
        stream_name = ""
        description = "This table provides coded comments across the dreams application for the following types"
        unique_identifier = ["data.PRFL_ID"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prfl"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
