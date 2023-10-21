"""Source Data Contract Template for PKG"""


from __future__ import annotations

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - PKG Data"""

    hybrd_mkt_cd: Optional[str] = Field(
        None,
        alias="HYBRD_MKT_CD",
        name="",
        description="",
        example="IntlUK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    hybrd_mkt_long_nm: Optional[str] = Field(
        None,
        alias="HYBRD_MKT_LONG_NM",
        name="",
        description="",
        example="International UK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mkt_offer_cd: Optional[str] = Field(
        None,
        alias="MKT_OFFER_CD",
        name="",
        description="",
        example="10444",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mkt_offer_nm: Optional[str] = Field(
        None,
        alias="MKT_OFFER_NM",
        name="",
        description="",
        example="WDW FY18 Canada Q4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_actv_in: str = Field(
        ...,
        alias="PKG_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_grp_cd: Optional[str] = Field(
        None,
        alias="PKG_GRP_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_guar_in: str = Field(
        ...,
        alias="PKG_GUAR_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_id: int = Field(
        ...,
        alias="PKG_ID",
        name="",
        description="",
        example=9166,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_nm: Optional[str] = Field(
        None,
        alias="PKG_PROD_CLS_NM",
        name="",
        description="",
        example="Promotional Offers",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_comm_typ_nm: str = Field(
        ...,
        alias="PKG_PROD_COMM_TYP_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_grp_id: Optional[int] = Field(
        None,
        alias="PKG_PROD_GRP_ID",
        name="",
        description="",
        example=320,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_grp_nm: Optional[str] = Field(
        None,
        alias="PKG_PROD_GRP_NM",
        name="",
        description="",
        example="Packager",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_max_nb: int = Field(
        ...,
        alias="PKG_PROD_MAX_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_min_nb: int = Field(
        ...,
        alias="PKG_PROD_MIN_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_pln_typ_id: Optional[int] = Field(
        None,
        alias="PKG_PROD_PLN_TYP_ID",
        name="",
        description="",
        example=2007,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_src_sys_nm: Optional[str] = Field(
        None,
        alias="PKG_PROD_SRC_SYS_NM",
        name="",
        description="",
        example="Packager",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plan_typ_nm: Optional[str] = Field(
        None,
        alias="PLAN_TYP_NM",
        name="",
        description="",
        example="Room Only",
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

    sub_pkg_in: str = Field(
        ...,
        alias="SUB_PKG_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePkgTModel(BaseModel):
    """Payload class for DREAMSPricePkgTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Package"
        stream_name = ""
        description = (
            "This table holds information regarding packages and their components for room reservations"  # optional
        )
        unique_identifier = ["data.PKG_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PKG_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
