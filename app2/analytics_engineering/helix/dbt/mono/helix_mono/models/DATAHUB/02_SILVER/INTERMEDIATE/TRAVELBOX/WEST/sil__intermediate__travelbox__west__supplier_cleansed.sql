{{
    config(
        materialized='incremental',
        unique_key= ['data_supplier_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'supplier') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_supplier_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_supplier_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_payment_type) as data_payment_type,
        src.data_modified_by as data_modified_by,
        src.data_modified_on as data_modified_on,
        src.data_entered_by as data_entered_by,
        src.data_entered_on as data_entered_on,
        TRIM(src.data_automatic_notification) as data_automatic_notification,
        TRIM(src.data_tax_excempt) as data_tax_excempt,
        TRIM(src.data_tax_number) as data_tax_number,
        TRIM(src.data_tax_override) as data_tax_override,
        TRIM(src.data_cancel_before) as data_cancel_before,
        TRIM(src.data_chain) as data_chain,
        TRIM(src.data_locale) as data_locale,
        src.data_max_concurrent_user_count as data_max_concurrent_user_count,
        TRIM(src.data_dedup_order) as data_dedup_order,
        TRIM(src.data_enable) as data_enable,
        src.data_last_modified_timestamp as data_last_modified_timestamp,
        src.data_supplier_id as data_supplier_id,
        TRIM(src.data_code) as data_code,
        TRIM(src.data_identity) as data_identity,
        TRIM(src.data_name) as data_name,
        TRIM(src.data_address) as data_address,
        TRIM(src.data_city) as data_city,
        TRIM(src.data_resort) as data_resort,
        TRIM(src.data_tourist_region) as data_tourist_region,
        TRIM(src.data_post_code) as data_post_code,
        TRIM(src.data_currency) as data_currency,
        TRIM(src.data_notes) as data_notes,
        src.data_pay_scheme as data_pay_scheme,
        src.data_cancel_scheme as data_cancel_scheme,
        src.data_commission as data_commission,
        TRIM(src.data_attended_person) as data_attended_person,
        TRIM(src.data_email) as data_email,
        TRIM(src.data_fax) as data_fax,
        TRIM(src.data_telephone) as data_telephone,
        TRIM(src.data_default_contact_method) as data_default_contact_method,
        TRIM(src.data_send_immediately) as data_send_immediately,
        TRIM(src.data_web_url) as data_web_url,
        src.data_preference as data_preference,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_payment_type',
            'src.data_modified_by',
            'src.data_modified_on',
            'src.data_entered_by',
            'src.data_entered_on',
            'src.data_automatic_notification',
            'src.data_tax_excempt',
            'src.data_tax_number',
            'src.data_tax_override',
            'src.data_cancel_before',
            'src.data_chain',
            'src.data_locale',
            'src.data_max_concurrent_user_count',
            'src.data_dedup_order',
            'src.data_enable',
            'src.data_last_modified_timestamp',
            'src.data_code',
            'src.data_identity',
            'src.data_name',
            'src.data_address',
            'src.data_city',
            'src.data_resort',
            'src.data_tourist_region',
            'src.data_post_code',
            'src.data_currency',
            'src.data_notes',
            'src.data_pay_scheme',
            'src.data_cancel_scheme',
            'src.data_commission',
            'src.data_attended_person',
            'src.data_email',
            'src.data_fax',
            'src.data_telephone',
            'src.data_default_contact_method',
            'src.data_send_immediately',
            'src.data_web_url',
            'src.data_preference',
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
    on src.data_supplier_id = min_source_update_datetime.data_supplier_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_supplier_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final