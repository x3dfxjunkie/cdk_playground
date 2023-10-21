CREATE OR REPLACE TABLE {{ environment }}_{{ table_database }}.{{ table_schema }}.{{ table.name | upper }}
(
    {%- for field in table.fields %}
    {{ field.padded_name | lower }} {{ field.type | upper }}{{ "," if not loop.last }}
    {%- endfor %}
);
