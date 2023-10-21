"""Source Data Contract for Dreams - Room Fulfillment Travel Plan Segment Party Locator"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Fulfillment Travel Plan Segment Party Locator data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-18T12:02:41Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MASKED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    idvl_fst_nm: str = Field(
        ...,
        alias="IDVL_FST_NM",
        name="",
        description="",
        example="VTfmyhDDZBmA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    idvl_lst_nm: str = Field(
        ...,
        alias="IDVL_LST_NM",
        name="",
        description="",
        example="sIWecYoBUrKL",
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

    lctr_typ_nm: str = Field(
        ...,
        alias="LCTR_TYP_NM",
        name="",
        description="",
        example="Address",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tps_id: int = Field(
        ...,
        alias="TPS_ID",
        name="",
        description="",
        example=392618430789,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_pty_lctr_id: int = Field(
        ...,
        alias="TXN_PTY_LCTR_ID",
        name="",
        description="",
        example=49656251,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_pty_lctr_vl: str = Field(
        ...,
        alias="TXN_PTY_LCTR_VL",
        name="",
        description="",
        example="97051-2011",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2020-04-08T21:12:50.025457Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MASKED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentTpsPtyLctrModel(BaseModel):
    """Payload class for Dreams - Room Fulfillment Travel Plan Segment Party Locator Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan Segment Party Locator"
        stream_name = ""
        description = "This table ties the guest/travel agency on a reservation to a locator type by last name, first name and transactional party ID., Address, Email, Phone"
        unique_identifier = ["data.TPS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tps_pty_lctr"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
