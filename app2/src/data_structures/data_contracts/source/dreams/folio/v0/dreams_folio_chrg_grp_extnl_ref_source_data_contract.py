"""Source Data Contract Template for CHRG_GRP_EXTNL_REF.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for CHRG_GRP_EXTNL_REF"""

    extnl_ref_id: int = Field(
        ...,
        alias="EXTNL_REF_ID",
        name="",
        description="",
        example=1011170092,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_id: int = Field(
        ...,
        alias="CHRG_GRP_ID",
        name="",
        description="",
        example=983389700,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prmy_extnl_ref_in: str = Field(
        ...,
        alias="PRMY_EXTNL_REF_IN",
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
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T18:58:06Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T18:58:06Z",
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


class DREAMSFolioChrgGrpExtnlRefModel(BaseModel):
    """Payload class for DREAMSFolioChrgGrpExtnlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Group External reference"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.EXTNL_REF_ID", "data.CHRG_GRP_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG_GRP_EXTNL_REF"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
