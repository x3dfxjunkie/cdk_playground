{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_booking_id', 'data_receipt_index','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__east__act_client_cc_receipt_cleansed'),
            join_columns=['data_booking_id', 'data_receipt_index'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__east__act_client_cc_receipt_cleansed') }}
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
            partition by data_booking_id, data_receipt_index
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
        partition_columns = ['data_booking_id', 'data_receipt_index']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_city,
        data_credit_card_brand,
        data_last_modified_time,
        data_card_category,
        data_future_payment,
        data_card_token,
        data_token_vault,
        data_ext_transaction_id,
        data_state,
        data_subscription_no_deleted,
        data_remittance_no,
        data_remt_date,
        data_hash_card_no,
        data_merchant,
        data_booking_id,
        data_receipt_index,
        data_cc_fee_price,
        data_card_no,
        data_issue_date,
        data_expiry_date,
        data_gateway_ref,
        data_transaction_ref,
        data_card_type,
        data_name_of_card,
        data_post_code,
        data_address,
        data_cc_fee_included,
        data_authorised_to_take_balance,
        data_transaction_status,
        data_auth_code,
        data_transaction_ref_id_returned,
        data_transaction_ref_no_returned,
        data_cc_last_five_digits,
        data_settlement_date,
        data_cc_fee_cost,
        data_airline_merchant,
        data_cc_fee_price_tax,
        data_cc_fee_cost_tax,
        data_house_no,
        data_airline_commission_amount,
        data_company_credit_card,
        data_card_no_first_six_digits,
        data_issue_no,
        data_passenger_no,
        data_product_code,
        data_item_no,
        data_security_no,
        data_address2,
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