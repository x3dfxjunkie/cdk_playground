"""Source Data Contract for DREAMS Ticket"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Ticket Data"""

    adm_prod_id: Optional[int] = Field(
        None,
        alias="ADM_PROD_ID",
        name="",
        description="",
        example=2839410,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_def_id: int = Field(
        ...,
        alias="AGE_DEF_ID",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T15:28:01.578000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    demog_info_rqd_in: str = Field(
        ...,
        alias="DEMOG_INFO_RQD_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exnl_prc_in: Optional[str] = Field(
        None,
        alias="EXNL_PRC_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1425,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    orig_rtl_price_am: float = Field(
        ...,
        alias="ORIG_RTL_PRICE_AM",
        name="",
        description="",
        example=240.69,
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

    prod_attr: Optional[str] = Field(
        None,
        alias="PROD_ATTR",
        name="",
        description="",
        example="P1060000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_am: float = Field(
        ...,
        alias="TKT_AM",
        name="",
        description="",
        example=233.47,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_cd: str = Field(
        ...,
        alias="TKT_CD",
        name="",
        description="",
        example="CKJDB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_id: int = Field(
        ...,
        alias="TKT_ID",
        name="",
        description="",
        example=1516,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_sls_end_dt: Optional[datetime] = Field(
        None,
        alias="TKT_SLS_END_DT",
        name="",
        description="",
        example="2005-12-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_sls_strt_dt: datetime = Field(
        ...,
        alias="TKT_SLS_STRT_DT",
        name="",
        description="",
        example="2016-02-15T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_tax_am: Optional[float] = Field(
        None,
        alias="TKT_TAX_AM",
        name="",
        description="",
        example=14.25,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_usg_end_dt: Optional[datetime] = Field(
        None,
        alias="TKT_USG_END_DT",
        name="",
        description="",
        example="2019-08-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_usg_strt_dt: datetime = Field(
        ...,
        alias="TKT_USG_STRT_DT",
        name="",
        description="",
        example="2016-02-15T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2006-10-18T15:28:01.578000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    vld_dt_meth_nm: Optional[str] = Field(
        None,
        alias="VLD_DT_METH_NM",
        name="",
        description="",
        example="T",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTktTModel(BaseModel):
    """Payload class for DREAMSPriceTktTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Ticket"
        stream_name = ""
        description = "Additional Ticket information"  # optional
        unique_identifier = ["data.TKT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "TKT_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
