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
    from {{ source('brz_travelbox_west', 'cli_direct_client') }}

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
        TRIM(src.data_exclude_archiving) as data_exclude_archiving,
        src.data_client_id as data_client_id,
        src.data_profile_id as data_profile_id,
        src.data_grade as data_grade,
        TRIM(src.data_do_not_contact) as data_do_not_contact,
        src.data_alloc_user_id as data_alloc_user_id,
        TRIM(src.data_exclude_from_mailings) as data_exclude_from_mailings,
        TRIM(src.data_vip) as data_vip,
        TRIM(src.data_sales_allowed) as data_sales_allowed,
        TRIM(src.data_documents_allowed) as data_documents_allowed,
        TRIM(src.data_exclude_partner_emailing) as data_exclude_partner_emailing,
        src.data_type_id as data_type_id,
        src.data_last_modified_time as data_last_modified_time,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_exclude_archiving',
            'src.data_profile_id',
            'src.data_grade',
            'src.data_do_not_contact',
            'src.data_alloc_user_id',
            'src.data_exclude_from_mailings',
            'src.data_vip',
            'src.data_sales_allowed',
            'src.data_documents_allowed',
            'src.data_exclude_partner_emailing',
            'src.data_type_id',
            'src.data_last_modified_time',
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