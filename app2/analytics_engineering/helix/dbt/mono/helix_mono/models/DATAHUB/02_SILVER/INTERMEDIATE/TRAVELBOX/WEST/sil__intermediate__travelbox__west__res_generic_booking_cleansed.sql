{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_item_no', 'data_product_code','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'res_generic_booking') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_booking_id,
        data_item_no,
        data_product_code,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_item_no,
        data_product_code
),

-- cleansing the table
renamed as (
    select
        src.data_booking_id as data_booking_id,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        src.data_duration as data_duration,
        TRIM(src.data_departure_time) as data_departure_time,
        TRIM(src.data_unit_cost) as data_unit_cost,
        src.data_units as data_units,
        TRIM(src.data_pax_unit) as data_pax_unit,
        src.data_category_id as data_category_id,
        src.data_reservation_id as data_reservation_id,
        TRIM(src.data_duration_type) as data_duration_type,
        src.data_category_type_id as data_category_type_id,
        src.data_element_group_id as data_element_group_id,
        TRIM(src.data_voucher_used) as data_voucher_used,
        src.data_ticketing_dead_line as data_ticketing_dead_line,
        src.data_max_release_day as data_max_release_day,
        TRIM(src.data_category_code) as data_category_code,
        TRIM(src.data_category_name) as data_category_name,
        TRIM(src.data_product_group_code) as data_product_group_code,
        TRIM(src.data_product_group_name) as data_product_group_name,
        TRIM(src.data_product_type_code) as data_product_type_code,
        TRIM(src.data_product_type_name) as data_product_type_name,
        src.data_content_supplier as data_content_supplier,
        TRIM(src.data_ticketed) as data_ticketed,
        TRIM(src.data_searched_as_fc) as data_searched_as_fc,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_fulfillment_freq) as data_fulfillment_freq,
        src.data_usage_lov_from as data_usage_lov_from,
        src.data_usage_lov_to as data_usage_lov_to,
        src.data_pricing_lov_from as data_pricing_lov_from,
        src.data_pricing_lov_to as data_pricing_lov_to,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_duration',
            'src.data_departure_time',
            'src.data_unit_cost',
            'src.data_units',
            'src.data_pax_unit',
            'src.data_category_id',
            'src.data_reservation_id',
            'src.data_duration_type',
            'src.data_category_type_id',
            'src.data_element_group_id',
            'src.data_voucher_used',
            'src.data_ticketing_dead_line',
            'src.data_max_release_day',
            'src.data_category_code',
            'src.data_category_name',
            'src.data_product_group_code',
            'src.data_product_group_name',
            'src.data_product_type_code',
            'src.data_product_type_name',
            'src.data_content_supplier',
            'src.data_ticketed',
            'src.data_searched_as_fc',
            'src.data_last_modified_time',
            'src.data_fulfillment_freq',
            'src.data_usage_lov_from',
            'src.data_usage_lov_to',
            'src.data_pricing_lov_from',
            'src.data_pricing_lov_to',
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
    and src.data_item_no = min_source_update_datetime.data_item_no
    and src.data_product_code = min_source_update_datetime.data_product_code
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_item_no, data_product_code, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final