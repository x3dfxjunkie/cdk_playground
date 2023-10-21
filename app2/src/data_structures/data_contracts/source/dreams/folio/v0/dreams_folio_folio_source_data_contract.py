"""Source Data Contract Template for FOLIO.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Folio Data Contract"""

    folio_id: int = Field(
        ...,
        alias="FOLIO_ID",
        name="",
        description="",
        example=276611200,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_typ_nm: str = Field(
        ...,
        alias="FOLIO_TYP_NM",
        name="",
        description="",
        example="INDIVIDUAL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_acct_ctr_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T17:05:48.390000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_cls_nm: str = Field(
        ...,
        alias="JDO_CLS_NM",
        name="",
        description="",
        example="ChargeGroupFolio",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T17:05:48.390000Z",
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


class DREAMSFolioFolioModel(BaseModel):
    """Payload class for DREAMSFolioFolioModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio"
        stream_name = ""
        description = "This table represents which guests are responsible for which Folio balance and if the guest elects to Express check out or Email of this shows what was processed on the credit card the guest has on file as a settlement method"  # optional
        unique_identifier = ["data.FOLIO_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "FOLIO"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
