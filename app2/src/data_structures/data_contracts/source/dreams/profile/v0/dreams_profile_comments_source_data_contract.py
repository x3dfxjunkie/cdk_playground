"""Source Data Contract Template for Dreams Profile Comments"""
from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data Payload for Comments"""

    acm_fac_id: int = Field(
        ...,
        alias="acm_fac_id",
        name="",
        description="",
        example=80010399,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    codes: str = Field(
        ...,
        alias="codes",
        name="",
        description="",
        example="CX,D1,D3,D2,D5,D8,EC,ET,EB,ED,RA,RX,3R,5R,RJ,RD,KR,OR,XR,ZR,RK,RI,R3,R5,RE,RL15,RG,RN,RF,RM,RT,BH,RH,RS,RP,R9,RV,RY,R7,RZ,2R,R8,RW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lilo_active: str = Field(
        ...,
        alias="lilo_active",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prfl_val_cd: str = Field(
        ...,
        alias="prfl_val_cd",
        name="",
        description="",
        example="NSKY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSProfileCommentsModel(BaseModel):
    """Payload class for DREAMSProfileCommentsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Comments"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "comments"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
