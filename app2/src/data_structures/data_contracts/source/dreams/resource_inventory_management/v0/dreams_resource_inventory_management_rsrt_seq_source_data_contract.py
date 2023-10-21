"""Source Data Contract Template for DREAMS Resource Inventory Management Resort Sequence"""


from __future__ import annotations

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2012-06-20T08:38:43.214000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_rack_ocpncy_pct: Optional[int] = Field(
        None,
        alias="END_RACK_OCPNCY_PCT",
        name="",
        description="",
        example=80,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_fac_id: Optional[int] = Field(
        None,
        alias="RSRT_FAC_ID",
        name="",
        description="",
        example=144943,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_seq_id: int = Field(
        ...,
        alias="RSRT_SEQ_ID",
        name="",
        description="",
        example=8533,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    seq_end_dt: Optional[datetime] = Field(
        None,
        alias="SEQ_END_DT",
        name="",
        description="",
        example="2015-01-21T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    seq_nm: str = Field(
        ...,
        alias="SEQ_NM",
        name="",
        description="",
        example="Fort Creekside 71-80",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    seq_strt_dt: datetime = Field(
        ...,
        alias="SEQ_STRT_DT",
        name="",
        description="",
        example="2012-06-21T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    seq_typ_nm: str = Field(
        ...,
        alias="SEQ_TYP_NM",
        name="",
        description="",
        example="ROOM_RACK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strt_rack_ocpncy_pct: Optional[int] = Field(
        None,
        alias="STRT_RACK_OCPNCY_PCT",
        name="",
        description="",
        example=71,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2015-01-21T15:08:28.181000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SCHNE004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrtSeqModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrtSeqModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resort Sequence"
        stream_name = ""
        description = """Resort Sequence IDs associated to Resort Facility IDs"""
        unique_identifier = ["data.RSRT_SEQ_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrt_seq"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
