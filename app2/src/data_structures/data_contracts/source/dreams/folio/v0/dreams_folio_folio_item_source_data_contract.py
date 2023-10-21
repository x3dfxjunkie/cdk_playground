"""Source Data Contract Template for FOLIO_ITEM.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for FOLIO_ITEM"""

    folio_item_id: int = Field(
        ...,
        alias="FOLIO_ITEM_ID",
        name="",
        description="",
        example=18203607652,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_id: Optional[int] = Field(
        None,
        alias="FOLIO_ID",
        name="",
        description="",
        example=275086861,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_item_typ_nm: str = Field(
        ...,
        alias="FOLIO_ITEM_TYP_NM",
        name="",
        description="",
        example="CHARGE_ITEM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_item_am: float = Field(
        ...,
        alias="FOLIO_ITEM_AM",
        name="",
        description="",
        example=9.13,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_item_crncy_cd: str = Field(
        ...,
        alias="FOLIO_ITEM_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-11T14:19:17.297000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-11T14:19:17.297000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_cls_nm: str = Field(
        ...,
        alias="JDO_CLS_NM",
        name="",
        description="",
        example="AdditionalChargeItem",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioFolioItemModel(BaseModel):
    """Payload class for DREAMSFolioFolioItemModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio Item"
        stream_name = ""
        description = "This table ties charge and payment folio items to a Folio"  # optional
        unique_identifier = ["data.FOLIO_ITEM_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "FOLIO_ITEM"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
