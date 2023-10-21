import boto3
from tempfile import TemporaryDirectory
from botocore.exceptions import ClientError
from urllib import parse
from pathlib import Path
from typing import List
import os
from werkzeug.datastructures import FileStorage
import io
import json
import uuid
from app.src.data_structures.utilities.ui.dataclass_generator.utils.utils import extract_json_objects
import contextlib


class AwsAuthenticationError(Exception):
    pass


@contextlib.contextmanager
def s3_file_downloader(s3_location: str, s3_client=None):
    s3_client = boto3.client("s3") if s3_client is None else s3_client

    parsed_url = parse.urlparse(s3_location)

    bucket_name = parsed_url.netloc
    prefix = parsed_url.path.lstrip("/")

    def key_exists(bucket: str, key: str) -> bool:
        key = key if len(key) > 0 else "/"
        try:
            s3_client.head_object(Bucket=bucket, Key=key)
        except ClientError as e:
            if e.response["Error"]["Code"] == "404":
                # The object does not exist.
                return False
            else:
                raise
        return True

    def is_directory(bucket: str, key: str) -> bool:
        if key in ("/", ""):
            return True
        s3 = boto3.resource("s3")
        key = key if len(key) > 0 else "/"
        obj_summary = s3.ObjectSummary(bucket, key)
        return "application/x-directory" in obj_summary.get()["ContentType"]

    def get_s3_files_list(bucket_name: str, prefix: str) -> List[str]:
        response = (
            s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter="/")
            if len(prefix) > 0
            else s3_client.list_objects_v2(Bucket=bucket_name, Delimiter="/")
        )
        # contents = response["Contents"] if "Contents" in response and response["Contents"] is not None else [{"Key": prefix}]
        contents = response.get("Contents", [{"Key": prefix}] if key_exists(bucket_name, prefix) else None)
        if contents is None:
            raise FileNotFoundError()
        assert contents is not None
        # we need to filter out all directories
        files = [obj["Key"] for obj in contents if not is_directory(bucket_name, obj["Key"])]
        return files

    def download_s3_file(bucket_name: str, file_key: str, local_file_path: str, create_path: bool = True):
        if create_path:
            file_path = Path(local_file_path)
            if not file_path.parent.exists():
                file_path.parent.mkdir(exist_ok=True, parents=True)
        s3_client.download_file(bucket_name, file_key, local_file_path)

    list_files = get_s3_files_list(bucket_name, prefix)

    with TemporaryDirectory() as temporary_directory:
        files = [Path(temporary_directory) / Path(file_key) for file_key in list_files]
        for file_key, file_path in zip(list_files, files):
            download_s3_file(
                bucket_name=bucket_name, file_key=file_key, local_file_path=os.fspath(file_path), create_path=True
            )

        def convert_to_file_storage(file: Path) -> FileStorage:
            root, ext = os.path.splitext(file)
            if not ext:
                ext = ".json"  # Default JSON interpretation
            with open(file, mode="rb") as file_stream:
                return FileStorage(filename=root + ext, stream=io.BytesIO(file_stream.read()))

        flask_converted_files = [convert_to_file_storage(file) for file in files]

        file_format = [
            file.filename.split(".")[-1].lower() for file in flask_converted_files if file.filename is not None
        ]

        result = (
            separate_json_files(flask_converted_files) if next(iter(file_format)) == "json" else flask_converted_files
        )

        yield result


def separate_json_files(files: List[FileStorage]) -> List[FileStorage]:
    """This is used for firehose which does not always have a certain delimiter"""

    def process_file(file: FileStorage) -> List[dict]:
        # Read FileStorage Text
        file_text = io.TextIOWrapper(file.stream).read().encode().decode("unicode_escape")
        json_objects = extract_json_objects(file_text)
        return json_objects

    json_objects_list = [process_file(file) for file in files]

    return [
        FileStorage(
            filename=str(uuid.uuid4()) + ".json", stream=io.BytesIO(bytes(json.dumps(json_object), encoding="utf-8"))
        )
        for json_objects in json_objects_list
        for json_object in json_objects
    ]
