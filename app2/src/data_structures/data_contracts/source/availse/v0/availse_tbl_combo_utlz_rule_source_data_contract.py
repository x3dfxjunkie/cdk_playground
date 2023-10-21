"""Source Data Contract Template for AvailSE - Table Combo Utilization Rule"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Table Combo Utilization Rule Data"""

    end_dt: Optional[datetime] = Field(
        None,
        alias="END_DT",
        name="",
        description="",
        example="2023-12-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_tm: Optional[datetime] = Field(
        None,
        alias="END_TM",
        name="",
        description="",
        example="1970-01-01T14:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_fac_id: int = Field(
        ...,
        alias="ENTRPRS_FAC_ID",
        name="",
        description="",
        example=354261,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    min_utlz_pct: float = Field(
        ...,
        alias="MIN_UTLZ_PCT",
        name="",
        description="",
        example=0.75,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strt_dt: Optional[datetime] = Field(
        None,
        alias="STRT_DT",
        name="",
        description="",
        example="2023-07-05T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strt_tm: Optional[datetime] = Field(
        None,
        alias="STRT_TM",
        name="",
        description="",
        example="1970-01-01T12:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tbl_combo_utlz_rule_id: str = Field(
        ...,
        alias="TBL_COMBO_UTLZ_RULE_ID",
        name="",
        description="",
        example="AA11AA11-035A-51C6-E043-9906F4D151C6",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="FAKEU004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: str = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="0001-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    version_sn: int = Field(
        ...,
        alias="VERSION_SN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSETblComboUtlzRuleModel(BaseModel):
    """Payload class for AvailSE - Table Combo Utilization Rule Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Table Combo Utilization Rule"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.TBL_COMBO_UTLZ_RULE_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tbl_combo_utlz_rule"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
