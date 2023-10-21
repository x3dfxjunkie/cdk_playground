"""
    Class Utils for appconfig
"""
import json
import boto3


class AppConfigUtils:
    """
    Class Utils for appconfig
    """

    def __init__(self, appconfig_data):
        if isinstance(appconfig_data, str):
            appconfig_data = json.loads(appconfig_data)

        self.appconfig_data = appconfig_data
        appconfig_client = boto3.client("appconfig")

        hosted_conf = appconfig_client.get_hosted_configuration_version(
            ApplicationId=self.appconfig_data.get("data")["application_id"],
            ConfigurationProfileId=self.appconfig_data.get("data")["configuration_profile_id"],
            VersionNumber=self.appconfig_data.get("data")["version_number"],
        )
        content = hosted_conf["Content"].read()
        self.app_data = json.loads(content.decode("utf-8"))

    def data_contract_list(self):
        """Return a list of data_contract and class_name for each item inside DataContracts key."""
        result = []
        for data_contract in self.app_data["data_contracts"]:
            result.append({"data_contract": data_contract["data_contract"], "class_name": data_contract["class_name"]})
        return result

    def kinesis_target_name(self, suffix):
        """Return a name string given suffix, using the stack_extension key."""
        stack_extension = self.appconfig_data["stack_extension"]
        return f"{stack_extension}-{suffix}"
