import pytest
import pika

from app.src.load_testing.lambdas.rabbitmq_test.lambda_function import lambda_handler


class MockBlockingConnection:
    def __init__(self, *args, **kwargs):
        # Needed to avoid the no arguments error with monkeypatch
        pass

    def channel(self):
        return MockChannel()

    def close(self):
        # close method it is necessary for the mock
        pass


class MockChannel:
    def __init__(self):
        self.queue_declared = False

    def queue_declare(self, queue):
        self.queue_declared = True

    def basic_publish(self, exchange, routing_key, body):
        # basic_publish method it is necessary for the mock
        pass


def test_publish_message_successful(monkeypatch):
    monkeypatch.setattr(pika, "BlockingConnection", MockBlockingConnection)

    assert lambda_handler(None, None) is True


def test_publish_message_failure(monkeypatch):
    def mock_blocking_connection(*args, **kwargs):
        raise Exception("Connection failed")  # NOSONAR avoid generic exception warning

    monkeypatch.setattr(pika, "BlockingConnection", mock_blocking_connection)

    assert lambda_handler(None, None) is False
