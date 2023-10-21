"""CTAM HTTP CLIENT"""
import urllib3
import logging

CONNECTION_TIMEOUT_SECS = 30
READ_TIMEOUT_SECS = 600

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


class CTAMResponse:
    """_summary_"""

    def __init__(self, status_code: int, response: str, error_reason: str):
        self.status_code = status_code
        self.response = response
        self.error_reason = error_reason


class HttpsClient:
    """_summary_"""

    def __init__(self):
        timeout = urllib3.Timeout(connect=CONNECTION_TIMEOUT_SECS, read=READ_TIMEOUT_SECS)
        self.https_client = urllib3.PoolManager(timeout=timeout)
        self.authorization_header = {}

    def rest_get(self, request_uri: str) -> CTAMResponse:
        headers = {"Accept-Encoding": "gzip", "Content-Type": "application/json"}
        LOGGER.info(request_uri)
        resp = self.https_client.request(method="GET", url=request_uri, headers=headers)
        LOGGER.info(resp.data)
        return CTAMResponse(status_code=resp.status, response=resp.data.decode("utf-8"), error_reason=resp.reason)

    def rest_post(self, request_uri: str, post_data: str) -> CTAMResponse:
        headers = {**self.authorization_header, "Accept-Encoding": "gzip", "Content-Type": "application/json"}
        resp = self.https_client.request(method="POST", url=request_uri, headers=headers, body=post_data)
        return CTAMResponse(status_code=resp.status, response=resp.data.decode("utf-8"), error_reason=resp.reason)

    def rest_patch(self, request_uri: str, patch_data: str) -> CTAMResponse:
        headers = {**self.authorization_header, "Accept-Encoding": "gzip", "Content-Type": "application/json"}
        resp = self.https_client.request(method="PATCH", url=request_uri, headers=headers, body=patch_data)
        return CTAMResponse(status_code=resp.status, response=resp.data.decode("utf-8"), error_reason=resp.reason)

    def rest_put(self, request_uri: str, put_data: str) -> CTAMResponse:
        headers = {**self.authorization_header, "Content-Type": "text/csv"}
        resp = self.https_client.request(method="PUT", url=request_uri, headers=headers, body=put_data)
        return CTAMResponse(status_code=resp.status, response=resp.data.decode("utf-8"), error_reason=resp.reason)

    def rest_delete(self, request_uri: str) -> CTAMResponse:
        resp = self.https_client.request(method="DELETE", url=request_uri, headers=self.authorization_header)
        return CTAMResponse(status_code=resp.status, response=resp.data.decode("utf-8"), error_reason=resp.reason)
