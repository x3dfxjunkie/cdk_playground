""" Test cases for rabbitmq consumer application"""
# Disable pylint redefinition of name: that is how fixtures work.
# pylint: disable=W0621
# pylint: disable=E0602

import asyncio
import json
import logging
from unittest.mock import AsyncMock, MagicMock, ANY, patch

import aio_pika
import aioboto3
from aiobotocore.client import AioBaseClient
from botocore.exceptions import ClientError
import app.guest360_docker.ingestion.rabbitmq.main as main
import pytest
from tenacity import wait_none, stop_after_attempt
from app.guest360_docker.ingestion.rabbitmq.main import (
    get_secret,
    orchestrate,
    consume,
    TaskTracker,
    process_message,
    rabbitmq_connect,
    s3_upload_failed_message,
    setup_logging,
    publish_to_kinesis,
    process_message_wrapper,
)

FAILED_MESSAGE_KEY = "failed_messages/123"
TEST_BODY = b'{"id": "123", "data": "test"}'

AIO_PIKA_CONNECT_ROBUST_PATCH = "app.guest360_docker.ingestion.rabbitmq.main.aio_pika.connect_robust"


@pytest.fixture
def mock_message():
    """Mocked rabbitmq Message"""
    message = MagicMock(spec=aio_pika.IncomingMessage)
    message.body = TEST_BODY
    message.message_id = "123"
    return message


@pytest.fixture
def rabbit_config():
    """Rabbit config for rabbit connect"""
    rabbit_config = {
        "hostname": "test_host",
        "port": "5672",
        "rabbit_usr": "test_user",
        "rabbit_pwd": "test_password",  # pragma: allowlist secret
        "virtual_host": "test_vhost",
    }
    return rabbit_config


@pytest.fixture
def kinesis_client():
    """Mocked Kinesis Client"""
    client = AsyncMock(spec=AioBaseClient)
    return client


@pytest.fixture
def s3_client():
    """Mocked s3 client"""
    client = AsyncMock(spec=AioBaseClient)
    return client


@pytest.fixture
def secretsmanager_client():
    """Mocked secretsmanager client"""
    client = AsyncMock(spec=AioBaseClient)
    return client


@pytest.fixture
def rabbitmq_credentials():
    """Fixture for rabbitmq credentials"""
    return {
        "RABBIT_USR": "test_user",
        "RABBIT_PWD": "test_password",  # pragma: allowlist secret
    }


@pytest.fixture
def mock_session():
    """Mocked aiobotocore session"""
    mock_session = MagicMock(spec=aioboto3.Session)
    return mock_session


@pytest.fixture
def tracker():
    """Task Tracker"""
    return TaskTracker()


class StopTestingException(Exception):
    """Exception for the purpose of exiting while true loops"""

    pass


async def test_coroutine():
    """Test coroutine"""
    pass


class TestException(Exception):
    """Exception for the purpose of testing correct exception handling"""

    pass


def test_init(tracker):
    """Tests the TaskTracker init method"""
    assert tracker.tasks == set()


def test_add(tracker):
    """Tests the TaskTracker add method"""
    task = asyncio.Task(test_coroutine())
    tracker.add(task)
    assert task in tracker.tasks


def test_cancel(tracker):
    """Tests the TaskTracker cancel method"""
    task1 = asyncio.Task(test_coroutine())
    task2 = asyncio.Task(test_coroutine())
    task1.cancelled = MagicMock(return_value=False)
    task2.cancelled = MagicMock(return_value=True)
    task1.cancel = MagicMock()
    task2.cancel = MagicMock()
    tracker.add(task1)
    tracker.add(task2)
    tracker.cancel()
    task1.cancel.assert_called_once()
    task2.cancel.assert_not_called()
    assert tracker.tasks == set()


@pytest.mark.asyncio
async def test_check_tasks(tracker):
    """Test to ensure check tasks behaves correctly"""
    # Create mock tasks
    task1 = asyncio.Task(test_coroutine())
    task2 = asyncio.Task(test_coroutine())
    task1.exception = MagicMock(return_value=None)
    task2.exception = MagicMock(return_value=None)
    tracker.add(task1)
    tracker.add(task2)

    # Mock asyncio.wait to simulate task completion
    with pytest.MonkeyPatch.context() as m:
        mock_logger = MagicMock()
        m.setattr("app.guest360_docker.ingestion.rabbitmq.main.logger", mock_logger)
        m.setattr("asyncio.wait", AsyncMock(return_value=({task1, task2}, set())))
        await tracker.check_tasks()

        mock_logger.info.assert_called_with("Successfully processed %s messages", 2)
        assert tracker.tasks == set()


@pytest.mark.asyncio
async def test_check_tasks_with_exception(tracker):
    """Tests to ensure when an exception occurs in a task that it is raised"""
    task = asyncio.Task(test_coroutine())
    task.exception = MagicMock(return_value=TestException)
    tracker.add(task)
    with pytest.MonkeyPatch.context() as m:
        mock_logger = MagicMock()
        m.setattr("app.guest360_docker.ingestion.rabbitmq.main.logger", mock_logger)
        m.setattr("asyncio.wait", AsyncMock(return_value=({task}, set())))
        with pytest.raises(TestException):
            await tracker.check_tasks()
    assert tracker.tasks == set()


@pytest.mark.asyncio
async def test_process_message_failure(mock_message, mock_session):
    """Tests that upon a message failing to process, it is uploaded to S3 and not acknowledged."""
    with pytest.MonkeyPatch.context() as m:
        mock_failed_message = AsyncMock()
        mock_kinesis_publish = AsyncMock(side_effect=TestException)
        m.setattr("app.guest360_docker.ingestion.rabbitmq.main.s3_upload_failed_message", mock_failed_message)
        m.setattr("app.guest360_docker.ingestion.rabbitmq.main.publish_to_kinesis", mock_kinesis_publish)
        kinesis_stream_name = "test_stream"
        s3_bucket = "test_bucket"

        with pytest.raises(TestException):
            await process_message(mock_message, mock_session, kinesis_stream_name, s3_bucket)

        mock_message.ack.assert_not_called()

        mock_message.reject.assert_called_once()

        mock_failed_message.assert_called_once()


@pytest.mark.asyncio
async def test_process_message_success(mock_message, mock_session):
    """Tests that a message is processed successully, ensures the message is acknowledged"""
    with pytest.MonkeyPatch.context() as m:
        mock_kinesis_publish = AsyncMock()
        m.setattr("app.guest360_docker.ingestion.rabbitmq.main.publish_to_kinesis", mock_kinesis_publish)
        kinesis_stream_name = "test_stream"
        s3_bucket = "test_bucket"

        await process_message(mock_message, mock_session, kinesis_stream_name, s3_bucket)

        mock_kinesis_publish.assert_called_once_with(mock_message, mock_session, kinesis_stream_name)

        mock_message.ack.assert_called_once()


@pytest.mark.asyncio
async def test_publish_to_kinesis_success(kinesis_client, mock_session, mock_message):
    """Tests a successful publish to kinesis"""
    with pytest.MonkeyPatch.context() as m:
        m.setattr("aioboto3.Session", lambda: mock_session)
        mock_session.client.return_value = kinesis_client
        kinesis_client.__aenter__.return_value = kinesis_client
        kinesis_client.put_record = AsyncMock()
        kinesis_stream_name = "test_stream"
        await publish_to_kinesis(mock_message, mock_session, kinesis_stream_name)
        kinesis_client.put_record.assert_called_once_with(
            StreamName=kinesis_stream_name, Data=mock_message.body, PartitionKey=ANY
        )


@pytest.mark.asyncio
async def test_publish_to_kinesis_retry(kinesis_client, mock_session, mock_message):
    """Tests that given the 4 retryable errors, that publish to kinesis retries each time and eventually raises the error on failure"""
    with pytest.MonkeyPatch.context() as m:
        m.setattr("aioboto3.Session", lambda: mock_session)
        m.setattr(publish_to_kinesis.retry, "wait", wait_none())
        mock_session.client.return_value = kinesis_client
        kinesis_client.__aenter__.return_value = kinesis_client
        # Test that these exceptions lead to retries
        exception_1 = ClientError(error_response={"Error": {"Code": "InternalFailureException"}}, operation_name="Test")
        exception_2 = ClientError(
            error_response={"Error": {"Code": "ProvisionedThroughputExceededException"}}, operation_name="Test"
        )
        exception_3 = ClientError(error_response={"Error": {"Code": "LimitExceededException"}}, operation_name="Test")
        exception_4 = ClientError(error_response={"Error": {"Code": "KMSThrottlingException"}}, operation_name="Test")
        mock_put_record = AsyncMock(side_effect=[exception_1, exception_2, exception_3, exception_4, exception_1])
        kinesis_client.put_record = mock_put_record
        kinesis_stream_name = "test_stream"
        # Test that an exception is thrown after max retries
        with pytest.raises(ClientError):
            await publish_to_kinesis(mock_message, mock_session, kinesis_stream_name)
        assert mock_put_record.call_count == 5

        # Test that the function exits correctly on a successful publish after failures
        mock_put_record = AsyncMock(side_effect=[exception_1, exception_2, None])
        kinesis_client.put_record = mock_put_record
        await publish_to_kinesis(mock_message, mock_session, kinesis_stream_name)
        assert mock_put_record.call_count == 3


@pytest.mark.asyncio
async def test_publish_to_kinesis_fail_no_retry(kinesis_client, mock_session, mock_message):
    """Tests that when an exception is not retryable, the function does not execute a retry"""
    with pytest.MonkeyPatch.context() as m:
        m.setattr("aioboto3.Session", lambda: mock_session)
        m.setattr(publish_to_kinesis.retry, "wait", wait_none())
        mock_session.client.return_value = kinesis_client
        kinesis_client.__aenter__.return_value = kinesis_client
        kinesis_client.put_record = AsyncMock(side_effect=TestException)
        kinesis_stream_name = "test_stream"
        with pytest.raises(TestException):
            await publish_to_kinesis(mock_message, mock_session, kinesis_stream_name)
        kinesis_client.put_record.assert_called_once_with(
            StreamName=kinesis_stream_name, Data=mock_message.body, PartitionKey=ANY
        )


@pytest.mark.asyncio
async def test_s3_upload_failed_message_failure(mock_session, s3_client):
    """Ensures that the s3 upload failed message function raises an error in failure"""
    with pytest.MonkeyPatch.context() as m:
        m.setattr("aioboto3.Session", lambda: mock_session)
        mock_session.client.return_value = s3_client
        s3_client.__aenter__.return_value = s3_client
        s3_client.put_object = AsyncMock()
        s3_client.put_object.side_effect = TestException("S3 error")

        with pytest.raises(TestException, match="S3 error"):
            await s3_upload_failed_message("test_bucket", FAILED_MESSAGE_KEY, TEST_BODY, mock_session)

        s3_client.put_object.assert_called_once_with(
            Bucket="test_bucket",
            Key=FAILED_MESSAGE_KEY,
            Body=TEST_BODY,
        )


@pytest.mark.asyncio
async def test_process_message_wrapper(tracker, mock_session, mock_message):
    """Tests the process_message_wrapper function by ensuring it adds the task to the tracker"""
    with pytest.MonkeyPatch.context() as m:
        task = asyncio.create_task(test_coroutine())
        m.setattr("asyncio.create_task", MagicMock(return_value=task))
        m.setattr("app.guest360_docker.ingestion.rabbitmq.main.process_message", AsyncMock())
        s3_bucket = "test_bucket"
        kinesis_stream_name = "test_stream"
        tracker.cancel()
        await process_message_wrapper(mock_message, mock_session, kinesis_stream_name, s3_bucket, tracker)

        assert task in tracker.tasks


@pytest.mark.asyncio
async def test_get_secret(secretsmanager_client, rabbitmq_credentials, mock_session):
    """Tests that secretsmanager correctly returns a credentials."""
    secret_name = "test_secret_name"  # pragma: allowlist secret
    secretsmanager_client.get_secret_value = AsyncMock()
    secretsmanager_client.get_secret_value.return_value = {
        "SecretString": json.dumps(rabbitmq_credentials),  # pragma: allowlist secret
    }

    with pytest.MonkeyPatch.context() as m:
        m.setattr("aioboto3.Session", lambda: mock_session)
        mock_session.client.return_value = secretsmanager_client
        secretsmanager_client.__aenter__.return_value = secretsmanager_client
        secretsmanager_client.get_secret = AsyncMock()
        result = await get_secret(secret_name, mock_session)

    assert result == rabbitmq_credentials
    secretsmanager_client.get_secret_value.assert_called_once_with(SecretId=secret_name)


@pytest.mark.asyncio
async def test_rabbitmq_connect_amqp(rabbit_config):
    """Tests that the rabbitmq connect function correctly formats amqp links"""
    mock_connection = AsyncMock(spec=aio_pika.abc.AbstractRobustConnection)
    mock_close = AsyncMock()
    with pytest.MonkeyPatch.context() as m:
        m.setattr(AIO_PIKA_CONNECT_ROBUST_PATCH, AsyncMock(return_value=mock_connection))
        mock_connection.close = mock_close
        m.setenv("USE_SSL", "False")
        async with rabbitmq_connect(rabbit_config):
            aio_pika.connect_robust.assert_called_once_with(
                host="test_host",
                port=5672,
                login="test_user",
                password="test_password",  # pragma: allowlist secret
                virtualhost="test_vhost",
                ssl=False,
            )
    # Assert that close is called after leaving the context
    mock_close.assert_called_once()


@pytest.mark.asyncio
async def test_rabbitmq_connect_amqps(rabbit_config):
    """Tests that the rabbitmq connect function correctly formats amqps links"""
    mock_connection = AsyncMock(spec=aio_pika.abc.AbstractRobustConnection)
    mock_close = AsyncMock()
    with pytest.MonkeyPatch.context() as m:
        m.setattr(AIO_PIKA_CONNECT_ROBUST_PATCH, AsyncMock(return_value=mock_connection))
        mock_connection.close = mock_close
        m.setenv("USE_SSL", "True")
        rabbit_config["port"] = "5671"
        async with rabbitmq_connect(rabbit_config):
            aio_pika.connect_robust.assert_called_once_with(
                host="test_host",
                port=5671,
                login="test_user",
                password="test_password",  # pragma: allowlist secret
                virtualhost="test_vhost",
                ssl=True,
            )
    # Assert that close is called after leaving the context
    mock_close.assert_called_once()


def test_setup_logging():
    """Tests that the setup logging function successfully creates the json logger"""
    json_logger = setup_logging()

    assert isinstance(json_logger, logging.Logger)
    assert json_logger.level == logging.INFO

    handler = json_logger.handlers[0]
    assert isinstance(handler, logging.StreamHandler)
    assert isinstance(handler.formatter, logging.Formatter)


@pytest.mark.asyncio
async def test_consume_success(mock_session, rabbit_config):
    """Tests the consume function ensuring it is successful, and with correct connection and channel closures on exit"""
    with pytest.MonkeyPatch.context() as m:
        mock_connection = AsyncMock(spec=aio_pika.abc.AbstractRobustConnection)
        mock_close = AsyncMock()
        rabbit_channel = MagicMock(spec=aio_pika.abc.AbstractRobustChannel)
        rabbit_queue = MagicMock(spec=aio_pika.abc.AbstractRobustQueue)
        mock_process = AsyncMock()
        mock_consume = AsyncMock()
        tracker = MagicMock(spec=TaskTracker)
        m.setattr(
            AIO_PIKA_CONNECT_ROBUST_PATCH,
            AsyncMock(return_value=mock_connection),
        )
        m.setattr("app.guest360_docker.ingestion.rabbitmq.main.process_message_wrapper", mock_process)
        m.setattr("asyncio.sleep", AsyncMock())
        m.setattr(consume.retry, "stop", stop_after_attempt(0))
        mock_connection.close = mock_close
        mock_connection.channel.return_value.__aenter__ = AsyncMock(return_value=rabbit_channel)
        rabbit_channel.get_queue = AsyncMock(return_value=rabbit_queue)
        rabbit_queue.consume = mock_consume
        tracker.check_tasks = AsyncMock(side_effect=StopTestingException("Stop testing exception"))
        with pytest.raises(StopTestingException):
            await consume(rabbit_config, 1, "test_queue", mock_session, "test_stream", "test_bucket", tracker)

        mock_consume.assert_called_once()
        mock_close.assert_called_once()
        assert mock_connection.channel.return_value.__aexit__.call_count == 1


@pytest.mark.asyncio
@pytest.mark.parametrize("exception_type", [TestException, asyncio.exceptions.CancelledError])
async def test_consume_retry(mock_session, rabbit_config, exception_type):
    """Tests the consume call retries, and that each time the connection and channel are successfully closed"""
    with pytest.MonkeyPatch.context() as m:
        mock_connection = AsyncMock(spec=aio_pika.abc.AbstractRobustConnection)
        mock_close = AsyncMock()
        rabbit_channel = MagicMock(spec=aio_pika.abc.AbstractRobustChannel)
        rabbit_queue = MagicMock(spec=aio_pika.abc.AbstractRobustQueue)
        mock_process = AsyncMock()
        mock_consume = AsyncMock()
        tracker = MagicMock(spec=TaskTracker)
        m.setattr(
            AIO_PIKA_CONNECT_ROBUST_PATCH,
            AsyncMock(return_value=mock_connection),
        )
        m.setattr("app.guest360_docker.ingestion.rabbitmq.main.process_message_wrapper", mock_process)
        m.setattr("asyncio.sleep", AsyncMock())
        m.setattr(consume.retry, "stop", stop_after_attempt(3))
        m.setattr(consume.retry, "wait", wait_none())
        mock_connection.close = mock_close
        mock_connection.channel.return_value.__aenter__ = AsyncMock(return_value=rabbit_channel)
        rabbit_channel.get_queue = AsyncMock(return_value=rabbit_queue)
        rabbit_queue.consume = mock_consume
        tracker.check_tasks = AsyncMock(side_effect=exception_type)
        with pytest.raises(exception_type):
            await consume(rabbit_config, 1, "test_queue", mock_session, "test_stream", "test_bucket", tracker)

        assert mock_consume.call_count == 3
        assert mock_close.call_count == 3
        assert mock_connection.channel.return_value.__aexit__.call_count == 3


@pytest.fixture
def orchestrator_test_context(mock_session, rabbitmq_credentials):
    with pytest.MonkeyPatch.context() as m:
        # Mock environment variables

        env_vars = {
            "RABBITMQ_SECRET_PATH": "test_secret",  # pragma: allowlist secret
            "RABBITMQ_QUEUE": "test_queue",
            "KINESIS_STREAM": "test_stream",
            "RABBITMQ_HOST": "test_host",
            "RABBITMQ_PORT": "5672",
            "RABBITMQ_VHOST": "test_vhost",
            "FAILED_MSG_BUCKET_NAME": "test_bucket",
            "MAX_RETRY_ATTEMPT": "1",
            "POLLING_TIME": ".1",
            "PREFETCH_COUNT": "10",
        }
        for key, value in env_vars.items():
            m.setenv(key, value)
        # Set local to false for this test
        main.LOCAL = False
        mock_get_secret = AsyncMock(return_value=rabbitmq_credentials)
        m.setattr("aioboto3.Session", lambda: mock_session)
        m.setattr("app.guest360_docker.ingestion.rabbitmq.main.get_secret", mock_get_secret)
        yield m


@pytest.mark.asyncio
async def test_orchestrator(mock_session, orchestrator_test_context, rabbit_config):
    """Test orchestrate function, use timeout error to exit loop"""

    # TODO: Mock vaious iterator functions to provide messages to process

    mock_consume = AsyncMock()
    orchestrator_test_context.setattr("app.guest360_docker.ingestion.rabbitmq.main.consume", mock_consume)
    await orchestrate()
    mock_consume.assert_called_once_with(
        rabbit_config=rabbit_config,
        prefetch_count=10,
        rabbit_queue_name="test_queue",
        aiosession=mock_session,
        kinesis_stream_name="test_stream",
        s3_bucket="test_bucket",
        tasks=ANY,
    )


@pytest.mark.asyncio
async def test_orchestrator_env_error():
    """Asserts that a KeyError is thrown for missing required environment variables"""
    # Missing Kinesis Stream
    with pytest.MonkeyPatch.context() as m:
        env_vars = {
            "RABBITMQ_SECRET_PATH": "test_secret",  # pragma: allowlist secret
            "RABBITMQ_QUEUE": "test_queue",
            "RABBITMQ_HOST": "test_host",
            "RABBITMQ_PORT": "5672",
            "RABBITMQ_VHOST": "test_vhost",
            "FAILED_MSG_BUCKET_NAME": "test_bucket",
            "MAX_RETRY_ATTEMPT": "0",
        }
        for key, value in env_vars.items():
            m.setenv(key, value)

        with pytest.raises(KeyError):
            # In case error isn't thrown, make sure function times out
            await asyncio.wait_for(orchestrate(), timeout=2)


@pytest.mark.asyncio
async def test_orchestrator_task_with_exception(orchestrator_test_context):
    """Test orchestrate function with an exception being raised in a task"""

    mock_connection = AsyncMock(spec=aio_pika.abc.AbstractRobustConnection)
    mock_close = AsyncMock()
    orchestrator_test_context.setattr(AIO_PIKA_CONNECT_ROBUST_PATCH, AsyncMock(return_value=mock_connection))
    mock_connection.close = mock_close

    async def task_that_raises_cancelled_error():
        raise asyncio.exceptions.CancelledError()

    with pytest.raises(asyncio.exceptions.CancelledError):
        with patch(
            "app.guest360_docker.ingestion.rabbitmq.main.asyncio.wait",
            return_value=((asyncio.create_task(task_that_raises_cancelled_error()),), tuple()),
        ), patch("app.guest360_docker.ingestion.rabbitmq.main.TaskTracker.has_tasks", lambda *args: True), patch(
            "app.guest360_docker.ingestion.rabbitmq.main.consume.retry.stop", stop_after_attempt(0)
        ):
            await orchestrate()

        assert mock_close.call_count == 2
        assert mock_connection.channel.return_value.__aexit__.call_count == 2


@pytest.mark.asyncio
async def test_orchestrator_exception_raised_during_connect(orchestrator_test_context):
    """Test the case where an error is experienced in the connection"""

    async def task_that_raises_cancelled_error():
        raise asyncio.exceptions.CancelledError()

    with patch("app.guest360_docker.ingestion.rabbitmq.main.rabbitmq_connect") as mock_rabbitmq_connect:
        mock_connection = AsyncMock(spec=aio_pika.abc.AbstractRobustConnection)
        rabbit_channel = MagicMock(spec=aio_pika.abc.AbstractRobustChannel)
        rabbit_queue = MagicMock(spec=aio_pika.abc.AbstractRobustQueue)
        mock_connection.channel.return_value.__aenter__ = AsyncMock(return_value=rabbit_channel)
        rabbit_channel.get_queue = AsyncMock(return_value=rabbit_queue)
        mock_close = AsyncMock()
        mock_connection.close = mock_close
        mock_rabbitmq_connect.return_value = mock_connection
        failing_task = asyncio.create_task(task_that_raises_cancelled_error())

        async def failing_connection():
            await asyncio.sleep(3)
            await failing_task
            return mock_connection

        mock_connection.__aenter__.side_effect = failing_connection
        with pytest.raises(asyncio.exceptions.CancelledError):
            await orchestrate()
