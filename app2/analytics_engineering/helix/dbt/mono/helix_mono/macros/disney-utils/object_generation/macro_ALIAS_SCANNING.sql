{% macro macro_ALIAS_SCANNING(truncated_file_name, node) %}
    {# This is for detecting whether the dbt filename matches the folder path we have also setup #}
    {% set schema_prefix = macro_SCHEMA_PREFIX_GENERATOR(node) %}
    {% set node_path_list =  node.fqn %}
    {% set detected_project =  node_path_list[0] %}

    {# only apply scanning to conventions in our helix projects #}
    {% if 'HELIX' in detected_project.upper() %}
        {% set identified_file_name = node_path_list[-1] %}
        {% set helix_convention_list = identified_file_name.split('__') %}
        {% set helix_convention_prefix = helix_convention_list[0].upper() %}
        {% set generated_schema_3la = schema_prefix.split('_')[0].upper() %}

        {# we don't care about intermediate models / ephemeral models
        as they will not be persisted as anything besides CTEs #}
        {% if generated_schema_3la in helix_convention_prefix and 'eph_' not in helix_convention_prefix[:4].lower() %}
            {% set truncated_file_name = helix_convention_list[-1].strip() %}
        {% endif %}
    {% endif %}

    {{ return([truncated_file_name, schema_prefix]) }}

{% endmacro %}