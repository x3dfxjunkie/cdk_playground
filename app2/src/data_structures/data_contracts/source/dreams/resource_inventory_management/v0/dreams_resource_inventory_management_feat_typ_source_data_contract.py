"""Source Data Contract for Dreams Resource Inventory Management Feature Type"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-10T14:05:54Z",
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

    feat_typ_ds: Optional[str] = Field(
        None,
        alias="FEAT_TYP_DS",
        name="",
        description="",
        example="View",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_typ_nm: str = Field(
        ...,
        alias="FEAT_TYP_NM",
        name="",
        description="",
        example="View",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_typ_req_nm: str = Field(
        ...,
        alias="FEAT_TYP_REQ_NM",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_typ_strt_dt: datetime = Field(
        ...,
        alias="FEAT_TYP_STRT_DT",
        name="",
        description="",
        example="2006-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-09-10T14:05:54Z",
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

    feat_typ_end_dt: Optional[datetime] = Field(
        None,
        alias="FEAT_TYP_END_DT",
        name="",
        description="",
        example="2009-11-12T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementFeatTypModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementFeatTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Feature Type"
        stream_name = ""
        description = """Holds the feature type names and their descriptions: FEAT_TYP_NM
Additional Bedding
Proximity
Pets
Wing
Floor Type
Cluster
Wing test
Theme
Building
View
Bedding
VIP
Area
TV Theme
Side
Connect
Physical
wing test A
Special
Floor"""
        unique_identifier = ["data.FEAT_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "feat_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
