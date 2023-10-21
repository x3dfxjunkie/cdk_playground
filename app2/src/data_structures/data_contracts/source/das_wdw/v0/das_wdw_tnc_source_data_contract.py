"""Source Data Contract for DAS WDW tnc"""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.das_wdw.global_das_wdw_source_data_contract import (
    GlobalDASWDWMetadata,
)


class Data(BaseModel):
    """
    Class for DAS WDW tnc Data
    """

    version: str = Field(
        ...,
        alias="VERSION",
        name="",
        description="",
        example="0.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tnc_txt: Optional[str] = Field(
        None,
        alias="TNC_TXT",
        name="",
        description="",
        example="default version of terms & conditions",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tnc_strt_dts: datetime = Field(
        ...,
        alias="TNC_STRT_DTS",
        name="",
        description="",
        example="2009-10-29 15:11:25",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tnc_end_dts: Optional[datetime] = Field(
        None,
        alias="TNC_END_DTS",
        name="",
        description="",
        example="2022-12-02 12:27:18",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="DASAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="1972-09-09 03:30:26",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="DASAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="1983-12-12 01:12:31",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lgcl_del_in: str = Field(
        ...,
        alias="LGCL_DEL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DASWDWTncModel(BaseModel):
    """
    Payload class for DAS WDW tnc
    """

    class Config:
        """Payload Level Metadata"""

        title = "Terms and Conditions"
        stream_name = "prd-use1-guest360-das-wdw-stream"
        description = "Reference table that specifies the different terms and condition versions in DAS and their start and end datetimes. A null end datetime, means it is the current active version."  # optional
        unique_identifier = ["data.VERSION"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "tnc"

    data: Data = Field(..., alias="data")
    metadata: GlobalDASWDWMetadata = Field(..., alias="metadata")
