"""Source Data Contract for DREAMS Product Channel"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Product Channel Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-01-31T00:18:19.145138Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_id: Optional[int] = Field(
        None,
        alias="ENTRPRS_ID",
        name="",
        description="",
        example=42,
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

    pkgr_prod_chan_id: int = Field(
        ...,
        alias="PKGR_PROD_CHAN_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_chan_cd: Optional[str] = Field(
        None,
        alias="PKG_CHAN_CD",
        name="",
        description="",
        example="IRO PASS",
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

    prod_chan_actv_in: str = Field(
        ...,
        alias="PROD_CHAN_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_end_dt: datetime = Field(
        ...,
        alias="PROD_CHAN_END_DT",
        name="",
        description="",
        example="2007-01-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_id: int = Field(
        ...,
        alias="PROD_CHAN_ID",
        name="",
        description="",
        example=2832,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_nm: str = Field(
        ...,
        alias="PROD_CHAN_NM",
        name="",
        description="",
        example="G0471030",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_rsr_in: str = Field(
        ...,
        alias="PROD_CHAN_RSR_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_strt_dt: datetime = Field(
        ...,
        alias="PROD_CHAN_STRT_DT",
        name="",
        description="",
        example="2007-01-21T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_typ_nm: str = Field(
        ...,
        alias="PROD_CHAN_TYP_NM",
        name="",
        description="",
        example="Sales Block",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-01-31T00:18:19.145138Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdChanTModel(BaseModel):
    """Payload class for DREAMSPriceProdChanTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Product Channel"
        stream_name = ""
        description = "This table has the IDs for product channel types and names"  # optional
        unique_identifier = ["data.PROD_CHAN_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PROD_CHAN_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
