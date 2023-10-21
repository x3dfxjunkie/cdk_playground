{% macro generate_alias_name(custom_alias_name=none, node=none) -%}

    {% set truncated_file_name = none %}
    {% set alias_scanning_list = macro_ALIAS_SCANNING(truncated_file_name, node) %}
    {% set truncated_file_name = alias_scanning_list[0] %}
    {% set schema_prefix       = alias_scanning_list[1] %}

    {%- if truncated_file_name is none -%}
        {% set node_name = node.name %}
    {% else %}
        {% set node_name = truncated_file_name %}
    {% endif %}

    {%- if var("environment").upper() != 'LOCAL' -%}

        {{ node_name }}

    {%- elif custom_alias_name is not none -%}

        {{ custom_alias_name | trim }}

    {% else %}

        {# Add the schema as a prefix to the table to ensure uniqueness
        and tracing in personal schemas #}

        {{ schema_prefix }}_{{ node_name }}

    {%- endif -%}

{%- endmacro %}
