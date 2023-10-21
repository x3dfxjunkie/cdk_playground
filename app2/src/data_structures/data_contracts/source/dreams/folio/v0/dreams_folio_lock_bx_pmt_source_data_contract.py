"""Source Data Contract Template for DREAMS Folio Lock Box Payment"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Lock Box Payment Data"""

    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=8061,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    lckbx_chk_nb_vl: str = Field(
        ...,
        alias="LCKBX_CHK_NB_VL",
        name="",
        description="",
        example="8192",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    lckbx_btch_extnl_nb_val: str = Field(
        ...,
        alias="LCKBX_BTCH_EXTNL_NB_VAL",
        name="",
        description="",
        example="N954",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    lckbx_extnl_btch_dts: datetime = Field(
        ...,
        alias="LCKBX_EXTNL_BTCH_DTS",
        name="",
        description="",
        example="2006-05-02T04:00:00.000Z",
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
        example="2008-12-05T08:48:59.915Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2008-12-05T08:48:59.915Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioLockBxPmtModel(BaseModel):
    """Payload class for DREAMSFolioLockBxPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Lock Box Payment"
        stream_name = ""
        description = """This table holds the information regarding checks that guests mail in to secure/Guarantee their reservations, it goes to a secure Lock Box at the reservation center"""
        unique_identifier = ["data.PMT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "LOCK_BX_PMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
