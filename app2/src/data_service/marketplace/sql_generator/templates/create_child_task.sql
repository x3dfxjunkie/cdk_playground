{%- set definitions = timestamp_validation.function_definitions -%}
CREATE OR REPLACE TASK {{ environment }}_{{ task_database }}.{{ task_schema }}.{{managed_artifacts_prefix}}_{{ table.name | upper }}_TASK
    {%- if usr_tsk_warehouse_size %}
    USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE = '{{ usr_tsk_warehouse_size }}'
    {%- else %}
    WAREHOUSE = '{{warehouse}}'
    {%- endif %}
    SCHEDULE = '{{ schedule }}'
    {%- if comment -%}
    COMMENT = '{{ comment }}'
    {%- endif %} 
    {%- if error_integration_name %}
    ERROR_INTEGRATION = {{error_integration_name}}
    {%- endif %}
    WHEN SYSTEM$STREAM_HAS_DATA('{{ environment }}_{{ stream_database }}.{{ stream_schema }}.{{stream_prefix}}_{{ table.name | upper }}_STREAM') 
    AS
MERGE INTO {{ environment }}_{{ table_database }}.{{ table_schema }}.{{ table.name | upper }} AS T
    {% set table_name = table.json_name.split('____') -%}
    {%- set table_name_length = table_name|length -%}
    USING (
        SELECT
        v.METADATA$ACTION AS METADATA$ACTION,
        v.METADATA$ISUPDATE AS METADATA$ISUPDATE,
        v.LANDING_CLOUDEVENT_VALIDATED as VALIDATED,
        {%- if table_name_length <= 2 %}
        v.LANDING_ID AS parent_id,
        {%- else %}
        md5(CONCAT(v{{ table_name_length - 2 }}.value, v.LANDING_ID)) as parent_id,
        {%- endif %}
        md5(CONCAT(v{{ table_name_length - 1 }}.value, v.LANDING_ID)) as id,
        {#- Three last two columns are id columns which are computed dinamically #}
        {% for field in table.fields[:-2] -%}
        v{{ table_name_length - 1 }}.value:{{ field.object_element | safe }} AS {{ field.name.split(":")[-1] | upper}}{{ "," if not loop.last }}
        {% endfor -%}
        FROM
        {%- for index in range(table_name_length) -%}
        {%- if index == 0 %}
            {{ environment }}_{{ stream_database }}.{{ stream_schema }}.{{stream_prefix}}_{{ table.name | upper }}_STREAM  AS v,
        {%- elif index == 1 %}
            LATERAL FLATTEN(input => v.LANDING_DATA:data.{{ table_name[index].replace("__",".") }}, outer => true) AS v{{ index }}{{ "," if not loop.last }}
        {%- else %}
            LATERAL FLATTEN(input => v{{ index -1 }}.value:{{ table_name[index].replace("__",".") }}, outer => true) AS v{{ index }}{{ "," if not loop.last }}
        {%- endif -%}
        {%- endfor %}
        WHERE v{{ table_name_length - 1 }}.value IS NOT NULL
        AND VALIDATED = true
        ) AS S
    ON S.id = T.id
    WHEN MATCHED 
        AND S.metadata$action = 'INSERT'
        AND S.metadata$isupdate 
    THEN
        UPDATE SET
            {%- for field in table.fields[:-1] -%}
            {%- if timestamp_validation.self_validation | lower == 'true' and field.type | upper == 'DATETIME' %}
            T.{{ field.padded_name }} = {{ definitions.database_name }}.{{ definitions.schema_name }}.{{ definitions.function_name}}( S.{{ field.name.split(":")[-1] | upper }} ),
            {%- else %}
            T.{{ field.padded_name }} = S.{{ field.name.split(":")[-1] | upper}}::{{ field.type | upper }},
            {%- endif %}
            {%- endfor %}
            T.{{ table.fields[-1].padded_name }} = S.parent_id::{{ table.fields[-1].type | upper }}
    WHEN MATCHED
        AND S.metadata$action = 'DELETE' THEN DELETE
    WHEN NOT MATCHED
        AND S.metadata$action = 'INSERT'
    THEN
        INSERT(
            {% for field in table.fields -%}
            {{ field.padded_name.replace(" ", "") }}{{ "," if not loop.last }}
            {% endfor -%}
        )
        VALUES(
            {%- for field in table.fields[:-1] -%}
            {%- if timestamp_validation.self_validation | lower == 'true' and field.type | upper == 'DATETIME' %}
            {{ definitions.database_name }}.{{ definitions.schema_name }}.{{ definitions.function_name}}( S.{{ field.name.split(":")[-1] | upper }} ),
            {%- else %}
            S.{{ field.name.split(":")[-1] | upper}}::{{ field.type | upper }},
            {%- endif %}
            {%- endfor %}
            S.parent_id ::STRING
            );
