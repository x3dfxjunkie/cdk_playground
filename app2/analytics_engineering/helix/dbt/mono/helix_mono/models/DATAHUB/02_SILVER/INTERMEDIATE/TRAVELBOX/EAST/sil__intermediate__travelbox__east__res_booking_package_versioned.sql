{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_booking_id', 'data_package_no','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__east__res_booking_package_cleansed'),
            join_columns=['data_booking_id', 'data_package_no'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__east__res_booking_package_cleansed') }}
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
            partition by data_booking_id, data_package_no
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
        partition_columns = ['data_booking_id', 'data_package_no']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_price_diff,
        data_tax_diff,
        data_extended_dest_booking_id,
        data_extended_dest_package_no,
        data_stop_sale,
        data_brand,
        data_base_package_no,
        data_commission,
        data_commission_percentage,
        data_manual_comm,
        data_markup_individually,
        data_discount,
        data_pkg_occ_scheme_key,
        data_booked_date,
        data_adult_price_adjustment,
        data_child_price_adjustment,
        data_infant_price_adjustment,
        data_cf_score,
        data_ws_session_id,
        data_adult_pkg_markup,
        data_child_pkg_markup,
        data_infant_pkg_markup,
        data_adult_pkg_discount,
        data_child_pkg_discount,
        data_infant_pkg_discount,
        data_discount_scheme_id,
        data_calculation_type,
        data_pkg_discount,
        data_price_grid_code,
        data_commission_rate,
        data_commission_override,
        data_appealing,
        data_threshold,
        data_promotion,
        data_removed_item_itin_nums,
        data_itinerary_name,
        data_manually_combined_package,
        data_cms_package_code,
        data_cms_itinerary_code,
        data_cms_grid_code,
        data_round_err_on_tot_price,
        data_reservation_id,
        data_sub_type,
        data_associate_pkg_no,
        data_associate_session_id,
        data_last_modified_time,
        data_item_bkg_source,
        data_nightly_prices,
        data_bypass_availability,
        data_send_to_property,
        data_send_to_property_status,
        data_total_duration,
        data_link_pkg_reference,
        data_quote_before_conv,
        data_baseline_priced,
        data_extended_src_booking_id,
        data_extended_src_product_code,
        data_extended_src_package_no,
        data_booking_id,
        data_package_no,
        data_type,
        data_booking_status,
        data_adult,
        data_child,
        data_infant,
        data_adult_cost,
        data_child_cost,
        data_infant_cost,
        data_adult_price,
        data_child_price,
        data_infant_price,
        data_total_cost,
        data_total_price,
        data_package_description,
        data_manually_added,
        data_price_overridden,
        data_departure_date,
        data_overall_margin,
        data_package_id,
        data_itinerary_no,
        data_product_group,
        data_product_type,
        data_holiday_type,
        data_package_code,
        data_package_name,
        data_nights,
        data_stop_sale_reason,
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