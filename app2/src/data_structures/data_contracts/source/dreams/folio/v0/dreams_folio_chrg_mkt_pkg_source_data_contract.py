"""Source Data Contract Template for CHRG_MKT_PKG.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for CHRG_MKT_PKG"""

    chrg_mkt_pkg_id: int = Field(
        ...,
        alias="CHRG_MKT_PKG_ID",
        name="",
        description="",
        example=160928201,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_id: int = Field(
        ...,
        alias="PKG_ID",
        name="",
        description="",
        example=7977630,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_ds: Optional[str] = Field(
        None,
        alias="PKG_DS",
        name="",
        description="",
        example="23 OL DVISARO RO Room Only (82RQC)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-13T08:42:39.347000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-13T08:42:39.347000Z",
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
    pkg_chan_id: Optional[int] = Field(
        None,
        alias="PKG_CHAN_ID",
        name="",
        description="",
        example=102,
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
    prnt_chrg_mkt_pkg_id: Optional[int] = Field(
        None,
        alias="PRNT_CHRG_MKT_PKG_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioChrgMktPkgModel(BaseModel):
    """Payload class for DREAMSFolioChrgMktPkgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Market Package"
        stream_name = ""
        description = "Ties the PKG ID and Description to a Charge Market Package ID"  # optional
        unique_identifier = ["data.CHRG_MKT_PKG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CHRG_MKT_PKG"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
