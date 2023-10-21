"""Source Data Contract for Dreams DCV_PRFL_RTE_TYP"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Profile Data"""

    prfl_rte_id: int = Field(
        ...,
        alias="PRFL_RTE_ID",
        name="",
        description="",
        example=233,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prfl_id: int = Field(
        ...,
        alias="PRFL_ID",
        name="",
        description="",
        example=233,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prfl_rte_typ_nm: str = Field(
        ...,
        alias="PRFL_RTE_TYP_NM",
        name="",
        description="",
        example="Reservation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dflt_prfl_rte_in: str = Field(
        ...,
        alias="DFLT_PRFL_RTE_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    kodo_prfl_rte_type_nm: str = Field(
        ...,
        alias="KODO_PRFL_RTE_TYP_NM",
        name="",
        description="",
        example="Routing",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-12T05:50:36.000-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-08-12T05:50:36.000-05:00",
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
    load_dts: Optional[str] = Field(
        None,
        alias="load_dts",
        name="",
        description="",
        example="20230619",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSProfilePrflRteModel(BaseModel):
    """Payload class for DREAMSProfilePrflRteModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Profile Route"
        stream_name = ""
        description = "This table links the route the profile should take based on type."
        unique_identifier = ["data.PRFL_RTE_ID"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prfl_rte"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
