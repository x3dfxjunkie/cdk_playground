"""Source Data Contract Template for PMT_EXTNL_REF.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for PMT_EXTNL_REF"""

    pmt_extnl_ref_id: int = Field(
        ...,
        alias="PMT_EXTNL_REF_ID",
        name="",
        description="",
        example=3597606,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=281077648,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    extnl_src_nm: str = Field(
        ...,
        alias="EXTNL_SRC_NM",
        name="",
        description="",
        example="DREAMS_TPS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_extnl_ref_vl: str = Field(
        ...,
        alias="PMT_EXTNL_REF_VL",
        name="",
        description="",
        example="153160994943",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T08:43:59.417000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T08:43:59.417000Z",
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


class DREAMSFolioPmtExtnlRefModel(BaseModel):
    """Payload class for DREAMSFolioPmtExtnlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Payment External Reference"
        stream_name = ""
        description = "This table associates external sources to payments. EXTNL_SRC_NM, DPMSGroupProfile, DREAMS_TP, DREAMS_TPS, SECURE_ID, VISUAL_ID"  # optional
        unique_identifier = ["data.PMT_EXTNL_REF_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PMT_EXTNL_REF"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
