"""Source Data Contract Template for DISC_PLCY"""


from __future__ import annotations

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - DISC_PLCY Data"""

    chg_typ_nm: str = Field(
        ...,
        alias="CHG_TYP_NM",
        name="",
        description="",
        example="Discount",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T15:25:43.975560Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    disc_plcy_am: Optional[float] = Field(
        None,
        alias="DISC_PLCY_AM",
        name="",
        description="",
        example=0.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    disc_plcy_id: int = Field(
        ...,
        alias="DISC_PLCY_ID",
        name="",
        description="",
        example=1000001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    disc_plcy_pc: float = Field(
        ...,
        alias="DISC_PLCY_PC",
        name="",
        description="",
        example=0.1,
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

    plcy_id: int = Field(
        ...,
        alias="PLCY_ID",
        name="",
        description="",
        example=1000001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2006-10-18T15:25:43.975560Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceDiscPlcyTModel(BaseModel):
    """Payload class for DREAMSPriceDiscPlcyTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Discount Policy"
        stream_name = ""
        description = "Subset of policies that apply to products"  # optional
        unique_identifier = ["data.DISC_PLCY_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "DISC_PLCY_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
