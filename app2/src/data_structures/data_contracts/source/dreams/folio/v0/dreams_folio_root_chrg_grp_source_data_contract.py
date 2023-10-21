"""Source Data Contract for Dreams Folio Root Charge Group"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Root Charge Group Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-08T18:53:15.933000Z",
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

    grp_pay_dpst_apply_in: str = Field(
        ...,
        alias="GRP_PAY_DPST_APPLY_IN",
        name="",
        description="",
        example="N",
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
        example="2011-01-26T01:41:32.803Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    root_chrg_grp_id: int = Field(
        ...,
        alias="ROOT_CHRG_GRP_ID",
        name="",
        description="",
        example=983255972,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trvl_agt_id: Optional[int] = Field(
        None,
        alias="TRVL_AGT_ID",
        name="",
        description="",
        example=102014,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-22T18:38:37.804000Z",
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


class DREAMSFolioRootChrgGrpModel(BaseModel):
    """Payload class for DREAMSFolioRootChrgGrpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Root Charge Group"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.ROOT_CHRG_GRP_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ROOT_CHRG_GRP"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
