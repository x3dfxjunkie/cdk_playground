-- Macro to override ref and to render identifiers without a database. This is important for cloning considerations.

{% macro ref(model_name, include_database = False) %}

  {% do return(builtins.ref(model_name).include(database=include_database)) %}

{% endmacro %}