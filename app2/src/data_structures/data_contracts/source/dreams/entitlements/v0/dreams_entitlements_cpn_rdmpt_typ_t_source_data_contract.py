"""Source Data Contract for Dreams Entitlement Coupon Redemption Type"""


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon Redemption Type Data"""

    cpn_rdmpt_typ_nm: str = Field(
        ...,
        alias="CPN_RDMPT_TYP_NM",
        name="",
        description="",
        example="DEBIT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-07-12T21:49:16Z",
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


class DREAMSEntitlementsCpnRdmptTypTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnRdmptTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Coupon Redemption Type"
        stream_name = ""
        description = ""
        unique_identifier = ["data.CPN_RDMPT_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_RDMPT_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
