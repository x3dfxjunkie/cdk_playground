{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_item_no', 'data_pax_item_no', 'data_product_code','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'res_pax_item') }}

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
        data_pax_item_no,
        data_product_code,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_item_no,
        data_pax_item_no,
        data_product_code
),

-- cleansing the table
renamed as (
    select
        src.data_external_base_price as data_external_base_price,
        TRIM(src.data_order_line_item_id) as data_order_line_item_id,
        TRIM(src.data_ext_order_line_item_id) as data_ext_order_line_item_id,
        TRIM(src.data_ext_price_token_time) as data_ext_price_token_time,
        TRIM(src.data_plu_code) as data_plu_code,
        TRIM(src.data_ext_base_currency) as data_ext_base_currency,
        src.data_booking_id as data_booking_id,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        src.data_pax_item_no as data_pax_item_no,
        src.data_passenger_no as data_passenger_no,
        TRIM(src.data_lead) as data_lead,
        TRIM(src.data_type) as data_type,
        src.data_departure_time as data_departure_time,
        TRIM(src.data_on_request) as data_on_request,
        src.data_departure_date as data_departure_date,
        TRIM(src.data_inf_seat) as data_inf_seat,
        src.data_cost as data_cost,
        src.data_price as data_price,
        src.data_tax as data_tax,
        src.data_discount as data_discount,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_travel_with_infant) as data_travel_with_infant,
        src.data_inf_passenger_no as data_inf_passenger_no,
        src.data_commission as data_commission,
        TRIM(src.data_ptc_code) as data_ptc_code,
        TRIM(src.data_special_care) as data_special_care,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_external_base_price',
            'src.data_order_line_item_id',
            'src.data_ext_order_line_item_id',
            'src.data_ext_price_token_time',
            'src.data_plu_code',
            'src.data_ext_base_currency',
            'src.data_passenger_no',
            'src.data_lead',
            'src.data_type',
            'src.data_departure_time',
            'src.data_on_request',
            'src.data_departure_date',
            'src.data_inf_seat',
            'src.data_cost',
            'src.data_price',
            'src.data_tax',
            'src.data_discount',
            'src.data_last_modified_time',
            'src.data_travel_with_infant',
            'src.data_inf_passenger_no',
            'src.data_commission',
            'src.data_ptc_code',
            'src.data_special_care',
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
    and src.data_pax_item_no = min_source_update_datetime.data_pax_item_no
    and src.data_product_code = min_source_update_datetime.data_product_code
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_item_no, data_pax_item_no, data_product_code, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final