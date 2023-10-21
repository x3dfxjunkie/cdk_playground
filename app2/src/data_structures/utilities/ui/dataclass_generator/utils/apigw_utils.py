"""This Module contains utilities to help with Lambda Functions"""
from __future__ import annotations
from urllib.parse import urlparse
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ApiGatewayRequestContext(BaseModel):
    """Request context for API Gateway Event"""

    resource_id: str = Field(..., alias="resourceId")
    resource_path: str = Field(..., alias="resourcePath")
    http_method: str = Field(..., alias="httpMethod")
    extended_request_id: str = Field(..., alias="extendedRequestId")
    request_time: str = Field(..., alias="requestTime")
    path: str
    account_id: str = Field(..., alias="accountId")
    protocol: str
    stage: str
    domain_prefix: str = Field(..., alias="domainPrefix")
    request_time_epoch: int = Field(..., alias="requestTimeEpoch")
    request_id: str = Field(..., alias="requestId")
    identity: Any
    domain_name: str = Field(..., alias="domainName")
    api_id: str = Field(..., alias="apiId")


def generate_api_gateway_url(api_gateway_request_context: ApiGatewayRequestContext) -> str:
    """Generates API Gateway URL"""
    return f"{api_gateway_request_context.domain_name}/{api_gateway_request_context.stage}/"


def add_prefix_to_path(url: str, prefix: str) -> str:
    """Adds prefix to url path"""
    parsed_url = urlparse(url)
    split_path = parsed_url.path.lstrip("/").split("/")
    if len(split_path) > 0:
        if split_path[0] == prefix:
            return url
    return parsed_url._replace(path=f"/{prefix}{parsed_url.path}").geturl()
