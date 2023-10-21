{{
    config(
        materialized='incremental',
        unique_key= ['data_location_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'location') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_location_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_location_id
),

-- cleansing the table
renamed as (
    select
        src.data_location_id as data_location_id,
        TRIM(src.data_name) as data_name,
        TRIM(src.data_city) as data_city,
        TRIM(src.data_country) as data_country,
        TRIM(src.data_region) as data_region,
        TRIM(src.data_resort) as data_resort,
        TRIM(src.data_location_type) as data_location_type,
        src.data_longitude as data_longitude,
        src.data_latitude as data_latitude,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_name',
            'src.data_city',
            'src.data_country',
            'src.data_region',
            'src.data_resort',
            'src.data_location_type',
            'src.data_longitude',
            'src.data_latitude',
            'src.dms_operation']) }} as metadata_checksum,
        metadata_timestamp,
        metadata_record_type,
        metadata_operation,
        metadata_partition_key_type,
        metadata_schema_name,
        metadata_table_name,
        metadata_transaction_id,
        metadata_transaction_record_id,
        metadata_prev_transaction_id,
        metadata_prev_transaction_record_id,
        metadata_commit_timestamp,
        metadata_stream_position,
        SYSDATE() as metadata_insert_datetime,
        '{{ env_var('DBT_SYNTHETIC_ID', "dbt") }}' as metadata_batch_user,
        landing_id,
        landing_file_name,
        landing_file_row_number,
        landing_file_last_modified,
        landing_timestamp,
        landing_cloudevent_id,
        landing_cloudevent_specversion,
        landing_cloudevent_time,
        landing_cloudevent_source,
        landing_cloudevent_subject,
        landing_cloudevent_stream,
        landing_cloudevent_type,
        landing_cloudevent_dataschema,
        landing_cloudevent_traceparent,
        landing_cloudevent_tracestate,
        landing_cloudevent_check_sum,
        landing_cloudevent_router_database,
        landing_cloudevent_router_schema,
        landing_cloudevent_router_table,
        landing_cloudevent_validated,
        landing_cloudevent_data_contract_version,
        landing_cloudevent_datacontenttype,
        landing_cloudevent_exception_error

    from source src
    inner join min_source_update_datetime
    on src.data_location_id = min_source_update_datetime.data_location_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_location_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final