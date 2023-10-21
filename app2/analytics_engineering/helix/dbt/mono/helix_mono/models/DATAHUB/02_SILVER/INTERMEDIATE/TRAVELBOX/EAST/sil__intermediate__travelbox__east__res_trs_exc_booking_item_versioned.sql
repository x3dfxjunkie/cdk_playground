{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_booking_id', 'data_item_no', 'data_product_code','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__east__res_trs_exc_booking_item_cleansed'),
            join_columns=['data_booking_id', 'data_item_no', 'data_product_code'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__east__res_trs_exc_booking_item_cleansed') }}
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
            partition by data_booking_id, data_item_no, data_product_code
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
        partition_columns = ['data_booking_id', 'data_item_no', 'data_product_code']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_booking_id,
        data_product_code,
        data_item_no,
        data_type,
        data_transfer_no,
        data_pickup_point,
        data_dropoff_point,
        data_description,
        data_transfer_mode_code,
        data_transfer_mode,
        data_pickup_point_code,
        data_pickup_point_type,
        data_dropoff_point_code,
        data_dropoff_point_type,
        data_exc_location_id,
        data_exc_location,
        data_transfer_mode_no,
        data_minimum_vehicles,
        data_return_compulsory,
        data_transfer_name,
        data_h2_h_product_id,
        data_h2_h_booking_type_id,
        data_outbound_flight_no,
        data_outbound_dep_apt,
        data_outbound_arr_time,
        data_outbound_airline,
        data_inbound_flight_no,
        data_inbound_arr_apt,
        data_inbound_dep_time,
        data_inbound_airline,
        data_outbound_ship_name,
        data_outbound_dep_port,
        data_inbound_arr_port,
        data_inbound_ship_name,
        data_cru_foreign_bkng_id,
        data_start_end_times_edited,
        data_last_modified_time,
        data_fulfillment_freq,
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