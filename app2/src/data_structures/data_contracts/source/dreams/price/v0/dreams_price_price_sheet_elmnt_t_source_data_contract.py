"""Source Data Contract for DREAMS Price Sheet Element"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Price Sheet Element Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-26T13:44:07.667705Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: Optional[str] = Field(
        None,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_price_id: Optional[str] = Field(
        None,
        alias="ENTRPRS_PRICE_ID",
        name="",
        description="",
        example="",
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

    price_sheet_elmnt_bkng_end_dts: Optional[datetime] = Field(
        None,
        alias="PRICE_SHEET_ELMNT_BKNG_END_DTS",
        name="",
        description="",
        example="2011-01-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_elmnt_id: int = Field(
        ...,
        alias="PRICE_SHEET_ELMNT_ID",
        name="",
        description="",
        example=12494261,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_elmnt_usg_end_dts: Optional[datetime] = Field(
        None,
        alias="PRICE_SHEET_ELMNT_USG_END_DTS",
        name="",
        description="",
        example="2010-10-07T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_elmnt_usg_strt_dts: Optional[datetime] = Field(
        None,
        alias="PRICE_SHEET_ELMNT_USG_STRT_DTS",
        name="",
        description="",
        example="2010-10-03T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_elmt_bkng_strt_dts: Optional[datetime] = Field(
        None,
        alias="PRICE_SHEET_ELMT_BKNG_STRT_DTS",
        name="",
        description="",
        example="2010-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_id: int = Field(
        ...,
        alias="PRICE_SHEET_ID",
        name="",
        description="",
        example=3531113,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rt_ctgy_cd: Optional[str] = Field(
        None,
        alias="RT_CTGY_CD",
        name="",
        description="",
        example="GEN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-01-26T13:44:07.667705Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: Optional[str] = Field(
        None,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePriceSheetElmntTModel(BaseModel):
    """Payload class for DREAMSPricePriceSheetElmntTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Price Sheet Element"
        stream_name = ""
        description = "This table ties the rate category to the price sheet along with start and end dates"  # optional
        unique_identifier = ["data.PRICE_SHEET_ELMNT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PRICE_SHEET_ELMNT_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
