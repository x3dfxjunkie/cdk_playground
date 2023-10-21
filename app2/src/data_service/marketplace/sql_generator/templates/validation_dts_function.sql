{%- set definitions = timestamp_validation.function_definitions -%}
CREATE OR REPLACE FUNCTION {{ definitions.database_name | upper }}.{{ definitions.schema_name | upper }}.{{ definitions.function_name | upper}}(input_string STRING)
RETURNS TIMESTAMP
LANGUAGE SQL
AS
$$
    CASE
    {%- for format in timestamp_validation.not_recognized_formats %}
    {{'  '}} WHEN TRY_TO_TIMESTAMP(input_string, '{{ format | safe }}') IS NOT NULL
    {{'   '}} THEN TRY_TO_TIMESTAMP(input_string, '{{ format | safe }}')
    {%- endfor %}
       ELSE input_string::DATETIME
    END
$$
;