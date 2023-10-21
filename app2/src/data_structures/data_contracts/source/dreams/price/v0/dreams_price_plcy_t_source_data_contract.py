"""Source Data Contract for Dreams Price Policy"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price Policy Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2018-03-09T09:32:50.290286Z",
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

    plcy_ds: str = Field(
        ...,
        alias="PLCY_DS",
        name="",
        description="",
        example="DVC - Mother's Day Brunch Check- in location",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plcy_id: int = Field(
        ...,
        alias="PLCY_ID",
        name="",
        description="",
        example=18998888,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plcy_nm: str = Field(
        ...,
        alias="PLCY_NM",
        name="",
        description="",
        example="DVC - Mother's Day Brunch Check- in location",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plcy_typ_nm: str = Field(
        ...,
        alias="PLCY_TYP_NM",
        name="",
        description="",
        example="Restriction / Requirement",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2018-03-09T09:32:50.290286Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePlcyTModel(BaseModel):
    """Payload class for DREAMSPricePlcyTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Policy"
        stream_name = ""
        description = "This table holds multiple policies related to products"  # optional
        unique_identifier = ["data.PLCY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PLCY_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
