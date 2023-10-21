{{
    config(
        materialized='incremental',
        unique_key= ['data_group_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'contract_group') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_group_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_group_id
),

-- cleansing the table
renamed as (
    select
        src.data_group_id as data_group_id,
        src.data_supplier_id as data_supplier_id,
        TRIM(src.data_reference) as data_reference,
        TRIM(src.data_description) as data_description,
        TRIM(src.data_company) as data_company,
        TRIM(src.data_division) as data_division,
        src.data_destination as data_destination,
        TRIM(src.data_product) as data_product,
        TRIM(src.data_addon) as data_addon,
        src.data_addon_priority as data_addon_priority,
        TRIM(src.data_pre_departure) as data_pre_departure,
        src.data_contract_source as data_contract_source,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_name) as data_name,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_supplier_id',
            'src.data_reference',
            'src.data_description',
            'src.data_company',
            'src.data_division',
            'src.data_destination',
            'src.data_product',
            'src.data_addon',
            'src.data_addon_priority',
            'src.data_pre_departure',
            'src.data_contract_source',
            'src.data_last_modified_time',
            'src.data_name',
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
    on src.data_group_id = min_source_update_datetime.data_group_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_group_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final