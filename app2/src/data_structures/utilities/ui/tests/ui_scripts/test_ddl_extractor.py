import json

from io import BytesIO
from unittest.mock import patch, MagicMock
from app.src.data_structures.utilities.ui.dataclass_generator.ui_scripts.ddl_extractor import DDLExtractor
from app.src.data_structures.utilities.ui.tests.conftest import (
    PATCH_DATACLASS_GEN_DIR,
    AWS_SECRET_MANAGER,
    DB_FORM_DETAILS,
    DB_AIRTABLE_DETAILS,
)


def init_airtable_api():
    ddl_extractor = DDLExtractor(DB_FORM_DETAILS, MagicMock())
    ddl_extractor.init_airtable_api()
    return ddl_extractor


@patch(f"{PATCH_DATACLASS_GEN_DIR}.ui_scripts.ddl_extractor.AirtableApi")
@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.aws_client.boto3.Session")
class TestDDLExtractor:
    def test__init__(self, boto3_session, airtable_api):
        ddl_extractor = DDLExtractor(DB_FORM_DETAILS)
        assert ddl_extractor.airtable_api is None
        assert ddl_extractor.db_form_details == DB_FORM_DETAILS

    def test_init_airtable_api(self, boto3_session, airtable_api):
        ddl_extractor = DDLExtractor(DB_FORM_DETAILS, MagicMock())
        ddl_extractor.init_airtable_api()
        assert ddl_extractor.airtable_api is not None

    def test_get_connection_ids(self, boto3_session, airtable_api):
        airtable_api.return_value.get_column_list.return_value = ["conn_id1", "conn_id2"]
        ddl_extractor = DDLExtractor(DB_FORM_DETAILS, MagicMock())
        ddl_extractor.init_airtable_api()
        conn_ids = ddl_extractor.get_connection_ids()
        assert isinstance(conn_ids, list)

    def test_get_connection_details(self, boto3_session, airtable_api):
        airtable_api.return_value.get_first_match.return_value = DB_AIRTABLE_DETAILS
        ddl_extractor = DDLExtractor(DB_FORM_DETAILS, MagicMock())
        ddl_extractor.init_airtable_api()
        conn_details = ddl_extractor.get_connection_details("Connection_ID")
        assert isinstance(conn_details, dict)
        assert conn_details == DB_AIRTABLE_DETAILS

    def test_config_dict_creator(self, boto3_session, airtable_api):
        secrets_dict = json.loads(AWS_SECRET_MANAGER["SecretString"])
        ddl_extractor = init_airtable_api()
        config_dict = ddl_extractor.config_dict_creator(secrets_dict, DB_FORM_DETAILS)
        expected_list = sorted(list(secrets_dict.keys()) + list(DB_FORM_DETAILS.keys()))
        assert expected_list == sorted(list(config_dict.keys()))

    def test_get_db_config(self, boto3_session, airtable_api):
        boto3_session.return_value.client.return_value.get_secret_value.return_value = AWS_SECRET_MANAGER
        airtable_api.return_value.get_first_match.return_value = DB_AIRTABLE_DETAILS
        ddl_extractor = init_airtable_api()
        db_config = ddl_extractor.get_db_config()
        assert isinstance(db_config, dict)
        assert "username" in db_config and "password" in db_config

    @patch(f"{PATCH_DATACLASS_GEN_DIR}.ui_scripts.ddl_extractor.DataContractGenerator")
    def test_get_table(self, contract_gen, boto3_session, airtable_api):
        contract_gen.generate_data_contract.return_value = ["data_contract_1", "data_contract_1", "data_contract_1"]
        boto3_session.return_value.client.return_value.get_secret_value.return_value = AWS_SECRET_MANAGER
        airtable_api.return_value.get_first_match.return_value = DB_AIRTABLE_DETAILS
        DB_FORM_DETAILS["tables-list"] = ["table_1", "table_2", "table_3"]
        ddl_extractor = init_airtable_api()
        response = ddl_extractor.get_tables()
        assert isinstance(response, dict)
        assert "contracts" in response
        assert response.get("show_contracts")

    @patch(f"{PATCH_DATACLASS_GEN_DIR}.ui_scripts.ddl_extractor.DataContractGenerator")
    def test_get_all_contracts(self, contract_gen, boto3_session, airtable_api):
        boto3_session.return_value.client.return_value.get_secret_value.return_value = AWS_SECRET_MANAGER
        airtable_api.return_value.get_first_match.return_value = DB_AIRTABLE_DETAILS
        ddl_extractor = init_airtable_api()
        zip_file = ddl_extractor.get_all_contracts_zip()
        assert isinstance(zip_file, BytesIO)
