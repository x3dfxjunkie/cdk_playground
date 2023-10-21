"""Script to create and validate a unit test"""
import os
import argparse
from data_contract_sample_extractor import get_sample_from_stream
from unit_test_writer import UnitTestWriter
from app.src.data_structures.data_contracts.tests.unit_testing_utils.global_unit_test_utils import get_test_dev_path

parser = argparse.ArgumentParser()
parser.add_argument("--model-name", type=str, required=True)
parser.add_argument("--render-sample", default=True, required=False, action=argparse.BooleanOptionalAction)
parser.add_argument("--keep-test", default=False, required=False, action=argparse.BooleanOptionalAction)
parser.add_argument("--exclusive-testing", default=True, required=False, action=argparse.BooleanOptionalAction)
parser.add_argument("--extract-sample", default=False, required=False, action=argparse.BooleanOptionalAction)
ARGS = parser.parse_args()
TESTS_GROUP, MODEL_NAME = ARGS.model_name.split(".")


def get_path_info():
    common_path = "app/src/data_structures/data_contracts"
    bazel_file_dir = f"/workspace/{common_path}/"
    bazel_test_target = f"//{common_path}"
    test_full_name, test_name = get_test_dev_path(MODEL_NAME)
    new_target = f'\npytest_test(name = "data_contracts_exclusive_testing", srcs = glob(["tests/unit_tests/**/{test_name}.py"]), data = glob(["tests/**/**/*.json"]), deps = [":data_contracts"],)'
    bazel_test_new_target = f"//{common_path}:data_contracts_exclusive_testing"
    return bazel_test_target, bazel_file_dir, new_target, bazel_test_new_target, test_full_name


def run_bazel(tests_group: str, model_name: str):
    bazel_test_target, bazel_file_dir, new_target, bazel_test_new_target, test_full_name = get_path_info()

    if not (ARGS.exclusive_testing):
        cmd = f"bazel test {bazel_test_target}:* --cache_test_results=no"
        os.system(cmd)
    else:
        cmd = (
            f"bazel test {bazel_test_target}:{tests_group} --test_arg=--model_name={model_name} --cache_test_results=no"
        )
        os.system(cmd)

    if not (ARGS.keep_test):
        os.system(f"rm {test_full_name}")


def main():
    if ARGS.extract_sample:
        get_sample_from_stream(MODEL_NAME)

    unit_test_writer = UnitTestWriter(MODEL_NAME)
    unit_test_writer.write_unit_test(render_sample_tests=ARGS.render_sample)

    run_bazel(TESTS_GROUP, MODEL_NAME)


if __name__ == "__main__":
    main()
