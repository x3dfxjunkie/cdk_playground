"""Source Data Contract for Dreams Resource Inventory Management wrk_loc_encdr"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Resource Inventory Management data"""

    encdr_id: int = Field(
        ...,
        alias="ENCDR_ID",
        name="",
        description="",
        example=1085,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wrk_loc_id: int = Field(
        ...,
        alias="WRK_LOC_ID",
        name="",
        description="",
        example=51,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    encdr_nm: str = Field(
        ...,
        alias="ENCDR_NM",
        name="",
        description="",
        example="Data Card SP55 - TIMELOX 0101",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    encdr_ip_addr_tx: Optional[str] = Field(
        None,
        alias="ENCDR_IP_ADDR_TX",
        name="",
        description="",
        example="99.99.99.999",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    encdr_drvr_nm: Optional[str] = Field(
        None,
        alias="ENCDR_DRVR_NM",
        name="",
        description="",
        example="Timelox",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MDMUPD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-05-14T14:11:50.249003Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="DAVIB154",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-08T10:16:35.398000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=46,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementWrkLocEncdrModel(BaseModel):
    """Final payload class for DREAMSResourceInventoryManagementWrkLocEncdrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Work Location Encoder"
        stream_name = ""
        description = "Room key encoder IDs, Name, IP address"  # optional
        unique_identifier = ["data.ENCDR_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "wrk_loc_prt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
