"""Source Data Contract Template for CHRG_EXTNL_REF.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for CHRG_EXTNL_REF"""

    chrg_extnl_ref_id: int = Field(
        ...,
        alias="CHRG_EXTNL_REF_ID",
        name="",
        description="",
        example=1788629896,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    extnl_src_nm: str = Field(
        ...,
        alias="EXTNL_SRC_NM",
        name="",
        description="",
        example="ROOM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_id: int = Field(
        ...,
        alias="CHRG_ID",
        name="",
        description="",
        example=3401415356,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_extnl_ref_vl: str = Field(
        ...,
        alias="CHRG_EXTNL_REF_VL",
        name="",
        description="",
        example="5239",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="GOHIS001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T14:01:31.874000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="GOHIS001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T14:01:31.874000Z",
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


class DREAMSFolioChrgExtnlRefModel(BaseModel):
    """Payload class for DREAMSFolioChrgExtnlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge External Reference"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CHRG_EXTNL_REF_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG_EXTNL_REF"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
