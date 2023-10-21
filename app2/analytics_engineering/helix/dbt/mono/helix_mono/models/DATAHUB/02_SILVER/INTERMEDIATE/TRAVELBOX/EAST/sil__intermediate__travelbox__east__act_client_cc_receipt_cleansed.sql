{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_receipt_index','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'act_client_cc_receipt') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_booking_id,
        data_receipt_index,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_receipt_index
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_city) as data_city,
        TRIM(src.data_credit_card_brand) as data_credit_card_brand,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_card_category) as data_card_category,
        TRIM(src.data_future_payment) as data_future_payment,
        TRIM(src.data_card_token) as data_card_token,
        TRIM(src.data_token_vault) as data_token_vault,
        TRIM(src.data_ext_transaction_id) as data_ext_transaction_id,
        TRIM(src.data_state) as data_state,
        TRIM(src.data_subscription_no_deleted) as data_subscription_no_deleted,
        src.data_remittance_no as data_remittance_no,
        src.data_remt_date as data_remt_date,
        TRIM(src.data_hash_card_no) as data_hash_card_no,
        TRIM(src.data_merchant) as data_merchant,
        src.data_booking_id as data_booking_id,
        src.data_receipt_index as data_receipt_index,
        src.data_cc_fee_price as data_cc_fee_price,
        TRIM(src.data_card_no) as data_card_no,
        src.data_issue_date as data_issue_date,
        src.data_expiry_date as data_expiry_date,
        TRIM(src.data_gateway_ref) as data_gateway_ref,
        TRIM(src.data_transaction_ref) as data_transaction_ref,
        TRIM(src.data_card_type) as data_card_type,
        TRIM(src.data_name_of_card) as data_name_of_card,
        TRIM(src.data_post_code) as data_post_code,
        TRIM(src.data_address) as data_address,
        TRIM(src.data_cc_fee_included) as data_cc_fee_included,
        TRIM(src.data_authorised_to_take_balance) as data_authorised_to_take_balance,
        TRIM(src.data_transaction_status) as data_transaction_status,
        TRIM(src.data_auth_code) as data_auth_code,
        TRIM(src.data_transaction_ref_id_returned) as data_transaction_ref_id_returned,
        TRIM(src.data_transaction_ref_no_returned) as data_transaction_ref_no_returned,
        TRIM(src.data_cc_last_five_digits) as data_cc_last_five_digits,
        src.data_settlement_date as data_settlement_date,
        src.data_cc_fee_cost as data_cc_fee_cost,
        TRIM(src.data_airline_merchant) as data_airline_merchant,
        src.data_cc_fee_price_tax as data_cc_fee_price_tax,
        src.data_cc_fee_cost_tax as data_cc_fee_cost_tax,
        TRIM(src.data_house_no) as data_house_no,
        src.data_airline_commission_amount as data_airline_commission_amount,
        TRIM(src.data_company_credit_card) as data_company_credit_card,
        TRIM(src.data_card_no_first_six_digits) as data_card_no_first_six_digits,
        TRIM(src.data_issue_no) as data_issue_no,
        src.data_passenger_no as data_passenger_no,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        TRIM(src.data_security_no) as data_security_no,
        TRIM(src.data_address2) as data_address2,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_city',
            'src.data_credit_card_brand',
            'src.data_last_modified_time',
            'src.data_card_category',
            'src.data_future_payment',
            'src.data_card_token',
            'src.data_token_vault',
            'src.data_ext_transaction_id',
            'src.data_state',
            'src.data_subscription_no_deleted',
            'src.data_remittance_no',
            'src.data_remt_date',
            'src.data_hash_card_no',
            'src.data_merchant',
            'src.data_cc_fee_price',
            'src.data_card_no',
            'src.data_issue_date',
            'src.data_expiry_date',
            'src.data_gateway_ref',
            'src.data_transaction_ref',
            'src.data_card_type',
            'src.data_name_of_card',
            'src.data_post_code',
            'src.data_address',
            'src.data_cc_fee_included',
            'src.data_authorised_to_take_balance',
            'src.data_transaction_status',
            'src.data_auth_code',
            'src.data_transaction_ref_id_returned',
            'src.data_transaction_ref_no_returned',
            'src.data_cc_last_five_digits',
            'src.data_settlement_date',
            'src.data_cc_fee_cost',
            'src.data_airline_merchant',
            'src.data_cc_fee_price_tax',
            'src.data_cc_fee_cost_tax',
            'src.data_house_no',
            'src.data_airline_commission_amount',
            'src.data_company_credit_card',
            'src.data_card_no_first_six_digits',
            'src.data_issue_no',
            'src.data_passenger_no',
            'src.data_product_code',
            'src.data_item_no',
            'src.data_security_no',
            'src.data_address2',
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
    and src.data_receipt_index = min_source_update_datetime.data_receipt_index
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_receipt_index, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final