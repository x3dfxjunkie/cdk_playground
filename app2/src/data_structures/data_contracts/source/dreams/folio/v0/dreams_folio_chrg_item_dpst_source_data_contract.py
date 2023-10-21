"""Source Data Contract Template for CHRG_ITEM_DPST.json"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for CHRG_ITEM_DPST"""

    chrg_item_dpst_id: int = Field(
        ...,
        alias="CHRG_ITEM_DPST_ID",
        name="",
        description="",
        example=489777063,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_item_id: int = Field(
        ...,
        alias="CHRG_ITEM_ID",
        name="",
        description="",
        example=18203720284,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_item_dpst_due_dt: datetime = Field(
        ...,
        alias="CHRG_ITEM_DPST_DUE_DT",
        name="",
        description="",
        example="2023-06-02T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_item_dpst_am: float = Field(
        ...,
        alias="CHRG_ITEM_DPST_AM",
        name="",
        description="",
        example=881.75,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_item_dpst_crncy_cd: str = Field(
        ...,
        alias="CHRG_ITEM_DPST_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="TbxSyncUser",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-11T17:32:07.629000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="TbxSyncUser",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-11T17:32:07.629000Z",
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
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioChrgItemDpstModel(BaseModel):
    """Payload class for DREAMSFolioChrgItemDpstModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Item Deposit"
        stream_name = ""
        description = "This table associates the charge items that are required for Guaranteeing the reservation and the date by which the deposit should be made to avoid cancellation"  # optional
        unique_identifier = ["data.CHRG_ITEM_DPST_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CHRG_ITEM_DPST"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
