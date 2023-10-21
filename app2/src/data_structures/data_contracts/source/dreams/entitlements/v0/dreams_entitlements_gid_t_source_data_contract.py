"""Source Data Contract for Dreams Entitlement GID_T"""


from __future__ import annotations

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for GID_T Data"""

    gid_cls_nb: int = Field(
        ...,
        alias="GID_CLS_NB",
        name="",
        description="",
        example=1111946,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gid_cls_nm: str = Field(
        ...,
        alias="GID_CLS_NM",
        name="",
        description="",
        example="com.wdw.entitlements.data.entity.EntitlementPlanExternalReference",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsGidTModel(BaseModel):
    """Payload class for DREAMSEntitlementsGidTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = ""
        unique_identifier = ["data.GID_CLS_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "True"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "GID_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
