"""
lambda that validate the sqs queue for load test
"""
import boto3


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    """
    queue validator lambda_handler
    """
    sqs = boto3.client("sqs")
    queue_url = event["queue_url"]

    response = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=["ApproximateNumberOfMessages"])

    return int(response["Attributes"]["ApproximateNumberOfMessages"]) > 0
