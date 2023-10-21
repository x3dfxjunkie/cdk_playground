"""Source Data Contract Template for DREAMS Price - Product Policy data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - prod_plcy_t Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-04T16:16:48.130326Z",
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
        example=40246,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-25T20:35:22.703832Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=73135,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_plcy_end_dt: Optional[datetime] = Field(
        None,
        alias="PROD_PLCY_END_DT",
        name="",
        description="",
        example="2020-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_plcy_strt_dt: datetime = Field(
        ...,
        alias="PROD_PLCY_STRT_DT",
        name="",
        description="",
        example="2009-09-04T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-09-04T16:16:48.130326Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdPlcyTModel(BaseModel):
    """Payload class for DREAMSPriceProdPlcyTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Product Policy"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.PROD_ID", "data.PLCY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PROD_PLCY_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
