{% macro generate_schema_name(custom_schema_name, node) -%}

    {# Inspired by https://stackoverflow.com/a/69849432 #}

    {%- set default_schema = target.schema -%}

    {%- if custom_schema_name is none -%}

        {# Check if the model does not contain a subfolder (e.g, models created at the MODELS root folder) #}
        {# If we are doing local work, send the tables to a users personal schema) #}

        {% if node.fqn[0:-1]|length == 0 or var("environment").upper() == 'LOCAL' %}
            {# dbt run --vars "{environment: $ENV}" WORKS FOR LOCAL/PROD etc. #}
            {{ default_schema }}

        {% else %}

            {{ macro_SCHEMA_PREFIX_GENERATOR(node) }}

        {% endif %}

    {%- else -%}

        {{ default_schema }}_{{ custom_schema_name | trim }}

    {%- endif -%}

{%- endmacro %}