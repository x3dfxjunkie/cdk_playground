"""Source Data Contract Template for FOLIO_PRFL.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for FOLIO_PRFL"""

    folio_prfl_id: int = Field(
        ...,
        alias="FOLIO_PRFL_ID",
        name="",
        description="",
        example=16053228,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dflt_settl_meth_id: int = Field(
        ...,
        alias="DFLT_SETTL_METH_ID",
        name="",
        description="",
        example=427664228,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="DIRSK001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-12T16:39:19.391000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioFolioPrflModel(BaseModel):
    """Payload class for DREAMSFolioFolioPrflModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio Profile"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.FOLIO_PRFL_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FOLIO_PRFL"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
