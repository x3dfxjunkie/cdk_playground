{% macro source(source_name, table_name, include_database = True) %}
-- We don't override source, as there can be version of sources that don't have environments.
    {% do return(builtins.source(source_name, table_name).include(database = include_database)) %}

{% endmacro %}