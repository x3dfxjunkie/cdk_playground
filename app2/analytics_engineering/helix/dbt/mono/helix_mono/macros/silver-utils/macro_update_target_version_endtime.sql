{% macro macro_update_target_version_endtime(cleansed_table, join_columns, timestamp_column) %}

{% if is_incremental() %}

    update
        {{ this }} trgt
    set
        trgt.metadata_version_end_datetime = {{ cleansed_table }}.{{ timestamp_column }}
    from
        {{ cleansed_table }}
    where
        {%- for column in join_columns %}
        {{ 'and ' if not loop.first }}trgt.{{ column }} = {{ cleansed_table }}.{{ column }}
        {%- endfor %}
        and trgt.metadata_version_end_datetime = cast('{{ var('metadata_version_end_date') }}' as datetime)
        and {{ cleansed_table }}.metadata_timestamp > trgt.metadata_timestamp

{% endif %}

{% endmacro %}