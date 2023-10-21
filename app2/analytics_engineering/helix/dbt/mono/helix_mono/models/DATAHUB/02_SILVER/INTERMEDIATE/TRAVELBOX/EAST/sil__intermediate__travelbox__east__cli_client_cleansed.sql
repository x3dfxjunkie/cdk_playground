{{
    config(
        materialized='incremental',
        unique_key= ['data_client_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'cli_client') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_client_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_client_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_unavailable) as data_unavailable,
        src.data_last_modified_timestamp as data_last_modified_timestamp,
        TRIM(src.data_external_ref_id) as data_external_ref_id,
        src.data_client_id as data_client_id,
        TRIM(src.data_type) as data_type,
        TRIM(src.data_client_ref) as data_client_ref,
        TRIM(src.data_name) as data_name,
        TRIM(src.data_client_status) as data_client_status,
        TRIM(src.data_media) as data_media,
        src.data_registered_date as data_registered_date,
        TRIM(src.data_client_group) as data_client_group,
        src.data_entered_on as data_entered_on,
        src.data_modified_on as data_modified_on,
        TRIM(src.data_registered_channel) as data_registered_channel,
        src.data_modified_by as data_modified_by,
        src.data_entered_by as data_entered_by,
        src.data_primary_sales_agent as data_primary_sales_agent,
        TRIM(src.data_status_message) as data_status_message,
        TRIM(src.data_tax_exempt) as data_tax_exempt,
        TRIM(src.data_tax_override) as data_tax_override,
        src.data_grade_id as data_grade_id,
        TRIM(src.data_dealing_company) as data_dealing_company,
        TRIM(src.data_dealing_division) as data_dealing_division,
        TRIM(src.data_currency) as data_currency,
        TRIM(src.data_active) as data_active,
        TRIM(src.data_dealing_brand) as data_dealing_brand,
        TRIM(src.data_locale) as data_locale,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_unavailable',
            'src.data_last_modified_timestamp',
            'src.data_external_ref_id',
            'src.data_type',
            'src.data_client_ref',
            'src.data_name',
            'src.data_client_status',
            'src.data_media',
            'src.data_registered_date',
            'src.data_client_group',
            'src.data_entered_on',
            'src.data_modified_on',
            'src.data_registered_channel',
            'src.data_modified_by',
            'src.data_entered_by',
            'src.data_primary_sales_agent',
            'src.data_status_message',
            'src.data_tax_exempt',
            'src.data_tax_override',
            'src.data_grade_id',
            'src.data_dealing_company',
            'src.data_dealing_division',
            'src.data_currency',
            'src.data_active',
            'src.data_dealing_brand',
            'src.data_locale',
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
    on src.data_client_id = min_source_update_datetime.data_client_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_client_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final