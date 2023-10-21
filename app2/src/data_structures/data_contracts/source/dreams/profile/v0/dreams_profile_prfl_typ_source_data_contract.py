"""Source Data Contract  for DREAMS Profile Type"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Profile Data"""

    prfl_typ_nm: str = Field(
        ...,
        alias="PRFL_TYP_NM",
        name="",
        description="",
        example="Alert",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_in: str = Field(
        ...,
        alias="GRP_IN",
        name="",
        description="",
        example="N",
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
        example="2009-08-12T05:50:29.000-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSProfilePrflTypModel(BaseModel):
    """Payload class for DREAMSProfilePrflTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Profile Type"
        stream_name = ""
        description = "The list of profile types: Message; Service; GRAND_GATHERING_TYPE; Attribute; Comment; Alert"
        unique_identifier = ["data.PRFL_TYP_NM"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prfl_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
