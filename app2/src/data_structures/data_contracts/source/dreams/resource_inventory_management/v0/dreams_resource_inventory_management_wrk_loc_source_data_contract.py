"""Source Data Contract for Dreams Resource Inventory Management wrk_loc"""


from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Resource Inventory Management data"""

    wrk_loc_id: int = Field(
        ...,
        alias="WRK_LOC_ID",
        name="",
        description="",
        example=51,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    wrk_loc_nm: str = Field(
        ...,
        alias="WRK_LOC_NM",
        name="",
        description="",
        example="Disney's Contemporary Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_acct_ctr_id: Optional[int] = Field(
        None,
        alias="TXN_ACCT_CTR_ID",
        name="",
        description="",
        example=14,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_acct_ctr_id: Optional[int] = Field(
        None,
        alias="BANK_ACCT_CTR_ID",
        name="",
        description="",
        example=10452,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_acct_ctr_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bus_org_id: int = Field(
        ...,
        alias="BUS_ORG_ID",
        name="",
        description="",
        example=2,
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
        example="2009-12-09T18:01:48.071235Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MICKM123",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-08T10:16:35.398000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=64,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    hm_rsrt_fac_id: Optional[int] = Field(
        None,
        alias="HM_RSRT_FAC_ID",
        name="",
        description="",
        example=273239,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementWrkLocModel(BaseModel):
    """DREAMSResourceInventoryManagementWrkLocModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Work Location"
        stream_name = ""
        description = "Work location IDs associated to resort facility IDs, Facility name, transactional account center ID, Bank account center ID and business organization ID"  # optional
        unique_identifier = ["data.WRK_LOC_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "wrk_loc"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
