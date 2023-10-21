{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_item_no', 'data_product_code', 'data_sector_no','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'res_flight_sector') }}

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
        data_sector_no,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_item_no,
        data_product_code,
        data_sector_no
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_booking_token) as data_booking_token,
        TRIM(src.data_flight_no) as data_flight_no,
        TRIM(src.data_des) as data_des,
        src.data_dep_date as data_dep_date,
        src.data_des_date as data_des_date,
        TRIM(src.data_dep_terminal) as data_dep_terminal,
        TRIM(src.data_arr_terminal) as data_arr_terminal,
        TRIM(src.data_equipment) as data_equipment,
        TRIM(src.data_status_code) as data_status_code,
        TRIM(src.data_held_by) as data_held_by,
        src.data_crs_seats as data_crs_seats,
        src.data_alloc_contract_id as data_alloc_contract_id,
        src.data_alloc_leg_no as data_alloc_leg_no,
        src.data_alloc_block_no as data_alloc_block_no,
        src.data_alloc_sector_no as data_alloc_sector_no,
        TRIM(src.data_alloc_brand) as data_alloc_brand,
        src.data_alloc_seats as data_alloc_seats,
        src.data_alloc_package_no as data_alloc_package_no,
        src.data_alloc_package_seats as data_alloc_package_seats,
        TRIM(src.data_baggage) as data_baggage,
        src.data_not_valid_after as data_not_valid_after,
        TRIM(src.data_checkin_before) as data_checkin_before,
        TRIM(src.data_touchdown) as data_touchdown,
        TRIM(src.data_note) as data_note,
        src.data_addon_id as data_addon_id,
        src.data_addon_sector as data_addon_sector,
        src.data_addon_charge_no as data_addon_charge_no,
        src.data_alloc_group_id as data_alloc_group_id,
        TRIM(src.data_fare_basis) as data_fare_basis,
        TRIM(src.data_pub_fare_type_code) as data_pub_fare_type_code,
        TRIM(src.data_operating_airline) as data_operating_airline,
        TRIM(src.data_cabin_class) as data_cabin_class,
        src.data_duration as data_duration,
        TRIM(src.data_mapping_fare_basis) as data_mapping_fare_basis,
        src.data_no_of_stops as data_no_of_stops,
        src.data_pkg_item_order as data_pkg_item_order,
        TRIM(src.data_airline_locator) as data_airline_locator,
        src.data_pub_ticket_info_id as data_pub_ticket_info_id,
        src.data_price_combination as data_price_combination,
        src.data_pub_contract_id as data_pub_contract_id,
        TRIM(src.data_baggage_chd) as data_baggage_chd,
        TRIM(src.data_baggage_inf) as data_baggage_inf,
        TRIM(src.data_designator) as data_designator,
        TRIM(src.data_operating_airline_flt_no) as data_operating_airline_flt_no,
        TRIM(src.data_seat_released) as data_seat_released,
        TRIM(src.data_info_only_key) as data_info_only_key,
        TRIM(src.data_meal_code) as data_meal_code,
        TRIM(src.data_change_of_gauge) as data_change_of_gauge,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_operating_airline_info) as data_operating_airline_info,
        TRIM(src.data_co2_info) as data_co2_info,
        src.data_booking_id as data_booking_id,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        src.data_sector_no as data_sector_no,
        src.data_itinerary_order as data_itinerary_order,
        src.data_leg_no as data_leg_no,
        TRIM(src.data_direction) as data_direction,
        TRIM(src.data_airline) as data_airline,
        TRIM(src.data_booking_class) as data_booking_class,
        TRIM(src.data_allocation_class) as data_allocation_class,
        TRIM(src.data_dep) as data_dep,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_booking_token',
            'src.data_flight_no',
            'src.data_des',
            'src.data_dep_date',
            'src.data_des_date',
            'src.data_dep_terminal',
            'src.data_arr_terminal',
            'src.data_equipment',
            'src.data_status_code',
            'src.data_held_by',
            'src.data_crs_seats',
            'src.data_alloc_contract_id',
            'src.data_alloc_leg_no',
            'src.data_alloc_block_no',
            'src.data_alloc_sector_no',
            'src.data_alloc_brand',
            'src.data_alloc_seats',
            'src.data_alloc_package_no',
            'src.data_alloc_package_seats',
            'src.data_baggage',
            'src.data_not_valid_after',
            'src.data_checkin_before',
            'src.data_touchdown',
            'src.data_note',
            'src.data_addon_id',
            'src.data_addon_sector',
            'src.data_addon_charge_no',
            'src.data_alloc_group_id',
            'src.data_fare_basis',
            'src.data_pub_fare_type_code',
            'src.data_operating_airline',
            'src.data_cabin_class',
            'src.data_duration',
            'src.data_mapping_fare_basis',
            'src.data_no_of_stops',
            'src.data_pkg_item_order',
            'src.data_airline_locator',
            'src.data_pub_ticket_info_id',
            'src.data_price_combination',
            'src.data_pub_contract_id',
            'src.data_baggage_chd',
            'src.data_baggage_inf',
            'src.data_designator',
            'src.data_operating_airline_flt_no',
            'src.data_seat_released',
            'src.data_info_only_key',
            'src.data_meal_code',
            'src.data_change_of_gauge',
            'src.data_last_modified_time',
            'src.data_operating_airline_info',
            'src.data_co2_info',
            'src.data_itinerary_order',
            'src.data_leg_no',
            'src.data_direction',
            'src.data_airline',
            'src.data_booking_class',
            'src.data_allocation_class',
            'src.data_dep',
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
    and src.data_sector_no = min_source_update_datetime.data_sector_no
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_item_no, data_product_code, data_sector_no, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final