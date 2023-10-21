"""Source Data Contract for Dreams Entitlement Coupon Point of Sale Location Configuration"""


from __future__ import annotations

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon Point of Sale Location Configuration Data"""

    cpn_acpt_in: str = Field(
        ...,
        alias="CPN_ACPT_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_pos_loc_config_id: int = Field(
        ...,
        alias="CPN_POS_LOC_CONFIG_ID",
        name="",
        description="",
        example=1117,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_rpst_in: str = Field(
        ...,
        alias="CPN_RPST_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-05-07T14:39:37.883186Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MDMUPD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: Optional[str] = Field(
        None,
        alias="PROD_ID",
        name="",
        description="",
        example="textid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rgstr_nb_vl: str = Field(
        ...,
        alias="RGSTR_NB_VL",
        name="",
        description="",
        example="00025",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sld_id_vl: str = Field(
        ...,
        alias="SLD_ID_VL",
        name="",
        description="",
        example="0005",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_acct_ctr_id: int = Field(
        ...,
        alias="TXN_ACCT_CTR_ID",
        name="",
        description="",
        example=11117,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-02-16T17:55:54.075000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MOUSM021",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsCpnPosLocConfigTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnPosLocConfigTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Coupon Point of Sale Location Configuration"
        stream_name = ""
        description = """This table associates Transaction Center Account IDs to Sales locations via Register Number Value this provides the configuration to know if a coupon charge is allowed to be accepted and/or reposted"""
        unique_identifier = ["data.CPN_POS_LOC_CONFIG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_POS_LOC_CONFIG_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
