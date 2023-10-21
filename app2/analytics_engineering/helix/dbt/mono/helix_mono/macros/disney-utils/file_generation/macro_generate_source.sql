{% macro macro_generate_source(database_name, schema_name, source_name) %}

{#
This macro will allow you to automatically generate a source.yml file in the CLI for the specific database and schema you desire.
Only use this if the specific source.yml file doesn't exist. We will likely be using some form of data contract inteface in the future.
However, this is still a valuable function for data sources that may exist in Snowflake without a Data Contract.
Data Sharing from external accounts directly to Snowflake are a great example.
#}

{# To run this command execute the following:

dbt run-operation macro_generate_source --args '{"database_name": "MY_DATABASE_NAME", "schema_name": "MY_SCHEMA_NAME", "source_name": "MY_SCHEMA_NAME"}'

#}

{% set sql %}
    with "columns" as (
        select '- name: ' || lower(column_name) || '\n            description: "'|| lower(column_name) || ' (snowflake data type: '|| lower(DATA_TYPE) || ')"'
            as column_statement,
            table_name,
            column_name
        from {{ database_name }}.information_schema.columns
        where table_schema = '{{ schema_name | upper }}'
    ),
    tables as (
        select table_name,
        '\n      - name: ' || lower(table_name) || '\n        columns:' || listagg('\n          ' || column_statement || '\n') within group ( order by column_name ) as table_desc
        from "columns"
        group by table_name
    )

    select listagg(table_desc) within group ( order by table_name )
    from tables;
{% endset %}

{%- call statement('generator', fetch_result=True) -%}
{{ sql }}
{%- endcall -%}
{# '{% raw %}{{ env_var("DBT_HELIX_MONO_SOURCE_DATABASE") }}{% endraw %}' #}
{%- set states=load_result('generator') -%}
{%- set states_data=states['data'] -%}
{%- set states_status=states['response'] -%}

{% set sources_yaml=[] %}
{% do sources_yaml.append('version: 2') %}
{% do sources_yaml.append('') %}
{% do sources_yaml.append('sources:') %}
{% do sources_yaml.append('  - name: ' ~ source_name | lower) %}
{% do sources_yaml.append('    description: ""' ) %}
{% do sources_yaml.append('    database: ' ~ '{% raw %}{{ env_var("DBT_HELIX_MONO_SOURCE_DATABASE", "LATEST_DATAHUB") }}{% endraw %}' ) %}
{% do sources_yaml.append('    schema: ' ~ schema_name | lower) %}
{% do sources_yaml.append('    loader: firehose/snowpipe-microbatch') %}
{% do sources_yaml.append('    loaded_at_field: LANDING_TIMESTAMP') %}
{% do sources_yaml.append('    freshness: # default freshness') %}
{% do sources_yaml.append('      warn_after: {count: 12, period: hour}') %}
{% do sources_yaml.append('      error_after: {count: 24, period: hour}') %}
{% do sources_yaml.append('    meta:') %}
{% do sources_yaml.append('      owner: ""') %}
{% do sources_yaml.append('      tags: [""]') %}
{% do sources_yaml.append('      subscribers: ["@data-team"]') %}

{% do sources_yaml.append('    tables:' ~ states_data[0][0] ) %}

{% if execute %}

{% set joined = sources_yaml | join ('\n') %}
{% set raw_removed = joined | replace("{% raw %}","'") %}
{% set raw_removed = raw_removed | replace("{% endraw %}","'") %}
{{ log(raw_removed, info=True) }}
{% do return(raw_removed) %}

{% endif %}

{% endmacro %}