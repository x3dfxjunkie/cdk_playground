""" Pipelines config networking model"""
from typing import Optional, List
from pydantic import BaseModel, Field


class Egress(BaseModel):
    cidrs: Optional[List[str]] = Field(
        None,
        alias="cidrs",
        name="",
        description="",
    )

    ports: List[int] = Field(
        ...,
        alias="ports",
        name="",
        description="",
    )


class LocalEgress(BaseModel):
    cidr: str = Field(
        ...,
        alias="cidr",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Ingress(BaseModel):
    cidrs: List[Optional[str]] = Field(
        list,
        alias="cidrs",
        name="",
        description="",
    )

    ports: List[Optional[int]] = Field(
        list,
        alias="ports",
        name="",
        description="",
    )


class Blocklist(BaseModel):
    ingress: Ingress = Field(
        ...,
        alias="ingress",
        name="",
        description="",
    )


class Allowlist(BaseModel):
    egress: Optional[Egress] = Field(
        None,
        alias="egress",
        name="",
        description="",
    )

    ingress: Optional[Ingress] = Field(
        None,
        alias="ingress",
        name="",
        description="",
    )

    local_egress: Optional[LocalEgress] = Field(
        None,
        alias="local_egress",
        name="",
        description="",
    )


class Networking(BaseModel):
    allowlist: Allowlist = Field(
        ...,
        alias="allowlist",
        name="",
        description="",
    )

    vpc_id: Optional[str] = Field(
        None,
        alias="vpc_id",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    is_default: Optional[bool] = Field(
        None,
        alias="is_default",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    blocklist: Optional[Blocklist] = Field(
        None,
        alias="blocklist",
        name="",
        description="",
    )
