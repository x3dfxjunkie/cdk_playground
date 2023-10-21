"""Source Data Contract Template for BILL_APLCBL.json"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for BILL_APLCBL"""

    bill_aplcbl_id: int = Field(
        ...,
        alias="BILL_APLCBL_ID",
        name="",
        description="",
        example=3322809,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_id: int = Field(
        ...,
        alias="BILL_ID",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_aplcbl_strt_dt: datetime = Field(
        ...,
        alias="BILL_APLCBL_STRT_DT",
        name="",
        description="",
        example="2023-06-08T20:08:59Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_aplcbl_end_dt: Optional[datetime] = Field(
        None,
        alias="BILL_APLCBL_END_DT",
        name="",
        description="",
        example="2078-03-11T20:08:59Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_id: Optional[int] = Field(
        None,
        alias="PKG_ID",
        name="",
        description="",
        example=7991924,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_acct_ctr_id: Optional[int] = Field(
        None,
        alias="TXN_ACCT_CTR_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    add_by_pkgr_in: str = Field(
        ...,
        alias="ADD_BY_PKGR_IN",
        name="",
        description="",
        example="Y",
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
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-08T20:08:59.660000Z",
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
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-08T20:08:59.660000Z",
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
    rev_cls_id: Optional[int] = Field(
        None,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=18984894,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_id: Optional[int] = Field(
        None,
        alias="PROD_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioBillAplcblModel(BaseModel):
    """Payload class for DREAMSFolioBillAplcblModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Bill Applicable"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.BILL_APLCBL_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "BILL_APLCBL"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
