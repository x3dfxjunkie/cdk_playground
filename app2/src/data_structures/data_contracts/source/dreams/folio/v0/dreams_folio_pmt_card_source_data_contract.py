"""Source Data Contract Template for PMT_CARD.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for PMT_CARD"""

    pmt_card_id: int = Field(
        ...,
        alias="PMT_CARD_ID",
        name="",
        description="",
        example=264082707,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    strts_rtrv_ref_nb: Optional[str] = Field(
        None,
        alias="STRTS_RTRV_REF_NB",
        name="",
        description="",
        example="235181219770",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    umsk_card_nb: str = Field(
        ...,
        alias="UMSK_CARD_NB",
        name="",
        description="",
        example="xxxxxxxxxxx1005",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_hld_nm: Optional[str] = Field(
        None,
        alias="PMT_CARD_HLD_NM",
        name="",
        description="",
        example="James H Deets",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_hld_addr_ln_1_vl: Optional[str] = Field(
        None,
        alias="PMT_CARD_HLD_ADDR_LN_1_VL",
        name="",
        description="",
        example="229 Vernon Dr",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_hld_cty_nm: Optional[str] = Field(
        None,
        alias="PMT_CARD_HLD_CTY_NM",
        name="",
        description="",
        example="Fate",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_hld_rgn_cd: Optional[str] = Field(
        None,
        alias="PMT_CARD_HLD_RGN_CD",
        name="",
        description="",
        example="TX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_hld_pstl_cd: Optional[str] = Field(
        None,
        alias="PMT_CARD_HLD_PSTL_CD",
        name="",
        description="",
        example="75087",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_hld_cntry_cd: Optional[str] = Field(
        None,
        alias="PMT_CARD_HLD_CNTRY_CD",
        name="",
        description="",
        example="US",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDW-MDX-IOS-",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-10T10:23:54.932000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_crd_use_sts_nm: str = Field(
        ...,
        alias="PMT_CRD_USE_STS_NM",
        name="",
        description="",
        example="Valid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rrn_key_nb: Optional[str] = Field(
        None,
        alias="RRN_KEY_NB",
        name="",
        description="",
        example="QiILGA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_brnd_nm: Optional[str] = Field(
        None,
        alias="PMT_CARD_BRND_NM",
        name="",
        description="",
        example="GENERIC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    card_exp_dt: Optional[str] = Field(
        None,
        alias="CARD_EXP_DT",
        name="",
        description="",
        example="gcYX/7IVeTVYjaFjWTdVRg==",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_dev_trmnl_id: Optional[str] = Field(
        None,
        alias="PMT_DEV_TRMNL_ID",
        name="",
        description="",
        example="0U5B",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_hld_addr_ln_2_vl: Optional[str] = Field(
        None,
        alias="PMT_CARD_HLD_ADDR_LN_2_VL",
        name="",
        description="",
        example="Apt 2B",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_hld_rgn_nm: Optional[str] = Field(
        None,
        alias="PMT_CARD_HLD_RGN_NM",
        name="",
        description="",
        example="England",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    strts_sts_cd: Optional[str] = Field(
        None,
        alias="STRTS_STS_CD",
        name="",
        description="",
        example="DECLINED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioPmtCardModel(BaseModel):
    """Payload class for DREAMSFolioPmtCardModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Payment Card"
        stream_name = ""
        description = "Additional information about credit card payments, including card holder and address"  # optional
        unique_identifier = ["data.PMT_CARD_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PMT_CARD"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
