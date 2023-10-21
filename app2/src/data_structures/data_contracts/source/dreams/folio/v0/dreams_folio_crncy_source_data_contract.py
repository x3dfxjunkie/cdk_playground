"""Source Data Contract Template for DREAMS Folio Currency"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Currency Data"""

    crncy_iso_cd: str = Field(
        ...,
        alias="CRNCY_ISO_CD",
        name="",
        description="",
        example="AUD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    crncy_nm: str = Field(
        ...,
        alias="CRNCY_NM",
        name="",
        description="",
        example="AUSTRALIA DOLLAR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    crncy_actv_in: str = Field(
        ...,
        alias="CRNCY_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    crncy_strt_dts: datetime = Field(
        ...,
        alias="CRNCY_STRT_DTS",
        name="",
        description="",
        example="2009-05-03T18:24:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    crncy_end_dts: Optional[datetime] = Field(
        None,
        alias="CRNCY_END_DTS",
        name="",
        description="",
        example="2020-05-03T15:59:59.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Lilo Conv",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-07-13T22:51:55.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="Lilo Conv",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-07-13T22:51:55.000Z",
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


class DREAMSFolioCrncyModel(BaseModel):
    """Payload class for DREAMSFolioCrncyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Currency"
        stream_name = ""
        description = """Type of currency"""
        unique_identifier = ["data.CRNCY_ISO_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CRNCY"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
