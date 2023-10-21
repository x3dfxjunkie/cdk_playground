"""
ECS calculator lambda_handler
"""
import math

import yaml


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    """
    ECS calculator lambda_handler
    """

    scenario_config = yaml.safe_load(event.get("scenario_config"))
    test_type = event.get("test_type", "load")

    if test_type == "system":
        return calculate_system_test_config(scenario_config)
    else:
        return calculate_load_test_config(scenario_config)


def calculate_system_test_config(scenario_config):
    limit_records = scenario_config.get("input").get("data").get("limit_records")
    duration_seconds = scenario_config.get("input").get("data").get("duration_seconds", 60)

    # default the number of workers and locust users in a system test
    # setting the number of locust to 1 to control the number of records sent to targets
    test_parameters = {
        "scenario_config": scenario_config,
        "limit_records": limit_records,
        "workers": 1,
        "expected_workers": "1",
        "total_users": "1",
        "spawn_rate": "1",
        "seconds": duration_seconds,
    }

    return test_parameters


def calculate_load_test_config(scenario_config):
    arrival_rate = scenario_config.get("phases")[0].get("arrival_rate", 1)
    duration_seconds = scenario_config.get("phases")[0].get("duration_seconds", 60)

    test_parameters = set_test_parameters(arrival_rate, duration_seconds)

    test_parameters["scenario_config"] = scenario_config

    return test_parameters


def set_test_parameters(arrival_rate, duration_seconds):
    max_events_per_worker = 400
    max_users_per_worker = 100
    workers_threshold = 0.8
    spawn_rate_per_worker = 10
    expected_throughput = arrival_rate
    workers = math.ceil(expected_throughput / max_events_per_worker)
    total_users = workers * max_users_per_worker
    expected_workers = math.ceil(workers * workers_threshold)
    spawn_rate = spawn_rate_per_worker * workers

    return {
        "workers": workers,
        "total_users": f"{total_users}",
        "expected_workers": f"{expected_workers}",
        "spawn_rate": f"{spawn_rate}",
        "seconds": duration_seconds,
    }
