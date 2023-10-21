"""Source Data Contract Template for CMP_EXTNL_REF.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for CMP_EXTNL_REF"""

    cmp_extnl_ref_id: int = Field(
        ...,
        alias="CMP_EXTNL_REF_ID",
        name="",
        description="",
        example=122134339,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_mkt_pkg_id: int = Field(
        ...,
        alias="CHRG_MKT_PKG_ID",
        name="",
        description="",
        example=160895839,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    extnl_src_nm: str = Field(
        ...,
        alias="EXTNL_SRC_NM",
        name="",
        description="",
        example="DREAMS_TC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cmp_extnl_ref_vl: str = Field(
        ...,
        alias="CMP_EXTNL_REF_VL",
        name="",
        description="",
        example="12092785498",
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
        example="2023-06-10T16:09:31.169000Z",
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
        example="2023-06-10T16:09:31.169000Z",
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


class DREAMSFolioCmpExtnlRefModel(BaseModel):
    """Payload class for DREAMSFolioCmpExtnlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Market Package External Reference"
        stream_name = ""
        description = """This table ties the charge market package ID to the Reservation Management Travel Component ID"""  # optional
        unique_identifier = ["data.CMP_EXTNL_REF_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CMP_EXTNL_REF"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
