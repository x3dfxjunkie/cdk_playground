"""
pytest fixtures and functions
"""
import importlib
import logging
import os
import pathlib
import sys

import pytest

logger = logging.getLogger(__name__)


def pytest_collection_modifyitems(config, items):
    """
    pytest add markers dynamically based on directory name
    <directoryname>_tests
    """
    # python 3.4/3.5 compat: rootdir = pathlib.Path(str(config.rootdir))
    rootdir = pathlib.Path(config.rootdir)
    for item in items:
        relPath = pathlib.Path(item.fspath).relative_to(rootdir)
        for part in relPath.parts:
            if part.endswith("_tests"):
                mark = getattr(pytest.mark, part)
                item.add_marker(mark)


def pytest_configure(config):
    """
    pytest register markers
    """
    config.addinivalue_line("markers", "unit_tests: unit tests for code coverage")
    config.addinivalue_line(
        "markers", "integration_tests: integration tests for validation in environments"
    )


def pytest_generate_tests(metafunc):
    """
    If fixture begins with data_ add a parametrize fixture
    """
    for fixture in metafunc.fixturenames:
        if "data_" in fixture:
            logger.debug("getting fixture=%s", fixture)
            metafunc.parametrize(fixture, loadTests(fixture))


def loadTests(name):
    """
    loads test data dynamically utilizing data_<name>.py in tests/data directory
    """
    # Load module which contains test data
    sys.path.append(os.path.join(os.path.dirname(__file__)))
    testsModule = importlib.import_module(f".{name}", "data")
    # Tests are to be found in the variable  of the module
    for test in testsModule.tests:
        yield test
