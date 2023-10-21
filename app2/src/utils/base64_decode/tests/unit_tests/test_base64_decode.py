"""
Tests for Base64Decode
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument for testing fixtures
import base64
import logging
import sys

from app.src.utils.base64_decode import base64_decode

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class TestBase64Decode:
    """
    TestBase64Decode class for grouping all tests
    """

    test_string = "foo bar is awesome"
    encoder = "UTF-8"

    def test_decode_base64_encoded_obj_bad(self):
        base64_obj = base64.b64encode(bytes(self.test_string, self.encoder))
        base64_obj += bytes("baddata", self.encoder)
        logger.debug(f"{base64_obj=}")
        assert base64_decode.b64decode(base64_obj) != self.test_string

    def test_decode_base64_encoded_obj(self):
        base64_obj = base64.b64encode(bytes(self.test_string, self.encoder))
        assert base64_decode.b64decode(base64_obj) == self.test_string

    def test_decode_str_obj(self):
        base64_obj = self.test_string
        assert base64_decode.b64decode(base64_obj) == self.test_string

    def test_decode_str_bytes_obj(self):
        base64_obj = bytes(self.test_string, self.encoder)
        assert base64_decode.b64decode(base64_obj) == self.test_string
