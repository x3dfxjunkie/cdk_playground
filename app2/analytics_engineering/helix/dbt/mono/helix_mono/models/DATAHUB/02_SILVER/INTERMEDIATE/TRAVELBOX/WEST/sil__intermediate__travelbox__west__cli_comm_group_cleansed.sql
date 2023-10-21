{{
    config(
        materialized='incremental',
        unique_key= ['data_comm_group_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'cli_comm_group') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_comm_group_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_comm_group_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_ref_code) as data_ref_code,
        src.data_comm_group_id as data_comm_group_id,
        TRIM(src.data_name) as data_name,
        TRIM(src.data_sales_priority) as data_sales_priority,
        TRIM(src.data_currency) as data_currency,
        TRIM(src.data_applicable_date_type) as data_applicable_date_type,
        TRIM(src.data_applicable_product) as data_applicable_product,
        TRIM(src.data_applicable_limit_booking) as data_applicable_limit_booking,
        TRIM(src.data_external_ref) as data_external_ref,
        src.data_com_grp_priority as data_com_grp_priority,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_ref_code',
            'src.data_name',
            'src.data_sales_priority',
            'src.data_currency',
            'src.data_applicable_date_type',
            'src.data_applicable_product',
            'src.data_applicable_limit_booking',
            'src.data_external_ref',
            'src.data_com_grp_priority',
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
    on src.data_comm_group_id = min_source_update_datetime.data_comm_group_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_comm_group_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final