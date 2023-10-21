{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_booking_id', 'data_item_no', 'data_product_code','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__west__res_flight_booking_cleansed'),
            join_columns=['data_booking_id', 'data_item_no', 'data_product_code'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__west__res_flight_booking_cleansed') }}
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
        data_last_modified_time,
        data_seat_type,
        data_gds_queue_error_id,
        data_mask,
        data_is_lcc_result,
        data_transport_type,
        data_org_fare_type,
        data_doc_delivery_email,
        data_instant_ticketed,
        data_is_tbx_only_name_change,
        data_dynamic_ptc,
        data_whole_sale_comm,
        data_whole_sale_comm_type,
        data_user_letter_generated,
        data_ticketed_user,
        data_bsp_travel_code,
        data_crs_rules,
        data_cancel_pnr,
        data_connected_item_no,
        data_minimal_deposit_amount,
        data_deposit_date_emergency,
        data_valid_for_ticketing,
        data_manual_ticket_only,
        data_pnr_price_override_date,
        data_manually_priced_flight,
        data_pnr_cnx_checked,
        data_ssr_notes,
        data_corporate_id,
        data_h2_h_hold_release_time,
        data_gds_queue_msg,
        data_original_crs,
        data_original_pnr,
        data_migrated_date,
        data_apis_info_sent,
        data_booking_id,
        data_product_code,
        data_item_no,
        data_contract_type,
        data_fare_type,
        data_out_contract,
        data_out_rule,
        data_out_route_group,
        data_out_route,
        data_out_ticket_info_id,
        data_in_contract,
        data_in_rule,
        data_in_route_group,
        data_in_route,
        data_in_ticket_info_id,
        data_pnr,
        data_ticketing_deadline,
        data_ticketed,
        data_ticket_issue_date,
        data_cost_offset,
        data_tax_offset,
        data_airline_for_comm_calc,
        data_domestic_for_comm_calc,
        data_history_created,
        data_out_cabin,
        data_in_cabin,
        data_ticket_type,
        data_crs,
        data_fare_diff_with_basic_flight,
        data_ext_charge,
        data_class_upgrade_charge,
        data_supplement_charge,
        data_addon_charge,
        data_fare_created_office_id,
        data_tour_code,
        data_endorsement,
        data_iata_comm_persc,
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