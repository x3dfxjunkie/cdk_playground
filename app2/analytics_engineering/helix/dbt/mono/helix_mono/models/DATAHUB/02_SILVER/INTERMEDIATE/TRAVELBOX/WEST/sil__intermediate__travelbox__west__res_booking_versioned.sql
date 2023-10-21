{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_booking_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__west__res_booking_cleansed'),
            join_columns=['data_booking_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__west__res_booking_cleansed') }}
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
            partition by data_booking_id
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
        partition_columns = ['data_booking_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_price_diff,
        data_tax_diff,
        data_unavailable,
        data_sales_order_id,
        data_product_types,
        data_refund_authorised_amount,
        data_comm_refund_allowed_amt,
        data_promotion_id,
        data_profit,
        data_brochure_id,
        data_locale,
        data_ledger_destination,
        data_website_id,
        data_vip_booking,
        data_admin_booking,
        data_admin_booking_authorization,
        data_authorized_user,
        data_agent_ref,
        data_non_commissionable_price,
        data_destination,
        data_location_id,
        data_source_id,
        data_dont_collect_commission,
        data_booking_style,
        data_group_name,
        data_main_dest_country,
        data_group_booking_margin,
        data_ext_booking_id,
        data_group_booking_pax_updated,
        data_atol_type,
        data_assigned_user,
        data_assigned_date,
        data_client_status,
        data_tc_pay_grp,
        data_rq_item_indc,
        data_manual_dest_calculation,
        data_dest_city,
        data_flight_only,
        data_act_dest_country,
        data_manual_acct_dest_calculation,
        data_dep_airport,
        data_return_date,
        data_source_market,
        data_all_docs_dispatched,
        data_secondary_client_id,
        data_secondary_commission,
        data_secondary_com_percentage,
        data_opec,
        data_link_bookings,
        data_reservation_time,
        data_cancellation_reference,
        data_exclude_from_auto_refund,
        data_suppress_confirmation,
        data_quote_date,
        data_booking_date,
        data_departure_date,
        data_definite_due_date,
        data_definite_date,
        data_firm_due_date,
        data_firm_date,
        data_balance_due_date,
        data_full_payment_received_date,
        data_manual_comm,
        data_commission,
        data_total_price,
        data_total_cost,
        data_invoice_total,
        data_manual_deposit,
        data_deposit,
        data_discount,
        data_booked_user,
        data_media_code,
        data_distribution_channel,
        data_selling_currency,
        data_selling_to_base_exchange_rate,
        data_locked,
        data_commission_adjustment,
        data_commission_percentage,
        data_last_modified_time,
        data_system_generated_expiry_date,
        data_constraints_exist,
        data_journal_batch_no,
        data_modified,
        data_air_only_booking,
        data_agent_id,
        data_profile_id,
        data_address_no,
        data_contact_method,
        data_contact_number,
        data_comm_chq_authorized,
        data_comm_chq_note,
        data_client_self_billing,
        data_gsa_join_date,
        data_gsa_client,
        data_total_commission,
        data_discount_on_commission,
        data_insurance_due,
        data_total_tax_cost,
        data_total_tax_price,
        data_tax_included,
        data_refund_authorised,
        data_auto_cancel,
        data_booking_source,
        data_dispatch_method,
        data_dispatch_address,
        data_insurance_excluded,
        data_your_reference,
        data_counselor_name,
        data_counselor_ref_key,
        data_counselor_ref_value,
        data_last_mod_source,
        data_data_types,
        data_manual_deposit_due_date,
        data_block_code,
        data_group_master_id,
        data_invoice_status,
        data_booking_id,
        data_client_id,
        data_company,
        data_division,
        data_brand,
        data_booking_product,
        data_booking_type,
        data_booking_status,
        data_option_status,
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