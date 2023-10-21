"""Utility module for common assertions within ingestion tests"""
from aws_cdk import assertions


def assert_template_contains_common_ingestion_resources(template: assertions.Template):
    template.resource_count_is("AWS::AppConfig::Deployment", 1)
    template.resource_count_is("AWS::Kinesis::Stream", 2)
    template.resource_count_is("AWS::Pipes::Pipe", 2)
    template.resource_count_is("AWS::Lambda::Function", 3)
    template.has_resource_properties(
        "AWS::Pipes::Pipe", {"SourceParameters": {"KinesisStreamParameters": {"ParallelizationFactor": 3}}}
    )


def assert_template_contains_dashboard_resources(template: assertions.Template):
    template.resource_count_is("AWS::CloudWatch::Dashboard", 1)
    for metric_name in ("rows_failed", "rows_warning"):
        template.has_resource_properties(
            "AWS::CloudWatch::Alarm",
            props={"MetricName": metric_name},
        )
