"""
retrieve data contract from appconfig resources 
"""
import boto3
import json
import os


def lambda_handler(_event, _context):
    # pylint: disable=unused-argument
    """
    Appconfig
    """
    appconfig_client = boto3.client("appconfig")
    config_list = get_configs_prefix(appconfig_client, _event)
    return config_list


# App Config
def get_configs_prefix(appconfig_client, _event):
    """function for build the array with all the appconfig profiles starting with the prefix,
    for each iteration the function append a dictionary to the array with the stack_extension"""
    list_of_configs = []
    dict_app = _event.get("app_config")

    hosted_conf = appconfig_client.get_hosted_configuration_version(
        ApplicationId=dict_app.get("data")["application_id"],
        ConfigurationProfileId=dict_app.get("data")["configuration_profile_id"],
        VersionNumber=dict_app.get("data")["version_number"],
    )
    content = hosted_conf["Content"].read()
    json_data = json.loads(content.decode("utf-8"))
    # Validation of Data contract , if empty do not append it to the list
    if "data_contracts" in json_data:
        dict_app["data_contracts"] = [
            dict((k, dc_dict[k]) for k in ["data_contract", "class_name"] if k in dc_dict)
            for dc_dict in json_data["data_contracts"]
        ]
        list_of_configs.append(json.dumps(dict_app))
    return list_of_configs
