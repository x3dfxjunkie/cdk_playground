"""Source Data Contract for Dreams Resource Inventory Management RSRC OWN"""


from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    adlt_cn: Optional[int] = Field(
        None,
        alias="ADLT_CN",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    asgn_ownr_id: int = Field(
        ...,
        alias="ASGN_OWNR_ID",
        name="",
        description="",
        example=346897710,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bkng_dt: datetime = Field(
        ...,
        alias="BKNG_DT",
        name="",
        description="",
        example="2023-08-15T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chld_cn: Optional[int] = Field(
        None,
        alias="CHLD_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-15T17:01:03.862000Z",
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
    onln_chkin_in: str = Field(
        ...,
        alias="ONLN_CHKIN_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    orig_shr_ocpnt_in: Optional[str] = Field(
        None,
        alias="ORIG_SHR_OCPNT_IN",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    own_ds: Optional[str] = Field(
        None,
        alias="OWN_DS",
        name="",
        description="",
        example="Mouse, Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    own_end_dts: datetime = Field(
        ...,
        alias="OWN_END_DTS",
        name="",
        description="",
        example="2023-11-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    own_frm_dts: datetime = Field(
        ...,
        alias="OWN_FRM_DTS",
        name="",
        description="",
        example="2023-11-04T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_own_id: int = Field(
        ...,
        alias="RSRC_OWN_ID",
        name="",
        description="",
        example=111095518,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-15T18:22:46.767000Z",
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


class DREAMSResourceInventoryManagementRsrcOwnModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcOwnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Owner"
        stream_name = ""
        description = "This table holds the owner name, from and to dates and adult and child count"
        unique_identifier = ["data.RSRC_OWN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_own"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
