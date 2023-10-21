import pytest
from app.guest360_constructs.kms_key import Guest360KMSKey
from aws_cdk import App, Stack, assertions

TEST_CONTEXT = {
    "prefix": "lst-test_sns_topic-use1",
}


@pytest.mark.timeout(30, method="signal")
def test_kms_key_created():
    app = App(context=TEST_CONTEXT)
    stack = Stack(app)
    Guest360KMSKey(stack, "KMSKey", {"alias": "test_kms_key"})
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::KMS::Key", 1)
