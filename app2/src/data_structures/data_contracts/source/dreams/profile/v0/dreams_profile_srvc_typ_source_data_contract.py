"""Source Data Contract for Dreams Profile SrvcTyp"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from datetime import datetime


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-12T10:07:21Z",
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

    srvc_typ_nm: str = Field(
        ...,
        alias="SRVC_TYP_NM",
        name="",
        description="",
        example="Delivery",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSProfileSrvcTypModel(BaseModel):
    """Payload class for DREAMSProfileSrvcTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Service Type"
        stream_name = ""
        description = ""
        unique_identifier = ["data.SRVC_TYP_NM"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "srvc_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
