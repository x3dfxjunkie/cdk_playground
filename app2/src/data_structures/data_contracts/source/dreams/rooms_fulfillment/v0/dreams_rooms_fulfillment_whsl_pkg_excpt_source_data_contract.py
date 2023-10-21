"""Source Data Contract for DREAMS Rooms Fulfillment Wholesale Package Exception"""


from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsData,
    GlobalDreamsMetadata,
)


class Data(GlobalDreamsData):
    """Class for Dreams Wholesale Package Exception Data"""

    pkg_excpt_id: int = Field(
        ...,
        alias="PKG_EXCPT_ID",
        name="",
        description="",
        example=100000008,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_excpt_typ_nm: str = Field(
        ...,
        alias="PKG_EXCPT_TYP_NM",
        name="",
        description="",
        example="Early Checkout",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_excpt_sts_nm: str = Field(
        ...,
        alias="PKG_EXCPT_STS_NM",
        name="",
        description="",
        example="Open",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_excpt_st_nm: str = Field(
        ...,
        alias="PKG_EXCPT_ST_NM",
        name="",
        description="",
        example="Original",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tp_id: int = Field(
        ...,
        alias="TP_ID",
        name="",
        description="",
        example=1111162317,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_id: int = Field(
        ...,
        alias="TPS_ID",
        name="",
        description="",
        example=11111116299,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_grp_nb: int = Field(
        ...,
        alias="TC_GRP_NB",
        name="",
        description="",
        example=111111,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_nm: str = Field(
        ...,
        alias="GRP_NM",
        name="",
        description="",
        example="WDW TRAVEL CO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="01234",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_ttl_am: float = Field(
        ...,
        alias="PKG_TTL_AM",
        name="",
        description="",
        example=2244.86,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_ttl_crncy_cd: str = Field(
        ...,
        alias="PKG_TTL_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chld_cn: int = Field(
        ...,
        alias="CHLD_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    adlt_cn: int = Field(
        ...,
        alias="ADLT_CN",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rm_typ_nm: str = Field(
        ...,
        alias="RM_TYP_NM",
        name="",
        description="",
        example="FD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    arvl_dt: datetime = Field(
        ...,
        alias="ARVL_DT",
        name="",
        description="",
        example="2023-05-26T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_cd: str = Field(
        ...,
        alias="PKG_CD",
        name="",
        description="",
        example="ABCGC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_lst_nm: str = Field(
        ...,
        alias="GUEST_LST_NM",
        name="",
        description="",
        example="Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_frst_nm: str = Field(
        ...,
        alias="GUEST_FRST_NM",
        name="",
        description="",
        example="Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transact_commit_timestamp: Optional[datetime] = Field(
        None,
        alias="transact_commit_timestamp",
        name="",
        description="",
        example="2023-01-11T14:58:44Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    transact_seq: Optional[str] = Field(
        None,
        alias="transact_seq",
        name="",
        description="",
        example="20210528005111000000000001961948297",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentWhslPkgExcptModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentWhslPkgExcptModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Rooms Fulfillment Wholesale Package Exception"
        stream_name = ""
        description = ""
        unique_identifier = ["data.PKG_EXCPT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "whsl_pkg_excpt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
