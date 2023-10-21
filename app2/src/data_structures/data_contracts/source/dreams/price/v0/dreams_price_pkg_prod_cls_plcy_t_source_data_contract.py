"""Source Data Contract Template for DREAMS Price - Package Product Class Policy"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - PKG_PROD_CLS_PLCY_T Data"""

    pkg_prod_cls_id: int = Field(
        ...,
        alias="PKG_PROD_CLS_ID",
        name="",
        description="",
        example=189393,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_plcy_id: int = Field(
        ...,
        alias="PKG_PROD_CLS_PLCY_ID",
        name="",
        description="",
        example=9537,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_plcy_strt_dt: datetime = Field(
        ...,
        alias="PKG_PROD_CLS_PLCY_STRT_DT",
        name="",
        description="",
        example="2009-04-21T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plcy_id: int = Field(
        ...,
        alias="PLCY_ID",
        name="",
        description="",
        example=1000009,
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


class DREAMSPricePkgProdClsPlcyTModel(BaseModel):
    """Payload class for DREAMSPricePkgProdClsPlcyTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """The association of a Package Product Classification to a Policy."""
        unique_identifier = ["data.PKG_PROD_CLS_PLCY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PKG_PROD_CLS_PLCY_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
