from unittest.mock import MagicMock
from app.src.data_structures.utilities.ui.dataclass_generator.utils.airtable import AirtableApi
from app.src.data_structures.utilities.ui.tests.conftest import (
    AIRTABLE_FILTER_COLUMN,
    DB_AIRTABLE_DETAILS,
)


class TestAirtableApi:
    def test__init__(self):
        airtable = AirtableApi(MagicMock())
        assert airtable.api
        assert airtable.table is None
        assert airtable.base_id is None
        assert airtable.table_id is None

    def test_init_table(self):
        airtable = AirtableApi(MagicMock())
        airtable.init_table()
        assert airtable.table is not None

    def test_get_column_list(self):
        airtable_api_mock = MagicMock()
        airtable_api_mock.Api.return_value.table.return_value.all.return_value = AIRTABLE_FILTER_COLUMN
        airtable = AirtableApi(airtable_api_mock)
        airtable.init_table()
        column_list = airtable.get_column_list("Connection Identifier")
        assert isinstance(column_list, list)
        assert "Test Connection ID" in column_list

    def test_get_first_match(self):
        airtable_api_mock = MagicMock()
        airtable_api_mock.Api.return_value.table.return_value.first.return_value = DB_AIRTABLE_DETAILS
        airtable = AirtableApi(airtable_api_mock)
        airtable.init_table()
        first_match = airtable.get_first_match("Connection Identifier", "Test Connection ID")
        assert isinstance(first_match, dict)
        assert first_match == DB_AIRTABLE_DETAILS
