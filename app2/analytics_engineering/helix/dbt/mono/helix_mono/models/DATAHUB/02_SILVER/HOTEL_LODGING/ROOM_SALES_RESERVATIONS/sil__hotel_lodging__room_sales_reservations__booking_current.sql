with cte_booking as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__res_booking_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_bookingstatus as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__res_booking_status_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_optionstatus as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__res_option_status_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_bookingtype as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__res_booking_type_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_company as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cmp_company_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_division as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cmp_division_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_distributionchannel as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__distribution_channel_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_brand as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__brand_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_locale as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__locale_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_client as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cli_client_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_clientgroup as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__client_group_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_bookingcnx as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__res_booking_cnx_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_bookingcnxreason as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__res_booking_cnx_reason_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final_query as (

    select
        cte_booking.data_booking_id as booking_id,
        cte_booking.data_company as booking_company,
        cte_booking.data_division as booking_division,
        cte_booking.data_brand as booking_brand,
        cte_booking.data_booking_type as booking_type,
        cte_booking.data_client_id as booking_client_id,
        cte_booking.data_booking_status as booking_status,
        cte_booking.data_option_status as booking_option_status,
        cte_company.data_name as company_name,
        cte_division.data_name as division_name,
        cte_brand.data_name as brand_name,
        cte_bookingtype.data_name as booking_type_name,
        cte_clientgroup.data_code as client_group_code,
        cte_clientgroup.data_name as client_group_name,
        cte_client.data_type as client_type,
        cte_client.data_client_ref as client_reference,
        cte_client.data_name as client_name,
        cte_bookingstatus.data_status as booking_status_name,
        cte_optionstatus.data_status as res_option_status_name,
        cte_booking.data_departure_date as booking_arrival_date,
        cte_booking.data_return_date as booking_departure_date,
        cte_booking.data_quote_date as booking_quote_date,
        cte_booking.data_booking_date as booking_date,
        cte_booking.data_definite_due_date as booking_definite_due_date,
        cte_booking.data_definite_date as booking_definite_date,
        cte_booking.data_firm_due_date as booking_firm_due_date,
        cte_booking.data_firm_date as booking_firm_date,
        cte_booking.data_balance_due_date as booking_balance_due_date,
        cte_booking.data_full_payment_received_date as booking_full_payment_received_date,
        cte_booking.data_manual_comm as booking_manual_commission,
        cte_booking.data_commission as booking_commission,
        cte_booking.data_total_price as booking_total_price,
        cte_booking.data_total_cost as booking_total_cost,
        cte_booking.data_manual_deposit as booking_manual_deposit,
        cte_booking.data_deposit as booking_deposit_amount,
        cte_booking.data_discount as booking_discount,
        cte_booking.data_booked_user as booking_booked_user,
        cte_booking.data_media_code as booking_media_code,
        cte_booking.data_distribution_channel as booking_distribution_channel,
        cte_distributionchannel.data_name as distribution_channel_name,
        cte_booking.data_selling_currency as booking_selling_currency,
        cte_booking.data_selling_to_base_exchange_rate as booking_selling_to_base_exchange_rate,
        cte_booking.data_locked as booking_locked,
        cte_booking.data_commission_adjustment as booking_commission_adjustment,
        cte_booking.data_commission_percentage as booking_commission_percentage,
        cte_booking.data_last_modified_time as booking_last_modified_time,
        cte_booking.data_system_generated_expiry_date as booking_system_generated_expiry_date,
        cte_booking.data_agent_id as booking_agent_id,
        cte_booking.data_profile_id as booking_profile_id,
        cte_booking.data_address_no as booking_address_number,
        cte_booking.data_contact_method as booking_contact_method,
        cte_booking.data_contact_number as booking_contact_number,
        cte_booking.data_client_self_billing as booking_client_self_billing,
        cte_booking.data_gsa_join_date as booking_gsa_join_date,
        cte_booking.data_gsa_client as booking_gsa_client,
        cte_booking.data_total_commission as booking_total_commission,
        cte_booking.data_discount_on_commission as booking_discount_on_commission,
        cte_booking.data_insurance_due as booking_insurance_due,
        cte_booking.data_total_tax_cost as booking_total_tax_cost,
        cte_booking.data_total_tax_price as booking_total_tax_price,
        cte_booking.data_tax_included as booking_tax_included,
        cte_booking.data_refund_authorised as booking_refund_authorized,
        cte_booking.data_refund_authorised_amount as booking_refund_authorized_amount,
        cte_booking.data_promotion_id as booking_promotion_id,
        cte_booking.data_profit as booking_profit,
        cte_booking.data_non_commissionable_price as booking_non_commissionable_price,
        cte_booking.data_brochure_id as booking_brochure_id,
        cte_booking.data_locale as booking_locale,
        cte_locale.data_language as locale_language,
        cte_locale.data_country as locale_country,
        cte_locale.data_name as locale_name,
        cte_locale.data_font as locale_font,
        cte_locale.data_iso_code as locale_iso_code,
        cte_booking.data_vip_booking as booking_vip_booking,
        cte_booking.data_destination as booking_destination,
        cte_booking.data_location_id as booking_location_id,
        cte_booking.data_source_id as booking_source_id,
        cte_booking.data_dont_collect_commission as booking_dont_collect_commission,
        cte_booking.data_group_name as booking_group_name,
        cte_booking.data_main_dest_country as booking_main_destination_country,
        cte_booking.data_ext_booking_id as booking_external_booking_id,
        cte_booking.data_atol_type as booking_atol_type,
        cte_booking.data_client_status as booking_client_status,
        cte_booking.data_tc_pay_grp as booking_trade_client_pay_group,
        cte_booking.data_rq_item_indc as booking_request_item_indc,
        cte_booking.data_manual_dest_calculation as booking_manual_destination_calculation,
        cte_booking.data_dest_city as booking_destination_city,
        cte_booking.data_flight_only as booking_flight_only,
        cte_booking.data_act_dest_country as booking_accounting_destination_country,
        cte_booking.data_manual_acct_dest_calculation as booking_manual_accounting_destination_calculation,
        cte_booking.data_dep_airport as booking_departure_airport,
        cte_booking.data_source_market as booking_source_market,
        cte_booking.data_all_docs_dispatched as booking_all_docs_dispatched,
        cte_booking.data_link_bookings as booking_link_bookings,
        cte_booking.data_reservation_time as booking_reservation_time,
        cte_booking.data_auto_cancel as booking_auto_cancel,
        cte_booking.data_booking_source as booking_booking_source,
        cte_booking.data_dispatch_method as booking_dispatch_method,
        cte_booking.data_dispatch_address as booking_dispatch_address,
        cte_booking.data_insurance_excluded as booking_insurance_excluded,
        cte_booking.data_your_reference as booking_your_reference,
        cte_booking.data_counselor_name as booking_counselor_name,
        cte_booking.data_counselor_ref_key as booking_counselor_ref_key,
        cte_booking.data_counselor_ref_value as booking_counselor_ref_value,
        cte_booking.data_last_mod_source as booking_last_mod_source,
        cte_booking.data_manual_deposit_due_date as booking_manual_deposit_due_date,
        cte_booking.data_block_code as booking_block_code,
        cte_bookingcnx.data_cnx_reason_id as booking_cancellation_reason_id,
        cte_bookingcnx.data_cnx_user as booking_cancellation_user,
        cte_bookingcnx.data_cnx_date as booking_cancellation_date,
        cte_bookingcnx.data_cnx_charge as booking_cancellation_charge,
        cte_bookingcnx.data_cnx_charge_commissionable as booking_cancellation_charge_commissionable,
        cte_bookingcnx.data_cnx_no as booking_cancellation_no,
        cte_bookingcnx.data_cnx_calculated_date as booking_cancellation_calculated_date,
        cte_bookingcnx.data_cause_id as booking_cancellation_cause_id,
        cte_bookingcnx.data_reason_type as booking_cancellation_reason_type,
        cte_bookingcnxreason.data_reason as booking_cancellation_reason,
        cte_bookingcnxreason.data_conf_doc_required as booking_cancellation_reason_conf_doc_required,
        cte_bookingcnxreason.data_status as booking_cancellation_reason_status,
        cte_bookingcnxreason.data_repricing_date as booking_cancellation_reason_repricing_date,
        cte_bookingcnxreason.data_applicable_products as booking_cancellation_reason_applicable_products
    from cte_booking
        left join cte_bookingstatus on cte_booking.data_booking_status = cte_bookingstatus.data_id
        left join cte_optionstatus on cte_booking.data_option_status = cte_optionstatus.data_id
        left join cte_bookingtype on cte_booking.data_booking_type = cte_bookingtype.data_code
        left join cte_company on cte_company.data_code = cte_booking.data_company
        left join cte_division on cte_division.data_code = cte_booking.data_division
        left join cte_distributionchannel on cte_distributionchannel.data_code = cte_booking.data_distribution_channel
        left join cte_brand on cte_brand.data_code = cte_booking.data_brand
        left join cte_locale on cte_locale.data_code = cte_booking.data_locale
        left join cte_client on cte_client.data_client_id = cte_booking.data_client_id
        left join cte_clientgroup on cte_client.data_client_group = cte_clientgroup.data_code
        left outer join cte_bookingcnx on cte_booking.data_booking_id = cte_bookingcnx.data_booking_id
        left outer join cte_bookingcnxreason on cte_bookingcnx.data_cnx_reason_id = cte_bookingcnxreason.data_id
)

select * from final_query