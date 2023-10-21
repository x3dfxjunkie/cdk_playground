"""Source Data Contract Template for Dreams - Dining Travel Component Group Type"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Dining Travel Component Group Type Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="1980-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Lilo Conv",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_grp_typ_nm: str = Field(
        ...,
        alias="TC_GRP_TYP_NM",
        name="",
        description="",
        example="ACCOMMODATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningTcGrpTypModel(BaseModel):
    """Payload class for Dreams - Dining Travel Component Group Type Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Group Type"
        stream_name = ""
        description = """Provides the types of travel component grouping  ie: TC_GRP_TYP_NM ACCOMMODATION ACTIVITY ADD_ON_PACKAGE ADMISSION CIRQUE COMP_TICKET DAY_GUEST_TICKET DME EVENTDINING FOODANDBEVERAGE HARD_TICKET_EVENT ONETIMEUSEPOINTS PACKAGE SHOWDINING SPA TABLESERVICEDINING"""
        unique_identifier = ["data.TC_GRP_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tc_grp_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
