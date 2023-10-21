"""Source Data Contract for Dreams Group Management Group Office"""
from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Group Management Group Office Data"""

    gro_nm: str = Field(
        ...,
        alias="GRO_NM",
        name="",
        description="",
        example="All Star GRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gro_phn_nb: str = Field(
        ...,
        alias="GRO_PHN_NB",
        name="",
        description="",
        example="(407) 938-4868",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGroModel(BaseModel):
    """Payload class for DREAMSGroupManagementGroModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Office"
        stream_name = ""
        description = "This has the Group Office Name and Phone number"  # optional
        unique_identifier = ["data.GRO_NM"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "gro"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
