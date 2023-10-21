import glob
import logging
import os
from typing import List

import yaml

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def static_config_from_path(path_pattern: str):
    
    returned_config_data = []
    list_of_config_file_names = glob.glob(path_pattern)
    for config_file_name in list_of_config_file_names:
        fn = os.path.basename(config_file_name).split('.')[0]

        if not os.path.isfile(config_file_name):
            logger.info(
                f"{config_file_name} config file not found. Will not run Construct for this Stack.")
            return
        
        with open(config_file_name) as f:
            # stack_config = yaml.safe_load(f)
            stack_config = yaml.unsafe_load(f)
            returned_config_data.append(stack_config)
    
    return returned_config_data

def config_from_path(path_pattern: str) -> List[dict]:
    """Dynamically returns configuration code based on glob library.

    Args:
        path_pattern (str): Path an arguement using the glob library syntax to return a list of config files.

    Returns:
        List[dict]: This is a list of dictionaries loaded with config data, both infra/app, for provisioning AWS resources in CDK
    """

    returned_config_data = []
    list_of_config_file_names = glob.glob(path_pattern)
    for config_file_name in list_of_config_file_names:
        fn = os.path.basename(config_file_name).split('.')[0]

        if not os.path.isfile(config_file_name):
            logger.info(
                f"{config_file_name} config file not found. Will not run Construct for this Stack.")
            return
        
        with open(config_file_name) as f:
            # stack_config = yaml.safe_load(f)
            stack_config = yaml.unsafe_load(f)

            sc = stack_config['stack_extension']
            if sc != fn:
                logger.exception(f'Issues with path {config_file_name}.')
                logger.exception(
                    f"Filename and stack_extension do not match. \n Filename: {fn} \n Stack_extension: {sc}")
                raise Exception('Check your configuration file...')
            else:
                d = {'construct_name': fn, 'stack_config': stack_config}
        
                returned_config_data.append(d)

    return returned_config_data
