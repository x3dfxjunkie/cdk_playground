"""Source Data Contract Template for DREAMs Dining Reservation Management Request"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMs Dining Reservation Management Request"""

    cfdntl_in: str = Field(
        ...,
        alias="CFDNTL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmt_req_typ_nm: Optional[str] = Field(
        None,
        alias="CMT_REQ_TYP_NM",
        name="",
        description="",
        example="Internal",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-13T16:26:14.285000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="JOHNM581",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gsr_in: str = Field(
        ...,
        alias="GSR_IN",
        name="",
        description="",
        example="N",
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

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    req_inactv_dts: Optional[datetime] = Field(
        None,
        alias="REQ_INACTV_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_mgmt_prfl_id: Optional[int] = Field(
        None,
        alias="RES_MGMT_PRFL_ID",
        name="",
        description="",
        example=827,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_mgmt_req_id: int = Field(
        ...,
        alias="RES_MGMT_REQ_ID",
        name="",
        description="",
        example=30313337889,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_mgmt_req_tx: str = Field(
        ...,
        alias="RES_MGMT_REQ_TX",
        name="",
        description="",
        example="Guest specifically wants a female to do the make-over.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_mgmt_req_tx_1: Optional[str] = Field(
        None,
        alias="RES_MGMT_REQ_TX_1",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_mgmt_req_typ_nm: str = Field(
        ...,
        alias="RES_MGMT_REQ_TYP_NM",
        name="",
        description="",
        example="TravelPlanSegmentComment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_id: Optional[int] = Field(
        None,
        alias="TC_ID",
        name="",
        description="",
        example=33333333296,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tps_id: Optional[int] = Field(
        None,
        alias="TPS_ID",
        name="",
        description="",
        example=111111115135,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tp_id: int = Field(
        ...,
        alias="TP_ID",
        name="",
        description="",
        example=555555555581,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-13T16:26:14.285000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="JOHNM581",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningResMgmtReqModel(BaseModel):
    """Payload class for DREAMSDiningResMgmtReqModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Management Request"
        stream_name = ""
        description = """This table has the Free form fields cast members use to put notes on a reservation. It also has profile IDs that also provide information to the guest. IE: Check in is at 3pm
        It also has coded comments that assist in assigning a room to a travel party."""
        unique_identifier = ["data.RES_MGMT_REQ_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "res_mgmt_req"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
