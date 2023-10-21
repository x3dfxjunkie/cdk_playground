"""Source Data Contract Template for NON_FOLIO_RFND_ITM.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for NON_FOLIO_RFND_ITM"""

    non_folio_rfnd_item_id: int = Field(
        ...,
        alias="NON_FOLIO_RFND_ITEM_ID",
        name="",
        description="",
        example=9034621,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_out_id: int = Field(
        ...,
        alias="BANK_OUT_ID",
        name="",
        description="",
        example=24554699,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    non_folio_rfnd_item_typ_nm: str = Field(
        ...,
        alias="NON_FOLIO_RFND_ITEM_TYP_NM",
        name="",
        description="",
        example="Machine Refunds",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    non_folio_item_rfnd_cn: int = Field(
        ...,
        alias="NON_FOLIO_ITEM_RFND_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    non_folio_item_rfnd_am: float = Field(
        ...,
        alias="NON_FOLIO_ITEM_RFND_AM",
        name="",
        description="",
        example=13.5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    non_folio_item_crncy_cd: str = Field(
        ...,
        alias="NON_FOLIO_ITEM_CRNCY_CD",
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
        example="GUERE041",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-08T21:13:50.610000Z",
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


class DREAMSFolioNonFolioRfndItmModel(BaseModel):
    """Payload class for DREAMSFolioNonFolioRfndItmModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Non Folio Refund Item"
        stream_name = ""
        description = "This table tracks refunds that occur at the Front Desk for items that would not be included in a guest folio.NON_FOLIO_RFND_ITEM_TYP_NM, Parking Refunds, Other Refunds, Machine Refunds"  # optional
        unique_identifier = ["data.NON_FOLIO_RFND_ITEM_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "NON_FOLIO_RFND_ITM"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
