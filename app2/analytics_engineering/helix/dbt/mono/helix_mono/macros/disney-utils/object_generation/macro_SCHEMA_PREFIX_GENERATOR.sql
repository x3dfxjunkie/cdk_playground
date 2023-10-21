{% macro macro_SCHEMA_PREFIX_GENERATOR(node) -%}

    {# Concat the subfolder(s) name #}
    {% set detected_project = node.fqn[0].upper() %}

    {# Helix related projects (internal) indicate our dbt projects, and ones that use our medallion approach #}
    {% if 'HELIX' in detected_project %}

        {% set schema_prefix = macro_NODE_POSITION_DETECTION(node) %}

    {# dbt packages (external) that we install from the dbt package hub can follow their own conventions #}
    {%- else -%}
        {# XTR is just meant to be a short hand for 'external' for external packages, and their associated models #}
        {% set schema_prefix = node.fqn[0:-1]|join('_') %}
        {% set schema_prefix = 'XTR_' ~ schema_prefix %}
        {% set schema_prefix = macro_REMOVE_TRAILING_LEADING_UNDERSCORES(schema_prefix) %}

    {# use the internal convention if it exists, instead of the external convention #}
    {% endif %}

    {{ return(schema_prefix | trim) }}

{%- endmacro %}