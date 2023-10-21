{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_booking_id', 'data_item_no', 'data_product_code','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__east__res_booking_item_cleansed'),
            join_columns=['data_booking_id', 'data_item_no', 'data_product_code'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__east__res_booking_item_cleansed') }}
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
        data_guaranteed_status,
        data_rsr,
        data_express_checkout,
        data_vip_level,
        data_tax_exempt_type,
        data_bkg_access_security,
        data_market_segment_code,
        data_group_master_id,
        data_contact_name,
        data_guaranteed_card_identifier,
        data_quote_before_conv,
        data_gen_booking_ref_id,
        data_res_booking_sub_status,
        data_extended_src_booking_id,
        data_extended_src_product_code,
        data_extended_src_item_no,
        data_pre_payment,
        data_post_payment_date,
        data_post_payment,
        data_vouchers_sent,
        data_booked_as_agent,
        data_foreign_booking_id,
        data_foreign_crs,
        data_manually_added,
        data_agent_markup,
        data_inform_supplier,
        data_converted,
        data_converted_message,
        data_pkg_item_order,
        data_start_time,
        data_end_time,
        data_contract_to_base_ex_rate,
        data_nett_adult,
        data_nett_child,
        data_nett_infant,
        data_city_code,
        data_contract_ref,
        data_adt_manual_override,
        data_chd_manual_override,
        data_inf_manual_override,
        data_agreed_c_i_c_taxable,
        data_cache_price_adjustment,
        data_foreign_references,
        data_supplier_commission,
        data_holiday_template_id,
        data_composition_id,
        data_parent_item_no,
        data_non_commissionable_price,
        data_contract_version,
        data_org_package_no,
        data_itinerary_item_no,
        data_vcc_card_id,
        data_pay_scheme_id,
        data_pay_scheme_type,
        data_group_id,
        data_manual_item,
        data_supplier_tax_on_commision,
        data_internal_rq,
        data_issue_atol_receipt,
        data_h2_h_price_diff,
        data_pax_wise,
        data_old_supplier_res_ref,
        data_swap_itinerary_item_no,
        data_optional_pkg_item,
        data_adt_manual_override_cost,
        data_chd_manual_override_cost,
        data_inf_manual_override_cost,
        data_manually_com_pkg_item,
        data_non_refundable,
        data_non_amendable,
        data_on_save,
        data_item_trackable,
        data_voucher_status,
        data_booking_id,
        data_product_code,
        data_item_no,
        data_booking_status,
        data_contract_id,
        data_supplier_id,
        data_from_date,
        data_to_date,
        data_adult,
        data_child,
        data_infant,
        data_price,
        data_cost,
        data_cost_in_contract,
        data_currency_in_contract,
        data_booked_date,
        data_supplier_payment_status,
        data_pre_payment_date,
        data_total_price,
        data_total_cost,
        data_active_for_quote,
        data_cost_in_contract_adjustment,
        data_contract_to_selling_exc_rate,
        data_provisional,
        data_last_modified_time,
        data_quote_price_expiry_date,
        data_agreed_cost_in_contract,
        data_manifested,
        data_rate_type,
        data_package_booking_id,
        data_package_no,
        data_supplier_res_ref,
        data_markup_ref,
        data_itinerary_order,
        data_brand,
        data_from_package,
        data_cost_state,
        data_pkg_element_no,
        data_pkg_alt_no,
        data_pkg_upg_no,
        data_commission,
        data_commission_percentage,
        data_manual_comm,
        data_note,
        data_country_code,
        data_state_code,
        data_agreed_cost_lock,
        data_item_desc,
        data_total_tax_price,
        data_total_tax_cost,
        data_total_cost_in_contract,
        data_overidden_comm_rate,
        data_manual_override,
        data_gross_adult,
        data_gross_child,
        data_gross_infant,
        data_booked_user,
        data_tax_included,
        data_pkg_element_name,
        data_associate_product_code,
        data_associate_item_no,
        data_associate_session_id,
        data_voucher_generated,
        data_item_bkg_source,
        data_breakage,
        data_group_code,
        data_group_type,
        data_fulfillment_status,
        data_confidential_rate,
        data_print_option,
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