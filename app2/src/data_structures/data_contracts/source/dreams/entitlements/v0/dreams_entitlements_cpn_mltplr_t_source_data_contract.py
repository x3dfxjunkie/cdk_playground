"""Source Data Contract for Dreams Entitlement Coupon Multiplier"""


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon Coupon Multiplier Data"""

    cpn_deb_am: int = Field(
        ...,
        alias="CPN_DEB_AM",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_mltplr_aplcbl_typ_nm: str = Field(
        ...,
        alias="CPN_MLTPLR_APLCBL_TYP_NM",
        name="",
        description="",
        example="PER_ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_mltplr_config_id: int = Field(
        ...,
        alias="CPN_MLTPLR_CONFIG_ID",
        name="",
        description="",
        example=2147479998,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_mltplr_frq_typ_nm: str = Field(
        ...,
        alias="CPN_MLTPLR_FRQ_TYP_NM",
        name="",
        description="",
        example="PER_PLAN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_prfl_id: int = Field(
        ...,
        alias="CPN_PRFL_ID",
        name="",
        description="",
        example=1111111120,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2021-08-09T03:46:48.499000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    iss_cn: int = Field(
        ...,
        alias="ISS_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_cpn_cd: str = Field(
        ...,
        alias="PKG_CPN_CD",
        name="",
        description="",
        example="PA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2021-08-09T03:46:48.499000Z",
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


class DREAMSEntitlementsCpnMltplrTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnMltplrTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Coupon Multiplier"
        stream_name = ""
        description = ""
        unique_identifier = ["data.CPN_MLTPLR_CONFIG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_MLTPLR_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
