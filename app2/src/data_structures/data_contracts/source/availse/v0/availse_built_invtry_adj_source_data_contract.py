"""Source Data Contract Template for AvailseBuiltinventoryadjusted"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Built Inventory Adjusted Data"""

    built_invtry_adj_actv_in: str = Field(
        ...,
        alias="BUILT_INVTRY_ADJ_ACTV_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_invtry_adj_end_dts: datetime = Field(
        ...,
        alias="BUILT_INVTRY_ADJ_END_DTS",
        name="",
        description="",
        example="2023-08-22T23:59:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_invtry_adj_id: str = Field(
        ...,
        alias="BUILT_INVTRY_ADJ_ID",
        name="",
        description="",
        example="11aa11aa-f45c-d266-1b47-bea06b6d6878",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_invtry_adj_series_id: Optional[str] = Field(
        None,
        alias="BUILT_INVTRY_ADJ_SERIES_ID",
        name="",
        description="",
        example="11aa11aa-c096-931e-1f88-334cabed99f1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_invtry_adj_srvc_prd_in: str = Field(
        ...,
        alias="BUILT_INVTRY_ADJ_SRVC_PRD_IN",
        name="",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_invtry_adj_strt_dts: datetime = Field(
        ...,
        alias="BUILT_INVTRY_ADJ_STRT_DTS",
        name="",
        description="",
        example="2023-08-22T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dow_nm: Optional[str] = Field(
        None,
        alias="DOW_NM",
        name="",
        description="",
        example="Wednesday",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_fac_srvc_prd_nm: str = Field(
        ...,
        alias="ENTRPRS_FAC_SRVC_PRD_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_rsrc_config_inv_adj_cn: int = Field(
        ...,
        alias="FAC_RSRC_CONFIG_INV_ADJ_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsn_id: str = Field(
        ...,
        alias="RSN_ID",
        name="",
        description="",
        example="aa11aa11-72e2-441e-8e1d-1b8102a89eb4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-459F-7044-E043-9906F4D17044",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="FAKEU005",
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


class AvailSEBuiltInvtryAdjModel(BaseModel):
    """Payload class for AvailSE - Built Inventory Adjusted Model"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """"""
        unique_identifier = ["data.BUILT_INVTRY_ADJ_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "built_invtry_adj"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
