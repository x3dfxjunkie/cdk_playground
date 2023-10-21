"""DPI WEST Global dataclass: for key fields and classes that will be repeated throughout DPI WEST only"""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

"""Dataclasses that need references to this will need to import the global_dpi_west_source_data_contract.py file"""


class GlobalDPIWESTSchemaName(Enum):
    """Global DPI WEST schema name"""

    AWAKENING = "dlr_photopass"


class GlobalDPIWESTTableName(Enum):
    """Global DPI WEST list of tables"""

    ASSOCIATIONS = "associations"
    ASSOCIATIONS_MSG = "associations_msg"
    MEDIA = "media"
    MEDIADOWNLOADS = "mediadownloads"
    META_ASSET = "meta_asset"
    META_ASSETCACHE = "meta_assetcache"
    META_ASSETCATEGORY = "meta_assetcategory"
    META_ASSETLOCATION = "meta_assetlocation"
    META_ASSETRENDITION = "meta_assetrendition"
    META_ASSETSUBJECT = "meta_assetsubject"
    META_CAMPUS = "meta_campus"
    META_CATEGORY = "meta_category"
    META_DEPLOYMENTGROUP = "meta_deploymentgroup"
    META_DEPLOYMENTGROUPLOCATION = "meta_deploymentgrouplocation"
    META_LOCATION = "meta_location"
    META_MODERATOR = "meta_moderator"
    META_OPERATOR = "meta_operator"
    META_PHOTOPASSSTOCK = "meta_photopassstock"
    META_SPORTSDIVISION = "meta_sportsdivision"
    META_SPORTSEVENT = "meta_sportsevent"
    META_SPORTSPHOTOPASS = "meta_sportsphotopass"
    META_SPORTSTEAM = "meta_sportsteam"
    META_SUBJECT = "meta_subject"
    META_VENUE = "meta_venue"
    META_VENUEGROUP = "meta_venuegroup"
    META_VIDEOARTCARD = "meta_videoartcard"
    META_VIDEOCLIP = "meta_videoclip"
    META_VIDEOTEMPLATE = "meta_videotemplate"
    SUBJECTS = "subjects"


class GlobalDPIWESTOperation(Enum):
    """DPI WEST Data Operation type"""

    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"
    LOAD = "load"


class GlobalDPIWESTMetadata(BaseModel):
    """Global DPI WEST Metadata Class Data"""

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="Record Timestamp",
        description="",
        example="2023-04-17T13:33:15.230Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    record_type: str = Field(
        ...,
        alias="record-type",
        name="Record Type",
        description="Record Type",
        example="data",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    operation: GlobalDPIWESTOperation = Field(
        ...,
        alias="operation",
        name="Operation",
        description="Specifies record operation as Insert or Update",
        example="Update",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="Partition Key Type",
        description="Partition Key Type",
        example="schema-table",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    schema_name: GlobalDPIWESTSchemaName = Field(
        ...,
        alias="schema-name",
        name="Schema Name",
        description="Database schema name storing the record",
        example="awakening",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    table_name: GlobalDPIWESTTableName = Field(
        ...,
        alias="table-name",
        name="Table Name",
        description="Database table name storing the record",
        example="associations_msg",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
