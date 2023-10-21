"""Modules required by testutils class"""
import random
import string

import pytest

import app.src.reliability.utils as utils  # pylint: disable=consider-using-from-import


class TestUtils:
    """TestUtils

    This Class Tests the Util Functions in test_utils.py

    """

    prefix = "tst-use1-guest360"
    short_prefix = "tst-use1-g360"
    base_name = f"TestBaseName-{''.join(random.choice(string.ascii_letters) for i in range(256))}"

    print(f"{prefix=}")
    print(f"{base_name=}")

    def test_DynamoDBTableName(self):
        name = utils.DynamoDBTableName(self.prefix, self.base_name).name()
        print(f"{name=}")
        assert name == "-".join([self.prefix, self.base_name]).lower()[:255]

    def test_KinesisStreamName(self):
        name = utils.KinesisStreamName(self.prefix, self.base_name).name()
        print(f"{name=}")
        assert name == "-".join([self.prefix, self.base_name]).lower()[:128]

    def test_KmsKeyAliasName(self):
        name = utils.KmsKeyAliasName(self.prefix, self.base_name).name()
        print(f"{name=}")
        assert name == "-".join([self.prefix, self.base_name]).lower()[:256]

    def test_LambdaFunctionName(self):
        name = utils.LambdaFunctionName(self.prefix, self.base_name).name()
        print(f"{name=}")
        assert name == "-".join([self.prefix, self.base_name]).lower()[:64]

    def test_QueueName(self):
        name = utils.QueueName(self.prefix, self.base_name).name()
        print(f"{name=}")
        assert name == "-".join([self.prefix, self.base_name]).lower()[:80]

    def test_RoleName(self):
        name = utils.RoleName(self.prefix, self.base_name).name()
        print(f"{name=}")
        assert name == "-".join([self.prefix, self.base_name]).lower()[:64]

    def test_LogGroup(self):
        name = utils.LogGroup(self.prefix, self.base_name).name()
        print(f"{name=}")
        assert name == "-".join([self.prefix, self.base_name]).lower()[:512]

    def test_S3BucketName(self):
        name = utils.S3BucketName(self.prefix, self.base_name).name()
        print(f"{name=}")
        assert name == "-".join([self.prefix, self.base_name]).lower()[:63]

        base_name_bad_chars = "BaD.ucket_N@me"
        bad_name = utils.S3BucketName(self.prefix, base_name_bad_chars).name()
        assert bad_name == "-".join([self.prefix, "bad-ucket-n-me"]).lower()[:63]

        base_name_ending_hyphen = "bucket_name-"
        bad_name = utils.S3BucketName(self.prefix, base_name_ending_hyphen).name()
        print(f"{bad_name=}")
        assert bad_name == "-".join([self.prefix, "bucket-name"]).lower()[:63]

    def test_S3BucketNameStrip(self):
        bad_name = "abc" * 45
        test_bad_name = "-".join([self.prefix, "-".join(bad_name.split("c"))]).lower()[:63]
        name = utils.S3BucketName(self.prefix, "-".join(bad_name.split("c"))).name()
        print(f"{test_bad_name=}")
        print(f"{name=}")
        assert name == f"{self.prefix}-{'ab-' * 14}ab"

    def test_build_name_long_prefix(self):
        """test_build_name_long_prefix

        Tests build name to correctly handle a long prefix

        """
        max_length = 80
        long_prefix = f"{self.prefix}-{''.join(random.choice(string.ascii_letters) for i in range(256))}"
        build_name = utils.BuildName(long_prefix, self.base_name, max_length=max_length).name()
        assert build_name == long_prefix[:max_length].lower()

    def test_build_name_negative(self):
        """test_build_name_zero

        Should raise error if value is negative

        """
        with pytest.raises(Exception):
            max_length = -1
            utils.BuildName("", "", max_length=max_length)

    def test_stack_name(self):
        """test_stack_name

        Tests if stack name contains basic functionality of the BuildName

        """
        build_name = utils.StackName("prefix", "basename")
        assert build_name.name() == "prefix-basename"

        # Makes sure that StackName is apart of BuildName
        # Ensures that the Build Name Tests still applies
        assert isinstance(build_name, utils.BuildName)

    def test_stack_name_characters(self):
        """test_stack_name

        Tests if stack name is ignored by illegal characters

        """
        base_name_bad_chars = "BaD_N@me"
        build_name = utils.StackName(self.prefix, base_name_bad_chars)
        assert build_name.name() == "tst-use1-guest360-bad-n-me"

        base_name_bad_chars = "______a"
        build_name_illegal_character = utils.StackName(self.prefix, base_name_bad_chars)
        assert build_name_illegal_character.name() == "tst-use1-guest360-------a"

    def test_event_bridge_pipe_good_name(self):
        base_name = "testing"
        name = utils.EventBridgePipeName(self.prefix, base_name).name()
        assert name == f"{self.prefix}-{base_name}"

    def test_event_bridge_pipe_invalid_name(self):
        base_name = "@testing@&^_)()FUN"
        name = utils.EventBridgePipeName(self.prefix, base_name).name()
        assert name == f"{self.prefix}-testing-fun"

    def test_shorten_prefix(self):
        new_prefix = utils.shorten_prefix(self.prefix)
        assert new_prefix == self.short_prefix

    def test_dms_resource_good_name(self):
        base_name = "testing"
        name = utils.DMSResourceName(self.prefix, base_name).name()
        assert name == f"{self.short_prefix}-{base_name}"

    def test_dms_resource_invalid_name(self):
        base_name = "@test@&^_)()FUN"
        name = utils.DMSResourceName(self.prefix, base_name).name()
        assert name == f"{self.short_prefix}-test-fun"

    def test_state_machine_good_name(self):
        base_name = "testing"
        name = utils.StateMachine(self.prefix, base_name).name()
        assert name == f"{self.prefix}-{base_name}"

    def test_state_machine_invalid_name(self):
        base_name = "thisnameissuperduperduperduperduperduperridiculouslywaytooooooooooooooooowaytoolong"
        name = utils.StateMachine(self.prefix, base_name).name()
        assert name == f"{self.prefix}-thisnameissuperduperduperduperduperduperridiculouslywaytoooooo"

    def test_dashboard_good_name(self):
        base_name = "testing"
        name = utils.DashboardName(self.prefix, base_name).name()
        assert name == f"{self.prefix}-{base_name}"

    def test_dashboard_invalid_name(self):
        base_name = "test@FUN"
        name = utils.DashboardName(self.prefix, base_name).name()
        assert name == f"{self.prefix}-test-fun"
