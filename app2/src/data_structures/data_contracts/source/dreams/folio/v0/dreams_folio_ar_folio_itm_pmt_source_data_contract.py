"""Source Data Contract Template for AR_FOLIO_ITM_PMT.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for AR_FOLIO_ITM_PMT"""

    ar_folio_itm_pmt_id: int = Field(
        ...,
        alias="AR_FOLIO_ITM_PMT_ID",
        name="",
        description="",
        example=15227166,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_id: int = Field(
        ...,
        alias="FOLIO_ID",
        name="",
        description="",
        example=117006211,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_item_id: int = Field(
        ...,
        alias="FOLIO_ITEM_ID",
        name="",
        description="",
        example=18202311937,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_pmt_id: int = Field(
        ...,
        alias="AR_PMT_ID",
        name="",
        description="",
        example=281062948,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_acct_dt: datetime = Field(
        ...,
        alias="AR_ACCT_DT",
        name="",
        description="",
        example="2023-06-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_pmt_dts: datetime = Field(
        ...,
        alias="AR_PMT_DTS",
        name="",
        description="",
        example="2023-06-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="SttlGMFol_15",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T02:30:33.917000Z",
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


class DREAMSFolioArFolioItmPmtModel(BaseModel):
    """Payload class for DREAMSFolioArFolioItmPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Receivable Folio Item Payment"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.AR_FOLIO_ITM_PMT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "AR_FOLIO_ITM_PMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
