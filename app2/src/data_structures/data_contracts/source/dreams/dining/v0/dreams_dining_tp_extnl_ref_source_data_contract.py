"""Source Data Contract for DREAMS Dining Travel Plan External Locator"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Dining TP_EXTNL_REF Data"""

    tp_extnl_ref_id: int = Field(
        ...,
        alias="TP_EXTNL_REF_ID",
        name="",
        description="",
        example=187,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tp_id: int = Field(
        ...,
        alias="TP_ID",
        name="",
        description="",
        example=111111116035,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tp_extnl_src_nm: str = Field(
        ...,
        alias="TP_EXTNL_SRC_NM",
        name="",
        description="",
        example="Siebel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tp_extnl_ref_vl: str = Field(
        ...,
        alias="TP_EXTNL_REF_VL",
        name="",
        description="",
        example="111111116035",
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
        example="2010-10-13 05:27:08.000000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-10-13 05:26:06.900168",
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


class DREAMSDiningTpExtnlRefModel(BaseModel):
    """Payload class for DREAMSDiningTpExtnlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan External Locator"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.TP_EXTNL_REF_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tp_extnl_ref"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
