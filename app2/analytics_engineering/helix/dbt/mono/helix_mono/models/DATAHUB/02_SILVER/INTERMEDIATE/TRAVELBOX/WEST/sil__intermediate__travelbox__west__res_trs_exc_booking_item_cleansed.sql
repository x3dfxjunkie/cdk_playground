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
    from {{ source('brz_travelbox_west', 'res_trs_exc_booking_item') }}

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
        TRIM(src.data_type) as data_type,
        src.data_transfer_no as data_transfer_no,
        TRIM(src.data_pickup_point) as data_pickup_point,
        TRIM(src.data_dropoff_point) as data_dropoff_point,
        TRIM(src.data_description) as data_description,
        TRIM(src.data_transfer_mode_code) as data_transfer_mode_code,
        TRIM(src.data_transfer_mode) as data_transfer_mode,
        TRIM(src.data_pickup_point_code) as data_pickup_point_code,
        TRIM(src.data_pickup_point_type) as data_pickup_point_type,
        TRIM(src.data_dropoff_point_code) as data_dropoff_point_code,
        TRIM(src.data_dropoff_point_type) as data_dropoff_point_type,
        src.data_exc_location_id as data_exc_location_id,
        TRIM(src.data_exc_location) as data_exc_location,
        src.data_transfer_mode_no as data_transfer_mode_no,
        src.data_minimum_vehicles as data_minimum_vehicles,
        TRIM(src.data_return_compulsory) as data_return_compulsory,
        TRIM(src.data_transfer_name) as data_transfer_name,
        src.data_h2_h_product_id as data_h2_h_product_id,
        src.data_h2_h_booking_type_id as data_h2_h_booking_type_id,
        TRIM(src.data_outbound_flight_no) as data_outbound_flight_no,
        TRIM(src.data_outbound_dep_apt) as data_outbound_dep_apt,
        src.data_outbound_arr_time as data_outbound_arr_time,
        TRIM(src.data_outbound_airline) as data_outbound_airline,
        TRIM(src.data_inbound_flight_no) as data_inbound_flight_no,
        TRIM(src.data_inbound_arr_apt) as data_inbound_arr_apt,
        src.data_inbound_dep_time as data_inbound_dep_time,
        TRIM(src.data_inbound_airline) as data_inbound_airline,
        TRIM(src.data_outbound_ship_name) as data_outbound_ship_name,
        TRIM(src.data_outbound_dep_port) as data_outbound_dep_port,
        TRIM(src.data_inbound_arr_port) as data_inbound_arr_port,
        TRIM(src.data_inbound_ship_name) as data_inbound_ship_name,
        TRIM(src.data_cru_foreign_bkng_id) as data_cru_foreign_bkng_id,
        TRIM(src.data_start_end_times_edited) as data_start_end_times_edited,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_fulfillment_freq) as data_fulfillment_freq,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_type',
            'src.data_transfer_no',
            'src.data_pickup_point',
            'src.data_dropoff_point',
            'src.data_description',
            'src.data_transfer_mode_code',
            'src.data_transfer_mode',
            'src.data_pickup_point_code',
            'src.data_pickup_point_type',
            'src.data_dropoff_point_code',
            'src.data_dropoff_point_type',
            'src.data_exc_location_id',
            'src.data_exc_location',
            'src.data_transfer_mode_no',
            'src.data_minimum_vehicles',
            'src.data_return_compulsory',
            'src.data_transfer_name',
            'src.data_h2_h_product_id',
            'src.data_h2_h_booking_type_id',
            'src.data_outbound_flight_no',
            'src.data_outbound_dep_apt',
            'src.data_outbound_arr_time',
            'src.data_outbound_airline',
            'src.data_inbound_flight_no',
            'src.data_inbound_arr_apt',
            'src.data_inbound_dep_time',
            'src.data_inbound_airline',
            'src.data_outbound_ship_name',
            'src.data_outbound_dep_port',
            'src.data_inbound_arr_port',
            'src.data_inbound_ship_name',
            'src.data_cru_foreign_bkng_id',
            'src.data_start_end_times_edited',
            'src.data_last_modified_time',
            'src.data_fulfillment_freq',
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