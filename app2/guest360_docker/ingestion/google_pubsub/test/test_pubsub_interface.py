#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from boto3 import client
from google.cloud.pubsub_v1 import SubscriberClient
from unittest.mock import patch, MagicMock

from app.guest360_docker.ingestion.google_pubsub.pubsub_interface import PubSubtoKinesis
from app.guest360_docker.ingestion.google_pubsub.runner import put_record_into_kinesis


# load_env_vars can be mocked since other tests validate it
@patch(
    "app.guest360_docker.ingestion.google_pubsub.pubsub_interface.load_env_vars",
    return_value={"GOOGLE_APPLICATION_CREDENTIALS": "someultrasecretname"},
)
@patch("app.guest360_docker.ingestion.google_pubsub.pubsub_interface.client", return_value=MagicMock(spec=client))
@patch("app.guest360_docker.ingestion.google_pubsub.pubsub_interface.SubscriberClient")
def test_validate_init(mock_pubsub_client, mock_client, mock_envvars):
    pubsub_ifc = PubSubtoKinesis(
        pubsub_stream_publisher=put_record_into_kinesis, env_vars=["GOOGLE_APPLICATION_CREDENTIALS"]
    )

    mk_subscriber = MagicMock(spec=SubscriberClient)
    pubsub_ifc.pubsub_subscriber_client = mk_subscriber

    mock_envvars.assert_called_with(env_vars=["GOOGLE_APPLICATION_CREDENTIALS"])
    mock_client.assert_called_with("kinesis")

    assert isinstance(pubsub_ifc.pubsub_subscriber_client, SubscriberClient)
