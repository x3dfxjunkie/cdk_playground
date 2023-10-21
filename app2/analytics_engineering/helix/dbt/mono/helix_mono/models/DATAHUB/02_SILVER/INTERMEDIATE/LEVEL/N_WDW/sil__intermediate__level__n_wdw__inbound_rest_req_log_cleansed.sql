{{
    config(
        materialized='incremental',
        unique_key= ['data_correlation_id', 'data_req_timestamp','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_level_n_wdw', 'inbound_rest_req_log') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_correlation_id,
        data_req_timestamp,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_correlation_id,
        data_req_timestamp
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_correlation_id) as data_correlation_id,
        src.data_req_timestamp as data_req_timestamp,
        TRIM(src.data_req_url) as data_req_url,
        TRIM(src.data_req_body) as data_req_body,
        TRIM(src.data_cst_id) as data_cst_id,
        TRIM(src.data_gst_id) as data_gst_id,
        TRIM(src.data_cip) as data_cip,
        TRIM(src.data_sys_id) as data_sys_id,
        TRIM(src.data_orgn_sys_id) as data_orgn_sys_id,
        TRIM(src.data_req_typ) as data_req_typ,
        TRIM(src.data_swid) as data_swid,
        TRIM(src.data_pl_hld1) as data_pl_hld1,
        TRIM(src.data_pl_hld2) as data_pl_hld2,
        TRIM(src.data_pl_hld3) as data_pl_hld3,
        TRIM(src.data_create_usr_id) as data_create_usr_id,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id) as data_updt_usr_id,
        src.data_updt_dts as data_updt_dts,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_req_url',
            'src.data_req_body',
            'src.data_cst_id',
            'src.data_gst_id',
            'src.data_cip',
            'src.data_sys_id',
            'src.data_orgn_sys_id',
            'src.data_req_typ',
            'src.data_swid',
            'src.data_pl_hld1',
            'src.data_pl_hld2',
            'src.data_pl_hld3',
            'src.data_create_usr_id',
            'src.data_create_dts',
            'src.data_updt_usr_id',
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
    on src.data_correlation_id = min_source_update_datetime.data_correlation_id
    and src.data_req_timestamp = min_source_update_datetime.data_req_timestamp
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_correlation_id, data_req_timestamp, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final