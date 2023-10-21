"""Source Data Contract for DREAMS Product"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Product Data"""

    acct_rev_cls_id: int = Field(
        ...,
        alias="ACCT_REV_CLS_ID",
        name="",
        description="",
        example=366837,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dest: Optional[str] = Field(
        None,
        alias="DEST",
        name="",
        description="",
        example="WDW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_prod_id: Optional[int] = Field(
        None,
        alias="ENTRPRS_PROD_ID",
        name="",
        description="",
        example=289341,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_adv_purch_day_ct: int = Field(
        ...,
        alias="MAX_ADV_PURCH_DAY_CT",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    min_adv_purch_day_ct: int = Field(
        ...,
        alias="MIN_ADV_PURCH_DAY_CT",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    offer_idx_nb: int = Field(
        ...,
        alias="OFFER_IDX_NB",
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

    prod_bkng_end_dts: Optional[datetime] = Field(
        None,
        alias="PROD_BKNG_END_DTS",
        name="",
        description="",
        example="2009-08-05T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_bkng_strt_dts: Optional[datetime] = Field(
        None,
        alias="PROD_BKNG_STRT_DTS",
        name="",
        description="",
        example="2008-06-17T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_cd: Optional[str] = Field(
        None,
        alias="PROD_CD",
        name="",
        description="",
        example="YZN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_cls_id: int = Field(
        ...,
        alias="PROD_CLS_ID",
        name="",
        description="",
        example=80000370,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_create_dts: Optional[datetime] = Field(
        None,
        alias="PROD_CREATE_DTS",
        name="",
        description="",
        example="2008-06-17T17:06:28.543000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_di: Optional[int] = Field(
        None,
        alias="PROD_DI",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_dt_in: str = Field(
        ...,
        alias="PROD_DT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_exp_dts: Optional[datetime] = Field(
        None,
        alias="PROD_EXP_DTS",
        name="",
        description="",
        example="2023-08-10T14:58:46.221222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_extnl_nm: Optional[str] = Field(
        None,
        alias="PROD_EXTNL_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_extrnl_ds: Optional[str] = Field(
        None,
        alias="PROD_EXTRNL_DS",
        name="",
        description="",
        example="3 Bedroom Grand Villa",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=39525,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_intrnl_ds: Optional[str] = Field(
        None,
        alias="PROD_INTRNL_DS",
        name="",
        description="",
        example="09 NG Grp and Conv",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_intrnl_nm: str = Field(
        ...,
        alias="PROD_INTRNL_NM",
        name="",
        description="",
        example="G0527410",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_rsrvbl_in: str = Field(
        ...,
        alias="PROD_RSRVBL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_typ_nm: str = Field(
        ...,
        alias="PROD_TYP_NM",
        name="",
        description="",
        example="CustomizedPackage",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_updt_dts: Optional[datetime] = Field(
        None,
        alias="PROD_UPDT_DTS",
        name="",
        description="",
        example="2023-08-10T14:58:46.221222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_usg_end_dts: Optional[datetime] = Field(
        None,
        alias="PROD_USG_END_DTS",
        name="",
        description="",
        example="2009-08-04T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_usg_strt_dts: Optional[datetime] = Field(
        None,
        alias="PROD_USG_STRT_DTS",
        name="",
        description="",
        example="2009-06-26T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_yr_nb: Optional[int] = Field(
        None,
        alias="PROD_YR_NB",
        name="",
        description="",
        example=2009,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sor: Optional[str] = Field(
        None,
        alias="SOR",
        name="",
        description="",
        example="TBX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdTModel(BaseModel):
    """Payload class for DREAMSPriceProdTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Product"
        stream_name = ""
        description = "This table holds product information for room reservations"  # optional
        unique_identifier = ["data.PROD_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PROD_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
