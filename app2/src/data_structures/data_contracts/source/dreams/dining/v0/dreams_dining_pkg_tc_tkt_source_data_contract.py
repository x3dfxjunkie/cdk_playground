"""Source Data Contract Template for Dreams - Dining Package Travel Component Ticket"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Dining Package Travel Component Ticket Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-12-01T18:25:24.524000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="FAKEU025",
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

    pkg_tc_id: int = Field(
        ...,
        alias="PKG_TC_ID",
        name="",
        description="",
        example=357371914,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_pkup_dts: datetime = Field(
        ...,
        alias="TKT_PKUP_DTS",
        name="",
        description="",
        example="2010-12-01T18:25:24.638000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_reprnt_cn: int = Field(
        ...,
        alias="TKT_REPRNT_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-12-01T18:25:24.524000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="FAKEU025",
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


class DREAMSDiningPkgTcTktModel(BaseModel):
    """Payload class for Dreams - Dining Package Travel Component Ticket Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Package Travel Component Ticket"
        stream_name = ""
        description = """If a package on a reservation includes tickets, this table provides the date and time when the ticket was picked up and whether or not it was re-printed."""
        unique_identifier = ["data.PKG_TC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "pkg_tc_tkt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
