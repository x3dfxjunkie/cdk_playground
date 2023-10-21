"""Source Data Contract for Dreams TC RSN"""

from __future__ import annotations
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class for Dreams TC RSN Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-13T22:38:21Z",
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

    prdf_tc_rsn_id: int = Field(
        ...,
        alias="PRDF_TC_RSN_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_id: int = Field(
        ...,
        alias="TC_ID",
        name="",
        description="",
        example=11111118432,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_cntct_nm: Optional[str] = Field(
        None,
        alias="TC_RSN_CNTCT_NM",
        name="",
        description="",
        example="Mickey ,Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_id: int = Field(
        ...,
        alias="TC_RSN_ID",
        name="",
        description="",
        example=11111118695,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_tx: Optional[str] = Field(
        None,
        alias="TC_RSN_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_typ_nm: str = Field(
        ...,
        alias="TC_RSN_TYP_NM",
        name="",
        description="",
        example="Cancel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-13T22:38:21Z",
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


class DREAMSDiningTcRsnModel(BaseModel):
    """Payload class for DREAMSDiningTcRsnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Reason"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table provides the reason for certain actions associated to a travel component. It also has the FK for the Preferred Travel Component Reason"  # optional
        unique_identifier = ["data.TC_RSN_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tc_rsn"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
