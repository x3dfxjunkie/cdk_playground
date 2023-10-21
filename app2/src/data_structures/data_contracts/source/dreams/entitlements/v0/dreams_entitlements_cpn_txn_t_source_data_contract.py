"""Source Data Contract for Dreams Entitlement Coupon Transaction"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon Transaction Data"""

    cpn_chrg_id: int = Field(
        ...,
        alias="CPN_CHRG_ID",
        name="",
        description="",
        example=111111103,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-18T11:09:27.657000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="unknown",
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

    orig_chrg_folio_indicator: str = Field(
        ...,
        alias="ORIG_CHRG_FOLIO_INDICATOR",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    orig_chrg_id: Optional[int] = Field(
        None,
        alias="ORIG_CHRG_ID",
        name="",
        description="",
        example=111111343,
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

    txn_cmt_tx: Optional[str] = Field(
        None,
        alias="TXN_CMT_TX",
        name="",
        description="",
        example="Passenger tried to use meal credits on batuu but was charged at docking bay 7 for a kids meal. Folio adjustment made to use adult coupon and refund them their above amount.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_id: str = Field(
        ...,
        alias="TXN_ID",
        name="",
        description="",
        example="000000985",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_proc_typ_nm: str = Field(
        ...,
        alias="TXN_PROC_TYP_NM",
        name="",
        description="",
        example="Created",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_rsn_cd: Optional[str] = Field(
        None,
        alias="TXN_RSN_CD",
        name="",
        description="",
        example="ACGIN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_typ_nm: str = Field(
        ...,
        alias="TXN_TYP_NM",
        name="",
        description="",
        example="SALE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-18T11:09:27.657000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="unknown",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsCpnTxnTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnTxnTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Coupon Transaction"
        stream_name = ""
        description = """This table ties the transaction type: TXN_TYP_NM
        SALE
        REV
        TRF
        with the coupon charge ID"""
        unique_identifier = ["data.TXN_ID", "data.CPN_CHRG_ID", "data.ORIG_CHRG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_TXN_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
