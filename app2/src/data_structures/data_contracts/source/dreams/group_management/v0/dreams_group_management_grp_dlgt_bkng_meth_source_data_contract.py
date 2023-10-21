"""Source Data Contract for DREAMS Group Management Group Delegate Booking Method"""


from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Group Management Group Delegate Booking Method Data"""

    grp_dlgt_bkng_meth_nm: str = Field(
        ...,
        alias="GRP_DLGT_BKNG_METH_NM",
        name="",
        description="",
        example="3rd Party Rooming List",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGrpDlgtBkngMethModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpDlgtBkngMethModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Group Management Group Delegate Booking Method"
        stream_name = ""
        description = "Domain"
        unique_identifier = ["data.GRP_DLGT_BKNG_METH_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_dlgt_bkng_meth"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
