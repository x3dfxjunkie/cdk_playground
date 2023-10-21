"""Source Data Contract for Dreams Entitlement Plan External Reference Type"""


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Entitlement Plan External Reference Type Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2017-10-17T03:33:54Z",
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

    enttl_ext_ref_typ_nm: str = Field(
        ...,
        alias="ENTTL_EXT_REF_TYP_NM",
        name="",
        description="",
        example="Facility",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsEnttlExtRefTypTModel(BaseModel):
    """Payload class for DREAMSEntitlementsEnttlExtRefTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Plan External Reference Type"
        stream_name = ""
        description = ""
        unique_identifier = ["data.ENTTL_EXT_REF_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ENTTL_EXT_REF_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
