"""Source Data Contract for Dreams Folio System Payment"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio System Payment Data"""

    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=281076533,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sys_pmt_ext_txn_nb_vl: str = Field(
        ...,
        alias="SYS_PMT_EXT_TXN_NB_VL",
        name="",
        description="",
        example="DCL06/9/2023",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sys_pmt_ext_res_nb_val: str = Field(
        ...,
        alias="SYS_PMT_EXT_RES_NB_VAL",
        name="",
        description="",
        example="040608318001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sys_pmt_btch_dts: datetime = Field(
        ...,
        alias="SYS_PMT_BTCH_DTS",
        name="",
        description="",
        example="2023-06-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="PostPayDCL_2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T06:02:56.903000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-06-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioSysPmtModel(BaseModel):
    """Payload class for DREAMSFolioSysPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "System Payment"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.PMT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"

        key_path_value = "SYS_PMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
