from io import BytesIO
from app.src.data_structures.utilities.ui.dataclass_generator.utils.airtable import AirtableApi
from app.src.data_structures.utilities.ui.dataclass_generator.config.aws_client import AWSClient
from app.src.data_structures.utilities.ui.dataclass_generator.utils.utils import create_zip_file
from app.src.data_structures.utilities.ui.dataclass_generator.utils.data_contract_generator import (
    DataContractGenerator,
)


class DDLExtractor:
    def __init__(self, db_form_details: dict = None, pyairtable_api=None):
        self.pyairtable_api_obj = pyairtable_api
        self.airtable_api = None
        self.db_form_details = db_form_details

    def init_airtable_api(self):
        """
        Initiates Airtable API instance.
        """
        self.airtable_api = AirtableApi(self.pyairtable_api_obj)
        self.airtable_api.init_table()

    def get_connection_ids(self) -> list:
        """
        Gets the list of Connection Identifiers in Airtable.
        Returns:
            List of connection identifiers.
        """
        if not self.airtable_api:
            self.init_airtable_api()
        return self.airtable_api.get_column_list("Connection Identifier")

    def get_connection_details(self, conn_id: str) -> dict:
        """
        Gets database connection details from Airtable API given a value from Connection Identifier column.
        Args:
            conn_id: Connection Identifier value from Airtable.

        Returns:
            First match found on Airtable.
        """
        if not self.airtable_api:
            self.init_airtable_api()
        return self.airtable_api.get_first_match("Connection Identifier", conn_id)

    def config_dict_creator(self, secrets_dict: dict, form_dict: dict) -> dict:
        """
        Creates the proper configuration dictionary from the AWS Secrets Manager response
        and the web interface form.
        Args:
            secrets_dict (dict): AWS Secrets Manager response.
            form_dict (dict): Web interface form.

        Returns:
            dict: Database configuration dictionary.
        """
        conn_details = self.get_connection_details(form_dict.get("conn-id"))["fields"]
        config_dict = {
            "host": conn_details["Hostname"],
            "port": conn_details["Port"],
            "database": conn_details["Database Name"],
            "username": secrets_dict["username"],
            "password": secrets_dict["password"],
            "db_type": conn_details["RDBMS (from Source Pipeline)"][0],
            "source_name": form_dict["source_name"].lower(),
        }
        return config_dict

    def get_db_config(self) -> dict:
        """
        Gets database configuration dictionary from a given database form,
        that helps to get credentials from AWS Secrets Manager.
        Returns:

        """
        secrets_dict = AWSClient().get_secrets_client(self.db_form_details.get("secrets-path"))
        return self.config_dict_creator(secrets_dict, self.db_form_details)

    def get_tables(self) -> dict:
        db_config = self.get_db_config()
        tables = list(self.db_form_details.get("tables-list") or filter(None, [self.db_form_details.get("table-name")]))
        contract_gen = DataContractGenerator(db_config)
        response = {
            "show_contracts": False,
            "tables": tables or contract_gen.get_list_of_tables(),
            "source": db_config.get("source_name"),
        }

        if tables:
            contracts = contract_gen.get_data_contracts(tables[:20])
            response["contracts"] = contracts
            response["show_contracts"] = True

        return response

    def get_all_contracts_zip(self) -> BytesIO:
        """
        Function processes data contracts for all tables from Database given a configuration dictionary.
        Returns:
            BytesIO: Zip file bytes.
        """
        db_config = self.get_db_config()
        contract_gen = DataContractGenerator(db_config)
        tables = contract_gen.get_list_of_tables()
        contracts = contract_gen.get_data_contracts(tables)
        return create_zip_file(db_config.get("source_name"), tables, contracts)
