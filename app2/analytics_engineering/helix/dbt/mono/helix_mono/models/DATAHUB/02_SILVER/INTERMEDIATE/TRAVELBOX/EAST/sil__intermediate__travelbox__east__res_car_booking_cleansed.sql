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
    from {{ source('brz_travelbox_east', 'res_car_booking') }}

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
        src.data_last_modified_time as data_last_modified_time,
        src.data_booking_id as data_booking_id,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        src.data_pickup_location_id as data_pickup_location_id,
        src.data_dropoff_location_id as data_dropoff_location_id,
        src.data_car_id as data_car_id,
        TRIM(src.data_car_product) as data_car_product,
        src.data_oneway_fee as data_oneway_fee,
        src.data_multihire_no as data_multihire_no,
        TRIM(src.data_car_name) as data_car_name,
        TRIM(src.data_pickup_location) as data_pickup_location,
        TRIM(src.data_dropoff_location) as data_dropoff_location,
        TRIM(src.data_pickup_time) as data_pickup_time,
        TRIM(src.data_dropoff_time) as data_dropoff_time,
        TRIM(src.data_car_class) as data_car_class,
        TRIM(src.data_car_type) as data_car_type,
        src.data_contract_type as data_contract_type,
        src.data_calculated_rented_days as data_calculated_rented_days,
        TRIM(src.data_pay_supplier_directly) as data_pay_supplier_directly,
        TRIM(src.data_foreign_reference) as data_foreign_reference,
        TRIM(src.data_air_conditioned) as data_air_conditioned,
        TRIM(src.data_transmission_type) as data_transmission_type,
        src.data_door_count as data_door_count,
        TRIM(src.data_milege_property) as data_milege_property,
        TRIM(src.data_image_url) as data_image_url,
        TRIM(src.data_fuel_type) as data_fuel_type,
        src.data_baggages as data_baggages,
        TRIM(src.data_drive_type) as data_drive_type,
        src.data_car_class_id as data_car_class_id,
        src.data_seat_count as data_seat_count,
        src.data_no_of_cars as data_no_of_cars,
        src.data_car_voucher_id as data_car_voucher_id,
        src.data_driver_passenger_no as data_driver_passenger_no,
        src.data_driver_age_min as data_driver_age_min,
        src.data_driver_age_max as data_driver_age_max,
        src.data_car_booking_group as data_car_booking_group,
        TRIM(src.data_car_product_name) as data_car_product_name,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_last_modified_time',
            'src.data_pickup_location_id',
            'src.data_dropoff_location_id',
            'src.data_car_id',
            'src.data_car_product',
            'src.data_oneway_fee',
            'src.data_multihire_no',
            'src.data_car_name',
            'src.data_pickup_location',
            'src.data_dropoff_location',
            'src.data_pickup_time',
            'src.data_dropoff_time',
            'src.data_car_class',
            'src.data_car_type',
            'src.data_contract_type',
            'src.data_calculated_rented_days',
            'src.data_pay_supplier_directly',
            'src.data_foreign_reference',
            'src.data_air_conditioned',
            'src.data_transmission_type',
            'src.data_door_count',
            'src.data_milege_property',
            'src.data_image_url',
            'src.data_fuel_type',
            'src.data_baggages',
            'src.data_drive_type',
            'src.data_car_class_id',
            'src.data_seat_count',
            'src.data_no_of_cars',
            'src.data_car_voucher_id',
            'src.data_driver_passenger_no',
            'src.data_driver_age_min',
            'src.data_driver_age_max',
            'src.data_car_booking_group',
            'src.data_car_product_name',
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