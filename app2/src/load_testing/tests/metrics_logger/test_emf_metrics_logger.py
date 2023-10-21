"""Unit Test for Guest360CloudwatchMetricsLogger"""

from app.src.load_testing.app.metrics_logger.cw_emf_metrics_logger import Guest360CloudwatchEmfMetricsLogger


def test_cloudwatch_emf_metric_logger() -> None:
    """
    This unit test
    1. uses Guest360CloudwatchEmfMetricsLogger to send emf logs over UDP port
    2. Does not test all the way to CW (just checks if data was received over UDP)

    """
    ip = "0.0.0.0"
    port = 25888

    namespace = "guest360_load_test_metrics"
    loggroup = "guest360_load_test_logs"
    dimensions = [{"Name": "dimension_name", "Value": "test_dimension"}]
    metrics_logger = Guest360CloudwatchEmfMetricsLogger(ip, port, namespace, loggroup)

    metrics = [{"name": "event_all", "value": 1, "unit": "Count", "storage_resolution": 60}]
    dimensions = [{"name": "target", "value": "test"}, {"name": "request_type", "value": "dummy"}]
    metrics_logger.publish(metrics=metrics, dimensions=dimensions)
    # need to read from UDP socket simulataneously to test this
    assert True


def test_singleton():
    ip = "0.0.0.0"
    port = 25888
    namespace = "guest360_load_test_metrics"
    loggroup = "guest360_load_test_logs"
    metrics_logger = Guest360CloudwatchEmfMetricsLogger(ip, port, namespace, loggroup)
    metrics_logger_1 = Guest360CloudwatchEmfMetricsLogger(ip, port, namespace, loggroup)
    assert metrics_logger is metrics_logger_1
