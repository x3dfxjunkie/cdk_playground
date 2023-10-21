"""Source Data Contract Template for DREAMS Pricing Fee Data"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - Fee Data"""

    acct_rev_cls_id: int = Field(
        ...,
        alias="ACCT_REV_CLS_ID",
        name="",
        description="",
        example=380193,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T15:25:45.616560Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Initial Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fee_nm: str = Field(
        ...,
        alias="FEE_NM",
        name="",
        description="",
        example="Cancellation Fee",
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2006-10-18T15:25:45.616560Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="Initial Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFeeTModel(BaseModel):
    """Payload class for DREAMSPriceFeeTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Fee"
        stream_name = ""
        description = """Items for which Disney can charge that are not products.  The charges may be involuntary to the guest and are based on their lack of proper payment or early cancellation."""
        unique_identifier = ["data.FEE_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FEE_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
