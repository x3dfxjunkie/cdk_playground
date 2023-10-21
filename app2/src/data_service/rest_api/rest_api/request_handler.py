import json
import typing
from abc import ABC, abstractmethod


def rest_api_response(
    status_code: int = 200,
    is_base64_encoded: bool = False,
    headers: dict[str, str] = {
        "content-type": "application/json",
    },
    body: typing.Optional[list] = None,
) -> dict[str, typing.Any]:
    """Encapsulates AWS Lambda HTTP response structure."""
    return {
        "statusCode": status_code,
        "isBase64Encoded": is_base64_encoded,
        "headers": headers,
        "body": json.dumps(body, default=str) if body else "",
    }


class RestAPIRequestHandler(ABC):
    """Interface for Rest API request processors.  Dependencies should passed into implememtation constructor."""

    @abstractmethod
    def process(
        self,
    ) -> dict[str, typing.Any]:
        pass
