"""Source Data Contract Template for Dreams - Dining Sales Channel"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Dining Sales Channel Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-06T10:36:29Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ABCDEONV",
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

    sls_chan_id: int = Field(
        ...,
        alias="SLS_CHAN_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sls_chan_nm: str = Field(
        ...,
        alias="SLS_CHAN_NM",
        name="",
        description="",
        example="Consumer Direct",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-08-06T10:36:29Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="ABCDEONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningSlsChanModel(BaseModel):
    """Payload class for DREAMSDiningSlsChanModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Sales Channel"
        stream_name = ""
        description = """The individual or organization that has brought the reservation to WDW or Aulani"""
        unique_identifier = ["data.SLS_CHAN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "sls_chan"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
