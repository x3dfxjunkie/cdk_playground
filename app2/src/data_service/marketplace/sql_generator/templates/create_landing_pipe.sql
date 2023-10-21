CREATE {{"OR REPLACE PIPE" if recreate_if_exists else "PIPE IF NOT EXISTS"}} {{ environment }}_{{pipe_database}}.{{pipe_schema}}.{{pipe_prefix}}_{{table.name | upper}}_PIPE
AUTO_INGEST = TRUE
{%- if error_integration_name %}
ERROR_INTEGRATION = {{error_integration_name}}
{%- endif %}
AS COPY INTO {{landing_database}}.{{landing_schema}}.{{table.name | upper}}(
    LANDING_ID,
    LANDING_DATA,
    LANDING_FILE_NAME,
    LANDING_FILE_ROW_NUMBER,
    LANDING_FILE_LAST_MODIFIED,
    LANDING_TIMESTAMP,
{%- if cloud_event_fields -%}
{%- for cloud_event_field in cloud_event_fields %}
    {{cloud_event_field["_name"]|upper}}{{ ", " if not loop.last else "" }}
{%- endfor %}
{%- endif %}
{%- if identifier_columns -%}
{%- for identifier_column in identifier_columns %}
    {{identifier_column["column_name"]|upper}}{{"" if loop.last else ","}}
{%- endfor %}
{%- endif %}
)
FROM(
SELECT
    LOWER(UUID_STRING('998bc5ba-a184-4144-8f97-d3b34526e37f', CONCAT(metadata$filename, ':', metadata$file_row_number))) AS LANDING_ID,
    $1                                                                 AS LANDING_DATA,
    metadata$filename                                                  AS LANDING_FILE_NAME,
    metadata$file_row_number                                           AS LANDING_FILE_ROW_NUMBER,
    metadata$file_last_modified                                        AS LANDING_FILE_LAST_MODIFIED,
    TO_TIMESTAMP_NTZ(CONVERT_TIMEZONE('UTC', CURRENT_TIMESTAMP()))     AS LANDING_TIMESTAMP,
{%- if cloud_event_fields -%}
{%- for cloud_event_field in cloud_event_fields %}
    $1:{{cloud_event_field["title"]}} :: {{cloud_event_field["_type"]}} AS {{cloud_event_field["_name"]|upper}}{{"" if loop.last else ","}}
{%- endfor %}
{%- endif %}
{%- if identifier_columns -%}
{%- for identifier_column in identifier_columns %}
    $1:{{identifier_column["path"]}}          AS LANDING_IDENTIFIER_{{identifier_column["column_name"]|upper}}{{"" if loop.last else ","}}
{%- endfor %}
{%- endif %}
FROM @{{ environment }}_{{external_stage}}/database={{landing_database}}/schema={{landing_schema}}/table={{table.name | upper}}/
)FILE_FORMAT = (TYPE = {{file_type or "JSON"}});

ALTER PIPE {{ environment }}_{{pipe_database}}.{{pipe_schema}}.{{pipe_prefix}}_{{table.name | upper}}_PIPE REFRESH;

--Helper query for pipe status:
-- SELECT SYSTEM$PIPE_STATUS('{{ environment }}_{{pipe_database}}.{{pipe_schema}}.{{pipe_prefix}}_{{table.name | upper}}_PIPE');