"""Source Data Contract Template for DREAMS Resource Inventory Management Experience Card Access"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-14T16:53:16.250219Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_card_accs_id: int = Field(
        ...,
        alias="EXPRNC_CARD_ACCS_ID",
        name="",
        description="",
        example=15,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exp_card_acss_nm: str = Field(
        ...,
        alias="EXP_CARD_ACSS_NM",
        name="",
        description="",
        example="Concierge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementExpCardAcssModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementExpCardAcssModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Experience Card Access"
        stream_name = ""
        description = """This table associates a unique identifier for the various areas within a resort that are accessible to cast and guest"""
        unique_identifier = ["data.EXPRNC_CARD_ACCS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exp_card_acss"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
