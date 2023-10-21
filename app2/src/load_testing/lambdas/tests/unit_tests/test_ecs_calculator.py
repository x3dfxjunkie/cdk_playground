"""
TestEcsCalculator
"""
import pytest
from app.src.load_testing.lambdas.ecs_calculator import lambda_function


class TestEcsCalculator:
    """
    TestEcsCalculator
    """

    @pytest.mark.parametrize(
        "expected_throughput, workers, total_users, expected_workers, spawn_rate",
        [(100, 1, 100, 1, 10), (1000, 3, 300, 3, 30), (10000, 25, 2500, 20, 250)],
    )
    def test_lambda_handler(self, expected_throughput, workers, total_users, expected_workers, spawn_rate):
        event = {
            "scenario_config": f"""
        phases:
            - name: normal
              duration_seconds: 3600
              arrival_rate: {expected_throughput}
            - name: peak
              duration_seconds: 1800 
              arrival_rate: 50000
        """
        }
        handler = None
        response = lambda_function.lambda_handler(event, handler)
        assert response["workers"] == workers
        assert response["total_users"] == f"{total_users}"
        assert response["expected_workers"] == f"{expected_workers}"
        assert response["spawn_rate"] == f"{spawn_rate}"
        assert response["seconds"] == 3600
        assert len(response["scenario_config"]) > 0

    def test_lambda_handler_system_test(self):
        event = {
            "test_type": "system",
            "scenario_config": f"""
        input:
            data:
                limit_records: 100
                duration_seconds: 3600
                
        """,
        }
        handler = None
        response = lambda_function.lambda_handler(event, handler)
        assert response["workers"] == 1
        assert response["total_users"] == "1"
        assert response["expected_workers"] == "1"
        assert response["spawn_rate"] == "1"
        assert response["seconds"] == 3600
        assert len(response["scenario_config"]) > 0
