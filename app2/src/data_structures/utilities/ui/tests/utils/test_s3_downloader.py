import io
import boto3
import json
from werkzeug.datastructures import FileStorage
from moto import mock_s3
from app.src.data_structures.utilities.ui.dataclass_generator.utils.s3_downloader import (
    s3_file_downloader,
    separate_json_files,
)


@mock_s3
def test_save_files():
    test_item = {"key": "value"}
    stringified_test_item = json.dumps(test_item)
    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="sample-bucket")
    s3_client.put_object(Bucket="sample-bucket", Key="folder1/folder2/file1.json", Body=stringified_test_item)
    with s3_file_downloader("s3://sample-bucket/folder1/folder2/file1.json") as files:
        assert all((isinstance(file, FileStorage) for file in files)) is True
        assert len(files) > 0
        returned_item_stream = io.TextIOWrapper(files[0].stream)
        assert returned_item_stream.read() == stringified_test_item
        returned_item_stream.close()


@mock_s3
def test_multiple_saved_files():
    test_items = [{"key": "value"}, {"key": "value2"}]
    bucket_name = "sample-bucket"
    prefix = "folder1/folder2"
    for index, test_item in enumerate(test_items):
        stringified_test_item = json.dumps(test_item)
        s3_client = boto3.client("s3", region_name="us-east-1")
        s3_client.create_bucket(Bucket="sample-bucket")
        s3_client.put_object(Bucket="sample-bucket", Key=f"{prefix}/file{index}.json", Body=stringified_test_item)
    with s3_file_downloader(f"s3://{bucket_name}/{prefix}/") as files:
        assert all((isinstance(file, FileStorage) for file in files)) is True
        assert len(files) == 2


@mock_s3
def test_firehose_json():
    test_items = [{"key": "value"}, {"key": "value2"}]
    delimiters = [",", "", " ", "\n"]
    stringified_items = [json.dumps(test_item) for test_item in test_items]

    items = [delimiter.join(stringified_items) for delimiter in delimiters]

    bucket_name = "sample-bucket"
    prefix = "folder1/folder2"

    # Ensure one file at a time works
    for item in items:
        stringified_test_item = item
        s3_client = boto3.client("s3", region_name="us-east-1")
        s3_client.create_bucket(Bucket="sample-bucket")
        s3_client.put_object(Bucket="sample-bucket", Key=f"{prefix}/file", Body=stringified_test_item)
        with s3_file_downloader(f"s3://{bucket_name}/{prefix}/file") as files:
            json_files = separate_json_files(files)
            assert len(json_files) > 0
            for json_file, expected in zip(json_files, stringified_items):
                returned_item_stream = io.TextIOWrapper(json_file.stream)
                assert returned_item_stream.read() == expected
                returned_item_stream.close()

    for index, item in enumerate(items):
        s3_client = boto3.client("s3", region_name="us-east-1")
        s3_client.create_bucket(Bucket="sample-bucket")
        s3_client.put_object(Bucket="sample-bucket", Key=f"{prefix}/file{index}", Body=item)

    with s3_file_downloader(f"s3://{bucket_name}/{prefix}/") as files:
        json_files = separate_json_files(files)
        assert len(json_files) > 0
        for json_file, expected in zip(json_files, stringified_items):
            returned_item_stream = io.TextIOWrapper(json_file.stream)
            assert returned_item_stream.read() == expected
            returned_item_stream.close()
