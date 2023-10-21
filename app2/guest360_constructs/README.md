# Guest360 L2 Constructs


### Importing

All of these constructs need to be imported before they can used. Your `PYTHONPATH` environment variable must include the root of the repository or there will be run-time errors.

```bash
export PYTHONPATH="/path/to/repo/guest360:${PYTHONPATH}"
```

Import the IAM Role construct:
```python
from app.guest360_constructs.iam_role import Guest360IamRole
```

### iam_role.py
---
Guest360 Construct for IAM Roles.

This includes some hard - coded values, as well as some overrideable defaults.
Required props:
```
{
    "assumed_by": IPrincipal,
    "description": string,
}
```

Optional props:
```
{
    "max_session_duration": aws_cdk.Duration  # Time a session is valid for. Lowest value is 15 minutes, default is 1 hour.
    "path": string                            # Logical path of the role. Only used for filtering.
}
```

Usage:
```
Guest360IamRole(self, f"{self.stack_name}-lambda-role",
                            {
                                'assumed_by': aws_iam.ServicePrincipal('lambda.amazonaws.com'),
                                'description': 'Lambda role for process.'
                            })
```

Retrieving a role by name is made easier via the class method, from_role_name.  This leverages
the RoleName function to dynamically produce the proper iam role name and perform a lookup.
Note that the actual lookup is done during cft deployment and an Irole is always returned by this method.

Usage:

```
lambda_role_by_name = Guest360IamRole.from_role_name(self, f"{self.stack_name}-lambda-role", "lambda")
```

Retrieving a role by arn is can also be done via the Gest360IamRole construct by passing the same arguments that aws cdk uses for Role.from_role_arn.
Note that the actual lookup is done during cft deployment and an Irole is always returned by this method.

Usage:

```
lambda_role_by_arn = Guest360IamRole.from_role_arn(self, f"{self.stack_name}-lambda-role", "aws:iam:role:arn")
```

### kinesis_datastream.py
---

* Enforces encryption using aws_kms.Ikey
  * if Ikey is not supplied one is created using the Guest360KMSKey
* retention_period for 'latest' environment set to 24 hours for cost savings
* stream_mode set to ON_DEMAND for 'latest' environment for cost savings

Example:
```
Guest360KinesisDatastream(stack, "MyKinesisDatastream")
```

Args:
* scope(Construct360): scope
* construct_id(str): Construct ID
* encryption_key(Optional[aws_kms.IKey]): encryption_key
* retention_period(aws_cdk.Duration): retention_period
* shard_count(Union[int, float, None]): shard_count
* stream_mode(aws_kinesis.StreamMode): stream_mode
* stream_name(Optional[str]): stream_name
* kwargs:

Returns:
    None

### kms_key.py
---

Guest360 Construct for KMS Keys.

This includes some hard-coded values, as well as some overrideable defaults.
Required props:
```python
{
    "alias": string,
}
```

Optional props:
```python
{
    "description": string  # Description of the key.
    "enabled": bool  # Enable or disable this key. Defaults to True.
    "pending_window": aws_cdk.Duration  # How long a key is pending delete before it's gone for good. Prod defaults to None, otherwise 7 days.
    "removal_policy": aws_cdk.RemovalPolicy  # destroy with the stack or not. Latest default to DESTROY, otherwise RETAIN.
}
```

Usage:
```python
Guest360KMSKey(self, f"{self.stack_name}-encryption-key-{id}",
                {
                    'alias': f"{prefix}-encryption-key",
                })
```

### kms_key_v2.py
---

Guest360 Construct for KMS Keys. This version extends the default aws_kms construct, and includes imporovements to allow decrypt access by tags.

This includes some hard-coded values, as well as some overrideable defaults.

Optional props:
```python
{
    "alias": string,
    "description": string  # Description of the key.
    "enabled": bool  # Enable or disable this key. Defaults to True.
    "pending_window": aws_cdk.Duration  # How long a key is pending delete before it's gone for good. Prod defaults to None, otherwise 7 days.
    "removal_policy": aws_cdk.RemovalPolicy  # destroy with the stack or not. Latest default to DESTROY, otherwise RETAIN.
    "tags_for_read": dict  # This is a dictionary of Tag/Value pairs to allow read access. All of the pairs must be present and match on the requester side to work.
}
```

Usage:
```python
Guest360KMSKey(self, "encryption-key-for-source",
                {
                    "alias": "encryption-key",
                    "tags_for_read": {"Source": "Dreams"},
                })
```

### lambda_function.py

Lambda Function Construct to wrap aws_lambda.Function
Handles Guest360 naming standards
LambdaFunctionProps - Any dictionary elements not listed will be passed directly to the aws_cdk.aws_lambda construct

```python
class LambdaFunctionProps(TypedDict):
    code: aws_lambda.Code
    description: str
    function_name: str
    handler: str
    runtime: aws_lambda.Runtime


class LambdaDockerProps(TypedDict):
    code: aws_lambda.DockerImageCode
    description: str
    function_name: str

```

```python
class Guest360LambdaFunction(Construct360):
    """Guest360 Construct for lambda function"""

    @property
    def function(self) -> Union[aws_lambda.Function, aws_lambda.DockerImageFunction]:
        return self._function

    @property
    def function_name(self) -> str:
        return self._function_name

    def __init__(self, scope: Construct, construct_id: str, props: Union[LambdaFunctionProps, LambdaDockerProps], **kwargs) -> None:

```


### s3_bucket.py
---

Guest360 Construct for S3 buckets.

This includes some hard-coded values, as well as some overrideable defaults.
Required props:
```
{
    "bucket_name": string
}
```

Optional props:
```
{
    "auto_delete_objects": bool  # Automatically delete objects before destroying the bucket. Defaults to True in latest.
    "block_public_access": aws_cdk.aws_s3.BlockPublicAccess # Specifies the policy regarding public access. Defaults to BLOCK_ALL.
    "bucket_key_enabled": bool  # Normal KMS or Bucket Key. Cost and security trade-offs. Defaults to True.
    "encryption_key": aws_cdk.aws_cdk.IKey  # KMS encryption key to use for SSE. If this is blank, a new one is created.
    "lifecycle_rules": list(dict) or list(aws_cdk.aws_s3.LifecycleRule)  # List of rules for object lifecycles.
    "removal_policy": aws_cdk.RemovalPolicy  # Policy about retaining or destroying this bucket on stack destroy. Defaults to DESTROY in latest.
    "versioned": bool  # Enable/disable object versioning. Defaults to True.
}
```

Usage:
```
Guest360S3Bucket(self, f"{stack_name}-pipeline-bucket", current_region,
                {
                    "bucket_name": f"{stack_name}-my-special-bucket",
                })
```

### sns_topic.py
---

Guest360 Construct for SNS Topics.

This includes some hard-coded values, as well as some overrideable defaults.
Required props:
```
{
    "topic_name": string,
}
```

Optional props:
```
{
    "content_based_deduplication": bool # Enables content-based deduplication for FIFO topics. Default: None
    "display_name": string # A developer-defined string that can be used to identify this SNS topic. Default: None
    "fifo": bool # Set to true to create a FIFO topic. Default: None
    "master_key": IKey # A KMS Key, either managed by this CDK app, or imported. Default: 'alias/aws/sns'
}
```

Usage:
```
Guest360SNSTopic(self, f"{self.stack_name}-notification-topic",
                {
                    'topic_name': f"{stack_name}-notifications",
                })
```
