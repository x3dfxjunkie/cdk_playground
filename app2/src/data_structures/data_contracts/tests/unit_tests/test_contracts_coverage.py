"""Set of tests to check if all data contracts are being properly tested."""

import fnmatch
import importlib.util
import inspect
import logging
import os
import re
import sys
from typing import List
from pydantic import BaseModel
import pytest

from unit_testing_utils.global_unit_test_utils import get_data_contracts_model_names


class TestContractsCoverage:
    """Test data contracts coverage."""

    test_file_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    bazel_build_file = f"{test_file_dir}/BUILD.bazel"
    contracts_folder = "app/src/data_structures/data_contracts/source"

    @pytest.fixture
    def logger(self):
        logger_instance = logging.getLogger(f"contracts_coverage_test_logger")
        logger_instance.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        stream_handler.setFormatter(formatter)
        logger_instance.addHandler(stream_handler)
        return logger_instance

    # To cache and reuse the results
    @pytest.fixture(scope="module")
    def data_contracts(self) -> List[str]:
        """Fixture for loading data contracts root names."""
        data_contracts = []
        module_tuples = [
            (root, file_name)
            for root, _, files in os.walk(self.contracts_folder)
            for file_name in files
            if file_name.endswith(".py")
        ]
        for root, file_name in module_tuples:
            module_path = os.path.join(root, file_name)
            module_name = os.path.splitext(file_name)[0]
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, BaseModel) and hasattr(obj.Config(), "stream_name"):
                    data_contracts.append(name)
        return data_contracts

    @pytest.fixture(scope="module")
    def json_mappings(self) -> List:
        """Fixture for loading data contracts root names in mapping files."""
        return get_data_contracts_model_names()

    @pytest.fixture
    def bazel_mappings(self) -> List:
        """Fixture for loading all the contract unit tests present in the BUILD.bazel file."""
        with open(self.bazel_build_file, "r", encoding="utf-8") as build_file:
            build_file_content = build_file.read()
        contract_unit_tests_pattern = re.compile(
            r'contracts_unit_tests\(\s*name\s*=\s*"(?P<name>[^"]+)",\s*args\s*=\s*\[(?P<args>[^\]]+)\],\s*\)'
        )
        results = []
        for match in contract_unit_tests_pattern.finditer(build_file_content):
            args_list = match.group("args")
            pattern = [arg.strip() for arg in args_list.split(" ")][1][:-1]
            results.append(pattern)
        return results

    def test_mappings_data_contract_coverage(self, data_contracts, json_mappings):
        """Test mappings coverage."""
        result_list = [x for x in data_contracts if x not in json_mappings]
        assert not result_list, f"the following data contracts are not listed in the json mappings: {result_list}"

    def test_bazel_data_contract_coverage(self, data_contracts, bazel_mappings):
        """Test bazel coverage."""
        matched_strings = set()
        for pattern in bazel_mappings:
            matched_subset = {
                contract_name for contract_name in data_contracts if fnmatch.fnmatch(contract_name, pattern)
            }
            matched_strings = matched_strings.union(matched_subset)
        result_set = set(data_contracts).difference(matched_strings)
        assert not result_set, f"the following data contract are not being included in bazel: {result_set}"
