{% macro macro_INTERNAL_LAYER_3LA(layer_full_name) -%}

    {# Swaps our layering conventions to three letter acronyms for readability in the UI console #}

    {% set detected_layer_full_name = layer_full_name.upper() %}

    {% if detected_layer_full_name == 'BRONZE' %}
        {% set layer_prefix = 'BRZ' %}
    {% elif detected_layer_full_name == 'SILVER' %}
        {% set layer_prefix = 'SIL' %}
    {% elif detected_layer_full_name == 'GOLD' %}
        {% set layer_prefix = 'GLD' %}
    {% elif detected_layer_full_name == 'DIAMOND' %}
        {% set layer_prefix = 'DMD' %}
    {%- else -%}
        {% set layer_prefix =  'UNK_' ~ detected_layer_full_name %}
    {% endif %}

    {{ return(layer_prefix) }}

{%- endmacro %}