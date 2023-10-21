"""Source Data Contract Template for DREAMS Folio Bill"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Bill Data"""

    bill_id: int = Field(
        ...,
        alias="BILL_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_cd_nm: str = Field(
        ...,
        alias="BILL_CD_NM",
        name="",
        description="",
        example="*DCL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_cd_ds: Optional[str] = Field(
        None,
        alias="BILL_CD_DS",
        name="",
        description="",
        example="DISNEY CRUISE LINES",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_cd_inactv_dts: Optional[datetime] = Field(
        None,
        alias="BILL_CD_INACTV_DTS",
        name="",
        description="",
        example="2030-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_cd_strt_dt: datetime = Field(
        ...,
        alias="BILL_CD_STRT_DT",
        name="",
        description="",
        example="1990-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_cd_end_dt: Optional[datetime] = Field(
        None,
        alias="BILL_CD_END_DT",
        name="",
        description="",
        example="2099-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-20T08:24:49.981Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="CLAET001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2012-09-17T14:50:31.304Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioBillModel(BaseModel):
    """Payload class for DREAMSFolioBillModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Bill"
        stream_name = ""
        description = """Billing codes that are associated to Conventions/Groups that determines who pays for what, the delegate or the Convention/Group"""
        unique_identifier = ["data.BILL_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "BILL"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
