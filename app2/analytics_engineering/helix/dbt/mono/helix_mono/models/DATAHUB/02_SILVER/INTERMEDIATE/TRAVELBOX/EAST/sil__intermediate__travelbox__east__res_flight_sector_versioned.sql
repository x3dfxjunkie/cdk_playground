{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_booking_id', 'data_item_no', 'data_product_code', 'data_sector_no','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__east__res_flight_sector_cleansed'),
            join_columns=['data_booking_id', 'data_item_no', 'data_product_code', 'data_sector_no'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__east__res_flight_sector_cleansed') }}
    {% if is_incremental() %}
    -- this filter will only be applied on an incremental run

        where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

-- adding the row_number column (rn) for ordering the incremental data by metadata_timestamp
renamed as (
    select
        *,
        row_number() over (
            partition by data_booking_id, data_item_no, data_product_code, data_sector_no
                order by
                    metadata_timestamp desc
        ) as rn
    from
        cleansed
),

-- adding version start and end dates metadata columns
versioned as (
    {{ macro_create_versions(
        cleansed_table = 'renamed',
        timestamp_column = 'metadata_timestamp',
        partition_columns = ['data_booking_id', 'data_item_no', 'data_product_code', 'data_sector_no']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_booking_token,
        data_flight_no,
        data_des,
        data_dep_date,
        data_des_date,
        data_dep_terminal,
        data_arr_terminal,
        data_equipment,
        data_status_code,
        data_held_by,
        data_crs_seats,
        data_alloc_contract_id,
        data_alloc_leg_no,
        data_alloc_block_no,
        data_alloc_sector_no,
        data_alloc_brand,
        data_alloc_seats,
        data_alloc_package_no,
        data_alloc_package_seats,
        data_baggage,
        data_not_valid_after,
        data_checkin_before,
        data_touchdown,
        data_note,
        data_addon_id,
        data_addon_sector,
        data_addon_charge_no,
        data_alloc_group_id,
        data_fare_basis,
        data_pub_fare_type_code,
        data_operating_airline,
        data_cabin_class,
        data_duration,
        data_mapping_fare_basis,
        data_no_of_stops,
        data_pkg_item_order,
        data_airline_locator,
        data_pub_ticket_info_id,
        data_price_combination,
        data_pub_contract_id,
        data_baggage_chd,
        data_baggage_inf,
        data_designator,
        data_operating_airline_flt_no,
        data_seat_released,
        data_info_only_key,
        data_meal_code,
        data_change_of_gauge,
        data_last_modified_time,
        data_operating_airline_info,
        data_co2_info,
        data_booking_id,
        data_product_code,
        data_item_no,
        data_sector_no,
        data_itinerary_order,
        data_leg_no,
        data_direction,
        data_airline,
        data_booking_class,
        data_allocation_class,
        data_dep,
        metadata_checksum,
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
        metadata_version_start_datetime,
        metadata_version_end_datetime,
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
    from versioned
)

select * from final