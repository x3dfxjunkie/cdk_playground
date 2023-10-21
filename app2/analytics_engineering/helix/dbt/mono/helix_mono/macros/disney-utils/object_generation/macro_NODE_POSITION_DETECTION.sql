{% macro macro_NODE_POSITION_DETECTION(node) -%}

    {# Intermediate / ephemeral models are in a different top level directory for ease of delcaration #}
    {% set typical_database_position = 1 %}
    {% set typical_layer_position    = 2 %}
    {% set typical_schema_position   = 3 %}

    {% if 'EPHEMERAL' in node.fqn[2].upper() %}
        {% set typical_database_position = typical_database_position + 1 %}
        {% set typical_layer_position    = typical_layer_position    + 1 %}
        {% set typical_schema_position   = typical_schema_position   + 1 %}
    {% endif %}

    {# Swap the full prefix in the folder path to the three letter acronym (3LA) #}
    {% set layer_prefix = macro_INTERNAL_LAYER_3LA(node.fqn[typical_layer_position][3:]) %}

    {% set schema_prefix = node.fqn[typical_schema_position:-1]|join('_') %}
    {% set schema_prefix = layer_prefix ~ '_' ~ schema_prefix %}
    {% set schema_prefix = macro_REMOVE_TRAILING_LEADING_UNDERSCORES(schema_prefix) %}

    {{ return(schema_prefix | trim) }}

{%- endmacro %}