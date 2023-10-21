"""Source Data Contract for Dreams Entitlement Coupon Restriction Type"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon Restriction Type Data"""

    cpn_rstrct_typ_nm: str = Field(
        ...,
        alias="CPN_RSTRCT_TYP_NM",
        name="",
        description="",
        example="PER_PERSON_PER_NIGHT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-17T11:18:42Z",
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


class DREAMSEntitlementsCpnRstrctTypTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnRstrctTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Coupon Restriction Type"
        stream_name = ""
        description = ""
        unique_identifier = ["data.CPN_RSTRCT_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_RSTRCT_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
