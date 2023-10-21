"""Source Data Contract for Dreams Price Grid"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Price Grid Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2008-02-11T15:13:48.357000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="corba007",
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

    price_grid_ds: str = Field(
        ...,
        alias="PRICE_GRID_DS",
        name="",
        description="",
        example="G0516689-Accommodation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_grid_id: int = Field(
        ...,
        alias="PRICE_GRID_ID",
        name="",
        description="",
        example=87372,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_grid_pkg_in: str = Field(
        ...,
        alias="PRICE_GRID_PKG_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_grid_typ_nm: str = Field(
        ...,
        alias="PRICE_GRID_TYP_NM",
        name="",
        description="",
        example="Other",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rt_grid_cd: Optional[str] = Field(
        None,
        alias="RT_GRID_CD",
        name="",
        description="",
        example="123587",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2008-02-11T15:13:48.357000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="corba007",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePriceGridTModel(BaseModel):
    """Payload class for DREAMSPricePriceGridTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Price Grid"
        stream_name = ""
        description = "This price grid description of tickets and 'other' products that are more associated to scheduled events"  # optional
        unique_identifier = ["data.PRICE_GRID_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PRICE_GRID_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
