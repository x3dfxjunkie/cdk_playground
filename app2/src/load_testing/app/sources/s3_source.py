"""
    Source S3
"""
import boto3
import os
from app.src.load_testing.app.sources.source import Source


class S3Source(Source):
    """
    Subclass. Implements a generic S3 reader.
    locust "users" will need to instatiate this to read sample data
    """

    def __init__(self, bucket_name: str, bucket_path: str) -> None:
        self.s3_client = boto3.client("s3")
        self.bucket_name = bucket_name  # Setting the bucket name
        self.bucket_path = bucket_path  # Setting the bucket path

    def get_sample_data(self):
        sample_data = []
        files = self.get_file_names()
        for file in files:
            data_file = self.read_content_from_file(file)
            sample_data.extend(data_file)
        return sample_data

    def get_file_names(self):
        file_names = []

        default_kwargs = {"Bucket": self.bucket_name, "Prefix": self.bucket_path}
        next_token = ""

        while next_token is not None:
            updated_kwargs = default_kwargs.copy()

            if next_token != "":
                updated_kwargs["ContinuationToken"] = next_token

            response = self.s3_client.list_objects_v2(**default_kwargs)
            contents = response.get("Contents")
            if contents is not None and len(contents) > 0:
                for result in contents:
                    key = result.get("Key")
                    if key[-1] != "/":
                        file_names.append(key)

            next_token = response.get("NextContinuationToken")

        return file_names

    def read_content_from_file(self, file_name):
        s3_response = self.s3_client.get_object(
            Bucket=self.bucket_name,
            Key=file_name,
        )
        s3_object_body = s3_response.get("Body")
        content = s3_object_body.read().decode().strip()

        return content.splitlines()

    def download_file(self, src_file_paths, local_folder_path="/home/locust"):
        if isinstance(src_file_paths, str):
            src_file_paths = [src_file_paths]

        local_file_paths = []
        for src_file_path in src_file_paths:
            local_file_paths.append(self._download_single_file(src_file_path, local_folder_path))

        return local_file_paths

    def _download_single_file(self, src_file_path, local_folder_path):
        local_file_path = os.path.join(local_folder_path, src_file_path)
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        list_dir = src_file_path.split("/")
        current_dir = local_folder_path
        for sub_dir in list_dir[:-1]:
            current_dir = os.path.join(current_dir, sub_dir)
            init_file_path = os.path.join(current_dir, "__init__.py")
            if not os.path.exists(init_file_path):
                open(init_file_path, "w").close()
        self.s3_client.download_file(self.bucket_name, src_file_path, local_file_path)
        return local_file_path
