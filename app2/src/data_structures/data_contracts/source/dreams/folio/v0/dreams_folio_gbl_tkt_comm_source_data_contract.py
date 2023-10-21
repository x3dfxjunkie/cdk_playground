"""Source Data Contract Template for DREAMS Folio Global Ticket Commission"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Global Ticket Commission Data"""

    glbl_tkt_comm_id: int = Field(
        ...,
        alias="GLBL_TKT_COMM_ID",
        name="",
        description="",
        example=17842800,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=3097454,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tkt_cd: str = Field(
        ...,
        alias="TKT_CD",
        name="",
        description="",
        example="CJF3N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    glbl_tkt_comm_pc: int = Field(
        ...,
        alias="GLBL_TKT_COMM_PC",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    glbl_tkt_comm_strt_dt: datetime = Field(
        ...,
        alias="GLBL_TKT_COMM_STRT_DT",
        name="",
        description="",
        example="2016-10-02T04:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    glbl_tkt_comm_chg_dt: Optional[datetime] = Field(
        None,
        alias="GLBL_TKT_COMM_CHG_DT",
        name="",
        description="",
        example="2016-09-10T04:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    glbl_tkt_comm_rfrsh_dt: Optional[datetime] = Field(
        None,
        alias="GLBL_TKT_COMM_RFRSH_DT",
        name="",
        description="",
        example="2017-02-04T12:00:34.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ATSR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2017-02-04T12:00:34.519Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="ATSR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2017-02-04T12:00:34.519Z",
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


class DREAMSFolioGblTktCommModel(BaseModel):
    """Payload class for DREAMSFolioGblTktCommModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Global Ticket Commission"
        stream_name = ""
        description = """This table ties the commission percentage for Tickets Last loaded on 1/26/2021"""
        unique_identifier = ["data.GLBL_TKT_COMM_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "GBL_TKT_COMM"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
