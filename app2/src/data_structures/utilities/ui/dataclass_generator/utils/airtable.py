import os


class AirtableApi:
    def __init__(self, pyairtable_api):
        self.table = None
        self.base_id = os.getenv("AIRTABLE_BASE_ID")
        self.table_id = os.getenv("AIRTABLE_TABLE_ID")
        self.api = pyairtable_api.Api(os.getenv("AIRTABLE_API_KEY"))
        self.pyairtable = pyairtable_api

    def init_table(self, table_id: str | None = os.getenv("AIRTABLE_TABLE_ID")):
        """
        Initiates Airtable table object given a table identifier.
        Args:
            table_id: Table identifier from Airtable
        """
        self.table = self.api.table(self.base_id, table_id)

    def get_column_list(self, col_name: str) -> list:
        """
        Gets a list of a column from Airtable given a column name.
        Args:
            col_name: Airtable column name

        Returns: List of column values.

        """
        return [fields["fields"][col_name] for fields in self.table.all(fields=[col_name])]

    def get_first_match(self, col_name: str, value: str) -> dict:
        """
        Gets the first match value in Airtable given a column name and value
        Args:
            col_name: Column name to filter.
            value: Value to search.

        Returns:
            First match found on Airtable.

        """
        formula = self.pyairtable.formulas.match({col_name: value})
        return self.table.first(formula=formula)
