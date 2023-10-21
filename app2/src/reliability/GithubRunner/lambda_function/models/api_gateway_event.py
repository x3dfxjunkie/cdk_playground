"""
    ApiGatewayEvent from Event
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from dataclasses_json import DataClassJsonMixin, config


@dataclass
class ApiGatewayEvent(DataClassJsonMixin):
    """
    This dataclass contains an API Gateway Event to promote strong typing
    """

    resource: str
    path: str
    http_method: str = field(metadata=config(field_name="httpMethod"))
    headers: Optional[Dict[str, str]]
    multi_value_headers: Optional[Dict[str, List[Any]]] = field(metadata=config(field_name="multiValueHeaders"))
    query_string_parameters: Any = field(metadata=config(field_name="queryStringParameters"))
    multi_value_query_string_parameters: Any = field(metadata=config(field_name="multiValueQueryStringParameters"))
    path_parameters: Any = field(metadata=config(field_name="pathParameters"))
    stage_variables: Any = field(metadata=config(field_name="stageVariables"))
    request_context: Optional[Dict[str, Any]] = field(metadata=config(field_name="requestContext"))
    body: str
    is_base_64_encoded: bool = field(metadata=config(field_name="isBase64Encoded"))
