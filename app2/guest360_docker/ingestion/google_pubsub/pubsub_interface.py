#!/usr/bin/env python
# -*- coding: utf-8 -*-

from boto3 import client
from google.cloud.pubsub_v1 import SubscriberClient
from logging import info

from environment_variables import load_env_vars


class PubSubtoKinesis:
    def __init__(self, pubsub_stream_publisher, env_vars: list):
        self.environment_vars = load_env_vars(env_vars=env_vars)

        self.kinesis_client = client("kinesis")
        self.pubsub_subscriber_client = SubscriberClient()
        self.pubsub_stream_publisher = pubsub_stream_publisher

    def get_subscription_future(self):
        """Returns the PubSub subscription with the ability of pulling streams"""
        subscription_path = self.pubsub_subscriber_client.subscription_path(
            self.environment_vars["pub_sub_project"], self.environment_vars["pub_sub_subscription"]
        )
        return self.pubsub_subscriber_client.subscribe(subscription_path, callback=self.process_payload)

    def process_payload(self, message):
        """Receive the PubSub payload and send this data to publisher."""

        self.pubsub_stream_publisher(message.data, self.kinesis_client, **self.environment_vars)

        message.ack()

    def start_consuming_pubsub(self):
        """Method that generates the process flow"""
        # Using the PubSub client and the subscription pulls messages asynchronously
        with self.pubsub_subscriber_client:
            try:
                info("The program now started pulling messages\n")
                # When `timeout` is not set, result() will block indefinitely unless an exception is encountered first.
                self.get_subscription_future().result()
            except TimeoutError:
                self.get_subscription_future().cancel()  # Trigger the shutdown.
                self.get_subscription_future().result()  # Block until the shutdown is complete.
