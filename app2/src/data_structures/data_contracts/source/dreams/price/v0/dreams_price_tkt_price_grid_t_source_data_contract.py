"""Source Data Contract for DREAMS Ticket Price Grid"""

from __future__ import annotations
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Ticket Price Grid Data"""

    tkt_price_grid_id: float = Field(
        ...,
        alias="TKT_PRICE_GRID_ID",
        name="",
        description="",
        example=58989.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    price_grid_tkt_feat_in: str = Field(
        ...,
        alias="PRICE_GRID_TKT_FEAT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    price_grid_tkt_cnvntn_in: str = Field(
        ...,
        alias="PRICE_GRID_TKT_CNVNTN_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    price_grid_tkt_intfc_cd: Optional[str] = Field(
        None,
        alias="PRICE_GRID_TKT_INTFC_CD",
        name="",
        description="",
        example="XUN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    price_grid_tkt_fsell_in: str = Field(
        ...,
        alias="PRICE_GRID_TKT_FSELL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tkt_sl_eff_dt: Optional[datetime] = Field(
        None,
        alias="TKT_SL_EFF_DT",
        name="",
        description="",
        example="2018-03-14T03:17:29Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tkt_sl_exp_dt: Optional[datetime] = Field(
        None,
        alias="TKT_SL_EXP_DT",
        name="",
        description="",
        example="2018-03-14T03:17:29Z",
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


class DREAMSPriceTktPriceGridTModel(BaseModel):
    """Payload class for DREAMSPriceTktPriceGridTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Ticket Price Grid"
        stream_name = ""
        description = "Price Grid associated to tickets"  # optional
        unique_identifier = ["data.TKT_PRICE_GRID_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "TKT_PRICE_GRID_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
