"""Source Data Contract Template for FFLMT_SHIPMT"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from datetime import datetime
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS FFLMT_SHIPMT Data
    """

    fflmt_shipmt_id: int = Field(
        ...,
        alias="FFLMT_SHIPMT_ID",
        name="",
        description="",
        example=523250,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_band_ord_id: int = Field(
        ...,
        alias="EXPRNC_BAND_ORD_ID",
        name="",
        description="",
        example=549751,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    addr_id: int = Field(
        ...,
        alias="ADDR_ID",
        name="",
        description="",
        example=725700,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ship_carrier_id: int = Field(
        ...,
        alias="SHIP_CARRIER_ID",
        name="",
        description="",
        example=10006,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ship_srvc_id: int = Field(
        ...,
        alias="SHIP_SRVC_ID",
        name="",
        description="",
        example=10010,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_band_ord_actl_ship_dt: datetime = Field(
        ...,
        alias="EXPRNC_BAND_ORD_ACTL_SHIP_DT",
        name="",
        description="",
        example="2012-02-20T18:30:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_band_ord_carrier_trk_nb: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_ORD_CARRIER_TRK_NB",
        name="",
        description="",
        example="BulkCards2212013",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_band_ord_fflmt_ship_nb: str = Field(
        ...,
        alias="EXPRNC_BAND_ORD_FFLMT_SHIP_NB",
        name="",
        description="",
        example="221201300000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="XBANDAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2014-09-08T15:51:13.400Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="XBANDAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2016-10-20T22:30:13.891Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    logical_del_in: str = Field(
        ...,
        alias="LOGICAL_DEL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_updt_sts_id: Optional[str] = Field(
        None,
        alias="SAP_UPDT_STS_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mtrl_doc_nb: Optional[str] = Field(
        None,
        alias="MTRL_DOC_NB",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fflmt_rprt_file_nm: Optional[str] = Field(
        None,
        alias="FFLMT_RPRT_FILE_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="",
        example="1977-06-20 20:53:18",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    record_type: str = Field(
        ...,
        alias="record-type",
        name="",
        description="",
        example="data",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operation: str = Field(
        ...,
        alias="operation",
        name="",
        description="",
        example="Insert",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="",
        description="",
        example="schema-table",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    schema_name: str = Field(
        ...,
        alias="schema-name",
        name="",
        description="",
        example="XBANDMD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="",
        example="BUILD_BAND_SKU_ACTVY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="",
        example=886,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_record_id: Optional[int] = Field(
        None,
        alias="transaction_record_id",
        name="",
        description="",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prev_transaction_id: Optional[int] = Field(
        None,
        alias="prev_transaction_id",
        name="",
        description="",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prev_transaction_record_id: Optional[int] = Field(
        None,
        alias="prev_transaction_record_id",
        name="",
        description="",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    commit_timestamp: Optional[datetime] = Field(
        None,
        alias="commit_timestamp",
        name="",
        description="",
        example="2023-03-29T15:30:19.109655Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    stream_position: Optional[str] = Field(
        None,
        alias="stream_position",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWFflmtShipmtModel(BaseModel):
    """
    Payload class for XBMS FFLMT_SHIPMT
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = ""  # optional
        unique_identifier = ["data.FFLMT_SHIPMT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "FFLMT_SHIPMT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
