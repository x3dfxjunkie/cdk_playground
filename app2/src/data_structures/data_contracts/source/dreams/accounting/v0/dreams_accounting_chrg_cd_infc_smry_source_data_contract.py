"""Source Data Contract for DREAMS Charge Code Interface Summary"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Charge Code Interface Summary Data"""

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
        example="65522",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_acct_ctr_id: int = Field(
        ...,
        alias="BANK_ACCT_CTR_ID",
        name="",
        description="",
        example=10452,
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
    chrg_cd_infc_smry_id: int = Field(
        ...,
        alias="CHRG_CD_INFC_SMRY_ID",
        name="",
        description="",
        example=16518734,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_cd_intfc_id: Optional[int] = Field(
        None,
        alias="CHRG_CD_INTFC_ID",
        name="",
        description="",
        example=20230828193314,
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
        example="2023-08-28T22:51:26.626000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ROGEN014",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cshr_id: str = Field(
        ...,
        alias="CSHR_ID",
        name="",
        description="",
        example="roxxn014",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    iso_crncy_cd: str = Field(
        ...,
        alias="ISO_CRNCY_CD",
        name="",
        description="",
        example="USD",
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
    tot_non_csh_am: float = Field(
        ...,
        alias="TOT_NON_CSH_AM",
        name="",
        description="",
        example=-25.26,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingChrgCdInfcSmryModel(BaseModel):
    """Payload class for DREAMSAccountingChrgCdInfcSmryModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Code Interface Summary"
        stream_name = ""
        description = "Summary of charges by accounting date and SAP IDs"  # optional
        unique_identifier = ["data.CHRG_CD_INFC_SMRY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "chrg_cd_infc_smry"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
