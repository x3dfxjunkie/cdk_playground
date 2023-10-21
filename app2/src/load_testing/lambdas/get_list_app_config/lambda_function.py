"""
retrieve list of appconfig resources 
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
    prefix = os.getenv("prefix")
    filter_app_id = (
        _event.get("filter_app_id") if _event.get("filter_app_id") and _event.get("filter_app_id") != "" else None
    )

    config_list = get_configs_prefix(appconfig_client, prefix, filter_app_id)
    return config_list


# App Config
def get_configs_prefix(appconfig_client, prefix, filter_app_id=None):
    """function for build the array with all the appconfig profiles starting with the prefix,
    for each iteration the function append a dictionary to the array with the stack_extension and data contracts"""
    list_of_configs = []
    response = retrieve_list_token(appconfig_client)

    for apps_ids in response:
        if apps_ids["Name"].startswith(prefix) and (not filter_app_id or filter_app_id in apps_ids["Name"]):
            dict_app = {
                "name": apps_ids["Name"],
                "stack_extension": transform_string(apps_ids["Name"], prefix),
                "data": None,
            }
            # Retrieve the list of profiles to get the Id
            profile = appconfig_client.list_configuration_profiles(ApplicationId=apps_ids["Id"])
            for profile_id in profile.get("Items", []):
                # Getting the hosted_configuration_version  to get the VersionNumber
                version = appconfig_client.list_hosted_configuration_versions(
                    ApplicationId=apps_ids["Id"], ConfigurationProfileId=profile_id["Id"]
                )
                for version_id in version.get("Items", []):
                    dict_app["data"] = {
                        "application_id": apps_ids["Id"],
                        "configuration_profile_id": profile_id["Id"],
                        "version_number": version_id["VersionNumber"],
                    }
                    list_of_configs.append(json.dumps(dict_app))
    return list_of_configs


def transform_string(input_string, prefix):
    """this function returns as string the stack_extension
    filter from the appconfig name"""
    if input_string.startswith(prefix):
        parts = input_string[len(prefix + "-") : -len("-app")].split("-")
    else:
        return "Invalid Input string , not matching with prefix"
    result = "-".join(parts)
    return result


def retrieve_list_token(appconfig_client):
    """retrieve all the list applications using
    the next token taking in account the pagination of the api"""
    next_token = ""
    list_config = []
    # The next_token is None in the last list_application operation
    while next_token is not None:
        if next_token != "":
            response = appconfig_client.list_applications(NextToken=next_token)
            list_config.extend(response["Items"])
            next_token = response.get("NextToken")
            continue
        # First execution, in order to retrieve the next_token paginator
        response = appconfig_client.list_applications()
        list_config = response.get("Items")
        next_token = response.get("NextToken")
    return list_config
