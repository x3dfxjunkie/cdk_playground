"""Source Data Contract Template for Dreams - Profile Criteria"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Profile Criteria Data"""

    all_fac_in: str = Field(
        ...,
        alias="ALL_FAC_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    all_pkg_in: str = Field(
        ...,
        alias="ALL_PKG_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    all_rsrc_invtry_typ_in: str = Field(
        ...,
        alias="ALL_RSRC_INVTRY_TYP_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-31T09:08:56.499000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ADAMM015",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dflt_prfl_in: str = Field(
        ...,
        alias="DFLT_PRFL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    excl_in: str = Field(
        ...,
        alias="EXCL_IN",
        name="",
        description="",
        example="N",
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

    prfl_crtra_id: int = Field(
        ...,
        alias="PRFL_CRTRA_ID",
        name="",
        description="",
        example=430700,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prfl_id: int = Field(
        ...,
        alias="PRFL_ID",
        name="",
        description="",
        example=188600,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    slct_in: str = Field(
        ...,
        alias="SLCT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-31T09:08:56.499000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="ADAMM015",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_invtry_typ_cd: Optional[str] = Field(
        None,
        alias="RSRC_INVTRY_TYP_CD",
        name="",
        description="",
        example="6A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acm_fac_id: Optional[int] = Field(
        None,
        alias="ACM_FAC_ID",
        name="",
        description="",
        example=80010392,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_id: Optional[int] = Field(
        None,
        alias="FAC_ID",
        name="",
        description="",
        example=80010392,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_id: Optional[int] = Field(
        None,
        alias="PKG_ID",
        name="",
        description="",
        example=5177,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSProfilePrflCrtraModel(BaseModel):
    """Payload class for DREAMSProfilePrflCrtraModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Profile Criteria"
        stream_name = ""
        description = ""
        unique_identifier = ["data.PRFL_CRTRA_ID"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prfl_crtra"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
