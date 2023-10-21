"""Source Data Contract for DREAMS Product Class"""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Product Class Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T15:25:10.075496Z",
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

    jdo_cls_nb: int = Field(
        ...,
        alias="JDO_CLS_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=8,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_calc_typ_nm: Optional[str] = Field(
        None,
        alias="PRICE_CALC_TYP_NM",
        name="",
        description="",
        example="Individual Calculator",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prnt_prod_cls_id: Optional[int] = Field(
        None,
        alias="PRNT_PROD_CLS_ID",
        name="",
        description="",
        example=80001188,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_cls_id: int = Field(
        ...,
        alias="PROD_CLS_ID",
        name="",
        description="",
        example=14230,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_cls_lvl_nb: int = Field(
        ...,
        alias="PROD_CLS_LVL_NB",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_cls_nm: str = Field(
        ...,
        alias="PROD_CLS_NM",
        name="",
        description="",
        example="Room Only",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2006-10-18T15:25:10.075496Z",
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


class DREAMSPriceProdClsTModel(BaseModel):
    """Payload class for DREAMSPriceProdClsTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Product Class"
        stream_name = ""
        description = "Product Class IDs, names and hierarchy"  # optional
        unique_identifier = ["data.PROD_CLS_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PROD_CLS_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
