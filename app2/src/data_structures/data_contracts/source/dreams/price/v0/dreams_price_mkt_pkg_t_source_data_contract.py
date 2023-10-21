"""Source Data Contract Template for MKT_PKG"""


from __future__ import annotations

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - MKT_PKG Data"""

    arvl_base_in: str = Field(
        ...,
        alias="ARVL_BASE_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dn_pln_extnl_nm: Optional[str] = Field(
        None,
        alias="DN_PLN_EXTNL_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kttw_typ_id: Optional[int] = Field(
        None,
        alias="KTTW_TYP_ID",
        name="",
        description="",
        example=50,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ovrd_rt_ctgy_cd: Optional[str] = Field(
        None,
        alias="OVRD_RT_CTGY_CD",
        name="",
        description="",
        example="GRP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkgr_pkg_id: Optional[int] = Field(
        None,
        alias="PKGR_PKG_ID",
        name="",
        description="",
        example=16239108,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_cd: str = Field(
        ...,
        alias="PKG_CD",
        name="",
        description="",
        example="*DPCA4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_chk_in_chg_in: str = Field(
        ...,
        alias="PKG_CHK_IN_CHG_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_fsell_in: str = Field(
        ...,
        alias="PKG_FSELL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_id: int = Field(
        ...,
        alias="PKG_ID",
        name="",
        description="",
        example=85037,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_max_nght_cn: int = Field(
        ...,
        alias="PKG_MAX_NGHT_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_min_cmpnt_cn: int = Field(
        ...,
        alias="PKG_MIN_CMPNT_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_min_nght_cn: int = Field(
        ...,
        alias="PKG_MIN_NGHT_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_rack_in: str = Field(
        ...,
        alias="PKG_RACK_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_rm_only_in: str = Field(
        ...,
        alias="PKG_RM_ONLY_IN",
        name="",
        description="",
        example="N",
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

    src_mkt_cd: Optional[str] = Field(
        None,
        alias="SRC_MKT_CD",
        name="",
        description="",
        example="LATAM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceMktPkgTModel(BaseModel):
    """Payload class for DREAMSPriceMktPkgTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Market Package"
        stream_name = ""
        description = "This table provides additional information about the package including the Market Package Code which is how the package is marketed"  # optional
        unique_identifier = ["data.PKG_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "MKT_PKG_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
