"""Source Data Contract for DAS WDW lnk"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.das_wdw.global_das_wdw_source_data_contract import (
    GlobalDASWDWMetadata,
)


class Data(BaseModel):
    """
    Class for DAS WDW lnk Data
    """

    lnk_id: str = Field(
        ...,
        alias="LNK_ID",
        name="",
        description="",
        example="0000732412E945C89B93F4DA8DB4AE52",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    frst_nm: Optional[str] = Field(
        None,
        alias="FRST_NM",
        name="",
        description="",
        example="clever",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mi: Optional[str] = Field(
        None,
        alias="MI",
        name="",
        description="",
        example="strategic",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lst_nm: Optional[str] = Field(
        None,
        alias="LST_NM",
        name="",
        description="",
        example="accused",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    suff: Optional[str] = Field(
        None,
        alias="SUFF",
        name="",
        description="",
        example="Jr.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    titl: Optional[str] = Field(
        None,
        alias="TITL",
        name="",
        description="",
        example="Mr.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="f-wdwmmpdas",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2021-08-23 11:44:33",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="f-wdwmmpdas",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2015-09-30 23:10:48",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lgcl_del_in: str = Field(
        ...,
        alias="LGCL_DEL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DASWDWLnkModel(BaseModel):
    """
    Payload class for DAS WDW lnk
    """

    class Config:
        """Payload Level Metadata"""

        title = "Link"
        stream_name = "prd-use1-guest360-das-wdw-stream"
        description = "A list of all Guests that were created for entitlements. Contains Guest PII, such as first name and last name, of Guest associated to account link id."  # optional
        unique_identifier = ["data.LNK_ID"]
        timezone = "UTC"  # optional
        pi_category = ["Data from Children"]  # optional
        isps = "Confidential"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "lnk"

    data: Data = Field(..., alias="data")
    metadata: GlobalDASWDWMetadata = Field(..., alias="metadata")
