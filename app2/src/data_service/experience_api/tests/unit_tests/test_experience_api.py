"""
This module includes unit tests for the experience api request handler and lambda functions.
"""
from copy import deepcopy

import boto3
from moto import mock_dynamodb, mock_kinesis

from app.src.data_service.experience_api.experience_api.request_handler import ExperienceRestAPIRequestHandler
from app.src.data_structures.tests import test_lookup
from app.src.data_structures.tests.utils.setup_dynamodb import setup_dynamodb


SAMPLE_EXPERIENCES_API_LAMBDA_EVENT = {
    "resource": "/api/v1/experiences",
    "path": "/api/v1/experiences/",
    "httpMethod": "GET",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": "Bearer DA_BEAR_A_TOKEN",
        "Host": "gatewayid-vpce-0001.execute-api.us-east-1.amazonaws.com",
        "Postman-Token": "77c2cbde-10a8-4564-a0c1-4bbb56f5a5d0",
        "User-Agent": "PostmanRuntime/7.30.0",
        "x-amzn-cipher-suite": "ECDHE-RSA-AES128-GCM-SHA256",
        "x-amzn-tls-version": "TLSv1.2",
        "x-amzn-vpc-id": "vpc-0001",
        "x-amzn-vpce-config": "1",
        "x-amzn-vpce-id": "vpce-0001",
        "X-Forwarded-For": "10.13.58.60",
    },
    "multiValueHeaders": {
        "Accept": ["*/*"],
        "Accept-Encoding": ["gzip, deflate, br"],
        "Authorization": ["Bearer DA_BEAR_A_TOKEN"],
        "Host": ["gatewayid-vpce-0001.execute-api.us-east-1.amazonaws.com"],
        "User-Agent": ["PostmanRuntime/7.30.0"],
        "x-amzn-cipher-suite": ["ECDHE-RSA-AES128-GCM-SHA256"],
        "x-amzn-tls-version": ["TLSv1.2"],
        "x-amzn-vpc-id": ["vpc-0001"],
        "x-amzn-vpce-config": ["1"],
        "x-amzn-vpce-id": ["vpce-0001"],
        "X-Forwarded-For": ["10.13.58.60"],
    },
    "queryStringParameters": {"id": "{abcde}", "idType": "swid"},
    "multiValueQueryStringParameters": {"id": ["{abcde}"], "idType": ["swid"]},
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "qgqszs",
        "authorizer": {"principalId": "TPR-GUESTPROFILETOOLS-PPD.B2B-STAGE", "integrationLatency": 188},
        "resourcePath": "/api/v1/experiences",
        "operationName": "getGuestExperiences",
        "httpMethod": "GET",
        "extendedRequestId": "fPvfNGFZIAMFUtQ=",
        "requestTime": "24/Jan/2023:11:50:18 +0000",
        "path": "/latest/api/v1/experiences/",
        "accountId": "543276908693",
        "protocol": "HTTP/1.1",
        "stage": "latest",
        "domainPrefix": "x5j9oi9gjb-vpce-0081be8a6c5e738e3",
        "requestTimeEpoch": 1674561018787,
        "requestId": "a1ef2b10-e929-4012-8eeb-442b71d6ad1f",
        "identity": {
            "cognitoIdentityPoolId": None,
            "cognitoIdentityId": None,
            "vpceId": "vpce-001",
            "principalOrgId": None,
            "cognitoAuthenticationType": None,
            "userArn": None,
            "userAgent": "PostmanRuntime/7.30.0",
            "accountId": None,
            "caller": None,
            "sourceIp": "10.13.58.60",
            "accessKey": None,
            "vpcId": "vpc-001",
            "cognitoAuthenticationProvider": None,
            "user": None,
        },
        "domainName": "gatewayid-vpce-0001.execute-api.us-east-1.amazonaws.com",
        "apiId": "x5j9oi9gjb",
    },
    "body": None,
    "isBase64Encoded": False,
}


EVENT_TABLE_NAME = "events"
PROFILE_TABLE_NAME = "profile_lookup"
IDENTITY_TABLE_NAME = "atomic_id_lookup"
IDENTITY_NODES_TABLE_NAME = "identity_nodes"
IDENTITY_EDGES_TABLE_NAME = "identity_edges"
IDENTITY_NOTIFICATION_STREAM_NAME = "identity_notification"


def init_monkeypatch(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    monkeypatch.setenv("IDENTITY_TABLE_NAME", IDENTITY_TABLE_NAME)
    monkeypatch.setenv("PROFILE_TABLENAME", PROFILE_TABLE_NAME)
    monkeypatch.setenv("EXPERIENCE_EVENT_TABLE_NAME", EVENT_TABLE_NAME)


@mock_dynamodb
@mock_kinesis
def test_request_handler_process_success(
    monkeypatch,
) -> None:
    init_monkeypatch(monkeypatch)
    setup_dynamodb(
        event_table_name=EVENT_TABLE_NAME,
        profile_table_name=PROFILE_TABLE_NAME,
        identity_table_name=IDENTITY_TABLE_NAME,
        identity_nodes_table_name=IDENTITY_NODES_TABLE_NAME,
        identity_edges_table_name=IDENTITY_EDGES_TABLE_NAME,
        identity_notification_stream=IDENTITY_NOTIFICATION_STREAM_NAME,
        create_table=True,
    )
    test_lookup.create_test_event()

    resource = boto3.resource("dynamodb")
    kinesis_client = boto3.client("kinesis")

    # Since we're mocking dynamo, this needs to be loaded at function
    # level so that mock_dynamodb applies:

    from app.src.data_service.experience_api.experience_api import lambda_function  # pylint: disable=C

    request_handler_instance = ExperienceRestAPIRequestHandler(
        lambda_event=SAMPLE_EXPERIENCES_API_LAMBDA_EVENT,
        dynamodb_resource=resource,
        kinesis_client=kinesis_client,
        identity_table_name=IDENTITY_TABLE_NAME,
        identity_nodes_table_name=IDENTITY_NODES_TABLE_NAME,
        identity_edges_table_name=IDENTITY_EDGES_TABLE_NAME,
        profile_table_name=PROFILE_TABLE_NAME,
        events_table_name=EVENT_TABLE_NAME,
        identity_notification_stream_name=IDENTITY_NOTIFICATION_STREAM_NAME,
    )
    process_response = request_handler_instance.process()
    assert process_response["statusCode"] == 200
    lambda_response = lambda_function.lambda_handler(
        SAMPLE_EXPERIENCES_API_LAMBDA_EVENT, None, request_handler_instance
    )

    assert lambda_response["statusCode"] == 200


@mock_dynamodb
@mock_kinesis
def test_request_handler_process_not_found(
    monkeypatch,
) -> None:
    init_monkeypatch(monkeypatch)
    setup_dynamodb(
        event_table_name=EVENT_TABLE_NAME,
        profile_table_name=PROFILE_TABLE_NAME,
        identity_table_name=IDENTITY_TABLE_NAME,
        identity_nodes_table_name=IDENTITY_NODES_TABLE_NAME,
        identity_edges_table_name=IDENTITY_EDGES_TABLE_NAME,
        identity_notification_stream=IDENTITY_NOTIFICATION_STREAM_NAME,
        create_table=True,
    )

    resource = boto3.resource("dynamodb")
    kinesis_client = boto3.client("kinesis")

    # Since we're mocking dynamo, this needs to be loaded at function
    # level so that mock_dynamodb applies:

    from app.src.data_service.experience_api.experience_api import lambda_function  # pylint: disable=C

    lambda_event_with_unknown_id = deepcopy(SAMPLE_EXPERIENCES_API_LAMBDA_EVENT)
    lambda_event_with_unknown_id["queryStringParameters"]["id"] = "{some_id_not_in_db}"
    request_handler_instance = ExperienceRestAPIRequestHandler(
        lambda_event=SAMPLE_EXPERIENCES_API_LAMBDA_EVENT,
        dynamodb_resource=resource,
        kinesis_client=kinesis_client,
        identity_table_name=IDENTITY_TABLE_NAME,
        identity_nodes_table_name=IDENTITY_NODES_TABLE_NAME,
        identity_edges_table_name=IDENTITY_EDGES_TABLE_NAME,
        profile_table_name=PROFILE_TABLE_NAME,
        events_table_name=EVENT_TABLE_NAME,
        identity_notification_stream_name=IDENTITY_NOTIFICATION_STREAM_NAME,
    )
    process_response = request_handler_instance.process()
    assert process_response["statusCode"] == 204

    lambda_response = lambda_function.lambda_handler(lambda_event_with_unknown_id, None, request_handler_instance)

    assert lambda_response["statusCode"] == 204
