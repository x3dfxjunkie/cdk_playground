"""pytest configurations"""

import fnmatch
import logging
import sys

import pytest

from unit_testing_utils.global_unit_test_utils import (
    get_data_contracts_model_names,
    get_model_class,
    get_model_sample,
)
from unit_testing_utils.unit_tests import (
    ContractsAgainstSampleTests,
    FieldSyntaxTests,
    RootModelTests,
)


def pytest_addoption(parser):
    parser.addoption("--model_name", action="store", default="*")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.getoption("model_name")
    if "model_name" in metafunc.fixturenames:
        model_names = [name for name in get_data_contracts_model_names() if fnmatch.fnmatch(name, option_value)]
        metafunc.parametrize("model_name", model_names, scope="module")


@pytest.fixture
def logger(model_name):
    logger_instance = logging.getLogger(f"{model_name}_test_logger")
    logger_instance.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stream_handler.setFormatter(formatter)
    logger_instance.addHandler(stream_handler)
    return logger_instance


@pytest.fixture
def sample(model_name):
    """Fixture for loading the sample to be tested."""
    sample_object = get_model_sample(model_name)
    return sample_object


@pytest.fixture
def contract_model(model_name):
    """Fixture for loading the contract model to be tested."""
    model_class = get_model_class(model_name)
    return model_class


@pytest.fixture
def field_syntax_tests(contract_model, logger):
    """Fixture for loading FieldSyntaxTests."""
    return FieldSyntaxTests(contract_model, logger)


@pytest.fixture
def contract_against_sample_tests(sample, contract_model, logger):
    """Fixture for loading ContractsAgainstSampleTests."""
    return ContractsAgainstSampleTests(contract_model, sample, logger)


@pytest.fixture
def root_model_tests(contract_model, logger):
    """Fixture for loading RootModelTests."""
    return RootModelTests(contract_model, logger)
