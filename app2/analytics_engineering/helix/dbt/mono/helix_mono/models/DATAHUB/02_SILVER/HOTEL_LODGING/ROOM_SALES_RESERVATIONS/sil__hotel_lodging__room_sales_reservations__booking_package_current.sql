-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.RES_BOOKING_VERSIONED
WITH cte_sterbv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__res_booking_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.CLI_CLIENT_VERSIONED
cte_steccv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__cli_client_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.RES_BOOKING_TYPE_VERSIONED
cte_sterbtv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__res_booking_type_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.RES_BOOKING_STATUS_VERSIONED
cte_sterbsv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__res_booking_status_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.RES_OPTION_STATUS_VERSIONED
cte_sterosv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__res_option_status_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.CLI_TRADE_CLIENT_VERSIONED
cte_stectcv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__cli_trade_client_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.CLI_TRADE_CLIENT_TYPE_VERSIONED
cte_stectctv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__cli_trade_client_type_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.PKG_ITINERARY_VERSIONED
cte_stepiv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__pkg_itinerary_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.PRODUCT_TYPE_VERSIONED
cte_steptv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__product_type_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.PKG_SELLABLE_MEMBERSHIP_TYPE_VERSIONED
cte_stepsmtv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__pkg_sellable_membership_type_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.PRODUCT_GROUP_VERSIONED
cte_stepgv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__product_group_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.CLI_FREQ_MEMBER_TYPE_VERSIONED
cte_stecfmtv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__cli_freq_member_type_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.RES_BOOKING_PACKAGE_VERSIONED
cte_sterbpv AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__res_booking_package_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- CTE for SIL_INTERMEDIATE_TRAVELBOX_EAST.RES_BOOKING_PACKAGE_VERSIONED
cte_stpkgh AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__travelbox__east__pkg_holiday_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- Main CTE joining all the tables
final_cte AS (
    SELECT
        cte_sterbpv.data_booking_id AS booking_package_id,
        cte_sterbpv.data_package_no AS booking_package_no,
        cte_sterbpv.data_type AS booking_package_type_value,
        cte_sterbpv.data_booking_status AS booking_package_status,
        cte_sterbpv.data_adult AS booking_package_adult_count,
        cte_sterbpv.data_child AS booking_package_child_count,
        cte_sterbpv.data_infant AS booking_package_infant_count,
        cte_sterbpv.data_adult_cost AS booking_package_adult_cost,
        cte_sterbpv.data_child_cost AS booking_package_child_cost,
        cte_sterbpv.data_infant_cost AS booking_package_infant_cost,
        cte_sterbpv.data_adult_price AS booking_package_adult_price,
        cte_sterbpv.data_child_price AS booking_package_child_price,
        cte_sterbpv.data_infant_price AS booking_package_infant_price,
        cte_sterbpv.data_total_cost AS booking_package_total_cost,
        cte_sterbpv.data_total_price AS booking_package_total_price,
        cte_sterbpv.data_package_description AS booking_package_description,
        cte_sterbpv.data_manually_added AS booking_package_manually_added,
        cte_sterbpv.data_price_overridden AS booking_package_price_overridden,
        cte_sterbpv.data_departure_date AS booking_package_departure_date,
        cte_sterbpv.data_overall_margin AS booking_package_overall_margin,
        cte_sterbpv.data_package_id AS booking_package_id,
        cte_sterbpv.data_itinerary_no AS booking_package_itinerary_no,
        cte_sterbpv.data_product_group AS booking_package_product_group,
        cte_sterbpv.data_product_type AS booking_package_product_type,
        cte_sterbpv.data_holiday_type AS booking_package_holiday_type,
        cte_sterbpv.data_package_code AS booking_package_code,
        cte_sterbpv.data_package_name AS booking_package_name,
        cte_sterbpv.data_nights AS booking_package_nights,
        cte_sterbpv.data_stop_sale AS booking_package_stop_sale,
        cte_sterbpv.data_stop_sale_reason AS booking_package_stop_sale_reason,
        cte_sterbpv.data_brand AS booking_package_brand,
        cte_sterbpv.data_commission AS booking_package_commission,
        cte_sterbpv.data_commission_percentage AS booking_package_commission_percentage,
        cte_sterbpv.data_manual_comm AS booking_package_manual_commission,
        cte_sterbpv.data_markup_individually AS booking_package_markup_individually,
        cte_sterbpv.data_discount AS booking_package_discount,
        cte_sterbpv.data_pkg_occ_scheme_key AS booking_package_occ_scheme_key,
        cte_sterbpv.data_booked_date AS booking_package_booked_date,
        cte_sterbpv.data_adult_price_adjustment AS booking_package_adult_price_adjustment,
        cte_sterbpv.data_child_price_adjustment AS booking_package_child_price_adjustment,
        cte_sterbpv.data_infant_price_adjustment AS booking_package_infant_price_adjustment,
        cte_sterbpv.data_cf_score AS booking_package_cf_score,
        cte_sterbpv.data_ws_session_id AS booking_package_widesearch_session_id,
        cte_sterbpv.data_adult_pkg_markup AS booking_package_adult_package_markup,
        cte_sterbpv.data_child_pkg_markup AS booking_package_child_package_markup,
        cte_sterbpv.data_infant_pkg_markup AS booking_package_infant_package_markup,
        cte_sterbpv.data_adult_pkg_discount AS booking_package_adult_package_discount,
        cte_sterbpv.data_child_pkg_discount AS booking_package_child_package_discount,
        cte_sterbpv.data_infant_pkg_discount AS booking_package_infant_package_discount,
        cte_sterbpv.data_discount_scheme_id AS booking_package_discount_scheme_id,
        cte_sterbpv.data_calculation_type AS booking_package_calculation_type,
        cte_sterbpv.data_pkg_discount AS booking_package_package_discount,
        cte_sterbpv.data_price_grid_code AS booking_package_price_grid_code,
        cte_sterbpv.data_commission_rate AS booking_package_commission_rate,
        cte_sterbpv.data_commission_override AS booking_package_commission_override,
        cte_sterbpv.data_appealing AS booking_package_appealing,
        cte_sterbpv.data_threshold AS booking_package_threshold_value,
        cte_sterbpv.data_promotion AS booking_package_promotion,
        cte_sterbpv.data_removed_item_itin_nums AS booking_package_removed_item_itinerary_numbers,
        cte_sterbpv.data_itinerary_name AS booking_package_itinerary_name,
        cte_sterbpv.data_manually_combined_package AS booking_package_manually_combined_package,
        cte_sterbpv.data_cms_package_code AS booking_package_cms_package_code,
        cte_sterbpv.data_cms_itinerary_code AS booking_package_cms_itinerary_code,
        cte_sterbpv.data_cms_grid_code AS booking_package_cms_grid_code,
        cte_sterbpv.data_round_err_on_tot_price AS booking_package_round_err_on_tot_price,
        cte_sterbpv.data_reservation_id AS booking_package_reservation_id,
        cte_sterbpv.data_sub_type AS booking_package_sub_type,
        cte_sterbpv.data_associate_pkg_no AS booking_package_associate_package_no,
        cte_sterbpv.data_associate_session_id AS booking_package_associate_session_id,
        cte_sterbpv.data_last_modified_time AS booking_package_last_modified_time,
        cte_sterbpv.data_item_bkg_source AS booking_package_item_booking_source,
        cte_sterbpv.data_nightly_prices AS booking_package_nightly_prices,
        cte_sterbv.data_company AS booking_company,
        cte_sterbv.data_division AS booking_division,
        cte_sterbv.data_brand AS booking_brand,
        cte_sterbv.data_booking_type AS booking_type,
        cte_sterbtv.data_name AS booking_type_name,
        cte_sterbv.data_client_id AS booking_client_id,
        cte_steccv.data_type AS client_type,
        cte_steccv.data_client_ref AS client_reference,
        cte_steccv.data_name AS client_name,
        cte_sterbv.data_booking_status AS booking_status,
        cte_sterbsv.data_status AS booking_status_name,
        cte_sterbv.data_option_status AS booking_option_status,
        cte_sterosv.data_status AS option_status_name,
        cte_sterbv.data_departure_date AS booking_arrival_date,
        cte_sterbv.data_return_date AS booking_departure_date,
        cte_sterbv.data_quote_date AS booking_quote_date,
        cte_sterbv.data_booking_date AS booking_booking_date,
        cte_sterbv.data_definite_due_date AS booking_definite_due_date,
        cte_sterbv.data_definite_date AS booking_definite_date,
        cte_sterbv.data_firm_due_date AS booking_firm_due_date,
        cte_sterbv.data_firm_date AS booking_firm_date,
        cte_sterbv.data_balance_due_date AS booking_balance_due_date,
        cte_sterbv.data_full_payment_received_date AS booking_full_payment_received_date,
        cte_sterbv.data_manual_comm AS booking_manual_commission,
        cte_sterbv.data_commission AS booking_commission,
        cte_sterbv.data_total_price AS booking_total_price,
        cte_sterbv.data_total_cost AS booking_total_cost,
        cte_sterbv.data_manual_deposit AS booking_manual_deposit,
        cte_sterbv.data_deposit AS booking_deposit_amount,
        cte_sterbv.data_discount AS booking_discount_amount,
        cte_sterbv.data_booked_user AS booking_booked_user,
        cte_sterbv.data_media_code AS booking_media_code,
        cte_sterbv.data_distribution_channel AS booking_distribution_channel,
        cte_sterbv.data_selling_currency AS booking_selling_currency,
        cte_sterbv.data_selling_to_base_exchange_rate AS booking_selling_to_base_exchange_rate,
        cte_sterbv.data_locked AS booking_locked_booking,
        cte_sterbv.data_commission_adjustment AS booking_commission_adjustment,
        cte_sterbv.data_commission_percentage AS booking_commission_percentage,
        cte_sterbv.data_last_modified_time AS booking_last_modified_time,
        cte_sterbv.data_agent_id AS booking_agent_id,
        cte_sterbv.data_profile_id AS booking_profile_id,
        cte_sterbv.data_address_no AS booking_address_no,
        cte_sterbv.data_contact_method AS booking_contact_method,
        cte_sterbv.data_contact_number AS booking_contact_number,
        cte_sterbv.data_client_self_billing AS booking_client_self_billing,
        cte_sterbv.data_gsa_join_date AS booking_general_sales_agent_join_date,
        cte_sterbv.data_gsa_client AS booking_general_sales_agent_client,
        cte_sterbv.data_total_commission AS booking_total_commission,
        cte_sterbv.data_discount_on_commission AS booking_discount_on_commission,
        cte_sterbv.data_insurance_due AS booking_insurance_due,
        cte_sterbv.data_total_tax_cost AS booking_total_tax_cost,
        cte_sterbv.data_total_tax_price AS booking_total_tax_price,
        cte_sterbv.data_tax_included AS booking_tax_included,
        cte_sterbv.data_refund_authorised AS booking_refund_authorized,
        cte_sterbv.data_refund_authorised_amount AS booking_refund_authorised_amount,
        cte_sterbv.data_promotion_id AS booking_promotion_id,
        cte_sterbv.data_profit AS booking_profit,
        cte_sterbv.data_non_commissionable_price AS booking_non_commissionable_price,
        cte_sterbv.data_brochure_id AS booking_brochure_id,
        cte_sterbv.data_locale AS booking_locale,
        cte_sterbv.data_vip_booking AS booking_vip_booking,
        cte_sterbv.data_destination AS booking_destination,
        cte_sterbv.data_location_id AS booking_location_id,
        cte_sterbv.data_source_id AS booking_source_id,
        cte_sterbv.data_dont_collect_commission AS booking_dont_collect_commission,
        cte_sterbv.data_main_dest_country AS booking_main_destination_country,
        cte_sterbv.data_ext_booking_id AS booking_external_booking_id,
        cte_sterbv.data_atol_type AS booking_atol_type,
        cte_sterbv.data_client_status AS booking_client_status,
        cte_sterbv.data_tc_pay_grp AS booking_trade_client_payment_group_id,
        cte_sterbv.data_rq_item_indc AS booking_item_on_request_indicator,
        cte_sterbv.data_manual_dest_calculation AS booking_manual_destestination_calculation,
        cte_sterbv.data_dest_city AS booking_destination_city,
        cte_sterbv.data_flight_only AS booking_flight_only,
        cte_sterbv.data_act_dest_country AS booking_tax_calculation_destination_country,
        cte_sterbv.data_manual_acct_dest_calculation AS booking_manual_tax_destination_calculation,
        cte_sterbv.data_dep_airport AS booking_departure_airport,
        cte_sterbv.data_source_market AS booking_source_market,
        cte_sterbv.data_all_docs_dispatched AS booking_all_docs_dispatched,
        cte_sterbv.data_link_bookings AS booking_link_bookings,
        cte_sterbv.data_reservation_time AS booking_reservation_time,
        cte_sterbv.data_auto_cancel AS booking_auto_cancel,
        cte_sterbv.data_booking_source AS booking_source,
        cte_sterbv.data_dispatch_method AS booking_dispatch_method,
        cte_sterbv.data_dispatch_address AS booking_dispatch_address,
        cte_sterbv.data_insurance_excluded AS booking_insurance_excluded,
        cte_sterbv.data_your_reference AS booking_your_reference,
        cte_sterbv.data_counselor_name AS booking_counselor_name,
        cte_sterbv.data_counselor_ref_key AS booking_counselor_reference_key,
        cte_sterbv.data_counselor_ref_value AS booking_counselor_reference_value,
        cte_sterbv.data_last_mod_source AS booking_last_modification_source,
        cte_sterbv.data_manual_deposit_due_date AS booking_manual_deposit_due_date,
        cte_sterbv.data_block_code AS booking_block_code,
        cte_sterbv.data_group_name AS booking_group_name,
        cte_stectcv.data_client_id AS trade_client_id,
        cte_stectcv.data_remit_commission_ho AS trade_client_remit_commission_headoffice,
        cte_stectcv.data_division AS trade_client_division,
        cte_stectcv.data_town AS trade_client_town,
        cte_stectcv.data_multiple AS trade_client_multiple,
        cte_stectcv.data_promotion AS trade_client_promotion,
        cte_stectcv.data_web AS trade_client_web,
        cte_stectcv.data_agreement_status AS trade_client_agreement_status,
        cte_stectcv.data_comission_from_ho AS trade_client_comission_from_headoffice,
        cte_stectcv.data_comm_group AS trade_client_commission_group,
        cte_stectcv.data_nett_rate AS trade_client_net_rate,
        cte_stectcv.data_client_rating AS trade_client_rating,
        cte_stectcv.data_deposit_scheme AS trade_client_deposit_scheme,
        cte_stectcv.data_comp_reg AS trade_client_company_registration_number,
        cte_stectcv.data_issue_invoice AS trade_client_issue_invoice,
        cte_stectcv.data_collect_from_client AS trade_client_collect_from_client,
        cte_stectcv.data_issue_itinerary AS trade_client_issue_itinerary,
        cte_stectcv.data_issue_voucher AS trade_client_issue_voucher,
        cte_stectcv.data_show_commission AS trade_client_show_commission,
        cte_stectcv.data_gsa_number AS trade_client_general_sales_agent_number,
        cte_stectcv.data_gsa_join_date AS trade_client_general_sales_agent_join_date,
        cte_stectcv.data_self_billing AS trade_client_self_billing,
        cte_stectcv.data_amendement_scheme AS trade_client_amendement_scheme,
        cte_stectcv.data_canx_scheme AS trade_client_cancellation_scheme,
        cte_stectcv.data_option_scheme AS trade_client_option_scheme,
        cte_stectcv.data_booking_ref_type AS trade_client_booking_reference_type,
        cte_stectcv.data_booking_ref_compulsary AS trade_client_booking_reference_compulsary,
        cte_stectcv.data_search_in_call_centre AS trade_client_search_in_call_center,
        cte_stectcv.data_logo AS trade_client_logo,
        cte_stectcv.data_credit_limit_ho AS trade_client_credit_limit_headoffice,
        cte_stectcv.data_wra_agents AS trade_client_wholesale_remittance_advice_agents,
        cte_stectcv.data_gsa_client AS trade_client_general_sales_agent_client,
        cte_stectcv.data_payment_group AS trade_client_payment_group,
        cte_stectcv.data_tax_reg_no AS trade_client_tax_registration_number,
        cte_stectcv.data_area AS trade_client_area,
        cte_stectcv.data_language_code AS trade_client_language_code,
        cte_stectcv.data_payment_method AS trade_client_payment_method,
        cte_stectcv.data_credit_agent_id AS trade_client_credit_agent_id,
        cte_stectcv.data_include_tax_on_comm AS trade_client_include_tax_on_commission,
        cte_stectcv.data_sales_allowed AS trade_client_sales_allowed,
        cte_stectcv.data_documents_allowed AS trade_client_documents_allowed,
        cte_stectcv.data_exclude_partner_emailing AS trade_client_exclude_partner_emailing,
        cte_stectcv.data_trade_client_type AS trade_client_type,
        cte_stectctv.data_type_id AS trade_client_type_type_id,
        cte_stectctv.data_name AS trade_client_type_name,
        cte_stectcv.data_accept_edocs AS trade_client_accept_edocs,
        cte_stectcv.data_accept_ebook_details AS trade_client_accept_ebook_details,
        cte_stectcv.data_atol_cert_not_required AS trade_client_atol_cert_not_required,
        cte_stectcv.data_atol_name AS trade_client_atol_name,
        cte_stectcv.data_mail_method AS trade_client_mail_method,
        cte_stectcv.data_client_level AS trade_client_level,
        cte_stectcv.data_last_modified_time AS trade_client_last_modified_time,
        cte_stepiv.data_itinerary_no AS package_itinerary_itinerary_no,
        cte_stepiv.data_code AS package_itinerary_code,
        cte_stepiv.data_name AS package_itinerary_name,
        cte_stepiv.data_nights AS package_itinerary_nights,
        cte_stepiv.data_status AS package_itinerary_status,
        cte_stepiv.data_stage AS package_itinerary_stage,
        cte_stepiv.data_stage_reason AS package_itinerary_stage_reason,
        cte_stepiv.data_extra_stays_only AS package_itinerary_extra_stays_only,
        cte_stepiv.data_package_stage AS package_itinerary_package_stage,
        cte_stepiv.data_calc_pax_base AS package_itinerary_calc_pax_base,
        cte_stepiv.data_push_sales_exist AS package_itinerary_push_sales_exist,
        cte_stepiv.data_special_offer_exist AS package_itinerary_special_offer_exist,
        cte_stepiv.data_blackout_exist AS package_itinerary_blackout_exist,
        cte_stepiv.data_visa_exist AS package_itinerary_visa_exist,
        cte_stepiv.data_iti_dest_city AS package_itinerary_destination_city,
        cte_stepiv.data_country AS package_itinerary_country,
        cte_stepiv.data_tour_region AS package_itinerary_tour_region,
        cte_stepiv.data_supplier_id AS package_itinerary_supplier_id,
        cte_stepiv.data_resort AS package_itinerary_resort,
        cte_stepiv.data_min_bkg_to_dep_days AS package_itinerary_min_bkg_to_dep_days,
        cte_stepiv.data_set_no AS package_itinerary_set_number,
        cte_stepiv.data_hotel_code AS package_itinerary_hotel_code,
        cte_stepiv.data_last_modified_time AS package_itinerary_last_modified_time,
        cte_steptv.data_code AS product_type_code,
        cte_steptv.data_product_group AS product_type_product_group,
        cte_steptv.data_name AS product_type_name,
        cte_stepsmtv.data_membership_type AS package_sellable_membership_type,
        cte_stepsmtv.data_membershipid AS package_sellable_membership_id,
        cte_stepsmtv.data_last_modified_time AS package_sellable_last_modified_time,
        cte_stepgv.data_name AS product_group_name,
        cte_stecfmtv.data_description AS client_freq_member_type_description,
        cte_stecfmtv.data_category_code AS client_freq_member_type_category_code,
        cte_stecfmtv.data_is_passenger_type AS client_freq_member_type_is_passenger_type,
        cte_stecfmtv.data_agency_id AS client_freq_member_type_agency_id,
        cte_stecfmtv.data_last_modified_time AS client_freq_member_type_last_modified_time,
        cte_sterbpv.data_package_no AS booking_package_no,
        cte_sterbpv.data_type AS booking_package_type_value,
        cte_sterbpv.data_booking_status AS booking_package_status,
        cte_sterbpv.data_adult AS booking_package_adult_count,
        cte_sterbpv.data_child AS booking_package_child_count,
        cte_sterbpv.data_infant AS booking_package_infant_count,
        cte_sterbpv.data_adult_cost AS booking_package_adult_cost,
        cte_sterbpv.data_child_cost AS booking_package_child_cost,
        cte_sterbpv.data_infant_cost AS booking_package_infant_cost,
        cte_sterbpv.data_adult_price AS booking_package_adult_price,
        cte_sterbpv.data_child_price AS booking_package_child_price,
        cte_sterbpv.data_infant_price AS booking_package_infant_price,
        cte_sterbpv.data_total_cost AS booking_package_total_cost,
        cte_sterbpv.data_total_price AS booking_package_total_price,
        cte_sterbpv.data_package_description AS booking_package_description,
        cte_sterbpv.data_manually_added AS booking_package_manually_added,
        cte_sterbpv.data_price_overridden AS booking_package_price_overridden,
        cte_sterbpv.data_departure_date AS booking_package_departure_date,
        cte_sterbpv.data_overall_margin AS booking_package_overall_margin,
        cte_sterbpv.data_package_id AS booking_package_id,
        cte_sterbpv.data_itinerary_no AS booking_package_itinerary_no,
        cte_sterbpv.data_product_group AS booking_package_product_group,
        cte_sterbpv.data_product_type AS booking_package_product_type,
        cte_sterbpv.data_holiday_type AS booking_package_holiday_type,
        cte_sterbpv.data_package_code AS booking_package_code,
        cte_sterbpv.data_package_name AS booking_package_name,
        cte_sterbpv.data_nights AS booking_package_nights,
        cte_sterbpv.data_stop_sale AS booking_package_stop_sale,
        cte_sterbpv.data_stop_sale_reason AS booking_package_stop_sale_reason,
        cte_sterbpv.data_brand AS booking_package_brand,
        cte_sterbpv.data_commission AS booking_package_commission,
        cte_sterbpv.data_commission_percentage AS booking_package_commission_percentage,
        cte_sterbpv.data_manual_comm AS booking_package_manual_commission,
        cte_sterbpv.data_markup_individually AS booking_package_markup_individually,
        cte_sterbpv.data_discount AS booking_package_discount,
        cte_sterbpv.data_pkg_occ_scheme_key AS booking_package_occ_scheme_key,
        cte_sterbpv.data_booked_date AS booking_package_booked_date,
        cte_sterbpv.data_adult_price_adjustment AS booking_package_adult_price_adjustment,
        cte_sterbpv.data_child_price_adjustment AS booking_package_child_price_adjustment,
        cte_sterbpv.data_infant_price_adjustment AS booking_package_infant_price_adjustment,
        cte_sterbpv.data_cf_score AS booking_package_cf_score,
        cte_sterbpv.data_ws_session_id AS booking_package_widesearch_session_id,
        cte_sterbpv.data_adult_pkg_markup AS booking_package_adult_package_markup,
        cte_sterbpv.data_child_pkg_markup AS booking_package_child_package_markup,
        cte_sterbpv.data_infant_pkg_markup AS booking_package_infant_package_markup,
        cte_sterbpv.data_adult_pkg_discount AS booking_package_adult_package_discount,
        cte_sterbpv.data_child_pkg_discount AS booking_package_child_package_discount,
        cte_sterbpv.data_infant_pkg_discount AS booking_package_infant_package_discount,
        cte_sterbpv.data_discount_scheme_id AS booking_package_discount_scheme_id,
        cte_sterbpv.data_calculation_type AS booking_package_calculation_type,
        cte_sterbpv.data_pkg_discount AS booking_package_package_discount,
        cte_sterbpv.data_price_grid_code AS booking_package_price_grid_code,
        cte_sterbpv.data_commission_rate AS booking_package_commission_rate,
        cte_sterbpv.data_commission_override AS booking_package_commission_override,
        cte_sterbpv.data_appealing AS booking_package_appealing,
        cte_sterbpv.data_threshold AS booking_package_threshold_value,
        cte_sterbpv.data_promotion AS booking_package_promotion,
        cte_sterbpv.data_removed_item_itin_nums AS booking_package_removed_item_itinerary_numbers,
        cte_sterbpv.data_itinerary_name AS booking_package_itinerary_name,
        cte_sterbpv.data_manually_combined_package AS booking_package_manually_combined_package,
        cte_sterbpv.data_cms_package_code AS booking_package_cms_package_code,
        cte_sterbpv.data_cms_itinerary_code AS booking_package_cms_itinerary_code,
        cte_sterbpv.data_cms_grid_code AS booking_package_cms_grid_code,
        cte_sterbpv.data_round_err_on_tot_price AS booking_package_round_err_on_tot_price,
        cte_sterbpv.data_reservation_id AS booking_package_reservation_id,
        cte_sterbpv.data_sub_type AS booking_package_sub_type,
        cte_sterbpv.data_associate_pkg_no AS booking_package_associate_package_no,
        cte_sterbpv.data_associate_session_id AS booking_package_associate_session_id,
        cte_sterbpv.data_last_modified_time AS booking_package_last_modified_time,
        cte_sterbpv.data_item_bkg_source AS booking_package_item_booking_source,
        cte_sterbpv.data_nightly_prices AS booking_package_nightly_prices,
        cte_sterbv.data_company AS booking_company,
        cte_sterbv.data_division AS booking_division,
        cte_sterbv.data_brand AS booking_brand,
        cte_sterbv.data_booking_type AS booking_type,
        cte_sterbtv.data_name AS booking_type_name,
        cte_sterbv.data_client_id AS booking_client_id,
        cte_steccv.data_type AS client_type,
        cte_steccv.data_client_ref AS client_reference,
        cte_steccv.data_name AS client_name,
        cte_sterbv.data_booking_status AS booking_status,
        cte_sterbsv.data_status AS booking_status_name,
        cte_sterbv.data_option_status AS booking_option_status,
        cte_sterosv.data_status AS option_status_name,
        cte_sterbv.data_departure_date AS booking_arrival_date,
        cte_sterbv.data_return_date AS booking_departure_date,
        cte_sterbv.data_quote_date AS booking_quote_date,
        cte_sterbv.data_booking_date AS booking_booking_date,
        cte_sterbv.data_definite_due_date AS booking_definite_due_date,
        cte_sterbv.data_definite_date AS booking_definite_date,
        cte_sterbv.data_firm_due_date AS booking_firm_due_date,
        cte_sterbv.data_firm_date AS booking_firm_date,
        cte_sterbv.data_balance_due_date AS booking_balance_due_date,
        cte_sterbv.data_full_payment_received_date AS booking_full_payment_received_date,
        cte_sterbv.data_manual_comm AS booking_manual_commission,
        cte_sterbv.data_commission AS booking_commission,
        cte_sterbv.data_total_price AS booking_total_price,
        cte_sterbv.data_total_cost AS booking_total_cost,
        cte_sterbv.data_manual_deposit AS booking_manual_deposit,
        cte_sterbv.data_deposit AS booking_deposit_amount,
        cte_sterbv.data_discount AS booking_discount_amount,
        cte_sterbv.data_booked_user AS booking_booked_user,
        cte_sterbv.data_media_code AS booking_media_code,
        cte_sterbv.data_distribution_channel AS booking_distribution_channel,
        cte_sterbv.data_selling_currency AS booking_selling_currency,
        cte_sterbv.data_selling_to_base_exchange_rate AS booking_selling_to_base_exchange_rate,
        cte_sterbv.data_locked AS booking_locked_booking,
        cte_sterbv.data_commission_adjustment AS booking_commission_adjustment,
        cte_sterbv.data_commission_percentage AS booking_commission_percentage,
        cte_sterbv.data_last_modified_time AS booking_last_modified_time,
        cte_sterbv.data_agent_id AS booking_agent_id,
        cte_sterbv.data_profile_id AS booking_profile_id,
        cte_sterbv.data_address_no AS booking_address_no,
        cte_sterbv.data_contact_method AS booking_contact_method,
        cte_sterbv.data_contact_number AS booking_contact_number,
        cte_sterbv.data_client_self_billing AS booking_client_self_billing,
        cte_sterbv.data_gsa_join_date AS booking_general_sales_agent_join_date,
        cte_sterbv.data_gsa_client AS booking_general_sales_agent_client,
        cte_sterbv.data_total_commission AS booking_total_commission,
        cte_sterbv.data_discount_on_commission AS booking_discount_on_commission,
        cte_sterbv.data_insurance_due AS booking_insurance_due,
        cte_sterbv.data_total_tax_cost AS booking_total_tax_cost,
        cte_sterbv.data_total_tax_price AS booking_total_tax_price,
        cte_sterbv.data_tax_included AS booking_tax_included,
        cte_sterbv.data_refund_authorised AS booking_refund_authorized,
        cte_sterbv.data_refund_authorised_amount AS booking_refund_authorised_amount,
        cte_sterbv.data_promotion_id AS booking_promotion_id,
        cte_sterbv.data_profit AS booking_profit,
        cte_sterbv.data_non_commissionable_price AS booking_non_commissionable_price,
        cte_sterbv.data_brochure_id AS booking_brochure_id,
        cte_sterbv.data_locale AS booking_locale,
        cte_sterbv.data_vip_booking AS booking_vip_booking,
        cte_sterbv.data_destination AS booking_destination,
        cte_sterbv.data_location_id AS booking_location_id,
        cte_sterbv.data_source_id AS booking_source_id,
        cte_sterbv.data_dont_collect_commission AS booking_dont_collect_commission,
        cte_sterbv.data_main_dest_country AS booking_main_destination_country,
        cte_sterbv.data_ext_booking_id AS booking_external_booking_id,
        cte_sterbv.data_atol_type AS booking_atol_type,
        cte_sterbv.data_client_status AS booking_client_status,
        cte_sterbv.data_tc_pay_grp AS booking_trade_client_payment_group_id,
        cte_sterbv.data_rq_item_indc AS booking_item_on_request_indicator,
        cte_sterbv.data_manual_dest_calculation AS booking_manual_destestination_calculation,
        cte_sterbv.data_dest_city AS booking_destination_city,
        cte_sterbv.data_flight_only AS booking_flight_only,
        cte_sterbv.data_act_dest_country AS booking_tax_calculation_destination_country,
        cte_sterbv.data_manual_acct_dest_calculation AS booking_manual_tax_destination_calculation,
        cte_sterbv.data_dep_airport AS booking_departure_airport,
        cte_sterbv.data_source_market AS booking_source_market,
        cte_sterbv.data_all_docs_dispatched AS booking_all_docs_dispatched,
        cte_sterbv.data_link_bookings AS booking_link_bookings,
        cte_sterbv.data_reservation_time AS booking_reservation_time,
        cte_sterbv.data_auto_cancel AS booking_auto_cancel,
        cte_sterbv.data_booking_source AS booking_source,
        cte_sterbv.data_dispatch_method AS booking_dispatch_method,
        cte_sterbv.data_dispatch_address AS booking_dispatch_address,
        cte_sterbv.data_insurance_excluded AS booking_insurance_excluded,
        cte_sterbv.data_your_reference AS booking_your_reference,
        cte_sterbv.data_counselor_name AS booking_counselor_name,
        cte_sterbv.data_counselor_ref_key AS booking_counselor_reference_key,
        cte_sterbv.data_counselor_ref_value AS booking_counselor_reference_value,
        cte_sterbv.data_last_mod_source AS booking_last_modification_source,
        cte_sterbv.data_manual_deposit_due_date AS booking_manual_deposit_due_date,
        cte_sterbv.data_block_code AS booking_block_code,
        cte_sterbv.data_group_name AS booking_group_name,
        cte_stectcv.data_client_id AS trade_client_id,
        cte_stectcv.data_remit_commission_ho AS trade_client_remit_commission_headoffice,
        cte_stectcv.data_division AS trade_client_division,
        cte_stectcv.data_town AS trade_client_town,
        cte_stectcv.data_multiple AS trade_client_multiple,
        cte_stectcv.data_promotion AS trade_client_promotion,
        cte_stectcv.data_web AS trade_client_web,
        cte_stectcv.data_agreement_status AS trade_client_agreement_status,
        cte_stectcv.data_comission_from_ho AS trade_client_comission_from_headoffice,
        cte_stectcv.data_comm_group AS trade_client_commission_group,
        cte_stectcv.data_nett_rate AS trade_client_net_rate,
        cte_stectcv.data_client_rating AS trade_client_rating,
        cte_stectcv.data_deposit_scheme AS trade_client_deposit_scheme,
        cte_stectcv.data_comp_reg AS trade_client_company_registration_number,
        cte_stectcv.data_issue_invoice AS trade_client_issue_invoice,
        cte_stectcv.data_collect_from_client AS trade_client_collect_from_client,
        cte_stectcv.data_issue_itinerary AS trade_client_issue_itinerary,
        cte_stectcv.data_issue_voucher AS trade_client_issue_voucher,
        cte_stectcv.data_show_commission AS trade_client_show_commission,
        cte_stectcv.data_gsa_number AS trade_client_general_sales_agent_number,
        cte_stectcv.data_gsa_join_date AS trade_client_general_sales_agent_join_date,
        cte_stectcv.data_self_billing AS trade_client_self_billing,
        cte_stectcv.data_amendement_scheme AS trade_client_amendement_scheme,
        cte_stectcv.data_canx_scheme AS trade_client_cancellation_scheme,
        cte_stectcv.data_option_scheme AS trade_client_option_scheme,
        cte_stectcv.data_booking_ref_type AS trade_client_booking_reference_type,
        cte_stectcv.data_booking_ref_compulsary AS trade_client_booking_reference_compulsary,
        cte_stectcv.data_search_in_call_centre AS trade_client_search_in_call_center,
        cte_stectcv.data_logo AS trade_client_logo,
        cte_stectcv.data_credit_limit_ho AS trade_client_credit_limit_headoffice,
        cte_stectcv.data_wra_agents AS trade_client_wholesale_remittance_advice_agents,
        cte_stectcv.data_gsa_client AS trade_client_general_sales_agent_client,
        cte_stectcv.data_payment_group AS trade_client_payment_group,
        cte_stectcv.data_tax_reg_no AS trade_client_tax_registration_number,
        cte_stectcv.data_area AS trade_client_area,
        cte_stectcv.data_language_code AS trade_client_language_code,
        cte_stectcv.data_payment_method AS trade_client_payment_method,
        cte_stectcv.data_credit_agent_id AS trade_client_credit_agent_id,
        cte_stectcv.data_include_tax_on_comm AS trade_client_include_tax_on_commission,
        cte_stectcv.data_sales_allowed AS trade_client_sales_allowed,
        cte_stectcv.data_documents_allowed AS trade_client_documents_allowed,
        cte_stectcv.data_exclude_partner_emailing AS trade_client_exclude_partner_emailing,
        cte_stectcv.data_trade_client_type AS trade_client_type,
        cte_stectctv.data_type_id AS trade_client_type_type_id,
        cte_stectctv.data_name AS trade_client_type_name,
        cte_stectcv.data_accept_edocs AS trade_client_accept_edocs,
        cte_stectcv.data_accept_ebook_details AS trade_client_accept_ebook_details,
        cte_stectcv.data_atol_cert_not_required AS trade_client_atol_cert_not_required,
        cte_stectcv.data_atol_name AS trade_client_atol_name,
        cte_stectcv.data_mail_method AS trade_client_mail_method,
        cte_stectcv.data_client_level AS trade_client_level,
        cte_stepiv.data_itinerary_no AS package_itinerary_itinerary_no,
        cte_stepiv.data_code AS package_itinerary_code,
        cte_stepiv.data_name AS package_itinerary_name,
        cte_stepiv.data_nights AS package_itinerary_nights,
        cte_stepiv.data_status AS package_itinerary_status,
        cte_stepiv.data_stage AS package_itinerary_stage,
        cte_stepiv.data_stage_reason AS package_itinerary_stage_reason,
        cte_stepiv.data_extra_stays_only AS package_itinerary_extra_stays_only,
        cte_stepiv.data_package_stage AS package_itinerary_package_stage,
        cte_stepiv.data_calc_pax_base AS package_itinerary_calc_pax_base,
        cte_stepiv.data_push_sales_exist AS package_itinerary_push_sales_exist,
        cte_stepiv.data_special_offer_exist AS package_itinerary_special_offer_exist,
        cte_stepiv.data_blackout_exist AS package_itinerary_blackout_exist,
        cte_stepiv.data_visa_exist AS package_itinerary_visa_exist,
        cte_stepiv.data_iti_dest_city AS package_itinerary_destination_city,
        cte_stepiv.data_country AS package_itinerary_country,
        cte_stepiv.data_tour_region AS package_itinerary_tour_region,
        cte_stepiv.data_supplier_id AS package_itinerary_supplier_id,
        cte_stepiv.data_resort AS package_itinerary_resort,
        cte_stepiv.data_min_bkg_to_dep_days AS package_itinerary_min_bkg_to_dep_days,
        cte_stepiv.data_set_no AS package_itinerary_set_number,
        cte_stepiv.data_hotel_code AS package_itinerary_hotel_code,
        cte_stepiv.data_last_modified_time AS package_itinerary_last_modified_time,
        cte_steptv.data_code AS product_type_code,
        cte_steptv.data_product_group AS product_type_product_group,
        cte_steptv.data_name AS product_type_name,
        cte_stepsmtv.data_membership_type AS package_sellable_membership_type,
        cte_stepsmtv.data_membershipid AS package_sellable_membership_id,
        cte_stepsmtv.data_last_modified_time AS package_sellable_last_modified_time,
        cte_stepgv.data_name AS product_group_name,
        cte_stecfmtv.data_description AS client_freq_member_type_description,
        cte_stecfmtv.data_category_code AS client_freq_member_type_category_code,
        cte_stecfmtv.data_is_passenger_type AS client_freq_member_type_is_passenger_type,
        cte_stecfmtv.data_agency_id AS client_freq_member_type_agency_id,
        cte_stecfmtv.data_last_modified_time AS client_freq_member_type_last_modified_time
    FROM
        cte_sterbv
        JOIN cte_sterbpv
        ON cte_sterbv.data_booking_id = cte_sterbpv.data_booking_id
        JOIN cte_sterbtv
        ON cte_sterbv.data_booking_type = cte_sterbtv.data_code
        JOIN cte_sterbsv
        ON cte_sterbv.data_booking_status = cte_sterbsv.data_id
        JOIN cte_sterosv
        ON cte_sterbv.data_option_status = cte_sterosv.data_id
        JOIN cte_steccv
        ON cte_sterbv.data_client_id = cte_steccv.data_client_id
        JOIN cte_stectcv
        ON cte_sterbv.data_client_id = cte_stectcv.data_client_id
        JOIN cte_stectctv
        ON cte_stectctv.data_code = cte_stectcv.data_trade_client_type
        JOIN cte_stepiv
        ON cte_stepiv.data_package_id = cte_sterbpv.data_package_id
        AND cte_stepiv.data_itinerary_no = cte_sterbpv.data_itinerary_no
        JOIN cte_stpkgh
        ON cte_stpkgh.data_package_id = cte_sterbpv.data_package_id
        JOIN cte_steptv
        ON cte_steptv.data_code = cte_stpkgh.data_product_type
        JOIN cte_stepsmtv
        ON cte_stepsmtv.data_pkg_group_id = cte_stpkgh.data_pkg_group_id
        JOIN cte_stepgv
        ON cte_stepgv.data_code = cte_steptv.data_product_group
        JOIN cte_stecfmtv
        ON cte_stecfmtv.data_id = cte_stepsmtv.data_membership_type
)

SELECT
    *
FROM
    final_cte
