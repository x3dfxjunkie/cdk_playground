"""Source Data Contract for Dreams Folio Resort Special Reservations Payment"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Resort Special Reservations Payment Data"""

    acct_ctr_sap_id: int = Field(
        ...,
        alias="ACCT_CTR_SAP_ID",
        name="",
        description="",
        example=1356911,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-23T08:19:17.925000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MickeyMouse_7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=283333630,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2011-01-26T01:41:32.803Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_gl_ref_id: int = Field(
        ...,
        alias="SAP_GL_REF_ID",
        name="",
        description="",
        example=3121560,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioRsrPmtModel(BaseModel):
    """Payload class for DREAMSFolioRsrPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resort Special Reservations Payment"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.PMT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "RSR_PMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
