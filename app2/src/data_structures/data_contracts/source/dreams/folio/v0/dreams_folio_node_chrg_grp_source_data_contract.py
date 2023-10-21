"""Source Data Contract Template for NODE_CHRG_GRP.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for NODE_CHRG_GRP"""

    root_chrg_grp_id: int = Field(
        ...,
        alias="ROOT_CHRG_GRP_ID",
        name="",
        description="",
        example=943973880,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guar_typ_nm: Optional[str] = Field(
        None,
        alias="GUAR_TYP_NM",
        name="",
        description="",
        example="DEPOSIT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_excpt_in: str = Field(
        ...,
        alias="PKG_EXCPT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="mdxCheckOut",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-10T09:56:29.545000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    node_chrg_grp_id: int = Field(
        ...,
        alias="NODE_CHRG_GRP_ID",
        name="",
        description="",
        example=943973881,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="5518139.1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2022-09-20T12:51:56.767000Z",
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
    ancstr_chrg_grp_id: Optional[int] = Field(
        None,
        alias="ANCSTR_CHRG_GRP_ID",
        name="",
        description="",
        example=983042693,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_chrg_grp_id: Optional[int] = Field(
        None,
        alias="BILL_CHRG_GRP_ID",
        name="",
        description="",
        example=82031,
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


class DREAMSFolioNodeChrgGrpModel(BaseModel):
    """Payload class for DREAMSFolioNodeChrgGrpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Node Charge Group"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.NODE_CHRG_GRP_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "NODE_CHRG_GRP"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
