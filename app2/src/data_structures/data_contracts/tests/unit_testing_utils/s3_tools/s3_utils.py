""" Module for S3 Samples Downloader Utils"""
import os

TEST_DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data"))
TEST_DIR = os.path.dirname(TEST_DATA_DIR)


def get_metadata(metadata: dict, model_name: str) -> tuple[str, str, str, str]:
    # Helper variables
    contract_filename = metadata["data-contract-name"]
    source_folder = metadata["data-source-folder"]
    bucket_name = list(metadata["s3"].keys())[0]
    # s3 path/to/folder/
    prefix_filter = metadata["s3"][bucket_name]["path-filter"]
    local_samples_base_dir = f"{TEST_DIR}/s3_samples"
    local_samples_model_dir = f"{local_samples_base_dir}/{source_folder}/{model_name}"
    # To generate final json sample file
    merged_file_dir = f"{TEST_DATA_DIR}/{source_folder}"
    merged_filename = f"{merged_file_dir}/{contract_filename}_sample.json"

    return bucket_name, prefix_filter, local_samples_base_dir, local_samples_model_dir, merged_filename


def create_local_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
