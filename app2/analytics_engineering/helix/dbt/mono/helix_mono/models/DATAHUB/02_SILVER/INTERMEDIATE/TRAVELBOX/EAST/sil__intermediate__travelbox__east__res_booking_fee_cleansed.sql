{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_fee_code', 'data_fee_code_index','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'res_booking_fee') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_booking_id,
        data_fee_code,
        data_fee_code_index,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_fee_code,
        data_fee_code_index
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_note) as data_note,
        src.data_last_modified_time as data_last_modified_time,
        src.data_fee_code_index as data_fee_code_index,
        src.data_modified_user as data_modified_user,
        src.data_booking_id as data_booking_id,
        TRIM(src.data_fee_code) as data_fee_code,
        src.data_cost as data_cost,
        src.data_price as data_price,
        src.data_adt_cost as data_adt_cost,
        src.data_adt_price as data_adt_price,
        src.data_chd_cost as data_chd_cost,
        src.data_chd_price as data_chd_price,
        src.data_inf_cost as data_inf_cost,
        src.data_inf_price as data_inf_price,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_note',
            'src.data_last_modified_time',
            'src.data_modified_user',
            'src.data_cost',
            'src.data_price',
            'src.data_adt_cost',
            'src.data_adt_price',
            'src.data_chd_cost',
            'src.data_chd_price',
            'src.data_inf_cost',
            'src.data_inf_price',
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
    on src.data_booking_id = min_source_update_datetime.data_booking_id
    and src.data_fee_code = min_source_update_datetime.data_fee_code
    and src.data_fee_code_index = min_source_update_datetime.data_fee_code_index
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_fee_code, data_fee_code_index, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final