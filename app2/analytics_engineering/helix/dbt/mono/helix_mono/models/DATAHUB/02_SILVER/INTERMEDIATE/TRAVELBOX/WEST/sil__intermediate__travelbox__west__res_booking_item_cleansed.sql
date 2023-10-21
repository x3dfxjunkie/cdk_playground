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
    from {{ source('brz_travelbox_west', 'res_booking_item') }}

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
        TRIM(src.data_print_option) as data_print_option,
        TRIM(src.data_guaranteed_status) as data_guaranteed_status,
        TRIM(src.data_rsr) as data_rsr,
        TRIM(src.data_express_checkout) as data_express_checkout,
        TRIM(src.data_vip_level) as data_vip_level,
        TRIM(src.data_tax_exempt_type) as data_tax_exempt_type,
        TRIM(src.data_bkg_access_security) as data_bkg_access_security,
        TRIM(src.data_market_segment_code) as data_market_segment_code,
        src.data_group_master_id as data_group_master_id,
        TRIM(src.data_contact_name) as data_contact_name,
        src.data_res_booking_sub_status as data_res_booking_sub_status,
        src.data_extended_src_booking_id as data_extended_src_booking_id,
        TRIM(src.data_extended_src_product_code) as data_extended_src_product_code,
        src.data_extended_src_item_no as data_extended_src_item_no,
        TRIM(src.data_guaranteed_card_identifier) as data_guaranteed_card_identifier,
        TRIM(src.data_quote_before_conv) as data_quote_before_conv,
        src.data_gen_booking_ref_id as data_gen_booking_ref_id,
        TRIM(src.data_pkg_element_name) as data_pkg_element_name,
        TRIM(src.data_associate_product_code) as data_associate_product_code,
        src.data_associate_item_no as data_associate_item_no,
        TRIM(src.data_associate_session_id) as data_associate_session_id,
        TRIM(src.data_voucher_generated) as data_voucher_generated,
        TRIM(src.data_item_bkg_source) as data_item_bkg_source,
        src.data_breakage as data_breakage,
        TRIM(src.data_group_code) as data_group_code,
        TRIM(src.data_group_type) as data_group_type,
        TRIM(src.data_fulfillment_status) as data_fulfillment_status,
        TRIM(src.data_confidential_rate) as data_confidential_rate,
        src.data_booking_id as data_booking_id,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        src.data_booking_status as data_booking_status,
        src.data_contract_id as data_contract_id,
        src.data_supplier_id as data_supplier_id,
        src.data_from_date as data_from_date,
        src.data_to_date as data_to_date,
        src.data_adult as data_adult,
        src.data_child as data_child,
        src.data_infant as data_infant,
        src.data_price as data_price,
        src.data_cost as data_cost,
        src.data_cost_in_contract as data_cost_in_contract,
        TRIM(src.data_currency_in_contract) as data_currency_in_contract,
        src.data_booked_date as data_booked_date,
        src.data_supplier_payment_status as data_supplier_payment_status,
        src.data_pre_payment_date as data_pre_payment_date,
        src.data_pre_payment as data_pre_payment,
        src.data_post_payment_date as data_post_payment_date,
        src.data_post_payment as data_post_payment,
        TRIM(src.data_vouchers_sent) as data_vouchers_sent,
        TRIM(src.data_booked_as_agent) as data_booked_as_agent,
        TRIM(src.data_foreign_booking_id) as data_foreign_booking_id,
        TRIM(src.data_foreign_crs) as data_foreign_crs,
        TRIM(src.data_manually_added) as data_manually_added,
        src.data_agent_markup as data_agent_markup,
        TRIM(src.data_inform_supplier) as data_inform_supplier,
        TRIM(src.data_converted) as data_converted,
        TRIM(src.data_converted_message) as data_converted_message,
        src.data_total_price as data_total_price,
        src.data_total_cost as data_total_cost,
        TRIM(src.data_active_for_quote) as data_active_for_quote,
        src.data_cost_in_contract_adjustment as data_cost_in_contract_adjustment,
        src.data_contract_to_selling_exc_rate as data_contract_to_selling_exc_rate,
        TRIM(src.data_provisional) as data_provisional,
        src.data_last_modified_time as data_last_modified_time,
        src.data_quote_price_expiry_date as data_quote_price_expiry_date,
        src.data_agreed_cost_in_contract as data_agreed_cost_in_contract,
        TRIM(src.data_manifested) as data_manifested,
        TRIM(src.data_rate_type) as data_rate_type,
        src.data_package_booking_id as data_package_booking_id,
        src.data_package_no as data_package_no,
        TRIM(src.data_supplier_res_ref) as data_supplier_res_ref,
        TRIM(src.data_markup_ref) as data_markup_ref,
        src.data_itinerary_order as data_itinerary_order,
        TRIM(src.data_brand) as data_brand,
        TRIM(src.data_from_package) as data_from_package,
        src.data_cost_state as data_cost_state,
        src.data_pkg_element_no as data_pkg_element_no,
        src.data_pkg_alt_no as data_pkg_alt_no,
        src.data_pkg_upg_no as data_pkg_upg_no,
        src.data_commission as data_commission,
        src.data_commission_percentage as data_commission_percentage,
        TRIM(src.data_manual_comm) as data_manual_comm,
        TRIM(src.data_note) as data_note,
        TRIM(src.data_country_code) as data_country_code,
        TRIM(src.data_state_code) as data_state_code,
        TRIM(src.data_agreed_cost_lock) as data_agreed_cost_lock,
        TRIM(src.data_item_desc) as data_item_desc,
        src.data_total_tax_price as data_total_tax_price,
        src.data_total_tax_cost as data_total_tax_cost,
        src.data_total_cost_in_contract as data_total_cost_in_contract,
        src.data_overidden_comm_rate as data_overidden_comm_rate,
        src.data_manual_override as data_manual_override,
        src.data_gross_adult as data_gross_adult,
        src.data_gross_child as data_gross_child,
        src.data_gross_infant as data_gross_infant,
        src.data_booked_user as data_booked_user,
        TRIM(src.data_tax_included) as data_tax_included,
        src.data_pkg_item_order as data_pkg_item_order,
        src.data_start_time as data_start_time,
        src.data_end_time as data_end_time,
        src.data_contract_to_base_ex_rate as data_contract_to_base_ex_rate,
        src.data_nett_adult as data_nett_adult,
        src.data_nett_child as data_nett_child,
        src.data_nett_infant as data_nett_infant,
        TRIM(src.data_city_code) as data_city_code,
        src.data_adt_manual_override as data_adt_manual_override,
        src.data_chd_manual_override as data_chd_manual_override,
        src.data_inf_manual_override as data_inf_manual_override,
        TRIM(src.data_agreed_c_i_c_taxable) as data_agreed_c_i_c_taxable,
        src.data_cache_price_adjustment as data_cache_price_adjustment,
        TRIM(src.data_foreign_references) as data_foreign_references,
        src.data_supplier_commission as data_supplier_commission,
        src.data_holiday_template_id as data_holiday_template_id,
        src.data_composition_id as data_composition_id,
        src.data_parent_item_no as data_parent_item_no,
        src.data_non_commissionable_price as data_non_commissionable_price,
        src.data_contract_version as data_contract_version,
        src.data_org_package_no as data_org_package_no,
        src.data_itinerary_item_no as data_itinerary_item_no,
        TRIM(src.data_vcc_card_id) as data_vcc_card_id,
        src.data_pay_scheme_id as data_pay_scheme_id,
        TRIM(src.data_pay_scheme_type) as data_pay_scheme_type,
        TRIM(src.data_group_id) as data_group_id,
        TRIM(src.data_manual_item) as data_manual_item,
        src.data_supplier_tax_on_commision as data_supplier_tax_on_commision,
        TRIM(src.data_internal_rq) as data_internal_rq,
        TRIM(src.data_issue_atol_receipt) as data_issue_atol_receipt,
        src.data_h2_h_price_diff as data_h2_h_price_diff,
        TRIM(src.data_pax_wise) as data_pax_wise,
        TRIM(src.data_old_supplier_res_ref) as data_old_supplier_res_ref,
        src.data_swap_itinerary_item_no as data_swap_itinerary_item_no,
        TRIM(src.data_optional_pkg_item) as data_optional_pkg_item,
        src.data_adt_manual_override_cost as data_adt_manual_override_cost,
        src.data_chd_manual_override_cost as data_chd_manual_override_cost,
        src.data_inf_manual_override_cost as data_inf_manual_override_cost,
        TRIM(src.data_manually_com_pkg_item) as data_manually_com_pkg_item,
        TRIM(src.data_non_refundable) as data_non_refundable,
        TRIM(src.data_non_amendable) as data_non_amendable,
        TRIM(src.data_on_save) as data_on_save,
        TRIM(src.data_item_trackable) as data_item_trackable,
        TRIM(src.data_voucher_status) as data_voucher_status,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_print_option',
            'src.data_guaranteed_status',
            'src.data_rsr',
            'src.data_express_checkout',
            'src.data_vip_level',
            'src.data_tax_exempt_type',
            'src.data_bkg_access_security',
            'src.data_market_segment_code',
            'src.data_group_master_id',
            'src.data_contact_name',
            'src.data_res_booking_sub_status',
            'src.data_extended_src_booking_id',
            'src.data_extended_src_product_code',
            'src.data_extended_src_item_no',
            'src.data_guaranteed_card_identifier',
            'src.data_quote_before_conv',
            'src.data_gen_booking_ref_id',
            'src.data_pkg_element_name',
            'src.data_associate_product_code',
            'src.data_associate_item_no',
            'src.data_associate_session_id',
            'src.data_voucher_generated',
            'src.data_item_bkg_source',
            'src.data_breakage',
            'src.data_group_code',
            'src.data_group_type',
            'src.data_fulfillment_status',
            'src.data_confidential_rate',
            'src.data_booking_status',
            'src.data_contract_id',
            'src.data_supplier_id',
            'src.data_from_date',
            'src.data_to_date',
            'src.data_adult',
            'src.data_child',
            'src.data_infant',
            'src.data_price',
            'src.data_cost',
            'src.data_cost_in_contract',
            'src.data_currency_in_contract',
            'src.data_booked_date',
            'src.data_supplier_payment_status',
            'src.data_pre_payment_date',
            'src.data_pre_payment',
            'src.data_post_payment_date',
            'src.data_post_payment',
            'src.data_vouchers_sent',
            'src.data_booked_as_agent',
            'src.data_foreign_booking_id',
            'src.data_foreign_crs',
            'src.data_manually_added',
            'src.data_agent_markup',
            'src.data_inform_supplier',
            'src.data_converted',
            'src.data_converted_message',
            'src.data_total_price',
            'src.data_total_cost',
            'src.data_active_for_quote',
            'src.data_cost_in_contract_adjustment',
            'src.data_contract_to_selling_exc_rate',
            'src.data_provisional',
            'src.data_last_modified_time',
            'src.data_quote_price_expiry_date',
            'src.data_agreed_cost_in_contract',
            'src.data_manifested',
            'src.data_rate_type',
            'src.data_package_booking_id',
            'src.data_package_no',
            'src.data_supplier_res_ref',
            'src.data_markup_ref',
            'src.data_itinerary_order',
            'src.data_brand',
            'src.data_from_package',
            'src.data_cost_state',
            'src.data_pkg_element_no',
            'src.data_pkg_alt_no',
            'src.data_pkg_upg_no',
            'src.data_commission',
            'src.data_commission_percentage',
            'src.data_manual_comm',
            'src.data_note',
            'src.data_country_code',
            'src.data_state_code',
            'src.data_agreed_cost_lock',
            'src.data_item_desc',
            'src.data_total_tax_price',
            'src.data_total_tax_cost',
            'src.data_total_cost_in_contract',
            'src.data_overidden_comm_rate',
            'src.data_manual_override',
            'src.data_gross_adult',
            'src.data_gross_child',
            'src.data_gross_infant',
            'src.data_booked_user',
            'src.data_tax_included',
            'src.data_pkg_item_order',
            'src.data_start_time',
            'src.data_end_time',
            'src.data_contract_to_base_ex_rate',
            'src.data_nett_adult',
            'src.data_nett_child',
            'src.data_nett_infant',
            'src.data_city_code',
            'src.data_adt_manual_override',
            'src.data_chd_manual_override',
            'src.data_inf_manual_override',
            'src.data_agreed_c_i_c_taxable',
            'src.data_cache_price_adjustment',
            'src.data_foreign_references',
            'src.data_supplier_commission',
            'src.data_holiday_template_id',
            'src.data_composition_id',
            'src.data_parent_item_no',
            'src.data_non_commissionable_price',
            'src.data_contract_version',
            'src.data_org_package_no',
            'src.data_itinerary_item_no',
            'src.data_vcc_card_id',
            'src.data_pay_scheme_id',
            'src.data_pay_scheme_type',
            'src.data_group_id',
            'src.data_manual_item',
            'src.data_supplier_tax_on_commision',
            'src.data_internal_rq',
            'src.data_issue_atol_receipt',
            'src.data_h2_h_price_diff',
            'src.data_pax_wise',
            'src.data_old_supplier_res_ref',
            'src.data_swap_itinerary_item_no',
            'src.data_optional_pkg_item',
            'src.data_adt_manual_override_cost',
            'src.data_chd_manual_override_cost',
            'src.data_inf_manual_override_cost',
            'src.data_manually_com_pkg_item',
            'src.data_non_refundable',
            'src.data_non_amendable',
            'src.data_on_save',
            'src.data_item_trackable',
            'src.data_voucher_status',
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