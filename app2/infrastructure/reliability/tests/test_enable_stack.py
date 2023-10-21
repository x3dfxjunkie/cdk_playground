from pathlib import Path
import json
import copy

import pytest
import yaml

from aws_cdk import App, Stack

from app.infrastructure.reliability.enable_stack import DeployFlag

APP_FOLDER = Path(__file__).parents[3]
PROJECT_FOLDER = APP_FOLDER.parent
LABELER_FILE = PROJECT_FOLDER / ".github" / "labeler.yml"
STACK_CONFIG_FILE = APP_FOLDER / "ephemeral-stack-config.yaml"
CDK_JSON = APP_FOLDER / "cdk.json"
DEFAULT_CONTEXT = json.load(CDK_JSON.open())["context"]


class TestDeployFlag:
    @pytest.fixture
    @staticmethod
    def stack_config():
        return yaml.safe_load(STACK_CONFIG_FILE.open())

    @pytest.fixture
    @staticmethod
    def labeler_config():
        return yaml.safe_load(LABELER_FILE.open())

    @pytest.fixture
    @staticmethod
    def stack_all_false_config(stack_config):
        """Makes a clean stack config for testing"""
        ephemeral_stack_config = copy.deepcopy(stack_config)
        for _, stack_settings in ephemeral_stack_config["stacks"].items():
            stack_settings["force_enable"] = False
        return ephemeral_stack_config

    def test_config_structure(self, stack_config):
        """Test for structural validity ephemeral stack config"""
        for _, stack_settings in stack_config["stacks"].items():
            assert "force_enable" in stack_settings
            if "children" in stack_settings:
                assert isinstance(stack_settings["children"], list)
                for child in stack_settings["children"]:
                    assert child in stack_config["stacks"]
            if "required_by" in stack_settings:
                assert isinstance(stack_settings["required_by"], list)
                for dependent in stack_settings["required_by"]:
                    assert dependent in stack_config["stacks"]

    def test_stacks_in_config_also_in_labeler(self, stack_config, labeler_config):
        """Test that all stacks in the config are also in the labeler"""
        for stack_name in stack_config["stacks"]:
            assert stack_name in labeler_config

    def test_no_stacks_activated(self, stack_all_false_config):
        """Test that no stacks are activated by default"""
        context = {
            **DEFAULT_CONTEXT,
            "is_static_env": False,
        }
        app = App(context=context)
        stack = Stack(app, "testStack")

        for stack_name in stack_all_false_config["stacks"]:
            assert not DeployFlag.is_stack_enabled(stack, stack_name, stack_config=json.dumps(stack_all_false_config))

    def test_static_env_activation(self, stack_all_false_config):
        """Test that static envs always activate stacks"""
        context = {
            **DEFAULT_CONTEXT,
            "is_static_env": True,
        }
        app = App(context=context)
        stack = Stack(app, "testStack")
        assert DeployFlag.is_stack_enabled(stack, "Infrastructure", stack_config=json.dumps(stack_all_false_config))

    def test_pr_label_activation(self, stack_all_false_config):
        """Test that PR labels activate stacks"""
        context = {
            **DEFAULT_CONTEXT,
            "is_static_env": False,
            "github_pr_labels": json.dumps(["RandomLabel", "Infrastructure", "SomeOtherLabel"]),
        }
        app = App(context=context)
        stack = Stack(app, "testStack")
        assert DeployFlag.is_stack_enabled(stack, "Infrastructure", stack_config=json.dumps(stack_all_false_config))
        assert not DeployFlag.is_stack_enabled(stack, "Processing", stack_config=json.dumps(stack_all_false_config))

    def test_release_check_activation(self, stack_all_false_config):
        """Test that release check activates stacks"""
        context = {
            **DEFAULT_CONTEXT,
            "is_static_env": False,
            "release_check": True,
        }
        app = App(context=context)
        stack = Stack(app, "testStack")
        assert DeployFlag.is_stack_enabled(stack, "Infrastructure", stack_config=json.dumps(stack_all_false_config))

    def test_dependent_activation(self, stack_all_false_config):
        """Test that dependencies are accounted for. Covers forced activation."""
        context = {
            **DEFAULT_CONTEXT,
            "is_static_env": False,
        }
        app = App(context=context)
        stack = Stack(app, "testStack")
        stack_config = stack_all_false_config
        stack_config["stacks"]["DataService/Consumer"]["force_enable"] = True

        # This first assertion covers the explicit, manual, app/ephemeral-stack-config.yaml
        assert DeployFlag.is_stack_enabled(stack, "DataService/Consumer", stack_config=json.dumps(stack_config))

        # Verify parent activated
        assert DeployFlag.is_stack_enabled(stack, "DataService", stack_config=json.dumps(stack_config))

        # Verify parent's dependencies activated
        assert DeployFlag.is_stack_enabled(stack, "Processing", stack_config=json.dumps(stack_config))
        assert DeployFlag.is_stack_enabled(stack, "Identity", stack_config=json.dumps(stack_config))

        # Verify parent's dependencies' dependencies activated
        assert DeployFlag.is_stack_enabled(stack, "Ingestion", stack_config=json.dumps(stack_config))

        # Verify unnecessary stacks not activated
        assert not DeployFlag.is_stack_enabled(stack, "Infrastructure", stack_config=json.dumps(stack_config))
        assert not DeployFlag.is_stack_enabled(stack, "LoadTesting/Static", stack_config=json.dumps(stack_config))
