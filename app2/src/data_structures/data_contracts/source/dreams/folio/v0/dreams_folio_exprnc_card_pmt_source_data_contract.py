"""Source Data Contract Template for DREAMS Folio Experience Card Payment"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Experience Card Payment Data"""

    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=194846235,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meal_prd_nm: Optional[str] = Field(
        None,
        alias="MEAL_PRD_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cpn_tndr_cd: Optional[str] = Field(
        None,
        alias="CPN_TNDR_CD",
        name="",
        description="",
        example="39",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gst_cn: Optional[int] = Field(
        None,
        alias="GST_CN",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="CHINR029",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2015-12-19T02:18:07.813Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="CHINR029",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2015-12-19T02:18:07.813Z",
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
    sld_id_vl: Optional[str] = Field(
        None,
        alias="SLD_ID_VL",
        name="",
        description="",
        example="0441",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    crdt_doc_nb: Optional[int] = Field(
        None,
        alias="CRDT_DOC_NB",
        name="",
        description="",
        example=1027079972,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ffl_fac_id: Optional[str] = Field(
        None,
        alias="FFL_FAC_ID",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2015-12-19T02:18:07.813Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioExprncCardPmtModel(BaseModel):
    """Payload class for DREAMSFolioExprncCardPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Experience Card Payment"
        stream_name = ""
        description = """This table holds Payments that were made by Resort guests at various POS/Dining and that payment becomes a charge the guest is responsible for on their Folio/Bill/Tab that shows what is being processed on the credit card the guest has on file as a settlement method"""
        unique_identifier = ["data.PMT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "EXPRNC_CARD_PMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
