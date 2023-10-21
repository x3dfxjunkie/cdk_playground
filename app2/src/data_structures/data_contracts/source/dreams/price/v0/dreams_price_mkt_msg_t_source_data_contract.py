"""Source Data Contract Template for DREAMS Price - Marketing Message"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - mkt_msg_t Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-16T18:53:23.061778Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_mkt_msg_id: int = Field(
        ...,
        alias="ENTRPRS_MKT_MSG_ID",
        name="",
        description="",
        example=403652,
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

    mkt_msg_id: int = Field(
        ...,
        alias="MKT_MSG_ID",
        name="",
        description="",
        example=496,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mkt_msg_site_nm: Optional[str] = Field(
        None,
        alias="MKT_MSG_SITE_NM",
        name="",
        description="",
        example="Additional Integrations",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mkt_msg_tx: str = Field(
        ...,
        alias="MKT_MSG_TX",
        name="",
        description="",
        example="<p>Kosher Meals and Celebration Cakes Available&#160;contacting the Location at least 4 days in advance.</p>",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-09-16T18:53:23.061778Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceMktMsgTModel(BaseModel):
    """Payload class for DREAMSPriceMktMsgTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Documents the specific marketing messages associated to a policy."""
        unique_identifier = ["data.MKT_MSG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "MKT_MSG_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
