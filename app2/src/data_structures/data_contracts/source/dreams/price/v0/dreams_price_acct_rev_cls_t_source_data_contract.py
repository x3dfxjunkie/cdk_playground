"""Source Data Contract Template for ACCT_REV_CLS"""


from __future__ import annotations

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - ACCT_REV_CLS Data"""

    acct_rev_cls_id: int = Field(
        ...,
        alias="ACCT_REV_CLS_ID",
        name="",
        description="",
        example=111121,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    acct_rev_cls_lvl_nb: int = Field(
        ...,
        alias="ACCT_REV_CLS_LVL_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    acct_rev_cls_nm: str = Field(
        ...,
        alias="ACCT_REV_CLS_NM",
        name="",
        description="",
        example="Wedding 4 Hour Limousine Charter",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-10-09T12:50:19.565297Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prnt_acct_rev_cls_id: Optional[int] = Field(
        None,
        alias="PRNT_ACCT_REV_CLS_ID",
        name="",
        description="",
        example=111113,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2022-08-15T02:34:46.385000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceAcctRevClsTModel(BaseModel):
    """Payload class for DREAMSAccountingAcctRcvTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Revenue  Class"
        stream_name = ""
        description = (
            "There are over 400 revenue classes associated to a subset of products in a reservation"  # optional
        )
        unique_identifier = ["data.ACCT_REV_CLS_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "ACCT_REV_CLS_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
