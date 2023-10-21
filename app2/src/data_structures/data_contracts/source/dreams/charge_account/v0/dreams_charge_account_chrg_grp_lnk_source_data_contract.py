"""Source Data Contract Template for Dreams - Charge Group Link"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Charge Group Link Data"""

    chrg_grp_lnk_dts: datetime = Field(
        ...,
        alias="CHRG_GRP_LNK_DTS",
        name="",
        description="",
        example="2021-10-01T14:27:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_grp_lnk_id: int = Field(
        ...,
        alias="CHRG_GRP_LNK_ID",
        name="",
        description="",
        example=11079757,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_grp_lnk_typ_nm: str = Field(
        ...,
        alias="CHRG_GRP_LNK_TYP_NM",
        name="",
        description="",
        example="MERGE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2021-10-01T14:27:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="xNOTIFIER",
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

    lnkd_chrg_grp_id: int = Field(
        ...,
        alias="LNKD_CHRG_GRP_ID",
        name="",
        description="",
        example=49383937,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lnkg_chrg_grp_id: int = Field(
        ...,
        alias="LNKG_CHRG_GRP_ID",
        name="",
        description="",
        example=46771322,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rlvnt_chrg_grp_id: int = Field(
        ...,
        alias="RLVNT_CHRG_GRP_ID",
        name="",
        description="",
        example=49421074,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2021-10-04T22:15:28Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="xNOTIFIER",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSChargeAccountChrgGrpLnkModel(BaseModel):
    """Payload class for Dreams - Charge Group Link Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Group Link"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.CHRG_GRP_LNK_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "chrg_grp_lnk"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
