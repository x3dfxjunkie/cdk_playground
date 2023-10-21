# kinesis_consumer

Generic construct for creating kinesis consumer stream resources
Will grant READONLY privileges to iam roles to all appropriate resources and allow kcl to add kinesis consumers based on iam role id prefix (WRITE).

## Resources Created

* producer - aws_cdk.aws_lambda.IFunction - given code to produce to kinesis consumer stream from provided kinesis stream
* producer_dlq - aws_cdk.aws_sqs.IQueue - dead letter queue for producer lambda.
* stream - aws_cdk.aws_kinesis.Stream - Consumer stream to allow x-account access to via api/kcl

## Properties

* stream_props - KinesisStreamProps
* lambda_producer_props - KinesisLambdaProducerProps
* lambda_producer_eventsource_props - KinesisLambdaProducerEventSourceProps
* role_configs - list[ KinesisKclRoleConfigProps ]

### KinesisStreamProps

Any dictionary elements not listed will be passed directly to the aws_cdk.kinesis construct

```
class KinesisStreamProps(TypedDict):
    stream_name: str
    stream_retention_days: int
```

### KinesisLambdaProducerProps

Any dictionary elements not listed will be passed directly to the aws_cdk.lambda construct

```
class KinesisLambdaProducerProps(TypedDict):
    runtime: aws_cdk.aws_lambda.Runtime
    code: aws_cdk.aws_lambda.Code
    handler: str
    timeout: int
    environment: dict

```

### KinesisLambdaProducerEventSourceProps

Any dictionary elements not listed will be passed directly to the aws_cdk.aws_lambda_event_sources construct

```
class KinesisLambdaProducerEventSourceProps(TypedDict):
    stream: aws_cdk.aws_kinesis.IStream

```

### KinesisKclRoleConfigProps

```
class KinesisKclRoleConfigProps(TypedDict):
    id: str
    role_arns: list[str]

```