"""
TestListFilesS3
"""
import boto3
from app.src.load_testing.lambdas.list_files_s3 import lambda_function
from moto import mock_s3


class TestListFilesS3:
    """
    TestListFilesS3
    """

    @mock_s3
    def test_lambda_handler(self):
        """test_lambda_handler"""
        sample_data = """
            TestListFilesS3
            """
        bucket_name = "bucket_test"
        bucket_path = "orion_ea_normal/"

        client = boto3.client("s3")
        client.create_bucket(Bucket=bucket_name)
        for i in range(10):
            client.put_object(
                Bucket=bucket_name, Body=bytes(sample_data, encoding="utf-8"), Key=f"orion_ea_normal/test_file_{i}.txt"
            )
        event = {"bucket_name": bucket_name, "bucket_path": bucket_path}
        handler = None
        response = lambda_function.lambda_handler(event, handler)
        assert len(response["scenarios"]) == 10
        assert response["scenarios"][9] == "orion_ea_normal/test_file_9.txt"
