"""Source Data Contract for DREAMS Account Center Payment Method Override"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Account Center Payment Method Override Data"""

    ovrd_rfnd_pmt_meth_id: int = Field(
        ...,
        alias="OVRD_RFND_PMT_METH_ID",
        name="",
        description="",
        example=262500,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_pmt_meth_id: int = Field(
        ...,
        alias="ACCT_CTR_PMT_METH_ID",
        name="",
        description="",
        example=2085302,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2021-04-05T15:45:15.217Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingAcctCtrPmthOvrdModel(BaseModel):
    """Payload class for DREAMSAccountingAcctCtrPmthOvrdModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center Payment method override"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.OVRD_RFND_PMT_METH_ID", "data.ACCT_CTR_PMT_METH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACCT_CTR_PMTH_OVRD"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
