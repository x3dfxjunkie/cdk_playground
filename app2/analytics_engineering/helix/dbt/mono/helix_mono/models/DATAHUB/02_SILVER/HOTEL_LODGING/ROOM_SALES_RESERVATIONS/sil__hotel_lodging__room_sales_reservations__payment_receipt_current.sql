with cte_clientreceipt as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__act_client_receipt_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_booking as (
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

cte_client as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cli_client_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_directclient as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__cli_direct_client_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_clientccreceipt as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__act_client_cc_receipt_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_cardtype as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__act_cc_card_type_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_clientrefund as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__act_client_refund_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_refundtype as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__act_client_refund_type_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

cte_ibtx as (
    select *
	from  {{ ref('sil__intermediate__travelbox__east__act_client_ibtx_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final_query as (

    select
        cte_clientreceipt.data_booking_id as receipt_booking_id,
        cte_clientreceipt.data_receipt_index as receipt_index,
        cte_clientreceipt.data_currency as receipt_currency,
        cte_clientreceipt.data_amount as receipt_amount,
        cte_clientreceipt.data_pay_or_refund as receipt_pay_or_refund,
        cte_clientreceipt.data_note as receipt_note,
        cte_clientreceipt.data_realised as receipt_realized,
        cte_clientreceipt.data_receipt_date as receipt_date,
        cte_clientreceipt.data_realised_date as receipt_realized_date,
        cte_clientreceipt.data_authorised as receipt_authorized,
        cte_clientreceipt.data_receipt_to_selling_ex_rate as receipt_to_selling_exchange_rate,
        cte_clientreceipt.data_receipt_to_base_ex_rate as receipt_to_base_exchange_rate,
        cte_clientreceipt.data_receipt_type as receipt_type,
        cte_clientreceipt.data_transaction_id as receipt_transaction_id,
        cte_clientreceipt.data_batch_no as receipt_batch_number,
        cte_clientreceipt.data_valid as receipt_valid,
        cte_clientreceipt.data_pending as receipt_pending,
        cte_clientreceipt.data_ibtx_exist as receipt_booking_transfer_exist,
        cte_clientreceipt.data_reconciled as receipt_reconciled,
        cte_clientreceipt.data_reconciled_date as receipt_reconciled_date,
        cte_clientreceipt.data_modified as receipt_modified,
        cte_clientreceipt.data_statement_id as receipt_statement_id_value,
        cte_clientreceipt.data_bank_transaction_id as receipt_bank_transaction_id,
        cte_clientreceipt.data_entered_user as receipt_entered_user,
        cte_clientreceipt.data_bank_code as receipt_bank_code,
        cte_clientreceipt.data_account_no as receipt_account_number,
        cte_clientreceipt.data_bounced_rcpts_exist as receipt_bounced_exist,
        cte_clientreceipt.data_bounced_receipt_index as receipt_bounced_index,
        cte_clientreceipt.data_batch_id as receipt_batch_id,
        cte_clientreceipt.data_doc_exists as receipt_doc_exists,
        cte_clientreceipt.data_remittance_id as receipt_remittance_id,
        cte_clientreceipt.data_location_id as receipt_location_id,
        cte_clientreceipt.data_ext_int_reconsiled as receipt_external_interface_reconciled,
        cte_clientreceipt.data_last_modified_time as receipt_last_modified_time,
        cte_booking.data_client_id as booking_client_id,
        cte_booking.data_company as booking_company,
        cte_booking.data_division as booking_division,
        cte_booking.data_brand as booking_brand,
        cte_booking.data_booking_status as booking_status,
        cte_bookingstatus.data_status as booking_status_name,
        cte_booking.data_option_status as booking_option_status,
        cte_optionstatus.data_status as option_status_name,
        cte_booking.data_booking_date as booking_date,
        cte_booking.data_departure_date as booking_arrival_date,
        cte_booking.data_return_date as booking_departure_date,
        cte_booking.data_balance_due_date as booking_balance_due_date,
        cte_client.data_type as client_type,
        cte_client.data_client_ref as client_reference,
        cte_client.data_name as client_name,
        cte_client.data_client_group as client_group,
        cte_directclient.data_profile_id as direct_client_profile_id,
        cte_clientccreceipt.data_transaction_ref as cc_receipt_transaction_reference,
        cte_clientccreceipt.data_card_type as cc_receipt_card_type,
        cte_cardtype.data_name as cc_card_type_name,
        cte_cardtype.data_merchant_fee as cc_card_type_merchant_fee,
        cte_cardtype.data_merchant_fee_cust as cc_card_type_merchant_fee_customer,
        cte_cardtype.data_taxable as cc_card_type_taxable,
        cte_clientrefund.data_refund_type as client_refund_type,
        cte_clientccreceipt.data_transaction_status as cc_receipt_transaction_status,
        cte_clientccreceipt.data_auth_code as cc_receipt_auth_code,
        cte_clientccreceipt.data_transaction_ref_id_returned as cc_receipt_transaction_ref_id_returned,
        cte_clientccreceipt.data_transaction_ref_no_returned as cc_receipt_transaction_ref_number_returned,
        cte_clientccreceipt.data_cc_last_five_digits as cc_receipt_cc_last_five_digits,
        cte_clientccreceipt.data_settlement_date as cc_receipt_settlement_date,
        cte_clientccreceipt.data_cc_fee_cost as cc_receipt_cc_fee_cost,
        cte_clientccreceipt.data_airline_merchant as cc_receipt_airline_merchant,
        cte_clientccreceipt.data_cc_fee_price_tax as cc_receipt_cc_fee_price_tax,
        cte_clientccreceipt.data_cc_fee_cost_tax as cc_receipt_cc_fee_cost_tax,
        cte_clientccreceipt.data_house_no as cc_receipt_house_number,
        cte_clientccreceipt.data_airline_commission_amount as cc_receipt_airline_commission_amount,
        cte_clientccreceipt.data_company_credit_card as cc_receipt_company_credit_card,
        cte_clientccreceipt.data_card_no_first_six_digits as cc_receipt_card_number_first_six_digits,
        cte_clientccreceipt.data_issue_no as cc_receipt_issue_number,
        cte_clientccreceipt.data_passenger_no as cc_receipt_passenger_number,
        cte_clientccreceipt.data_product_code as cc_receipt_product_code,
        cte_clientccreceipt.data_item_no as cc_receipt_item_number,
        cte_clientccreceipt.data_security_no as cc_receipt_security_number,
        cte_clientccreceipt.data_address as cc_receipt_address,
        cte_clientccreceipt.data_city as cc_receipt_city,
        cte_clientccreceipt.data_state as cc_receipt_state,
        cte_clientccreceipt.data_subscription_no_deleted as cc_receipt_subscription_number_deleted,
        cte_clientccreceipt.data_remittance_no as cc_receipt_remittance_number,
        cte_clientccreceipt.data_remt_date as cc_receipt_remittance_date,
        cte_clientccreceipt.data_hash_card_no as cc_receipt_hash_card_number,
        cte_clientccreceipt.data_merchant as cc_receipt_merchant,
        cte_clientccreceipt.data_last_modified_time as cc_receipt_last_modified_time,
        cte_clientccreceipt.data_card_category as cc_receipt_card_category,
        cte_clientccreceipt.data_credit_card_brand as cc_receipt_credit_card_brand,
        cte_clientrefund.data_authorised as refund_authorized,
        cte_clientrefund.data_transfer_receipt_index as refund_transfer_receipt_index,
        cte_clientrefund.data_refund_batch_no as refund_batch_number,
        cte_clientrefund.data_auto_refund as refund_auto_refund,
        cte_clientrefund.data_authorised_user as refund_authorized_user,
        cte_clientrefund.data_cheque_refund_index as refund_cheque_refund_index,
        cte_clientrefund.data_last_modified_time as refund_last_modified_time,
        cte_refundtype.data_code as refund_type_code,
        cte_refundtype.data_name as refund_type_name,
        cte_refundtype.data_exgratia as refund_type_exgratia,
        cte_refundtype.data_sys_defined as refund_type_sys_defined,
        cte_ibtx.data_booking_id as booking_transfer_booking_id,
        cte_ibtx.data_receipt_index as booking_transfer_receipt_index,
        cte_ibtx.data_from_booking as booking_transfer_from_booking,
        cte_ibtx.data_from_receipt_index as booking_transfer_from_receipt_index,
        cte_ibtx.data_to_booking as booking_transfer_to_booking,
        cte_ibtx.data_last_modified_time as booking_transfer_last_modified_time
    from cte_clientreceipt
        inner join cte_booking on cte_booking.data_booking_id = cte_clientreceipt.data_booking_id
        left join cte_bookingstatus on cte_booking.data_booking_status = cte_bookingstatus.data_id
        left join cte_optionstatus on cte_booking.data_option_status = cte_optionstatus.data_id
        left join cte_client on cte_client.data_client_id = cte_booking.data_client_id
        left join cte_directclient on cte_directclient.data_client_id = cte_booking.data_client_id
        left join cte_clientccreceipt on cte_clientccreceipt.data_booking_id = cte_clientreceipt.data_booking_id
        and cte_clientccreceipt.data_receipt_index = cte_clientreceipt.data_receipt_index
        left join cte_cardtype on cte_cardtype.data_code = cte_clientccreceipt.data_card_type
        left join cte_clientrefund on cte_clientrefund.data_booking_id = cte_clientreceipt.data_booking_id
        and cte_clientrefund.data_receipt_index = cte_clientreceipt.data_receipt_index
        left join cte_refundtype on cte_refundtype.data_code = cte_clientrefund.data_refund_type
        left join cte_ibtx on cte_ibtx.data_booking_id = cte_clientreceipt.data_booking_id
        and cte_ibtx.data_receipt_index = cte_clientreceipt.data_receipt_index
    where cte_ibtx.data_booking_id is not null
)

select * from final_query