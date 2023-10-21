import json
import aws_cdk.aws_dms as dms
from typing import Union

class Guest360ConfigDMSValidation():
    """
    Validation of DMS Types
    """
    
    def getDMSStorage(stack_config: dict) -> Union[str, None]:
        """Validate Storage Size is an integer and > 0

        Args:
            stack_config (dict): Pass in the value for the storage size to be validated

        Returns:
            str | None: Returns the value if it is an integer and it's value is > 0, or None if invalid
        """
        # Check if integer
        if isinstance(stack_config['dms']['dms_allocated_storage'], int) and stack_config['dms']['dms_allocated_storage'] > 0:
            return stack_config['dms']['dms_allocated_storage']
        else:
            return None

    def getDMSTableMappings(stack_config: dict) -> str:
        """Returns the JSON formatted filter for the DMS schema and table selection. 
        It will convert the string to JSON and back to String to validate the JSON input

        Args:
            stack_config (dict): Expects a valid JSON configuration

        Returns:
            str: returns the validated JSON configuration as a JSON string
        """
        # Simple validation to conver to a JSON object and then back to the string object that DMS is expecting.
        # This will provide a simple validation step for malformed data
        if stack_config['dms']['dms_table_mappings']:
            return json.dumps(json.loads(stack_config['dms']['dms_table_mappings']))
        else:
            return '{}'
