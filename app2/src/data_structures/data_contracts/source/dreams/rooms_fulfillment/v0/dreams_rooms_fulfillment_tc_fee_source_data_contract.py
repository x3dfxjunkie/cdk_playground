"""Source Data Contract for Dreams - Room Fulfillment Travel Component Fee"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Fulfillment Travel Component Fee data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-10-28T13:07:18.504000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="TIMLP001",
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

    tc_fee_id: int = Field(
        ...,
        alias="TC_FEE_ID",
        name="",
        description="",
        example=7416408,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_fee_ovrd_in: str = Field(
        ...,
        alias="TC_FEE_OVRD_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_fee_typ_nm: str = Field(
        ...,
        alias="TC_FEE_TYP_NM",
        name="",
        description="",
        example="Cancel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_id: int = Field(
        ...,
        alias="TC_ID",
        name="",
        description="",
        example=329791489,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-10-28T13:07:18.504000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="TIMLP001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentTcFeeModel(BaseModel):
    """Payload class for Dreams - Room Fulfillment Travel Component Fee Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Fee"
        stream_name = ""
        description = "There are fees associated to certain types of components that indicate that a fee was one of these types:, Exchange, Cancel"
        unique_identifier = ["data.TC_FEE_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tc_fee"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
