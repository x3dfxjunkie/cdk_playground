"""Source Data Contract Template Entitlement Plan"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Entitlement Plan Data"""

    cpn_am: Optional[str] = Field(
        None,
        alias="CPN_AM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_cn: int = Field(
        ...,
        alias="CPN_CN",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_prfl_id: int = Field(
        ...,
        alias="CPN_PRFL_ID",
        name="",
        description="",
        example=1111110120,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-17T12:18:55.471000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ENTITLTLEMEN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_pln_ds: str = Field(
        ...,
        alias="ENTTL_PLN_DS",
        name="",
        description="",
        example="Quick Service Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_pln_end_dt: datetime = Field(
        ...,
        alias="ENTTL_PLN_END_DT",
        name="",
        description="",
        example="2023-11-11T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_pln_id: int = Field(
        ...,
        alias="ENTTL_PLN_ID",
        name="",
        description="",
        example=11111712,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_pln_strt_dt: datetime = Field(
        ...,
        alias="ENTTL_PLN_STRT_DT",
        name="",
        description="",
        example="2023-08-17T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    incognito: Optional[str] = Field(
        None,
        alias="INCOGNITO",
        name="",
        description="",
        example="",
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
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    src_acct_ctr_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-17T12:18:55.471000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="ENTITLTLEMEN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsEnttlPlnTModel(BaseModel):
    """Payload class for DREAMSEntitlementsEnttlPlnTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Plan"
        stream_name = ""
        description = """This table provides additional information about an entitlement plan, the count of coupons for the Entitlement Plan description and coupon profile ID"""
        unique_identifier = ["data.ENTTL_PLN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ENTTL_PLN_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
