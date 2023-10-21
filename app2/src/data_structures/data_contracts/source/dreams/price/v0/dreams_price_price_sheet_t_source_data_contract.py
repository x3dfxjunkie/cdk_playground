"""Source Data Contract for DREAMS Price Sheet"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Price Sheet Data"""

    cmpnt_prod_id: int = Field(
        ...,
        alias="CMPNT_PROD_ID",
        name="",
        description="",
        example=24029,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2012-06-24T04:20:32.754641Z",
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

    fflmt_cmpnt_cd: Optional[str] = Field(
        None,
        alias="FFLMT_CMPNT_CD",
        name="",
        description="",
        example="*VQ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fflmt_dlvr_meth_nm: Optional[str] = Field(
        None,
        alias="FFLMT_DLVR_METH_NM",
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

    pkg_id: Optional[int] = Field(
        None,
        alias="PKG_ID",
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

    price_sheet_id: int = Field(
        ...,
        alias="PRICE_SHEET_ID",
        name="",
        description="",
        example=9216066,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_nm: str = Field(
        ...,
        alias="PRICE_SHEET_NM",
        name="",
        description="",
        example="8 DAY W/8 FUN VISITS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2012-06-24T04:20:32.754641Z",
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


class DREAMSPricePriceSheetTModel(BaseModel):
    """Payload class for DREAMSPricePriceSheetTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Price Sheet"
        stream_name = ""
        description = "This table holds component IDs and Names of the price sheet"  # optional
        unique_identifier = ["data.PRICE_SHEET_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PRICE_SHEET_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
