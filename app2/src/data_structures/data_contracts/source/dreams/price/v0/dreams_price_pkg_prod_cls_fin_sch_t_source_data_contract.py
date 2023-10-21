"""Source Data Contract Template for DREAMS Price - Package Product Class Finance Schedule"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - PKG_PROD_CLS_FIN_SCH_T Data"""

    fin_sch_id: int = Field(
        ...,
        alias="FIN_SCH_ID",
        name="",
        description="",
        example=6335,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_prod_cls_id: int = Field(
        ...,
        alias="PKG_PROD_CLS_ID",
        name="",
        description="",
        example=2631037,
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


class DREAMSPricePkgProdClsFinSchTModel(BaseModel):
    """Payload class for DREAMSPricePkgProdClsFinSchTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = (
            """The set of associations that exist between a Package Product Classification and a Deposit Schedule."""
        )
        unique_identifier = ["data.PKG_PROD_CLS_ID", "data.FIN_SCH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PKG_PROD_CLS_FIN_SCH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
