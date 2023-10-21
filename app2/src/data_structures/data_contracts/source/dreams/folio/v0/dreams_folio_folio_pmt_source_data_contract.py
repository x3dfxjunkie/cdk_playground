"""Source Data Contract Template for FOLIO_PMT.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for FOLIO_PMT"""

    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=281062082,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_settl_meth_id: int = Field(
        ...,
        alias="FOLIO_SETTL_METH_ID",
        name="",
        description="",
        example=62724462,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_folio_id: int = Field(
        ...,
        alias="CHRG_GRP_FOLIO_ID",
        name="",
        description="",
        example=269646470,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="SttlGPFol_15",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T02:23:06.403000Z",
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


class DREAMSFolioFolioPmtModel(BaseModel):
    """Payload class for DREAMSFolioFolioPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio Payment"
        stream_name = ""
        description = (
            "This table ties the payment ID to Folio Settlement Method and the Charge Group Folio ID"  # optional
        )
        unique_identifier = ["data.PMT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "FOLIO_PMT"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
