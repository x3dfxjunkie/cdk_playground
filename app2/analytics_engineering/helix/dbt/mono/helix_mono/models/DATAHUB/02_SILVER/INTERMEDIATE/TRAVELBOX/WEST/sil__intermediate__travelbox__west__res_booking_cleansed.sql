{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'res_booking') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_booking_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id
),

-- cleansing the table
renamed as (
    select
        src.data_price_diff as data_price_diff,
        src.data_tax_diff as data_tax_diff,
        TRIM(src.data_unavailable) as data_unavailable,
        TRIM(src.data_sales_order_id) as data_sales_order_id,
        TRIM(src.data_product_types) as data_product_types,
        src.data_refund_authorised_amount as data_refund_authorised_amount,
        src.data_comm_refund_allowed_amt as data_comm_refund_allowed_amt,
        src.data_promotion_id as data_promotion_id,
        src.data_profit as data_profit,
        src.data_brochure_id as data_brochure_id,
        TRIM(src.data_locale) as data_locale,
        src.data_ledger_destination as data_ledger_destination,
        TRIM(src.data_website_id) as data_website_id,
        TRIM(src.data_vip_booking) as data_vip_booking,
        TRIM(src.data_admin_booking) as data_admin_booking,
        TRIM(src.data_admin_booking_authorization) as data_admin_booking_authorization,
        src.data_authorized_user as data_authorized_user,
        TRIM(src.data_agent_ref) as data_agent_ref,
        src.data_non_commissionable_price as data_non_commissionable_price,
        TRIM(src.data_destination) as data_destination,
        src.data_location_id as data_location_id,
        src.data_source_id as data_source_id,
        TRIM(src.data_dont_collect_commission) as data_dont_collect_commission,
        src.data_booking_style as data_booking_style,
        TRIM(src.data_group_name) as data_group_name,
        TRIM(src.data_main_dest_country) as data_main_dest_country,
        src.data_group_booking_margin as data_group_booking_margin,
        TRIM(src.data_ext_booking_id) as data_ext_booking_id,
        TRIM(src.data_group_booking_pax_updated) as data_group_booking_pax_updated,
        TRIM(src.data_atol_type) as data_atol_type,
        src.data_assigned_user as data_assigned_user,
        src.data_assigned_date as data_assigned_date,
        TRIM(src.data_client_status) as data_client_status,
        src.data_tc_pay_grp as data_tc_pay_grp,
        TRIM(src.data_rq_item_indc) as data_rq_item_indc,
        TRIM(src.data_manual_dest_calculation) as data_manual_dest_calculation,
        TRIM(src.data_dest_city) as data_dest_city,
        TRIM(src.data_flight_only) as data_flight_only,
        TRIM(src.data_act_dest_country) as data_act_dest_country,
        TRIM(src.data_manual_acct_dest_calculation) as data_manual_acct_dest_calculation,
        TRIM(src.data_dep_airport) as data_dep_airport,
        src.data_return_date as data_return_date,
        TRIM(src.data_source_market) as data_source_market,
        TRIM(src.data_all_docs_dispatched) as data_all_docs_dispatched,
        src.data_secondary_client_id as data_secondary_client_id,
        src.data_secondary_commission as data_secondary_commission,
        src.data_secondary_com_percentage as data_secondary_com_percentage,
        TRIM(src.data_opec) as data_opec,
        TRIM(src.data_link_bookings) as data_link_bookings,
        src.data_reservation_time as data_reservation_time,
        TRIM(src.data_cancellation_reference) as data_cancellation_reference,
        TRIM(src.data_exclude_from_auto_refund) as data_exclude_from_auto_refund,
        TRIM(src.data_suppress_confirmation) as data_suppress_confirmation,
        src.data_quote_date as data_quote_date,
        src.data_booking_date as data_booking_date,
        src.data_departure_date as data_departure_date,
        src.data_definite_due_date as data_definite_due_date,
        src.data_definite_date as data_definite_date,
        src.data_firm_due_date as data_firm_due_date,
        src.data_firm_date as data_firm_date,
        src.data_balance_due_date as data_balance_due_date,
        src.data_full_payment_received_date as data_full_payment_received_date,
        TRIM(src.data_manual_comm) as data_manual_comm,
        src.data_commission as data_commission,
        src.data_total_price as data_total_price,
        src.data_total_cost as data_total_cost,
        src.data_invoice_total as data_invoice_total,
        TRIM(src.data_manual_deposit) as data_manual_deposit,
        src.data_deposit as data_deposit,
        src.data_discount as data_discount,
        src.data_booked_user as data_booked_user,
        TRIM(src.data_media_code) as data_media_code,
        TRIM(src.data_distribution_channel) as data_distribution_channel,
        TRIM(src.data_selling_currency) as data_selling_currency,
        src.data_selling_to_base_exchange_rate as data_selling_to_base_exchange_rate,
        TRIM(src.data_locked) as data_locked,
        src.data_commission_adjustment as data_commission_adjustment,
        src.data_commission_percentage as data_commission_percentage,
        src.data_last_modified_time as data_last_modified_time,
        src.data_system_generated_expiry_date as data_system_generated_expiry_date,
        TRIM(src.data_constraints_exist) as data_constraints_exist,
        src.data_journal_batch_no as data_journal_batch_no,
        TRIM(src.data_modified) as data_modified,
        TRIM(src.data_air_only_booking) as data_air_only_booking,
        src.data_agent_id as data_agent_id,
        src.data_profile_id as data_profile_id,
        src.data_address_no as data_address_no,
        TRIM(src.data_contact_method) as data_contact_method,
        TRIM(src.data_contact_number) as data_contact_number,
        TRIM(src.data_comm_chq_authorized) as data_comm_chq_authorized,
        TRIM(src.data_comm_chq_note) as data_comm_chq_note,
        TRIM(src.data_client_self_billing) as data_client_self_billing,
        src.data_gsa_join_date as data_gsa_join_date,
        TRIM(src.data_gsa_client) as data_gsa_client,
        src.data_total_commission as data_total_commission,
        src.data_discount_on_commission as data_discount_on_commission,
        src.data_insurance_due as data_insurance_due,
        src.data_total_tax_cost as data_total_tax_cost,
        src.data_total_tax_price as data_total_tax_price,
        TRIM(src.data_tax_included) as data_tax_included,
        TRIM(src.data_refund_authorised) as data_refund_authorised,
        src.data_auto_cancel as data_auto_cancel,
        TRIM(src.data_booking_source) as data_booking_source,
        TRIM(src.data_dispatch_method) as data_dispatch_method,
        TRIM(src.data_dispatch_address) as data_dispatch_address,
        TRIM(src.data_insurance_excluded) as data_insurance_excluded,
        TRIM(src.data_your_reference) as data_your_reference,
        TRIM(src.data_counselor_name) as data_counselor_name,
        TRIM(src.data_counselor_ref_key) as data_counselor_ref_key,
        TRIM(src.data_counselor_ref_value) as data_counselor_ref_value,
        TRIM(src.data_last_mod_source) as data_last_mod_source,
        TRIM(src.data_data_types) as data_data_types,
        TRIM(src.data_manual_deposit_due_date) as data_manual_deposit_due_date,
        TRIM(src.data_block_code) as data_block_code,
        src.data_group_master_id as data_group_master_id,
        TRIM(src.data_invoice_status) as data_invoice_status,
        src.data_booking_id as data_booking_id,
        src.data_client_id as data_client_id,
        TRIM(src.data_company) as data_company,
        TRIM(src.data_division) as data_division,
        TRIM(src.data_brand) as data_brand,
        TRIM(src.data_booking_product) as data_booking_product,
        TRIM(src.data_booking_type) as data_booking_type,
        src.data_booking_status as data_booking_status,
        src.data_option_status as data_option_status,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_price_diff',
            'src.data_tax_diff',
            'src.data_unavailable',
            'src.data_sales_order_id',
            'src.data_product_types',
            'src.data_refund_authorised_amount',
            'src.data_comm_refund_allowed_amt',
            'src.data_promotion_id',
            'src.data_profit',
            'src.data_brochure_id',
            'src.data_locale',
            'src.data_ledger_destination',
            'src.data_website_id',
            'src.data_vip_booking',
            'src.data_admin_booking',
            'src.data_admin_booking_authorization',
            'src.data_authorized_user',
            'src.data_agent_ref',
            'src.data_non_commissionable_price',
            'src.data_destination',
            'src.data_location_id',
            'src.data_source_id',
            'src.data_dont_collect_commission',
            'src.data_booking_style',
            'src.data_group_name',
            'src.data_main_dest_country',
            'src.data_group_booking_margin',
            'src.data_ext_booking_id',
            'src.data_group_booking_pax_updated',
            'src.data_atol_type',
            'src.data_assigned_user',
            'src.data_assigned_date',
            'src.data_client_status',
            'src.data_tc_pay_grp',
            'src.data_rq_item_indc',
            'src.data_manual_dest_calculation',
            'src.data_dest_city',
            'src.data_flight_only',
            'src.data_act_dest_country',
            'src.data_manual_acct_dest_calculation',
            'src.data_dep_airport',
            'src.data_return_date',
            'src.data_source_market',
            'src.data_all_docs_dispatched',
            'src.data_secondary_client_id',
            'src.data_secondary_commission',
            'src.data_secondary_com_percentage',
            'src.data_opec',
            'src.data_link_bookings',
            'src.data_reservation_time',
            'src.data_cancellation_reference',
            'src.data_exclude_from_auto_refund',
            'src.data_suppress_confirmation',
            'src.data_quote_date',
            'src.data_booking_date',
            'src.data_departure_date',
            'src.data_definite_due_date',
            'src.data_definite_date',
            'src.data_firm_due_date',
            'src.data_firm_date',
            'src.data_balance_due_date',
            'src.data_full_payment_received_date',
            'src.data_manual_comm',
            'src.data_commission',
            'src.data_total_price',
            'src.data_total_cost',
            'src.data_invoice_total',
            'src.data_manual_deposit',
            'src.data_deposit',
            'src.data_discount',
            'src.data_booked_user',
            'src.data_media_code',
            'src.data_distribution_channel',
            'src.data_selling_currency',
            'src.data_selling_to_base_exchange_rate',
            'src.data_locked',
            'src.data_commission_adjustment',
            'src.data_commission_percentage',
            'src.data_last_modified_time',
            'src.data_system_generated_expiry_date',
            'src.data_constraints_exist',
            'src.data_journal_batch_no',
            'src.data_modified',
            'src.data_air_only_booking',
            'src.data_agent_id',
            'src.data_profile_id',
            'src.data_address_no',
            'src.data_contact_method',
            'src.data_contact_number',
            'src.data_comm_chq_authorized',
            'src.data_comm_chq_note',
            'src.data_client_self_billing',
            'src.data_gsa_join_date',
            'src.data_gsa_client',
            'src.data_total_commission',
            'src.data_discount_on_commission',
            'src.data_insurance_due',
            'src.data_total_tax_cost',
            'src.data_total_tax_price',
            'src.data_tax_included',
            'src.data_refund_authorised',
            'src.data_auto_cancel',
            'src.data_booking_source',
            'src.data_dispatch_method',
            'src.data_dispatch_address',
            'src.data_insurance_excluded',
            'src.data_your_reference',
            'src.data_counselor_name',
            'src.data_counselor_ref_key',
            'src.data_counselor_ref_value',
            'src.data_last_mod_source',
            'src.data_data_types',
            'src.data_manual_deposit_due_date',
            'src.data_block_code',
            'src.data_group_master_id',
            'src.data_invoice_status',
            'src.data_client_id',
            'src.data_company',
            'src.data_division',
            'src.data_brand',
            'src.data_booking_product',
            'src.data_booking_type',
            'src.data_booking_status',
            'src.data_option_status',
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
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final