"""Source Data Contract Template for Entitlement Plan Guest"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Entitlement Plan Guest Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-17T13:48:04.105000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ENTITLTLEMEN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_pln_id: int = Field(
        ...,
        alias="ENTTL_PLN_ID",
        name="",
        description="",
        example=11111560,
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

    shr_enttl_in: str = Field(
        ...,
        alias="SHR_ENTTL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_idvl_pty_id: int = Field(
        ...,
        alias="TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=111111599,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsEnttlPlnGstTModel(BaseModel):
    """Payload class for DREAMSEntitlementsEnttlPlnGstTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Plan Guest"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.TXN_IDVL_PTY_ID", "data.ENTTL_PLN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ENTTL_PLN_GST_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
