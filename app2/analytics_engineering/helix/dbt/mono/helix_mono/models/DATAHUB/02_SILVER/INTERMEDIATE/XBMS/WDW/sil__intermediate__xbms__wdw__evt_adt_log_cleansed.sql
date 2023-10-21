{{
    config(
        materialized='incremental',
        unique_key= ['data_evt_adt_log_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_xbms_wdw', 'evt_adt_log') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_evt_adt_log_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_evt_adt_log_id
),

-- cleansing the table
renamed as (
    select
        src.data_evt_adt_log_id as data_evt_adt_log_id,
        TRIM(src.data_evt_loc_tx) as data_evt_loc_tx,
        TRIM(src.data_evt_ref_id) as data_evt_ref_id,
        TRIM(src.data_evt_typ_tx) as data_evt_typ_tx,
        TRIM(src.data_evt_gst_id) as data_evt_gst_id,
        TRIM(src.data_evt_correlation_id) as data_evt_correlation_id,
        TRIM(src.data_evt_payload_tx) as data_evt_payload_tx,
        src.data_evt_timestamp as data_evt_timestamp,
        TRIM(src.data_evt_prmy_acknwl_sys_nm) as data_evt_prmy_acknwl_sys_nm,
        TRIM(src.data_evt_sec_acknwl_sys_nm) as data_evt_sec_acknwl_sys_nm,
        TRIM(src.data_create_usr_id) as data_create_usr_id,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id) as data_updt_usr_id,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_logical_del_in) as data_logical_del_in,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_evt_loc_tx',
            'src.data_evt_ref_id',
            'src.data_evt_typ_tx',
            'src.data_evt_gst_id',
            'src.data_evt_correlation_id',
            'src.data_evt_payload_tx',
            'src.data_evt_timestamp',
            'src.data_evt_prmy_acknwl_sys_nm',
            'src.data_evt_sec_acknwl_sys_nm',
            'src.data_create_usr_id',
            'src.data_create_dts',
            'src.data_updt_usr_id',
            'src.data_logical_del_in',
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
    on src.data_evt_adt_log_id = min_source_update_datetime.data_evt_adt_log_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_evt_adt_log_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final