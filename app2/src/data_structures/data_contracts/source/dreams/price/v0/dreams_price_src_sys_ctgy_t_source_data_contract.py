"""Source Data Contract Template for DREAMS Pricing Source System Category Type"""


from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - SRC_SYS_CTGY_T Data"""

    src_sys_ctgy_nm: str = Field(
        ...,
        alias="SRC_SYS_CTGY_NM",
        name="",
        description="",
        example="Activity Type",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    src_sys_ctgy_proc_typ_nm: str = Field(
        ...,
        alias="SRC_SYS_CTGY_PROC_TYP_NM",
        name="",
        description="",
        example="ProductClassification",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceSrcSysCtgyTModel(BaseModel):
    """Payload class for DREAMSPriceSrcSysCtgyTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """A product classifications type (Category Admin in One Source)  that we receive and process from One Source.  This configuration entity serves to distinguish the values fed from this generic domain lookup entity and determine how each should be processed within PRODUCT PRICING. (This configuration table eliminates a process that was previously hard-coded in the pricing code)."""
        unique_identifier = ["data.SRC_SYS_CTGY_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SRC_SYS_CTGY_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
