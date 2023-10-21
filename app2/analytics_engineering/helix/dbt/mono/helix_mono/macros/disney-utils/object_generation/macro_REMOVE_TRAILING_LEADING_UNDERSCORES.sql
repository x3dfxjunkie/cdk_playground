{% macro macro_REMOVE_TRAILING_LEADING_UNDERSCORES(input_string) -%}

    {% set input_string_clean = input_string.lstrip('_').rstrip('_')%}

    {{ return(input_string_clean) }}

{%- endmacro %}