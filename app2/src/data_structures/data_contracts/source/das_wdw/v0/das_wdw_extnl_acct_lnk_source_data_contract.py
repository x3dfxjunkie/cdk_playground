"""Source Data Contract for DAS WDW extnl_acct_lnk"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.das_wdw.global_das_wdw_source_data_contract import (
    GlobalDASWDWMetadata,
)


class Data(BaseModel):
    """
    Class for DAS WDW extnl_acct_lnk Data
    """

    extnl_acct_lnk_id: int = Field(
        ...,
        alias="EXTNL_ACCT_LNK_ID",
        name="",
        description="""""",
        example=10001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lnk_id: str = Field(
        ...,
        alias="LNK_ID",
        name="",
        description="""""",
        example="B3D19259F6484D84871ED8BF2996CA65",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    extnl_sys_entty_nm: str = Field(
        ...,
        alias="EXTNL_SYS_ENTTY_NM",
        name="",
        description="""""",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    extnl_sys_entty_vl: str = Field(
        ...,
        alias="EXTNL_SYS_ENTTY_VL",
        name="",
        description="""""",
        example="{438DACFB-BC64-43B6-9CA1-AF983DF}",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="DASAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="1984-03-13 02:57:28",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="DASAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="1981-12-21 05:15:18",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lgcl_del_in: str = Field(
        ...,
        alias="LGCL_DEL_IN",
        name="",
        description="""""",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DASWDWExtnlAcctLnkModel(BaseModel):
    """
    Payload class for DAS WDW extnl_acct_lnk
    """

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Account LInk"
        stream_name = "prd-use1-guest360-das-wdw-stream"
        description = "Contains linkage between the DAS entitlement and the GAM keyring guest ID associated with it. Such as guid, xid, swid, ea-link-id, transactional-gues-id, gss-link-id, etc."  # optional
        unique_identifier = ["data.EXTNL_ACCT_LNK_ID"]
        timezone = "UTC"  # optional
        pi_category = ["Data from Children"]  # optional
        isps = "Confidential"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "extnl_acct_lnk"

    data: Data = Field(..., alias="data")
    metadata: GlobalDASWDWMetadata = Field(..., alias="metadata")
