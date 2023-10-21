{{
    config(
        materialized='incremental',
        unique_key= ['data_category_no', 'data_contract_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'gen_category') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_category_no,
        data_contract_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_category_no,
        data_contract_id
),

-- cleansing the table
renamed as (
    select
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_voucher_code) as data_voucher_code,
        TRIM(src.data_fulfillment_freq) as data_fulfillment_freq,
        TRIM(src.data_los_variation_code) as data_los_variation_code,
        TRIM(src.data_dynamic) as data_dynamic,
        TRIM(src.data_dynamic_name) as data_dynamic_name,
        TRIM(src.data_daily) as data_daily,
        TRIM(src.data_single_day) as data_single_day,
        src.data_contract_id as data_contract_id,
        src.data_category_no as data_category_no,
        TRIM(src.data_code) as data_code,
        TRIM(src.data_name) as data_name,
        src.data_errata_group as data_errata_group,
        TRIM(src.data_prepaid) as data_prepaid,
        src.data_max_adults as data_max_adults,
        src.data_max_child as data_max_child,
        TRIM(src.data_description) as data_description,
        src.data_max_infant as data_max_infant,
        src.data_min_adults as data_min_adults,
        TRIM(src.data_cost_type) as data_cost_type,
        TRIM(src.data_max_teens) as data_max_teens,
        src.data_valid_before as data_valid_before,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_last_modified_time',
            'src.data_voucher_code',
            'src.data_fulfillment_freq',
            'src.data_los_variation_code',
            'src.data_dynamic',
            'src.data_dynamic_name',
            'src.data_daily',
            'src.data_single_day',
            'src.data_code',
            'src.data_name',
            'src.data_errata_group',
            'src.data_prepaid',
            'src.data_max_adults',
            'src.data_max_child',
            'src.data_description',
            'src.data_max_infant',
            'src.data_min_adults',
            'src.data_cost_type',
            'src.data_max_teens',
            'src.data_valid_before',
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
    on src.data_category_no = min_source_update_datetime.data_category_no
    and src.data_contract_id = min_source_update_datetime.data_contract_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_category_no, data_contract_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final