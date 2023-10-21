{{
    config(
        materialized='incremental',
        unique_key= ['data_xband_extnl_prod_id','metadata_checksum'],
        on_schema_change='append_new_columns',
        snowflake_warehouse='DSE_QUERY_LST_WH'
    )
}}

-- source is the bronze table
with source as (
    select * from {{ source('brz_xbms_wdw', 'xband_extnl_prod') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_xband_extnl_prod_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_xband_extnl_prod_id
),

-- cleansing the table
renamed as (
    select
        src.data_xband_extnl_prod_id as data_xband_extnl_prod_id,
        TRIM(src.data_extnl_prod_src_sys_ntv_id) as data_extnl_prod_src_sys_ntv_id,
        TRIM(src.data_extnl_prod_txn_src_sys_tx) as data_extnl_prod_txn_src_sys_tx,
        src.data_extnl_prod_strt_dts as data_extnl_prod_strt_dts,
        src.data_extnl_prod_end_dts as data_extnl_prod_end_dts,
        src.data_extnl_prod_create_strt_dts as data_extnl_prod_create_strt_dts,
        src.data_extnl_prod_create_end_dts as data_extnl_prod_create_end_dts,
        TRIM(src.data_xband_enttl_prod_assc_actv_in) as data_xband_enttl_prod_assc_actv_in,
        TRIM(src.data_create_usr_id) as data_create_usr_id,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_group_in) as data_group_in,
        TRIM(src.data_updt_usr_id) as data_updt_usr_id,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_lgcl_del_in) as data_lgcl_del_in,
        TRIM(src.data_dual_order) as data_dual_order,
        src.data_fac_id as data_fac_id,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_extnl_prod_src_sys_ntv_id',
            'src.data_extnl_prod_txn_src_sys_tx',
            'src.data_extnl_prod_strt_dts',
            'src.data_extnl_prod_end_dts',
            'src.data_extnl_prod_create_strt_dts',
            'src.data_extnl_prod_create_end_dts',
            'src.data_xband_enttl_prod_assc_actv_in',
            'src.data_create_usr_id',
            'src.data_create_dts',
            'src.data_group_in',
            'src.data_updt_usr_id',
            'src.data_lgcl_del_in',
            'src.data_dual_order',
            'src.data_fac_id']) }} as metadata_checksum,
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
    on src.data_xband_extnl_prod_id = min_source_update_datetime.data_xband_extnl_prod_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_xband_extnl_prod_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final