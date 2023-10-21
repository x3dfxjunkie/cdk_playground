"""Source Data Contract Template for Dreams - Dining Admission Component"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Dining Admission Component Data"""

    adm_tc_id: int = Field(
        ...,
        alias="ADM_TC_ID",
        name="",
        description="",
        example=111117507,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ats_recon_in: str = Field(
        ...,
        alias="ATS_RECON_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ats_tkt_cd: str = Field(
        ...,
        alias="ATS_TKT_CD",
        name="",
        description="",
        example="CK00Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2011-09-14T16:47:05.953000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="FAKEU015",
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
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_prc_am: Optional[float] = Field(
        None,
        alias="TKT_PRC_AM",
        name="",
        description="",
        example=305.66,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2011-09-14T16:47:05.953000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="FAKEU015",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validity_end_dt: Optional[datetime] = Field(
        None,
        alias="VALIDITY_END_DT",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validity_strt_dt: Optional[datetime] = Field(
        None,
        alias="VALIDITY_STRT_DT",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningAdmCmpntModel(BaseModel):
    """Payload class for Dreams - Dining Admission Component Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Admission Component"
        stream_name = ""
        description = """When a reservation has admission components included, this table provides the enterprise Ticket Product Code that connects ticket product information across multiple applications. It also contains the tickets validity start and end dates which is a key attribute for date based tickets"""
        unique_identifier = ["data.ADM_TC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "adm_cmpnt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
