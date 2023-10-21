"""Source Data Contract Template for DREAMS Resource Inventory Management Assigned Rate Type"""


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    asgn_rt_typ_scr_nb: int = Field(
        ...,
        alias="ASGN_RT_TYP_SCR_NB",
        name="",
        description="",
        example=100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-10T14:11:24Z",
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

    rsrt_asgn_scr_id: int = Field(
        ...,
        alias="RSRT_ASGN_SCR_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rt_typ_nm: str = Field(
        ...,
        alias="RT_TYP_NM",
        name="",
        description="",
        example="GRP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-09-10T14:11:24Z",
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


class DREAMSResourceInventoryManagementAsgnRtTypModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementAsgnRtTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Assigned Rate Type"
        stream_name = ""
        description = """This table contains the rate category codes without any known FKs:
                        GEN
                        GRP
                        PAR
                        SP1
                        SP2
                        SP3
                        SP4
                        UPS
                    """
        unique_identifier = ["data.RSRT_ASGN_SCR_ID", "data.RT_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "asgn_rt_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
