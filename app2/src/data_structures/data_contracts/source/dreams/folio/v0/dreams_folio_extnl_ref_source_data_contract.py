"""Source Data Contract Template for EXTNL_REF.json"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for EXTNL_REF"""

    extnl_ref_id: int = Field(
        ...,
        alias="EXTNL_REF_ID",
        name="",
        description="",
        example=1011148940,
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
    extnl_ref_val: str = Field(
        ...,
        alias="EXTNL_REF_VAL",
        name="",
        description="",
        example="153160000486",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="4274843.1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T16:10:18.622000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="4274843.1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T16:10:18.622000Z",
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
    incognito: Optional[str] = Field(
        None,
        alias="INCOGNITO",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioExtnlRefModel(BaseModel):
    """Payload class for DREAMSFolioExtnlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "External Reference"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.EXTNL_REF_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "EXTNL_REF"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
