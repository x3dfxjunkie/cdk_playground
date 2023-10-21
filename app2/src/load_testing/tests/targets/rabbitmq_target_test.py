"""RabbitMQ target tests"""
import pytest
import pika
import gc
from unittest.mock import MagicMock, patch
from app.src.load_testing.app.targets.rabbitmq_target import RabbitMQTarget


@pytest.fixture
def mock_pika():
    with patch("app.src.load_testing.app.targets.rabbitmq_target.pika") as mock:
        mock.BlockingConnection.return_value = MagicMock(spec=pika.BlockingConnection)
        mock.ConnectionParameters.return_value = MagicMock(spec=pika.ConnectionParameters)
        yield mock


@pytest.fixture
def rabbit(mock_pika):
    return RabbitMQTarget(
        "rabbitmq.lst-use1-pr-3400-load-testing-static",
        5672,
        "vhost",
        "guest",
        "guest",
    )


def test_rabbitmq_init(mock_pika, rabbit):
    mock_pika.ConnectionParameters.assert_called_with(
        host="rabbitmq.lst-use1-pr-3400-load-testing-static",
        virtual_host="vhost",
        port=5672,
        credentials=mock_pika.PlainCredentials("guest", "guest"),
    )
    mock_pika.BlockingConnection.assert_called_with(mock_pika.ConnectionParameters())
    assert rabbit.connection == mock_pika.BlockingConnection()


def test_rabbitmq_publish(rabbit):
    rabbit.send_data({"Hello": "Helix"})
    rabbit.channel.basic_publish.assert_called_with(
        exchange="",
        routing_key="default_queue",
        body='{"Hello": "Helix"}',
    )


def test_rabbitmq_close(rabbit):
    rabbit.close()
    rabbit.connection.close.assert_called_once()


def test_rabbitmq_del(mock_pika):
    rabbit = RabbitMQTarget("host", 5672, "vhost", "guest", "guest")
    connection = rabbit.connection
    del rabbit
    gc.collect()
    connection.close.assert_called_once()
