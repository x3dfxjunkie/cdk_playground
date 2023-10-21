"""Source Data Contract for DREAMS SAP Stratus Card Class"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams SAP Stratus Card Class Data"""

    strts_card_cls_cd: str = Field(
        ...,
        alias="STRTS_CARD_CLS_CD",
        name="",
        description="",
        example="0118",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    strts_card_cls_nm: str = Field(
        ...,
        alias="STRTS_CARD_CLS_NM",
        name="",
        description="",
        example="Gift Card",
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
        example="2006-10-18T19:46:53.675Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingStrtsCardClsModel(BaseModel):
    """Payload class for DREAMSAccountingStrtsCardClsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Stratus Card Class"
        stream_name = ""
        description = """Stratus Card Class names associated to Stratus Card Class IDs"""
        unique_identifier = ["data.STRTS_CARD_CLS_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "STRTS_CARD_CLS"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
