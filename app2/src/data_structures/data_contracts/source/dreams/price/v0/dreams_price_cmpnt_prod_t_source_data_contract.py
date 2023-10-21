"""Source Data Contract Template for CMPNT_PROD"""


from __future__ import annotations

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - CMPNT_PROD Data"""

    cmpnt_prod_adlt_cpcty_nb: Optional[int] = Field(
        None,
        alias="CMPNT_PROD_ADLT_CPCTY_NB",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmpnt_prod_cd: Optional[str] = Field(
        None,
        alias="CMPNT_PROD_CD",
        name="",
        description="",
        example="18DIZDINE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmpnt_prod_cpcty_nb: Optional[int] = Field(
        None,
        alias="CMPNT_PROD_CPCTY_NB",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmpnt_prod_frnt_dsk_prt_in: str = Field(
        ...,
        alias="CMPNT_PROD_FRNT_DSK_PRT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmpnt_prod_nm: Optional[str] = Field(
        None,
        alias="CMPNT_PROD_NM",
        name="",
        description="",
        example="Disney Dining Plan",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dflt_price_sheet_id: Optional[int] = Field(
        None,
        alias="DFLT_PRICE_SHEET_ID",
        name="",
        description="",
        example=24859171,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_frq_nm: Optional[str] = Field(
        None,
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
        example="Per Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gst_fcg_prod_nm: Optional[str] = Field(
        None,
        alias="GST_FCG_PROD_NM",
        name="",
        description="",
        example="Disney Dining Plan",
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

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=4903414,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_grp_id: int = Field(
        ...,
        alias="TAX_GRP_ID",
        name="",
        description="",
        example=80007254,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceCmpntProdTModel(BaseModel):
    """Payload class for DREAMSPriceCmpntProdTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Component Product"
        stream_name = ""
        description = "Additional information for component products, provides How the component/entitlement is distributed: Per Adult, Per Room, Per Person, Per Individual, Per Package, Per Child, Per Reservation, as well as when the component/entitlement is valid for, One Time, Per Meal Period, Per Meal Period Snack, Per Night, Per Once, And it also ties it to a default price sheet"  # optional
        unique_identifier = ["data.PROD_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CMPNT_PROD_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
