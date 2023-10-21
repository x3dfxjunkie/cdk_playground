"""Source Data Contract for DREAMS Revenue Class"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Revenue Class Data"""

    rev_cls_id: int = Field(
        ...,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=12118584,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_nm: str = Field(
        ...,
        alias="REV_CLS_NM",
        name="",
        description="",
        example="Guest Inconvenience Ala Carte",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_actv_in: str = Field(
        ...,
        alias="REV_CLS_ACTV_IN",
        name="",
        description="",
        example="Y",
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
        example="2010-01-20T05:12:30.027Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="CLAET001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2011-02-18T17:08:36.797Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_lvl_nb: int = Field(
        ...,
        alias="REV_CLS_LVL_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prnt_rev_cls_id: Optional[int] = Field(
        None,
        alias="PRNT_REV_CLS_ID",
        name="",
        description="",
        example=13773708,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    root_rev_cls_id: int = Field(
        ...,
        alias="ROOT_REV_CLS_ID",
        name="",
        description="",
        example=12118584,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    root_rev_cls_nm: Optional[str] = Field(
        None,
        alias="ROOT_REV_CLS_NM",
        name="",
        description="",
        example="Phone Calls - All Types",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingRevClsModel(BaseModel):
    """Payload class for DREAMSAccountingRevClsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Revenue Class"
        stream_name = ""
        description = """List of Revenue Class names associated to Revenue Class IDs"""
        unique_identifier = ["data.REV_CLS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "REV_CLS"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
