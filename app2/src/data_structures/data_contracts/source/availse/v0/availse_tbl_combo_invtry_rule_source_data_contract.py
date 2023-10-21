"""Source Data Contract Template for AvailSE - Table Combo Inventory Rule"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Table Combo Inventory Rule Data"""

    end_dt: Optional[datetime] = Field(
        None,
        alias="END_DT",
        name="",
        description="",
        example="1970-01-01T08:35:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_tm: Optional[datetime] = Field(
        None,
        alias="END_TM",
        name="",
        description="",
        example="1970-01-01T07:45:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_fac_id: int = Field(
        ...,
        alias="ENTRPRS_FAC_ID",
        name="",
        description="",
        example=16515009,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_combinable_pct: Optional[float] = Field(
        None,
        alias="MAX_COMBINABLE_PCT",
        name="",
        description="",
        example=0.5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-5ad3-49fe-af5f-c292a02b5efc",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strt_dt: Optional[str] = Field(
        None,
        alias="STRT_DT",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strt_tm: Optional[datetime] = Field(
        None,
        alias="STRT_TM",
        name="",
        description="",
        example="1970-01-01T07:30:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tbl_combo_invtry_rule_id: str = Field(
        ...,
        alias="TBL_COMBO_INVTRY_RULE_ID",
        name="",
        description="",
        example="aa11aa11-0b88-4233-ba3d-89756936b114",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="FAKEU010",
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


class AvailSETblComboInvtryRuleModel(BaseModel):
    """Payload class for AvailSE - Table Combo Inventory Rule Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Table Combo Inventory Rule"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.TBL_COMBO_INVTRY_RULE_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tbl_combo_invtry_rule"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
