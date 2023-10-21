with cte_tradeclient as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cli_trade_client_versioned') }}
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

cte_tradeclienttype as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cli_trade_client_type_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_address as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cli_address_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_distributionchannel as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__distribution_channel_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_paymentgroup as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cli_payment_group_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_commgroup as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cli_comm_group_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
final_query as (

    select
        cte_tradeclient.data_client_id as trade_client_id,
        cte_tradeclient.data_remit_commission_ho as trade_client_remit_commission_headoffice,
        cte_tradeclient.data_division as trade_client_division,
        cte_tradeclient.data_town as trade_client_town,
        cte_tradeclient.data_multiple as trade_client_multiple,
        cte_tradeclient.data_promotion as trade_client_promotion,
        cte_tradeclient.data_web as trade_client_web,
        cte_tradeclient.data_agreement_status as trade_client_agreement_status,
        cte_tradeclient.data_comission_from_ho as trade_client_commission_from_headoffice,
        cte_tradeclient.data_comm_group as trade_client_commission_group,
        cte_tradeclient.data_nett_rate as trade_client_net_rate,
        cte_tradeclient.data_client_rating as trade_client_rating,
        cte_tradeclient.data_deposit_scheme as trade_client_deposit_scheme,
        cte_tradeclient.data_comp_reg as trade_client_company_registration_number,
        cte_tradeclient.data_issue_invoice as trade_client_issue_invoice,
        cte_tradeclient.data_collect_from_client as trade_client_collect_from_client,
        cte_tradeclient.data_issue_itinerary as trade_client_issue_itinerary,
        cte_tradeclient.data_issue_voucher as trade_client_issue_voucher,
        cte_tradeclient.data_show_commission as trade_client_show_commission,
        cte_tradeclient.data_gsa_number as trade_client_general_sales_agent_number,
        cte_tradeclient.data_gsa_join_date as trade_client_general_sales_agent_join_date,
        cte_tradeclient.data_self_billing as trade_client_self_billing,
        cte_tradeclient.data_canx_scheme as trade_client_cancellation_scheme,
        cte_tradeclient.data_option_scheme as trade_client_option_scheme,
        cte_tradeclient.data_booking_ref_type as trade_client_booking_reference_type,
        cte_tradeclient.data_booking_ref_compulsary as trade_client_booking_reference_compulsary,
        cte_tradeclient.data_search_in_call_centre as trade_client_search_in_call_center,
        cte_tradeclient.data_logo as trade_client_logo,
        cte_tradeclient.data_credit_limit_ho as trade_client_credit_limit_headoffice,
        cte_tradeclient.data_wra_agents as trade_client_wholesale_remittance_advice_agents,
        cte_tradeclient.data_gsa_client as trade_client_general_sales_agent_client,
        cte_tradeclient.data_payment_group as trade_client_payment_group,
        cte_paymentgroup.data_name as payment_group_name,
        cte_tradeclient.data_tax_reg_no as trade_client_tax_registration_number,
        cte_tradeclient.data_area as trade_client_area,
        cte_tradeclient.data_language_code as trade_client_language_code,
        cte_tradeclient.data_payment_method as trade_client_payment_method,
        cte_tradeclient.data_credit_agent_id as trade_client_credit_agent_id,
        cte_tradeclient.data_include_tax_on_comm as trade_client_include_tax_on_commission,
        cte_tradeclient.data_sales_allowed as trade_client_sales_allowed,
        cte_tradeclient.data_documents_allowed as trade_client_documents_allowed,
        cte_tradeclient.data_exclude_partner_emailing as trade_client_exclude_partner_emailing,
        cte_tradeclient.data_trade_client_type as trade_client_type,
        cte_tradeclienttype.data_type_id as trade_client_type_id,
        cte_tradeclienttype.data_name as trade_client_type_name,
        cte_tradeclient.data_accept_edocs as trade_client_accept_edocs,
        cte_tradeclient.data_accept_ebook_details as trade_client_accept_ebook_details,
        cte_tradeclient.data_atol_cert_not_required as trade_client_atol_cert_not_required,
        cte_tradeclient.data_atol_name as trade_client_atol_name,
        cte_tradeclient.data_mail_method as trade_client_mail_method,
        cte_tradeclient.data_client_level as trade_client_level,
        cte_tradeclient.data_last_modified_time as trade_client_last_modified_time,
        cte_client.data_type as client_type,
        cte_client.data_client_ref as client_reference,
        cte_client.data_name as client_name,
        cte_client.data_client_status as client_status,
        cte_client.data_media as client_media,
        cte_client.data_registered_date as client_registered_date,
        cte_client.data_client_group as client_group,
        cte_clientgroup.data_name as client_group_name,
        cte_client.data_entered_on as client_entered_on,
        cte_client.data_modified_on as client_modified_on,
        cte_client.data_registered_channel as client_registered_channel,
        cte_distributionchannel.data_name as distribution_channel_name,
        cte_client.data_modified_by as client_modified_by,
        cte_client.data_entered_by as client_entered_by,
        cte_client.data_primary_sales_agent as client_primary_sales_agent,
        cte_client.data_status_message as client_status_message,
        cte_client.data_tax_exempt as client_tax_exempt,
        cte_client.data_tax_override as client_tax_override,
        cte_client.data_grade_id as client_grade_id,
        cte_client.data_dealing_company as client_dealing_company,
        cte_client.data_dealing_division as client_dealing_division,
        cte_client.data_currency as client_currency,
        cte_client.data_active as client_active,
        cte_client.data_dealing_brand as client_dealing_brand,
        cte_client.data_locale as client_locale,
        cte_address.data_address_no as address_number,
        cte_address.data_title as address_title,
        cte_address.data_first_name as address_first_name,
        cte_address.data_middle_name as address_middle_name,
        cte_address.data_last_name as address_last_name,
        cte_address.data_department as address_department,
        cte_address.data_designation as address_designation,
        cte_address.data_street as address_street,
        cte_address.data_city as address_city,
        cte_address.data_county as address_county,
        cte_address.data_postal_code as address_post_code,
        cte_address.data_country as address_country,
        cte_address.data_contact_type as address_contact_type,
        cte_address.data_main as address_main,
        cte_address.data_middle_name as address_middle_name,
        cte_address.data_contact_category as address_contact_category,
        cte_commgroup.data_name as commission_group_name,
        cte_commgroup.data_sales_priority as commission_group_sales_priority,
        cte_commgroup.data_currency as commission_group_currency,
        cte_commgroup.data_applicable_date_type as commission_group_applicable_date_type,
        cte_commgroup.data_applicable_product as commission_group_applicable_product,
        cte_commgroup.data_applicable_limit_booking as commission_group_applicable_limit_booking,
        cte_commgroup.data_external_ref as commission_group_external_reference,
        cte_commgroup.data_com_grp_priority as commission_group_priority
    from cte_tradeclient
        inner join cte_client on cte_tradeclient.data_client_id = cte_client.data_client_id
        inner join cte_clientgroup on cte_client.data_client_group = cte_clientgroup.data_code
        left join cte_tradeclienttype on cte_tradeclient.data_trade_client_type = cte_tradeclienttype.data_code
        left join cte_address on cte_tradeclient.data_client_id = cte_address.data_client_id
        left join cte_distributionchannel on cte_client.data_registered_channel = cte_distributionchannel.data_code
        left join cte_paymentgroup on cte_tradeclient.data_payment_group = cte_paymentgroup.data_id
        left join cte_commgroup on cte_tradeclient.data_comm_group = cte_commgroup.data_comm_group_id
)

select * from final_query