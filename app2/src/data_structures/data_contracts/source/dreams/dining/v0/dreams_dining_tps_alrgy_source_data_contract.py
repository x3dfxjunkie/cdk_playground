"""Source Data Contract for Dreams Dining TPS ALRGY"""
from __future__ import annotations
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from pydantic import BaseModel, Field
from typing import Optional


class Data(BaseModel):
    """Class for Dreams Dining TPS ALRGY Data"""

    alrgy_id: int = Field(
        ...,
        alias="ALRGY_ID",
        name="Allergy Identifier",
        description="An auto-assigned value either thru application or database.",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_id: int = Field(
        ...,
        alias="TPS_ID",
        name="Travel Plan Segment Identification",
        description="A unique numeric identifier for a travel plan segment.",
        example=530631525237,
        guest_identifier=True,
        identifier_tag="indirect",
        transaction_identifier=False,
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="Create User Identification Code",
        description="The identification value for the user or application that created a row in this table.",
        example="WDPRO",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="Create Date Time",
        description="The month day century year hour minute and second when a row was created in this table.",
        example="2023-03-29T11:30:10.669000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningTpsAlrgyModel(BaseModel):
    """Payload class for DREAMSDiningTpsAlrgyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan Segment Allergy"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table ties an allergy type to a specific reservation"
        unique_identifier = ["data.ALRGY_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tps_alrgy"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
