"""Source Data Contract Template for DREAMS Price - Finance Schedule"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - fin_sch_t Data"""

    chg_typ_nm: Optional[str] = Field(
        None,
        alias="CHG_TYP_NM",
        name="",
        description="",
        example="Deposit Requirement",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: Optional[datetime] = Field(
        None,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2007-04-11T16:26:41.688744Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_meth_nm: str = Field(
        ...,
        alias="ENTTL_METH_NM",
        name="",
        description="",
        example="Per Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fee_nm: Optional[str] = Field(
        None,
        alias="FEE_NM",
        name="",
        description="",
        example="Cancellation Fee",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fin_sch_id: int = Field(
        ...,
        alias="FIN_SCH_ID",
        name="",
        description="",
        example=143,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plcy_id: int = Field(
        ...,
        alias="PLCY_ID",
        name="",
        description="",
        example=117201,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_frm_am: Optional[int] = Field(
        None,
        alias="SCH_FRM_AM",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_meth_nm: str = Field(
        ...,
        alias="SCH_METH_NM",
        name="",
        description="",
        example="Prior To Arrival",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_to_am: Optional[int] = Field(
        None,
        alias="SCH_TO_AM",
        name="",
        description="",
        example=15,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_typ_nm: str = Field(
        ...,
        alias="SCH_TYP_NM",
        name="",
        description="",
        example="CancellationFlatAmountRule",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_unt_cn: Optional[int] = Field(
        None,
        alias="SCH_UNT_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_vl: float = Field(
        ...,
        alias="SCH_VL",
        name="",
        description="",
        example=100.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_vl_typ_nm: str = Field(
        ...,
        alias="SCH_VL_TYP_NM",
        name="",
        description="",
        example="N/A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    uom_typ_nm: str = Field(
        ...,
        alias="UOM_TYP_NM",
        name="",
        description="",
        example="Day",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: Optional[datetime] = Field(
        None,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2007-04-11T16:26:41.688744Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFinSchTModel(BaseModel):
    """Payload class for DREAMSPriceFinSchTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Financial Schedule"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.FIN_SCH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FIN_SCH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
