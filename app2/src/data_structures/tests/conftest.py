"""Collection of fixtures used in test modules for data structures"""
import pytest


@pytest.fixture(scope="module")
def monkeypatch_module():
    mpatch = pytest.MonkeyPatch()
    yield mpatch
    mpatch.undo()


@pytest.fixture(scope="module", autouse=True)
def mock_os_env(monkeypatch_module):  # pylint: disable=redefined-outer-name
    monkeypatch_module.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch_module.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch_module.setenv("AWS_DEFAULT_REGION", "us-east-1")
