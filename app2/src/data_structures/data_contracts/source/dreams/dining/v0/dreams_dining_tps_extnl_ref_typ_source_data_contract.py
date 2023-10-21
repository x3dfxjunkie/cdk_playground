"""Source Data Contract Template for Dreams - Dining Travel Plan Segment External Reference Type"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Dining TPS_EXTNL_REF_TYP Data"""

    tps_extnl_ref_typ_nm: str = Field(
        ...,
        alias="TPS_EXTNL_REF_TYP_NM",
        name="",
        description="",
        example="APP_REF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="S-584559",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2019-03-19 07:46:06.000000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningTpsExtnlRefTypModel(BaseModel):
    """Payload class for DREAMSDiningTpsExtnlRefTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan Segment External Reference Type"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.TPS_EXTNL_REF_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tps_extnl_ref_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
