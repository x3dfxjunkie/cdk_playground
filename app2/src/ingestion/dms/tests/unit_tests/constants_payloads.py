"""
Module to define dms example payloads to use in tests:
 - EVENT_TASK_FAILED , EVENT_TASK_STARTED, EVENT_TASK_CREATED are example payloads that Event Bridge rule send to
   Step Function (and this to lambda task manager)
 - DESCRIBE_TASK_FAILED is what we got when describing a dms task after it fails using boto3 or aws cli
"""
DETAIL_TYPE_STATE_CHANGE = "DMS Replication Task State Change"
EVENT_SOURCE = "aws.dms"
TASK_ARN = "arn:aws:dms:us-east-1:123456789012:task:dmsreplicationtask01"

REPLICATION_TASK_PROPS = {
    "ReplicationTaskIdentifier": "dmsreplicationtask01",
    "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:source-endpoint",
    "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:target-endpoint",
    "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:ABCDE12345ABCDE12",
    "MigrationType": "full-load-and-cdc",
    "TableMappings": '{"TableMappings": [{"Type": "Include", "SourceSchema": "schema1", "SourceTable": "table1", "TargetTable": "table1"}, {"Type": "Exclude", "SourceSchema": "schema2", "SourceTable": "table2"}]}',
    "ReplicationTaskSettings": '{"TargetMetadata": {"TargetSchema": "target_schema"}}',
}

EVENT_TASK_FAILED_ORIGINAL = {
    "version": "0",
    "id": "f22b3ffd-5812-a762-c41f-d06c6de67d3e",
    "detail-type": DETAIL_TYPE_STATE_CHANGE,
    "source": EVENT_SOURCE,
    "account": "123456789012",
    "time": "2023-08-22T23:40:45Z",
    "region": "us-east-1",
    "resources": [TASK_ARN],
    "detail": {
        "eventType": "REPLICATION_TASK_FAILED",
        "detailMessage": "Last Error  ODBC general error. Stop Reason RECOVERABLE_ERROR Error Level RECOVERABLE",
        "type": "REPLICATION_TASK",
        "category": "Failure",
    },
}

# Event modified on file app/infrastructure/ingestion/ingestion_dms_task_manager.py ,EVENT BRIDGE SECTION
EVENT_TASK_FAILED = {
    "resource": TASK_ARN,
    "eventType": "REPLICATION_TASK_FAILED",
    "originalEvent": EVENT_TASK_FAILED_ORIGINAL,
}

EVENT_TASK_CREATED = {
    "version": "0",
    "id": "b94e5298-aa49-6d29-012a-a72f40e7dc1a",
    "detail-type": DETAIL_TYPE_STATE_CHANGE,
    "source": EVENT_SOURCE,
    "account": "123456789012",
    "time": "2023-08-22T02:54:23Z",
    "region": "us-east-1",
    "resources": [TASK_ARN],
    "detail": {
        "eventId": "DMS-EVENT-0074",
        "eventType": "REPLICATION_TASK_CREATED",
        "detailMessage": "The replication task has been created.",
        "type": "REPLICATION_TASK",
        "category": "Creation",
    },
}

EVENT_TASK_STARTED_ORIGINAL = {
    "version": "0",
    "id": "207c4235-99c8-ae77-273a-d7268f7028c5",
    "detail-type": DETAIL_TYPE_STATE_CHANGE,
    "source": EVENT_SOURCE,
    "account": "123456789012",
    "time": "2023-08-22T02:57:53Z",
    "region": "us-east-1",
    "resources": [TASK_ARN],
    "detail": {
        "eventId": "DMS-EVENT-0069",
        "eventType": "REPLICATION_TASK_STARTED",
        "detailMessage": "Replication task started, with flag, fresh start",
        "type": "REPLICATION_TASK",
        "category": "StateChange",
    },
}

EVENT_TASK_STARTED = {
    "resource": TASK_ARN,
    "eventType": "REPLICATION_TASK_STARTED",
    "originalEvent": EVENT_TASK_STARTED_ORIGINAL,
}

EVENT_TASK_STOPPED_ORIGINAL = {
    "version": "0",
    "id": "d3817571-08e8-94c9-36ec-beac509b35cc",
    "detail-type": DETAIL_TYPE_STATE_CHANGE,
    "source": EVENT_SOURCE,
    "account": "123456789012",
    "time": "2023-08-22T02:58:34Z",
    "region": "us-east-1",
    "resources": [TASK_ARN],
    "detail": {
        "eventId": "DMS-EVENT-0079",
        "eventType": "REPLICATION_TASK_STOPPED",
        "detailMessage": "Replication task stopped",
        "type": "REPLICATION_TASK",
        "category": "StateChange",
    },
}
EVENT_TASK_STOPPED = {
    "eventType": "REPLICATION_TASK_STOPPED",
    "resource": TASK_ARN,
    "originalEvent": EVENT_TASK_STOPPED_ORIGINAL,
}

DESCRIBE_TASK_FAILED = {
    "ReplicationTasks": [
        {
            "ReplicationTaskIdentifier": "dmsreplicationtask01",
            "SourceEndpointArn": "arn:aws:dms:us-east-1: 220271737897:endpoint:YWO4T52UX6QACRPB56EB2GNKNVR2QL2PDUIIXHA",
            "TargetEndpointArn": "arn:aws:dms:us-east-1: 220271737897:endpoint:N4ISDPQMIWQ7SSMZUVR5NPKTSNAAUQXCOAINN6Q",
            "ReplicationInstanceArn": "arn:aws:dms:us-east-1: 220271737897:rep:NMYWE2V7WNL7XTI6RZHPNDDXBTRYQV3M3M3RBZY",
            "MigrationType": "full-load-and-cdc",
            "TableMappings": """{
                "rules": [
                    {
                        "rule-type": "selection",
                        "rule-id": "1",
                        "rule-name": "1",
                        "object-locator": {
                            "schema-name": "michaeltestdb1",
                            "table-name": "retail_trans2"
                        },
                        "rule-action": "include",
                        "filters": []
                    },
                    {
                        "rule-type": "object-mapping",
                        "rule-id": "2",
                        "rule-name": "DefaultMapToKinesis",
                        "rule-action": "map-record-to-record",
                        "object-locator": {
                            "schema-name": "michaeltestdb1",
                            "table-name": "retail_trans2"
                        }
                    }
                ]
            }""",
            "ReplicationTaskSettings": """{
                "Logging": {
                    "EnableLogging": true,
                    "EnableLogContext": false,
                    "LogComponents": [
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "TRANSFORMATION"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "SOURCE_UNLOAD"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "IO"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "TARGET_LOAD"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "PERFORMANCE"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "SOURCE_CAPTURE"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "SORTER"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "REST_SERVER"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "VALIDATOR_EXT"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "TARGET_APPLY"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "TASK_MANAGER"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "TABLES_MANAGER"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "METADATA_MANAGER"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "FILE_FACTORY"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "COMMON"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "ADDONS"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "DATA_STRUCTURE"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "COMMUNICATION"
                        },
                        {
                            "Severity": "LOGGER_SEVERITY_DEFAULT",
                            "Id": "FILE_TRANSFER"
                        }
                    ],
                    "CloudWatchLogGroup": "dms-tasks-myinstance-mtaquia-01",
                    "CloudWatchLogStream": "dms-task-E2FDDWUKQJV7UCIKU3GCEWAXX6HYE5OKAILG7AA" # pragma: allowlist secret
                },
                "StreamBufferSettings": {
                    "StreamBufferCount": 3,
                    "CtrlStreamBufferSizeInMB": 5,
                    "StreamBufferSizeInMB": 8
                },
                "ErrorBehavior": {
                    "FailOnNoTablesCaptured": true,
                    "ApplyErrorUpdatePolicy": "LOG_ERROR",
                    "FailOnTransactionConsistencyBreached": false,
                    "RecoverableErrorThrottlingMax": 1800,
                    "DataErrorEscalationPolicy": "SUSPEND_TABLE",
                    "ApplyErrorEscalationCount": 0,
                    "RecoverableErrorStopRetryAfterThrottlingMax": true,
                    "RecoverableErrorThrottling": true,
                    "ApplyErrorFailOnTruncationDdl": false,
                    "DataTruncationErrorPolicy": "LOG_ERROR",
                    "ApplyErrorInsertPolicy": "LOG_ERROR",
                    "EventErrorPolicy": "IGNORE",
                    "ApplyErrorEscalationPolicy": "LOG_ERROR",
                    "RecoverableErrorCount": -1,
                    "DataErrorEscalationCount": 0,
                    "TableErrorEscalationPolicy": "STOP_TASK",
                    "RecoverableErrorInterval": 5,
                    "ApplyErrorDeletePolicy": "IGNORE_RECORD",
                    "TableErrorEscalationCount": 0,
                    "FullLoadIgnoreConflicts": true,
                    "DataErrorPolicy": "LOG_ERROR",
                    "TableErrorPolicy": "SUSPEND_TABLE"
                },
                "TTSettings": {
                    "TTS3Settings": null,
                    "TTRecordSettings": null,
                    "EnableTT": false
                },
                "FullLoadSettings": {
                    "CommitRate": 10000,
                    "StopTaskCachedChangesApplied": false,
                    "StopTaskCachedChangesNotApplied": false,
                    "MaxFullLoadSubTasks": 9,
                    "TransactionConsistencyTimeout": 600,
                    "CreatePkAfterFullLoad": false,
                    "TargetTablePrepMode": "DROP_AND_CREATE"
                },
                "TargetMetadata": {
                    "ParallelApplyBufferSize": 1000,
                    "ParallelApplyQueuesPerThread": 16,
                    "ParallelApplyThreads": 9,
                    "TargetSchema": "",
                    "InlineLobMaxSize": 0,
                    "ParallelLoadQueuesPerThread": 0,
                    "SupportLobs": true,
                    "LobChunkSize": 64,
                    "TaskRecoveryTableEnabled": false,
                    "ParallelLoadThreads": 0,
                    "LobMaxSize": 32,
                    "BatchApplyEnabled": false,
                    "FullLobMode": false,
                    "LimitedSizeLobMode": true,
                    "LoadMaxFileSize": 0,
                    "ParallelLoadBufferSize": 0
                },
                "BeforeImageSettings": null,
                "ControlTablesSettings": {
                    "historyTimeslotInMinutes": 5,
                    "HistoryTimeslotInMinutes": 5,
                    "StatusTableEnabled": false,
                    "SuspendedTablesTableEnabled": false,
                    "HistoryTableEnabled": false,
                    "ControlSchema": "",
                    "FullLoadExceptionTableEnabled": false
                },
                "LoopbackPreventionSettings": null,
                "CharacterSetSettings": null,
                "FailTaskWhenCleanTaskResourceFailed": false,
                "ChangeProcessingTuning": {
                    "StatementCacheSize": 50,
                    "CommitTimeout": 1,
                    "BatchApplyPreserveTransaction": true,
                    "BatchApplyTimeoutMin": 1,
                    "BatchSplitSize": 0,
                    "BatchApplyTimeoutMax": 30,
                    "MinTransactionSize": 1000,
                    "MemoryKeepTime": 60,
                    "BatchApplyMemoryLimit": 500,
                    "MemoryLimitTotal": 1024
                },
                "ChangeProcessingDdlHandlingPolicy": {
                    "HandleSourceTableDropped": true,
                    "HandleSourceTableTruncated": true,
                    "HandleSourceTableAltered": true
                },
                "PostProcessingRules": null
            }""",
            "Status": "failed",
            "LastFailureMessage": "Last Error  No tables were found at task initialization. Either the selected table(s) or schemas(s) no longer exist or no match was found for the table selection pattern(s). If you would like to start a Task that does not initially capture any tables, set Task Setting FailOnNoTablesCaptured to false and restart task. Stop Reason FATAL_ERROR Error Level FATAL",
            "StopReason": "Last Error  No tables were found at task initialization. Either the selected table(s) or schemas(s) no longer exist or no match was found for the table selection pattern(s). If you would like to start a Task that does not initially capture any tables, set Task Setting FailOnNoTablesCaptured to false and restart task. Stop Reason FATAL_ERROR Error Level FATAL",
            "ReplicationTaskCreationDate": None,
            "ReplicationTaskStartDate": None,
            "RecoveryCheckpoint": "",
            "ReplicationTaskArn": "arn:aws:dms:us-east-1: 220271737897:task:E2FDDWUKQJV7UCIKU3GCEWAXX6HYE5OKAILG7AA",
            "ReplicationTaskStats": {
                "FullLoadProgressPercent": 100,
                "ElapsedTimeMillis": 0,
                "TablesLoaded": 0,
                "TablesLoading": 0,
                "TablesQueued": 0,
                "TablesErrored": 0,
                "FreshStartDate": None,
                "StartDate": None,
                "StopDate": None,
            },
        }
    ],
    "ResponseMetadata": {
        "RequestId": "13df579f-0dad-4087-aa32-5687fa4b16ac",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "13df579f-0dad-4087-aa32-5687fa4b16ac",
            "date": "Wed,19 Apr 2023 21: 12: 38 GMT",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "6284",
        },
        "RetryAttempts": 0,
    },
}

DESCRIBE_INSTANCE = {
    "ReplicationInstances": [
        {
            "ReplicationInstanceIdentifier": "myinstance-01",
            "ReplicationInstanceClass": "dms.t3.medium",
            "ReplicationInstanceStatus": "available",
            "AllocatedStorage": 50,
            "InstanceCreateTime": "2023-05-18T13:34:29.396000-05:00",
            "VpcSecurityGroups": [{"VpcSecurityGroupId": "sg-07e3558ca309507a1", "Status": "active"}],
            "AvailabilityZone": "us-east-1a",
            "ReplicationSubnetGroup": {
                "ReplicationSubnetGroupIdentifier": "dmsreplicationsubnetgroup-ehyp1ausv7elkrif",
                "ReplicationSubnetGroupDescription": "DMS Replication Subnet Group",
                "VpcId": "vpc-0e793ed37223b5069",
                "SubnetGroupStatus": "Complete",
                "Subnets": [
                    {
                        "SubnetIdentifier": "subnet-0f358a64013fba210",
                        "SubnetAvailabilityZone": {"Name": "us-east-1b"},
                        "SubnetStatus": "Active",
                    },
                    {
                        "SubnetIdentifier": "subnet-0993c47265d96e07d",
                        "SubnetAvailabilityZone": {"Name": "us-east-1a"},
                        "SubnetStatus": "Active",
                    },
                ],
            },
            "PreferredMaintenanceWindow": "sat:03:17-sat:03:47",
            "PendingModifiedValues": {},
            "MultiAZ": False,
            "EngineVersion": "3.4.6",
            "AutoMinorVersionUpgrade": False,
            "KmsKeyId": "arn:aws:kms:us-east-1:188528706638:key/52b07a17-779d-4deb-8af8-45312ec74de2",
            "ReplicationInstanceArn": "arn:aws:dms:us-east-1:188528706638:rep:WNG7524P6U3G52K2K6OIB5SJ5QUNDYQT2OAQHGQ",
            "ReplicationInstancePrivateIpAddress": None,
            "ReplicationInstancePublicIpAddresses": [None],
            "ReplicationInstancePrivateIpAddresses": [None],
            "PubliclyAccessible": False,
        }
    ]
}
