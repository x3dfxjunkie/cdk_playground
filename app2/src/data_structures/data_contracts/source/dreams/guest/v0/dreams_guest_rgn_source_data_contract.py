"""Source Data Contract Template for rgn.json"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for rgn"""

    cntry_cd: str = Field(
        ...,
        alias="CNTRY_CD",
        name="",
        description="",
        example="ABW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rgn_cd: str = Field(
        ...,
        alias="RGN_CD",
        name="",
        description="",
        example="AW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    alt_rgn_cd: str = Field(
        ...,
        alias="ALT_RGN_CD",
        name="",
        description="",
        example="AW-AW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sub_div_ctgy_nm: Optional[str] = Field(
        None,
        alias="SUB_DIV_CTGY_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prmy_sub_div_nm: str = Field(
        ...,
        alias="PRMY_SUB_DIV_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sec_sub_div_nm: Optional[str] = Field(
        None,
        alias="SEC_SUB_DIV_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trnry_sub_div_nm: Optional[str] = Field(
        None,
        alias="TRNRY_SUB_DIV_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rgn_div_nm: Optional[str] = Field(
        None,
        alias="RGN_DIV_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dsny_ext_in: str = Field(
        ...,
        alias="DSNY_EXT_IN",
        name="",
        description="",
        example="Y",
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
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-07-08T22:14:56Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-07-08T22:14:56Z",
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


class DREAMSGuestRgnModel(BaseModel):
    """DREAMSGuestRgnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Region"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CNTRY_CD", "data.RGN_CD"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rgn"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
