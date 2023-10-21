{{
    config(
        materialized='incremental',
        unique_key= ['data_code','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'act_transaction_type') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_code,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_code
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_apm_type) as data_apm_type,
        TRIM(src.data_api_enabled) as data_api_enabled,
        TRIM(src.data_manually_refundable) as data_manually_refundable,
        TRIM(src.data_code) as data_code,
        TRIM(src.data_name) as data_name,
        TRIM(src.data_receipt) as data_receipt,
        TRIM(src.data_payment) as data_payment,
        src.data_refund_order as data_refund_order,
        TRIM(src.data_sys_defined) as data_sys_defined,
        TRIM(src.data_bankable) as data_bankable,
        TRIM(src.data_expense) as data_expense,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_apm_type',
            'src.data_api_enabled',
            'src.data_manually_refundable',
            'src.data_name',
            'src.data_receipt',
            'src.data_payment',
            'src.data_refund_order',
            'src.data_sys_defined',
            'src.data_bankable',
            'src.data_expense',
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
    on src.data_code = min_source_update_datetime.data_code
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_code, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final