"""Source Data Contract Template for Dreams - Dining Resort Guest Booking Window Options"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Dining Resort Guest Booking Window Options Data"""

    actv_in: str = Field(
        ...,
        alias="ACTV_IN",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    avail_lvl_used: int = Field(
        ...,
        alias="AVAIL_LVL_USED",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2022-12-13T06:02:15Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dng_res_cncld: str = Field(
        ...,
        alias="DNG_RES_CNCLD",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gst_id: str = Field(
        ...,
        alias="GST_ID",
        name="",
        description="",
        example="111113351",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_gst_bkng_wndw_opt_id: int = Field(
        ...,
        alias="RSRT_GST_BKNG_WNDW_OPT_ID",
        name="",
        description="",
        example=163237,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_res_cncld: str = Field(
        ...,
        alias="RSRT_RES_CNCLD",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_res_nb: int = Field(
        ...,
        alias="RSRT_RES_NB",
        name="",
        description="",
        example=111116931669,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    src_acct_ctr_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tps_id: int = Field(
        ...,
        alias="TPS_ID",
        name="",
        description="",
        example=111117580306,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2022-12-13T06:02:15Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="jdo_seq_nb",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningRsrtGstBkngWndwOptModel(BaseModel):
    """Payload class for Dreams - Dining Resort Guest Booking Window Options Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Guest Booking Window Options"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRT_GST_BKNG_WNDW_OPT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrt_gst_bkng_wndw_opt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
