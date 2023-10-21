"""Script to write base unit testing"""

import black
from jinja2 import Template
from pathlib import Path
from app.src.data_structures.data_contracts.tests.unit_testing_utils.global_unit_test_utils import (
    get_data_contracts_info,
    get_test_dev_path,
)


class UnitTestWriter:
    """Class to write unit tests for data contracts."""

    utils_path = Path(__file__).parent
    template_path = utils_path / "unit_test_template.j2"

    def __init__(self, model_name, template_path=template_path):
        self.model_name = model_name
        self.data_contract_mapping = get_data_contracts_info()
        self.template_path = template_path
        self.template = self._load_template()

    def _load_template(self):
        with open(self.template_path, encoding="utf-8") as f:
            return Template(f.read())

    def _render_unit_test(self, render_sample_tests):
        rendered_test = self.template.render(
            model_name=self.model_name,
            exec_sample_tests=render_sample_tests,
        )
        return rendered_test

    def write_unit_test(self, render_sample_tests=True):
        test_path, _ = get_test_dev_path(self.model_name)
        rendered_test = self._render_unit_test(render_sample_tests)

        with open(test_path, "w", encoding="utf-8") as f:
            f.write(rendered_test)
        black.format_file_in_place(Path(test_path), fast=True, mode=black.FileMode())
