"""Source Data Contract Template for DREAMS Resource Inventory Management Campus Configuration"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    allow_rpst_in: str = Field(
        ...,
        alias="ALLOW_RPST_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    byps_bal_due_in: str = Field(
        ...,
        alias="BYPS_BAL_DUE_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmps_config_id: int = Field(
        ...,
        alias="CMPS_CONFIG_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmps_id: Optional[int] = Field(
        None,
        alias="CMPS_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-10T14:08:19Z",
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

    dftl_crncy_cd: str = Field(
        ...,
        alias="DFTL_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dftl_lang_cd: str = Field(
        ...,
        alias="DFTL_LANG_CD",
        name="",
        description="",
        example="eng",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dt_fmt_vl: str = Field(
        ...,
        alias="DT_FMT_VL",
        name="",
        description="",
        example="MM/dd/yyyy",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tm_zn_nm: str = Field(
        ...,
        alias="TM_ZN_NM",
        name="",
        description="",
        example="America/New_York",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-02-22T01:22:51.272000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementCmpsConfigModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementCmpsConfigModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Campus Configuration"
        stream_name = ""
        description = """This table provides configuration information like date format, time zone, etc."""
        unique_identifier = ["data.CMPS_CONFIG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "cmps_config"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
