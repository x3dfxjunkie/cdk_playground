from unittest.mock import patch

from constructs import Construct
import pytest


class MockDockerImageAsset:
    asset_hash = "dummy_hash"
    image_uri = "dummy_uri"

    def __init__(self, *args, **kwargs) -> None:
        """Dummy init for mock"""
        pass


@pytest.fixture(autouse=True)
def mock_image_asset():
    # This will prevent docker image builds
    with patch("aws_cdk.aws_ecr_assets.DockerImageAsset", new=MockDockerImageAsset):
        yield


class MockECRDeployment(Construct):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args)


@pytest.fixture(autouse=True)
def mock_ecr_deployment():
    with patch("cdk_ecr_deployment.ECRDeployment", new=MockECRDeployment):
        yield


@pytest.fixture(autouse=True)
def mock_node_add_dependency():
    with patch("constructs.Node.add_dependency", return_value="dummy_dependency"):
        yield
