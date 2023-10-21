"""Source Data Contract Template for CNTRY.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for CNTRY"""

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
    alt_cntry_cd: str = Field(
        ...,
        alias="ALT_CNTRY_CD",
        name="",
        description="",
        example="AW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cntry_nb: int = Field(
        ...,
        alias="CNTRY_NB",
        name="",
        description="",
        example=533,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cntry_short_nm: str = Field(
        ...,
        alias="CNTRY_SHORT_NM",
        name="",
        description="",
        example="ARUBA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cntry_full_nm: Optional[str] = Field(
        None,
        alias="CNTRY_FULL_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cntry_ds: Optional[str] = Field(
        None,
        alias="CNTRY_DS",
        name="",
        description="",
        example="",
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
        example="2009-07-08T22:15:05Z",
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
        example="2009-07-08T22:15:05Z",
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


class DREAMSGuestCntryModel(BaseModel):
    """DREAMSGuestCntryModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Country"
        stream_name = ""
        description = "Country Codes and Names"  # optional
        unique_identifier = ["data.CNTRY_CD"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "cntry"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
