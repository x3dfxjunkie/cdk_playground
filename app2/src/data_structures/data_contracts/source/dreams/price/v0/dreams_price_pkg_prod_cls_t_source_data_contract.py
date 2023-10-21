"""Source Data Contract for Dreams Price Package Product Class"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Price Package Product Class Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-12-22T10:10:18.950000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="racum001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_frq_nm: str = Field(
        ...,
        alias="ENTTL_FRQ_NM",
        name="",
        description="",
        example="Per Night",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_meth_nm: Optional[str] = Field(
        None,
        alias="ENTTL_METH_NM",
        name="",
        description="",
        example="Per Individual",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_cls_nb: int = Field(
        ...,
        alias="JDO_CLS_NB",
        name="",
        description="",
        example=2,
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

    pkg_id: int = Field(
        ...,
        alias="PKG_ID",
        name="",
        description="",
        example=14561,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_cn: int = Field(
        ...,
        alias="PKG_PROD_CLS_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_id: int = Field(
        ...,
        alias="PKG_PROD_CLS_ID",
        name="",
        description="",
        example=21282,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_max_nb: int = Field(
        ...,
        alias="PKG_PROD_CLS_MAX_NB",
        name="",
        description="",
        example=999,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_min_nb: int = Field(
        ...,
        alias="PKG_PROD_CLS_MIN_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_opt_in: str = Field(
        ...,
        alias="PKG_PROD_CLS_OPT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_slct_in: str = Field(
        ...,
        alias="PKG_PROD_CLS_SLCT_IN",
        name="",
        description="",
        example="Y",
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

    prod_cls_id: int = Field(
        ...,
        alias="PROD_CLS_ID",
        name="",
        description="",
        example=80000366,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2006-12-22T10:10:18.950000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="racum001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePkgProdClsTModel(BaseModel):
    """Payload class for DREAMSPricePkgProdClsTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Package Product Class"
        stream_name = ""
        description = "This table provides the product classification ID associated to the product and some additional information about the package"  # optional
        unique_identifier = ["data.PKG_PROD_CLS_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PKG_PROD_CLS_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
