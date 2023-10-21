"""Source Data Contract Template for DREAMS Pricing Schedule Type data"""


from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - SCH_TYP_T"""

    entrprs_sch_typ_id: int = Field(
        ...,
        alias="ENTRPRS_SCH_TYP_ID",
        name="",
        description="",
        example=80000425,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_typ_nm: str = Field(
        ...,
        alias="SCH_TYP_NM",
        name="",
        description="",
        example="Closed",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceSchTypTModel(BaseModel):
    """Payload class for DREAMSPriceSchTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Documents the sub-schedules as found in One Source.  These really are subtypes of the different schedules that may exist for a Facility."""
        unique_identifier = ["data.SCH_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SCH_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
