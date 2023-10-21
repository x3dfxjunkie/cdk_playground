"""Source Data Contract Template for DREAMS Price - Key to the World Type"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - kttw_typ_t Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-10-09T12:44:27.207889Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: Optional[str] = Field(
        None,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="RM13399957",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kttw_ds: str = Field(
        ...,
        alias="KTTW_DS",
        name="",
        description="",
        example="LENGTH-OF-STAY TICKET MEDIA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kttw_shrt_ds: Optional[str] = Field(
        None,
        alias="KTTW_SHRT_DS",
        name="",
        description="",
        example="HOMEYMOON PKG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kttw_typ_id: int = Field(
        ...,
        alias="KTTW_TYP_ID",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-10-09T12:44:27.207889Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceKttwTypTModel(BaseModel):
    """Payload class for DREAMSPriceKttwTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """"""
        unique_identifier = ["data.KTTW_TYP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "KTTW_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
