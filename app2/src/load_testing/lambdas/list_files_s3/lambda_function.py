"""
List files S3 lambda_handler
"""
import boto3


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    """
    List files S3 lambda_handler
    """
    s3_client = boto3.client("s3")
    bucket_name = event.get("bucket_name")
    bucket_path = event.get("bucket_path")
    response = {"scenarios": get_file_names(s3_client, bucket_name, bucket_path)}
    return response


def get_file_names(s3_client, bucket_name, bucket_path):
    """
    get list of files
    """
    file_names = []
    default_kwargs = {"Bucket": bucket_name, "Prefix": bucket_path}
    next_token = ""
    while next_token is not None:
        updated_kwargs = default_kwargs.copy()
        if next_token != "":
            updated_kwargs["ContinuationToken"] = next_token
        response = s3_client.list_objects_v2(**default_kwargs)
        contents = response.get("Contents")
        if contents is not None and len(contents) > 0:
            for result in contents:
                key = result.get("Key")
                if key[-1] != "/":
                    file_names.append(key)
        next_token = response.get("NextContinuationToken")
    return file_names
