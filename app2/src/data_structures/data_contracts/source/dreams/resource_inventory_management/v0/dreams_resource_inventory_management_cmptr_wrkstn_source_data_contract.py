"""Source Data Contract Template for CMPTR_WRKSTN.json"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    cmptr_wrkstn_id: int = Field(
        ...,
        alias="CMPTR_WRKSTN_ID",
        name="",
        description="",
        example=111160,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cmptr_wrkstn_ip_addr_tx: Optional[str] = Field(
        None,
        alias="CMPTR_WRKSTN_IP_ADDR_TX",
        name="",
        description="",
        example="W7-PC08HLPY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cmptr_wrkstn_nm: str = Field(
        ...,
        alias="CMPTR_WRKSTN_NM",
        name="",
        description="",
        example="PAGO 1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2020-09-29T08:21:31.466000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="AAAAA006",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dflt_prt_id: Optional[int] = Field(
        None,
        alias="DFLT_PRT_ID",
        name="",
        description="",
        example=1184,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dftl_encdr_id: Optional[int] = Field(
        None,
        alias="DFTL_ENCDR_ID",
        name="",
        description="",
        example=40016,
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
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2020-09-29T10:07:11.617000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="GARAA006",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wrk_loc_id: int = Field(
        ...,
        alias="WRK_LOC_ID",
        name="",
        description="",
        example=57,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementCmptrWrkstnModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementCmptrWrkstnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Computer Workstation"
        stream_name = ""
        description = """This table provides information regarding the different technical devices used when interacting with guests """
        unique_identifier = ["data.CMPTR_WRKSTN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "cmptr_wrkstn"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
