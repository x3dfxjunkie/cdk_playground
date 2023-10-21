"""Source Data Contract for Dreams Price Definition"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price Definition Data"""

    age_def_id: int = Field(
        ...,
        alias="AGE_DEF_ID",
        name="",
        description="",
        example=29,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-27T11:20:07.171984Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
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

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-10T14:58:46.221222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_def_age_am: int = Field(
        ...,
        alias="PRICE_DEF_AGE_AM",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_def_disc_am: Optional[float] = Field(
        None,
        alias="PRICE_DEF_DISC_AM",
        name="",
        description="",
        example=0.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_def_id: int = Field(
        ...,
        alias="PRICE_DEF_ID",
        name="",
        description="",
        example=15838633,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_def_price_am: float = Field(
        ...,
        alias="PRICE_DEF_PRICE_AM",
        name="",
        description="",
        example=-0.01,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_def_tax_am: Optional[float] = Field(
        None,
        alias="PRICE_DEF_TAX_AM",
        name="",
        description="",
        example=0.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_def_tax_in: str = Field(
        ...,
        alias="PRICE_DEF_TAX_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_def_tkt_in: str = Field(
        ...,
        alias="PRICE_DEF_TKT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_elmnt_id: int = Field(
        ...,
        alias="PRICE_SHEET_ELMNT_ID",
        name="",
        description="",
        example=12616906,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_id: Optional[int] = Field(
        None,
        alias="TKT_ID",
        name="",
        description="",
        example=14665,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-01-27T11:20:07.171984Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePriceDefTModel(BaseModel):
    """Payload class for DREAMSPricePriceDefTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Price Definition"
        stream_name = ""
        description = "This tables contains the Price Sheet Element ID and the Age Definition ID and pricing information amounts, discount, by age, ticket and tax"  # optional
        unique_identifier = ["data.PRICE_DEF_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PRICE_DEF_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
