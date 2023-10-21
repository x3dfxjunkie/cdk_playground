"""Source Data Contract Template for Coupon Profile"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime


from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon Profile Data"""

    cpn_prfl_id: float = Field(
        ...,
        alias="CPN_PRFL_ID",
        name="",
        description="",
        example=26.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cpn_rdmpt_typ_nm: str = Field(
        ...,
        alias="CPN_RDMPT_TYP_NM",
        name="",
        description="",
        example="GUEST_COUNT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cpn_cd: str = Field(
        ...,
        alias="CPN_CD",
        name="",
        description="",
        example="BK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cpn_ds: str = Field(
        ...,
        alias="CPN_DS",
        name="",
        description="",
        example="Breakfast Only",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cpn_shrt_ds: str = Field(
        ...,
        alias="CPN_SHRT_DS",
        name="",
        description="",
        example="BREAKFAST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cpn_tndr_cd: str = Field(
        ...,
        alias="CPN_TNDR_CD",
        name="",
        description="",
        example="33",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ENGLD006",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2011-07-12T11:06:21.299000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="CLAET001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2011-07-12T11:06:21.299000Z",
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


class DREAMSEntitlementsCpnPrflTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnPrflTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Coupon Profile"
        stream_name = ""
        description = """This table ties coupon descriptions to a coupon profile ID by these coupon types:CPN_RDMPT_TYP_NM
        UNLIMITED_RECREATION
        DEBIT
        GUEST_COUNT"""
        unique_identifier = ["data.CPN_PRFL_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_PRFL_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
