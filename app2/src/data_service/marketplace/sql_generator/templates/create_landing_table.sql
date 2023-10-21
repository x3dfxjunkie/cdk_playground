CREATE {{"OR REPLACE TABLE" if recreate_if_exists else "TABLE IF NOT EXISTS"}} {{ table_database }}.{{ table_schema }}.{{ table.name | upper }}(
    LANDING_ID                                  STRING,
    LANDING_DATA                                VARIANT,
    LANDING_FILE_NAME                           STRING,
    LANDING_FILE_ROW_NUMBER                     INT,
    LANDING_FILE_LAST_MODIFIED                  DATETIME,
    LANDING_TIMESTAMP                           DATETIME,
{%- if cloud_event_fields -%}
{%- for cloud_event_field in cloud_event_fields %}
    {{cloud_event_field["_name"]|upper}} {{cloud_event_field["_type"]}}{{"" if loop.last else ","}}
{%- endfor %}
{%- endif %}
{{"," if identifier_columns else "" }}
{%- if identifier_columns -%}
{%- for identifier_column in identifier_columns %}
    LANDING_IDENTIFIER_{{identifier_column["column_name"]|upper}} STRING{{"" if loop.last else ","}}
{%- endfor %}
{%- endif %}
);
