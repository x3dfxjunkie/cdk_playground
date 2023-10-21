"""Source Data Contract Template for DENOM_ITEM_BNK_OUT.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Denom_Item_Bnk_Out Data Payload"""

    denom_item_bnk_out_id: int = Field(
        ...,
        alias="DENOM_ITEM_BNK_OUT_ID",
        name="",
        description="",
        example=18827976,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    denom_item_typ_nm: str = Field(
        ...,
        alias="DENOM_ITEM_TYP_NM",
        name="",
        description="",
        example="DISNEY_DOLLAR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_out_id: int = Field(
        ...,
        alias="BANK_OUT_ID",
        name="",
        description="",
        example=24560589,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    denom_item_typ_cn: str = Field(
        ...,
        alias="DENOM_ITEM_TYP_CN",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    denom_item_am: float = Field(
        ...,
        alias="DENOM_ITEM_AM",
        name="",
        description="",
        example=50.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    denom_item_crncy_cd: str = Field(
        ...,
        alias="DENOM_ITEM_CRNCY_CD",
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
        example="2023-06-13T11:34:00.625000Z",
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


class DREAMSFolioDenomItemBnkOutModel(BaseModel):
    """Payload class for DREAMSFolioDenomItemBnkOutModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Denomination Item Bank Out"
        stream_name = ""
        description = "This table connects the type of denomination that is included in a front desk cashier's till bank out: DENOM_ITEM_TYP_NM (DISNEY_DOLLAR, TRAVELERS_CHECK, CURRENCY, COIN)"  # optional
        unique_identifier = ["data.DENOM_ITEM_BNK_OUT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "DENOM_ITEM_BNK_OUT"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
