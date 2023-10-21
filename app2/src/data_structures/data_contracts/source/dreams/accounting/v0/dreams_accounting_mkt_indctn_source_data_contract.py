"""Source Data Contract for DREAMS Market Indication"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Market Indication Data"""

    mkt_indctn_cd: str = Field(
        ...,
        alias="MKT_INDCTN_CD",
        name="",
        description="",
        example="H",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    mkt_indctn_ds: str = Field(
        ...,
        alias="MKT_INDCTN_DS",
        name="",
        description="",
        example="Resort Reservations",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Initial Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T19:46:53.175Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingMktIndctnModel(BaseModel):
    """Payload class for DREAMSAccountingMktIndctnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Market Indication"
        stream_name = ""
        description = """One record with a code for Resort Reservations"""
        unique_identifier = ["data.MKT_INDCTN_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "MKT_INDCTN"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
