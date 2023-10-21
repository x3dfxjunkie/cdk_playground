"""Source Data Contract for Dreams TP PTY"""

from __future__ import annotations
from enum import Enum
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTpId,
    GlobalDreamsData,
    GlobalDreamsTransactCommitTimestamp,
    GlobalDreamsMetadata,
)


class IdvlPtyIn(Enum):
    Y = "Y"
    N = "N"


class PrmyPtyIn(Enum):
    Y = "Y"
    N = "N"


class Data(GlobalDreamsTpId, GlobalDreamsData, GlobalDreamsTransactCommitTimestamp):
    """Class for Dreams TP PTY Data"""

    txn_pty_id: int = Field(
        ...,
        alias="TXN_PTY_ID",
        name="Transaction Party Identification",
        description="The unique identification of the transactional party (individual/organization) associated to this travel plan. Transaction party information is persisted in the Guest Domain.",
        example=737139124,
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="indirect",
    )
    idvl_pty_in: str = Field(
        ...,
        alias="IDVL_PTY_IN",
        name="Transaction Party Indicator",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prmy_pty_in: str = Field(
        ...,
        alias="PRMY_PTY_IN",
        name="Primary Party Indicator",
        description="Identifies that an individual or organization has (Y) or has not (N) been designated as the primary party for a travel plan.  Default setting is N, the individual or organization is not the primary party for the travel plan.",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gst_fst_nm: str = Field(
        ...,
        alias="GST_FST_NM",
        name="Guest First Name",
        description="",
        example="Mickey",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    gst_lst_nm: str = Field(
        ...,
        alias="GST_LST_NM",
        name="",
        description="Guest Last Name",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )


class DREAMSDiningTpPtyModel(BaseModel):
    """Payload class for DREAMSDiningTpPtyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Party Party"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table provides all the guest IDs associated to their Travel Plan"  # optional
        unique_identifier = ["data.TP_ID", "data.TXN_PTY_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tp_pty"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
