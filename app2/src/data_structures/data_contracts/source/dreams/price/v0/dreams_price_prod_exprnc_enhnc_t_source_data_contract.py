"""Source Data Contract Template for DREAMS Price - Product Experience Enhancement data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - prod_exprnc_enhnc_t Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2019-03-04T16:33:33.820059Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_enhnc_nm: str = Field(
        ...,
        alias="EXPRNC_ENHNC_NM",
        name="",
        description="",
        example="DTR",
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

    prod_exprnc_enhnc_id: int = Field(
        ...,
        alias="PROD_EXPRNC_ENHNC_ID",
        name="",
        description="",
        example=246314,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=5293453,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2019-03-04T16:33:33.820059Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdExprncEnhncTModel(BaseModel):
    """Payload class for DREAMSPriceProdExprncEnhncTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Implemented initially as a Product, the Bypass Front Desk experience enhancement identifies which products (packages and in future component products perhaps) qualify for this process enhancement."""
        unique_identifier = ["data.PROD_EXPRNC_ENHNC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PROD_EXPRNC_ENHNC_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
