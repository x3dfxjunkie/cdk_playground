"""
Downloads S3 files, consolidates them and
creates a sample file of one or more models for unit testing purposes
This feature supports gz compressed files and any other uncompressed file like json and txt with json structured content).
"""
import time
import json
import argparse
import os
from botocore.exceptions import ClientError, NoCredentialsError
from app.src.data_structures.data_contracts.tests.unit_testing_utils.global_unit_test_utils import (
    get_data_contracts_info,
)
from app.src.data_structures.data_contracts.tests.unit_testing_utils.s3_tools.s3_utils import (
    get_metadata,
    create_local_directory,
)
import glob
import re

# To work in async manner
import aioboto3
import asyncio

# Module to copy files
import shutil
import gzip

# User defined constants
# Role to be used to access AWS environment
USER_ROLE_ARN = "arn:aws:iam::543276908693:role/WDPR-GUEST360_DEVELOPER"
# Gets all mappings file info.
DATA_CONTRACT_MAPPING = get_data_contracts_info()


async def create_session():
    """Function to create the AWS Session"""
    session = aioboto3.Session()
    # AWS Security Token Service for requesting temporary, limited-privilege credentials.
    async with session.client("sts") as sts:
        # Assume role defined before
        response = await sts.assume_role(RoleArn=USER_ROLE_ARN, RoleSessionName="s3-extractor")
        session = aioboto3.Session(
            aws_access_key_id=response["Credentials"]["AccessKeyId"],
            aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
            aws_session_token=response["Credentials"]["SessionToken"],
        )
        return session


async def get_session():
    """Function to get the AWS Session"""

    try:
        session = await create_session()
        return session

    except (ClientError, NoCredentialsError):
        # Executes aws-saml-auth command on terminal
        os.system("aws-saml-auth")

    session = await create_session()
    return session


async def get_sample_files(bucket_name: str, prefix_filter: str, samples_dir: str) -> bool:
    """Function to get files from s3"""
    status = False
    # Pass the asynchronous aioboto3 session from get_session() to create S3 client
    aiosession = await get_session()
    async with aiosession.client("s3", region_name="us-east-1") as s3_client:
        # Retrieves the list of objects (up to what is set on MaxItems prop)
        paginator = s3_client.get_paginator("list_objects_v2")

        # Paginates through a result set in the event the number of sample files required might be too large to retrieve all at once API call. Paginating is common when working with AWS service APIs, like Amazon S3, where you want to retrieve multiple items from a result set in chunks or pages.
        # Configure the paginator props
        response_iterator = paginator.paginate(
            Bucket=bucket_name,
            Prefix=prefix_filter,
            PaginationConfig={
                # Max items desired
                "MaxItems": 3000,
                # Max items per page
                "PageSize": 1000,
            },
        )
        # Lists of download awaitable tasks (coroutines)
        download_tasks = []
        # To control the number of files to download
        num_files = 0
        # Creates local sample directory on container
        create_local_directory(samples_dir)
        # Builds the pattern based on the args provided. If EXTENSION_FILTER is not defined will download all file formats in the path
        pattern = rf"{BASE_PATTERN}\.({EXTENSION_FILTER})$" if EXTENSION_FILTER else rf"{BASE_PATTERN}\..*"
        st = time.time()
        # Iterates over each page of the paginator response
        async for response in response_iterator:
            # Sets a limit of files to download
            if num_files >= SAMPLE_SIZE:
                break
            if not response.get("Contents"):
                print(f"Exception:\n{MODEL_NAME}: Couldn't find files for the model in the S3 path filter and bucket")
                status = False
                return status
            objects = response["Contents"]
            # Filters objects based on the pattern
            filtered_objects = filter(lambda obj: re.match(pattern, obj["Key"]), objects)
            delta = abs(SAMPLE_SIZE - num_files)
            # Selects the files to download based on the delta
            # files_to_download = filtered_objects[:delta]
            # Iterates over the files to download to create the awaitable tasks that will be execute concurrently later with asyncio.gather()
            for index, file_obj in enumerate(filtered_objects):
                key = file_obj["Key"]
                # Gets the filename on the local system
                filename = key.split("/")[-1]
                local_filename = f"{samples_dir}/{filename}"
                """
                    Downloads the file from S3 to the local system:
                    bucket_name (str) – The name of the bucket to download from.
                    key (str) – The name of the key to download from.
                    local_filename (str) – The path to the file to download to.
                """
                # Creates an awaitable task to download the file
                download_task = asyncio.create_task(s3_client.download_file(bucket_name, key, local_filename))
                # Adds it to a list of asynchronous tasks
                download_tasks.append(download_task)
                num_files += 1
                if index + 1 >= delta:
                    break
        et = time.time()
        elt = et - st
        print(f"0.Download task list created in {elt:.4f} seconds.")
        if num_files < SAMPLE_SIZE:
            print(f"Warning: Couldn't find more than {num_files} files in the S3 path")
        st = time.time()
        # Runs the download tasks concurrently
        await asyncio.gather(*download_tasks)
        et = time.time()
        elt = et - st
        status = True
        print(f"1.Download completed: {len(download_tasks)} sample files were pulled down in {elt:.4f} seconds.")

    return status


def consolidate_s3_samples(base_sample_directory: str, s3_samples_directory: str, json_sample_filename: str) -> bool:
    """Function to merge s3 samples previously pulled down"""
    status = False
    pattern = f"{s3_samples_directory}/*"
    filenames = glob.glob(pattern)
    final_sample_dir = os.path.dirname(json_sample_filename)
    create_local_directory(final_sample_dir)
    # Creates a new file if it does not exist or truncates the file if it exists.
    # r	Open a file for reading. (default)
    # w	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
    # b	Open in binary mode.
    # +	Open a file for updating (reading and writing)
    with open(json_sample_filename, "wb+") as wfp:
        wfp.write("[".encode())
        for fn in filenames:
            file_extension = fn.split(".")[-1]
            if file_extension == "gz":
                with gzip.open(fn, "rb") as rfp:
                    shutil.copyfileobj(rfp, wfp)
            else:
                with open(fn, "rb") as rfp:
                    shutil.copyfileobj(rfp, wfp)
        # write() move read/write pointer position to the last byte written
        wfp.write("]".encode())
        # Returning to initial byte (byte 0 by default)
        wfp.seek(0)
        # read() left read/write pointer position (offset) in the last byte
        text = wfp.read().replace(b"}{", b"},{").replace(b"}\n{", b"},{")
        # Returning to initial byte
        wfp.seek(0)
        wfp.write(text)
        wfp.seek(0)
        # Moves pointer position to the last byte.
        data = json.load(wfp)
        filtered_data = [item.get("data") for item in data if item.get("data").get("data")]
        # Check if the data is a empty list
        if not filtered_data:
            remove_data(json_sample_filename)
            remove_data(base_sample_directory)
            print(
                "2.Error: The S3 files contents doesn't include any usable data item.S3 files and the final json sample file were removed.\nTry with another S3 path or increasing the SAMPLE_SIZE."
            )
            return False
        # Converts object to a valid json string
        s = json.dumps(filtered_data, indent=4)
        wfp.seek(0)
        # Delete previous data
        wfp.truncate()
        wfp.write(s.encode())
        status = True
    print(f"2.Consolidation completed. Sample file created:\n{json_sample_filename}")

    return status


def remove_data(path: str) -> bool:
    """Function to remove s3 samples from the container"""
    os.system(f"rm -r {path}")
    return True


async def get_sample_from_s3() -> bool:
    """Function to get a sample file from s3"""
    status = False
    if MODEL_NAME in DATA_CONTRACT_MAPPING.keys():
        metadata = DATA_CONTRACT_MAPPING[MODEL_NAME]
        # Loads initial params
        bucket_name, prefix_filter, local_samples_base_dir, local_samples_model_dir, merged_filename = get_metadata(
            metadata, MODEL_NAME
        )
        got_sample_files_sucessfully = await get_sample_files(bucket_name, prefix_filter, local_samples_model_dir)
        if got_sample_files_sucessfully:
            if consolidate_s3_samples(local_samples_base_dir, local_samples_model_dir, merged_filename):
                if KEEP_SAMPLES:
                    print(
                        "3.Samples remain on container, don't forget to remove them after making a backup externally if needed and exclude app/src/data_structures/data_contracts/tests/s3_samples path from your local git repo adding it to your /workspace/.git/info/exclude file before any further git operation"
                    )
                else:
                    # Removes the base sample dir used to download files from S3
                    remove_data(local_samples_base_dir)
                    print("3.s3 input files removed.")
                status = True
    else:
        print(f"Exception:\n{MODEL_NAME}: Model is not mapped in the mapping file.")

    return status


if __name__ == "__main__":
    # Define the program arguments
    parser = argparse.ArgumentParser()
    """
    SAMPLE_SIZE: (int) - Expected number of files to download - 50 is by default.
    KEEP_SAMPLES : (bool)  - To preserve files downloaded locally on app/src/data_structures/data_contracts/tests/s3_samples - False is by default
    BASE_PATTERN: (str) - Pattern for matching file names -  ".*" is by default so everything is matched.
    EXTENSION_FILTER: (str) - To filter specific file formats. Ex. 'gz' or 'gz|json' or 'gz|json|txt' or None. None is by default so all file formats are collected.
    MODEL_NAME: (str) - Data Contract Model to work with (from the list provided in --models arg)
    """
    parser.add_argument("--models", nargs="*", type=str, required=True)
    parser.add_argument("--sample-size", type=int, nargs="?", const=50, default=50, required=False)
    parser.add_argument("--keep-samples", type=bool, nargs="?", const=False, default=False, required=False)
    parser.add_argument("--extension-filter", type=str, nargs="?", const=None, default=None, required=False)
    parser.add_argument("--base-pattern-filter", type=str, nargs="?", const=".*", default=".*", required=False)
    ARGS = parser.parse_args()
    for model in ARGS.models:
        MODEL_NAME = model
        SAMPLE_SIZE = ARGS.sample_size
        KEEP_SAMPLES = ARGS.keep_samples
        EXTENSION_FILTER = ARGS.extension_filter
        BASE_PATTERN = ARGS.base_pattern_filter
        print(f"\nModel: {MODEL_NAME}\n")
        # Record the start time
        start_time = time.time()
        asyncio.run(get_sample_from_s3())
        # Record the end time
        end_time = time.time()
        # Calculate the elapsed time
        elapsed_time = end_time - start_time
        print(f"Finished in: {elapsed_time:.4f} seconds")
