"""Source Data Contract Template for DCV_PRFL_RTE_TYP"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Profile Data"""

    prfl_rte_typ_nm: str = Field(
        ...,
        alias="PRFL_RTE_TYP_NM",
        name="",
        description="",
        example="AutoFulfillment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="AULANI_MDM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2011-06-07T06:02:49.176-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSProfilePrflRteTypModel(BaseModel):
    """Payload class for DREAMSProfilePrflRteTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Profile Route Type"
        stream_name = ""
        description = "List of different profile route types: PRFL_RTE_TYP_NM; AutoFulfillment; Celebrations; Dispatch System; Guest History; Guest Recovery; Guest Request; HouseKeeping; Inventory; Reservation; Reservation and Confirmation; Resort Call Center; SE SPL Needs; SPL Event"
        unique_identifier = ["data.PRFL_RTE_TYP_NM"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prfl_rte_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
