{%- macro macro_create_versions(cleansed_table, timestamp_column, partition_columns) -%}

    SELECT
        *,
        {{ timestamp_column }} AS metadata_version_start_datetime,
        CASE
            WHEN rn > 1 THEN LAG({{ timestamp_column }}, 1) OVER (
                PARTITION BY {{ partition_columns |
                join(', ') }}
                ORDER BY
                    {{ partition_columns |
                    join(', ') }},
                    {{ timestamp_column }} DESC
            )
            WHEN rn = 1 THEN CAST(
                '{{ var('metadata_version_end_date') }}' AS datetime
            )
            ELSE NULL
        END AS metadata_version_end_datetime
    FROM
        {{ cleansed_table }}

{%- endmacro -%}
