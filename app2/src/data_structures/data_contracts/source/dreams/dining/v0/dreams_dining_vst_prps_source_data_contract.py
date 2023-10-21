"""Source Data Contract Template for DREAMS Dining - Visit Purpose"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Dining - vst_prps Data"""

    vst_prps_nm: str = Field(
        ...,
        alias="VST_PRPS_NM",
        name="",
        description="",
        example="Convention",
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
        example="2009-08-06 10:36:33.000000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningVstPrpsModel(BaseModel):
    """Payload class for DREAMSDiningVstPrpsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Visit Purpose"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.VST_PRPS_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "vst_prps"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
