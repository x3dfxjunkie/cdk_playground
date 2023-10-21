"""Source Data Contract for Dreams Resource Inventory Management FEAT"""


from __future__ import annotations
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-10T14:08:19Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feat_ds: Optional[str] = Field(
        None,
        alias="FEAT_DS",
        name="",
        description="",
        example="Full Patio, Wet Bar",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feat_end_dt: Optional[datetime] = Field(
        None,
        alias="FEAT_END_DT",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feat_id: int = Field(
        ...,
        alias="FEAT_ID",
        name="",
        description="",
        example=224,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feat_nm: str = Field(
        ...,
        alias="FEAT_NM",
        name="",
        description="",
        example="Full Patio, Wet Bar",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feat_req_nm: str = Field(
        ...,
        alias="FEAT_REQ_NM",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feat_strt_dt: datetime = Field(
        ...,
        alias="FEAT_STRT_DT",
        name="",
        description="",
        example="2006-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feat_typ_nm: str = Field(
        ...,
        alias="FEAT_TYP_NM",
        name="",
        description="",
        example="Physical",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-09-10T14:08:19Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementFeatModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementFeatModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Feature"
        stream_name = ""
        description = """This table associates a unique identifier for the various features of the resort"""
        unique_identifier = ["data.FEAT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "feat"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
