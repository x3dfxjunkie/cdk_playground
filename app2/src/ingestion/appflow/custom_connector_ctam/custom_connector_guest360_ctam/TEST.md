# Commands to test 

## Using aws cli to manually test AppFlow lambda in LocalStack.
```shell
awslocal lambda invoke \
--function-name lcl-use1-guest360-ctam-appflow \
--invocation-type Event \
--payload file:///workspace/app/src/ingestion/appflow/custom_connector_ctam/custom_connector_guest360_ctam/test/resources/retrieve_data_request_valid.json test
```

## Using aws cli to manually test AppFlow lambda in AWS.
```shell
aws lambda invoke \
--function-name lcl-use1-guest360 \
--invocation-type Event \
--payload file:///workspace/app/src/ingestion/appflow/custom_connector_ctam/custom_connector_guest360_ctam/test/resources/retrieve_data_request_valid.json test

```


