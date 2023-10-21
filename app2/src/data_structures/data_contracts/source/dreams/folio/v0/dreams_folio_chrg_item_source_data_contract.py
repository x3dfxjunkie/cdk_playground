"""Source Data Contract Template for CHRG_ITEM.json"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for CHRG_ITEM"""

    chrg_item_id: int = Field(
        ...,
        alias="CHRG_ITEM_ID",
        name="",
        description="",
        example=18203872897,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_id: int = Field(
        ...,
        alias="CHRG_ID",
        name="",
        description="",
        example=3408896661,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_item_typ_nm: str = Field(
        ...,
        alias="CHRG_ITEM_TYP_NM",
        name="",
        description="",
        example="Base",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_typ_id: int = Field(
        ...,
        alias="REV_TYP_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_typ_nm: str = Field(
        ...,
        alias="REV_TYP_NM",
        name="",
        description="",
        example="Base",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    splt_chrg_item_in: str = Field(
        ...,
        alias="SPLT_CHRG_ITEM_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_item_in: str = Field(
        ...,
        alias="TAX_ITEM_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_item_am: float = Field(
        ...,
        alias="CHRG_ITEM_AM",
        name="",
        description="",
        example=-105.08,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_item_crncy_cd: str = Field(
        ...,
        alias="CHRG_ITEM_CRNCY_CD",
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
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-12T00:04:22.671000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-12T00:04:22.671000Z",
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
    chrg_item_inactv_dts: Optional[datetime] = Field(
        None,
        alias="CHRG_ITEM_INACTV_DTS",
        name="",
        description="",
        example="2023-06-11T17:03:21.480000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rflt_dts: Optional[datetime] = Field(
        None,
        alias="RFLT_DTS",
        name="",
        description="",
        example="2023-06-11T17:04:46.451000Z",
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
    chrg_item_ovrd_dts: Optional[datetime] = Field(
        None,
        alias="CHRG_ITEM_OVRD_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioChrgItemModel(BaseModel):
    """Payload class for DREAMSFolioChrgItemModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Item"
        stream_name = ""
        description = "This table has the items associated to certain charges, there are 2 types: CHRG_ITEM_TYP_NM (Additional, Base) This are associated to 45 different revenue types, the main ones being BASE, DISCOUNT and different state/county taxes"  # optional
        unique_identifier = ["data.CHRG_ITEM_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CHRG_ITEM"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
