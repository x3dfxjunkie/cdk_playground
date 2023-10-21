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
    WHEN SYSTEM$STREAM_HAS_DATA('{{ environment }}_{{ stream_database }}.{{ stream_schema }}.{{managed_artifacts_prefix}}_{{ table.name | upper }}_STREAM')  
    AS
MERGE INTO {{ environment }}_{{ table_database }}.{{ table_schema }}.{{ table.name | upper }} AS T
    USING ( SELECT 
            ST.METADATA$ACTION AS METADATA$ACTION,
            ST.METADATA$ISUPDATE AS METADATA$ISUPDATE,
            {%- for field in table.fields %}
            {%- if  not field.is_landing_field %}
            {%- if field.name != "id"  %}
            {%- if '____' not in  field.full_name %}
            {%- if timestamp_validation.self_validation | lower == 'true' and field.type | upper == 'DATETIME' %}
            {{ definitions.database_name }}.{{ definitions.schema_name }}.{{ definitions.function_name}}( ST.LANDING_DATA:data."{{ '"."'.join(field.full_name.split('__')) | safe }}"  ) AS {{ field.name.split(":")[-1] | upper}}{{ "," if not loop.last }}
            {%- else %}
            ST.LANDING_DATA:data."{{ '"."'.join(field.full_name.split('__')) | safe }}"::{{ field.type | upper }} AS {{ field.name.split(":")[-1] | upper}}{{ "," if not loop.last }}
            {%- endif %}
            {%- else %}
            {%- set route = field.full_name.split('____') %}
            {%- if timestamp_validation.self_validation | lower == 'true' and field.type | upper == 'DATETIME' %}
            {{ definitions.database_name }}.{{ definitions.schema_name }}.{{ definitions.function_name}}({{'_'.join(route[:-1]).replace('__','_').replace("-","_")}}.value:"{{ '"."'.join(route[-1].split('__')) | safe }}") AS {{ field.name.split(":")[-1] | upper}}{{ "," if not loop.last }}
            {%- else %}
            {{'_'.join(route[:-1]).replace('__','_').replace("-","_")}}.value:"{{ '"."'.join(route[-1].split('__')) | safe }}"::{{ field.type | upper }} AS {{ field.name.split(":")[-1] | upper}}{{ "," if not loop.last }}
            {%- endif %} 
            {%- endif %} 
            {%- endif %}
            {%- else %}
            ST.{{ field.name }} AS {{ field.name.split(":")[-1] | upper}}{{ "," if not loop.last }}
            {%- endif %} 
            {%- endfor %}
            FROM {{ environment }}_{{ stream_database }}.{{ stream_schema }}.{{managed_artifacts_prefix}}_{{ table.name | upper }}_STREAM AS ST
            {%- if table.flatten_routes %}
            , {{ table.flatten_routes | safe }}
            {%- endif %} 
            WHERE ST.LANDING_CLOUDEVENT_VALIDATED = true )  AS S
    ON S.landing_id = T.landing_id
    WHEN MATCHED
        AND S.metadata$action = 'INSERT'
        AND S.metadata$isupdate
    THEN
        UPDATE SET
            {%- for field in table.fields -%}
            {%- if field.name == "id" or field.name == "landing_data:id" %}
            T.{{ field.padded_name }} = S.LANDING_CLOUDEVENT_ID{{ "," if not loop.last }}
            {%- else %}
            T.{{ field.padded_name }} = S.{{ field.name.split(":")[-1] | upper}}{{ "," if not loop.last }}
            {%- endif -%}
            {% endfor %}
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
            {% for field in table.fields -%}
            {%- if field.name == "id" or field.name == "landing_data:id" %}
            S.LANDING_CLOUDEVENT_ID{{ "," if not loop.last }}
            {%- else %}
            S.{{ field.name.split(":")[-1] | upper}}{{ "," if not loop.last }}
            {%- endif -%}
            {% endfor %}
            );