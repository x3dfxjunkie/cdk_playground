"""Custom exceptions, enums and functions for lambda_task_manager.py
"""
from enum import Enum


class UnknownMigrationTypeError(Exception):
    """Custom exception for unknown migration types"""


class UnknownManualTaskError(Exception):
    """Custom exception for unknown manual tasks"""


class ReplicationInstanceNotAvailable(Exception):
    """Custom exception for handling a replication instance never becoming available"""


class ReplicationInstanceNotFound(Exception):
    """Custom exception for handling a replication instance not being found after calling describe"""


class ReplicationTaskCreatingStatus(Exception):
    """Custom exception for dms replication task creating status"""


class ReplicationTaskNotReadyStatus(Exception):
    """Custom exception for dms replication task starting and stopping status"""


class UnableToExecuteManualTaskError(Exception):
    """Custom exception for failures to execute a manual task like start/stop/reload/resume"""


class MigrationType(str, Enum):
    """DMS Migration Type: 'full-load'|'cdc'|'full-load-and-cdc'"""

    FULL_LOAD: str = "full-load"
    CDC: str = "cdc"
    FULL_LOAD_AND_CDC: str = "full-load-and-cdc"


class StartReplicationTaskType(str, Enum):
    """Valid Values from docs
    (https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#API_StartReplicationTask_RequestSyntax)
    """

    START_REPLICATION: str = "start-replication"
    RESUME_PROCESSING: str = "resume-processing"
    RELOAD_TARGET: str = "reload-target"


class ManualTask(str, Enum):
    """States for a DMS Task. RESTART: Restart the full load operation from the beginning.
    RESUME: Resume the task from the last stopped point.
    """

    START: str = "start"
    STOP: str = "stop"
    RESUME: str = "resume"
    RELOAD: str = "reload"


# Note: this enums may be overkill, but I wanted to include all states in case
# we wanted to include further custom logic based on task/instance state
class DMSReplicationTaskStatus(str, Enum):
    """Valid values from docs (https://docs.aws.amazon.com/cli/latest/reference/dms/describe-replication-tasks.html)"""

    MOVING: str = "moving"
    CREATING: str = "creating"
    READY: str = "ready"
    FAILED: str = "failed"
    DELETING: str = "deleting"
    STARTING: str = "starting"
    RUNNING: str = "running"
    STOPPED: str = "stopped"
    STOPPING: str = "stopping"
    MODIFYING: str = "modifying"
    FAILED_MOVE: str = "failed-move"
    TESTING: str = "testing"


class DMSReplicationInstanceStatus(str, Enum):
    """Valid values from docs (https://docs.aws.amazon.com/cli/latest/reference/dms/describe-replication-instances.html)"""

    AVAILABLE: str = "available"
    CREATING: str = "creating"
    DELETED: str = "deleted"
    DELETING: str = "deleting"
    FAILED: str = "failed"
    MODIFYING: str = "modifying"
    UPGRADING: str = "upgrading"
    REBOOTING: str = "rebooting"
    STORAGE_FULL: str = "storage-full"
    INCOMPATIBLE_CREDENTIALS: str = "incompatible-credentials"
    INCOMPATIBLE_NETWORK: str = "incompatible-network"
    RESETTING_MASTER_CREDENTIALS: str = "resetting-master-credentials"


class DMSReplicationTaskEventCategory(str, Enum):
    """Not Found a legitimate doc for valid values, completed the list based in real payloads"""

    CREATION: str = "Creation"
    STATE_CHANGE: str = "StateChange"
    FAILURE: str = "Failure"
    DELETION: str = "Deletion"


class DMSReplicationTaskEventType(str, Enum):
    """Not Found a legitimate doc for valid values, completed the list based on real payloads"""

    TASK_CREATED: str = "REPLICATION_TASK_CREATED"
    TASK_STARTED: str = "REPLICATION_TASK_STARTED"
    TASK_FAILED: str = "REPLICATION_TASK_FAILED"
    TASK_STOPPED: str = "REPLICATION_TASK_STOPPED"
    TASK_DELETED: str = "REPLICATION_TASK_DELETED"
    READING_PAUSED_SWAP_FILES_LIMIT_REACHED: str = "READING_PAUSED_SWAP_FILES_LIMIT_REACHED"
