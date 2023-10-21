{{
    config(
        materialized='incremental',
        unique_key= ['data_pay_scheme_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'payment_scheme') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_pay_scheme_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_pay_scheme_id
),

-- cleansing the table
renamed as (
    select
        src.data_pay_scheme_id as data_pay_scheme_id,
        TRIM(src.data_payment_ref) as data_payment_ref,
        TRIM(src.data_description) as data_description,
        TRIM(src.data_product) as data_product,
        TRIM(src.data_pre_payment_method) as data_pre_payment_method,
        TRIM(src.data_pre_payment_type) as data_pre_payment_type,
        src.data_pre_date as data_pre_date,
        src.data_pre_amount as data_pre_amount,
        TRIM(src.data_pre_amount_type) as data_pre_amount_type,
        TRIM(src.data_pre_currency) as data_pre_currency,
        TRIM(src.data_post_payment_method) as data_post_payment_method,
        TRIM(src.data_post_payment_type) as data_post_payment_type,
        src.data_post_payment_month_no as data_post_payment_month_no,
        src.data_post_date as data_post_date,
        src.data_inv_due_period as data_inv_due_period,
        TRIM(src.data_checkout_date_consider) as data_checkout_date_consider,
        TRIM(src.data_depo_aft_bkg_bef_dept) as data_depo_aft_bkg_bef_dept,
        TRIM(src.data_bal_aft_bkg_bef_dept) as data_bal_aft_bkg_bef_dept,
        TRIM(src.data_payment_media) as data_payment_media,
        TRIM(src.data_auto_payment) as data_auto_payment,
        TRIM(src.data_interface_code) as data_interface_code,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_payment_ref',
            'src.data_description',
            'src.data_product',
            'src.data_pre_payment_method',
            'src.data_pre_payment_type',
            'src.data_pre_date',
            'src.data_pre_amount',
            'src.data_pre_amount_type',
            'src.data_pre_currency',
            'src.data_post_payment_method',
            'src.data_post_payment_type',
            'src.data_post_payment_month_no',
            'src.data_post_date',
            'src.data_inv_due_period',
            'src.data_checkout_date_consider',
            'src.data_depo_aft_bkg_bef_dept',
            'src.data_bal_aft_bkg_bef_dept',
            'src.data_payment_media',
            'src.data_auto_payment',
            'src.data_interface_code',
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
    on src.data_pay_scheme_id = min_source_update_datetime.data_pay_scheme_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_pay_scheme_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final