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
    from {{ source('brz_travelbox_east', 'act_client_receipt') }}

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
        src.data_booking_id as data_booking_id,
        src.data_receipt_index as data_receipt_index,
        TRIM(src.data_currency) as data_currency,
        src.data_amount as data_amount,
        TRIM(src.data_pay_or_refund) as data_pay_or_refund,
        TRIM(src.data_note) as data_note,
        TRIM(src.data_realised) as data_realised,
        src.data_receipt_date as data_receipt_date,
        src.data_realised_date as data_realised_date,
        TRIM(src.data_authorised) as data_authorised,
        src.data_receipt_to_selling_ex_rate as data_receipt_to_selling_ex_rate,
        src.data_receipt_to_base_ex_rate as data_receipt_to_base_ex_rate,
        TRIM(src.data_receipt_type) as data_receipt_type,
        TRIM(src.data_batch_no) as data_batch_no,
        TRIM(src.data_valid) as data_valid,
        TRIM(src.data_pending) as data_pending,
        TRIM(src.data_ibtx_exist) as data_ibtx_exist,
        TRIM(src.data_reconciled) as data_reconciled,
        src.data_reconciled_date as data_reconciled_date,
        src.data_journal_batch_no as data_journal_batch_no,
        TRIM(src.data_modified) as data_modified,
        src.data_statement_id as data_statement_id,
        src.data_reverse_journal_batch_no as data_reverse_journal_batch_no,
        src.data_reversed_for_journal_batch_no as data_reversed_for_journal_batch_no,
        src.data_bank_transaction_id as data_bank_transaction_id,
        src.data_entered_user as data_entered_user,
        TRIM(src.data_temp_user) as data_temp_user,
        src.data_deposited_by as data_deposited_by,
        TRIM(src.data_bank_code) as data_bank_code,
        TRIM(src.data_account_no) as data_account_no,
        TRIM(src.data_bounced_rcpts_exist) as data_bounced_rcpts_exist,
        src.data_bounced_receipt_index as data_bounced_receipt_index,
        src.data_deposit_batch_no as data_deposit_batch_no,
        src.data_batch_id as data_batch_id,
        TRIM(src.data_doc_exists) as data_doc_exists,
        TRIM(src.data_remittance_id) as data_remittance_id,
        src.data_location_id as data_location_id,
        TRIM(src.data_ext_int_reconsiled) as data_ext_int_reconsiled,
        TRIM(src.data_transaction_id) as data_transaction_id,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_pay_details) as data_pay_details,
        TRIM(src.data_slip_ref) as data_slip_ref,
        src.data_balance_due_his as data_balance_due_his,
        TRIM(src.data_receipt_category) as data_receipt_category,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_currency',
            'src.data_amount',
            'src.data_pay_or_refund',
            'src.data_note',
            'src.data_realised',
            'src.data_receipt_date',
            'src.data_realised_date',
            'src.data_authorised',
            'src.data_receipt_to_selling_ex_rate',
            'src.data_receipt_to_base_ex_rate',
            'src.data_receipt_type',
            'src.data_batch_no',
            'src.data_valid',
            'src.data_pending',
            'src.data_ibtx_exist',
            'src.data_reconciled',
            'src.data_reconciled_date',
            'src.data_journal_batch_no',
            'src.data_modified',
            'src.data_statement_id',
            'src.data_reverse_journal_batch_no',
            'src.data_reversed_for_journal_batch_no',
            'src.data_bank_transaction_id',
            'src.data_entered_user',
            'src.data_temp_user',
            'src.data_deposited_by',
            'src.data_bank_code',
            'src.data_account_no',
            'src.data_bounced_rcpts_exist',
            'src.data_bounced_receipt_index',
            'src.data_deposit_batch_no',
            'src.data_batch_id',
            'src.data_doc_exists',
            'src.data_remittance_id',
            'src.data_location_id',
            'src.data_ext_int_reconsiled',
            'src.data_transaction_id',
            'src.data_last_modified_time',
            'src.data_pay_details',
            'src.data_slip_ref',
            'src.data_balance_due_his',
            'src.data_receipt_category',
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