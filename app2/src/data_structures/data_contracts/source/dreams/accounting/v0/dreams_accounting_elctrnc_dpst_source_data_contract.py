"""Source Data Contract for DREAMS Electronic Deposit"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Electronic Deposit Data"""

    acct_dt: datetime = Field(
        ...,
        alias="ACCT_DT",
        name="",
        description="",
        example="2023-08-28T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bag_id_vl: str = Field(
        ...,
        alias="BAG_ID_VL",
        name="",
        description="",
        example="65813",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bus_org_id: int = Field(
        ...,
        alias="BUS_ORG_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cmps_id: int = Field(
        ...,
        alias="CMPS_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-28T22:50:17.483000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOORM084",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cshr_id: str = Field(
        ...,
        alias="CSHR_ID",
        name="",
        description="",
        example="moxxm084",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dpst_crncy_cd: str = Field(
        ...,
        alias="DPST_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ed_intfc_id: Optional[int] = Field(
        None,
        alias="ED_INTFC_ID",
        name="",
        description="",
        example=20230828230252,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    elctrnc_dpst_id: int = Field(
        ...,
        alias="ELCTRNC_DPST_ID",
        name="",
        description="",
        example=21859275,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_typ_nm: Optional[str] = Field(
        None,
        alias="PMT_METH_TYP_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-28T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rgstr_nb_vl: str = Field(
        ...,
        alias="RGSTR_NB_VL",
        name="",
        description="",
        example="839AP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_prft_ctr_cd: str = Field(
        ...,
        alias="SAP_PRFT_CTR_CD",
        name="",
        description="",
        example="0001140191",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_card_am: float = Field(
        ...,
        alias="TOT_CARD_AM",
        name="",
        description="",
        example=1676.62,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_coin_am: int = Field(
        ...,
        alias="TOT_COIN_AM",
        name="",
        description="",
        example=12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_csh_am: float = Field(
        ...,
        alias="TOT_CSH_AM",
        name="",
        description="",
        example=2383.02,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_non_csh_am: float = Field(
        ...,
        alias="TOT_NON_CSH_AM",
        name="",
        description="",
        example=25.26,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_rcpt_am: float = Field(
        ...,
        alias="TOT_RCPT_AM",
        name="",
        description="",
        example=6.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingElctrncDpstModel(BaseModel):
    """Payload class for DREAMSAccountingElctrncDpstModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Electronic Deposit"
        stream_name = ""
        description = "Information associated to a Front Desk Cashier banking out their till"  # optional
        unique_identifier = ["data.ELCTRNC_DPST_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "elctrnc_dpst"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
