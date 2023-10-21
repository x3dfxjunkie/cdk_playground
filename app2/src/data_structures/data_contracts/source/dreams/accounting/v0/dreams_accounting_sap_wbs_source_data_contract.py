"""Source Data Contract for DREAMS Accounting SAP WBS"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Accounting SAP WBS Data"""

    sap_wbs_cd: str = Field(
        ...,
        alias="SAP_WBS_CD",
        name="",
        description="",
        example="5230004.SL.OT.02.02",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_wbs_nm: Optional[str] = Field(
        None,
        alias="SAP_WBS_NM",
        name="",
        description="",
        example="5230004.SL.OT.02.02",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="GOLXX002",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-16T15:05:11.684000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapWbsModel(BaseModel):
    """Payload class for DREAMSAccountingSapWbsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Accounting SAP WBS"
        stream_name = ""
        description = "SAP WBS Names associated to SAP WBS Codes"  # optional
        unique_identifier = ["data.SAP_WBS_CD"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "sap_wbs"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
