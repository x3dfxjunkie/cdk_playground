"""Source Data Contract Template for DREAMS Price - Experience Enhancement Data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - exprnc_enhnc_t Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2013-04-30T06:15:10Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="DMTeam",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_ds: str = Field(
        ...,
        alias="EXPRNC_ENHNC_DS",
        name="",
        description="",
        example="Direct-To-Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_end_dt: Optional[datetime] = Field(
        None,
        alias="EXPRNC_ENHNC_END_DT",
        name="",
        description="",
        example="2023-08-25T20:35:22.703832Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_nm: str = Field(
        ...,
        alias="EXPRNC_ENHNC_NM",
        name="",
        description="",
        example="DTR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_strt_dt: datetime = Field(
        ...,
        alias="EXPRNC_ENHNC_STRT_DT",
        name="",
        description="",
        example="2013-04-30T06:15:10Z",
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2013-04-30T06:15:10Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="DMTeam",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceExprncEnhncTModel(BaseModel):
    """Payload class for DREAMSPriceExprncEnhncTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """An enhancement to the participation in an event or activity.  Initially requested for the Bypass Desk functionality from NGE.  In the future, the business may wish to enhance other Guest experiences.   """
        unique_identifier = ["data.EXPRNC_ENHNC_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "EXPRNC_ENHNC_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
