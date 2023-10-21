{{
    config(
        materialized='incremental',
        unique_key= ['data_dsny_fac_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_xbms_wdw', 'dsny_fac') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_dsny_fac_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_dsny_fac_id
),

-- cleansing the table
renamed as (
    select
        src.data_dsny_fac_id as data_dsny_fac_id,
        src.data_addr_id as data_addr_id,
        src.data_dsny_fac_typ_id as data_dsny_fac_typ_id,
        src.data_ship_ctct_id as data_ship_ctct_id,
        src.data_fac_id as data_fac_id,
        TRIM(src.data_dsny_fac_nm) as data_dsny_fac_nm,
        TRIM(src.data_dsny_fac_avail_for_bulk_ord_in) as data_dsny_fac_avail_for_bulk_ord_in,
        TRIM(src.data_dsny_fac_for_rcv_gst_ord_in) as data_dsny_fac_for_rcv_gst_ord_in,
        TRIM(src.data_create_usr_id) as data_create_usr_id,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id) as data_updt_usr_id,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_logical_del_in) as data_logical_del_in,
        TRIM(src.data_rl_asgn_fac_in) as data_rl_asgn_fac_in,
        TRIM(src.data_rtl_loc_in) as data_rtl_loc_in,
        TRIM(src.data_dsny_fac_short_nm) as data_dsny_fac_short_nm,
        src.data_cost_ctr_id as data_cost_ctr_id,
        src.data_bus_area_id as data_bus_area_id,
        src.data_gnrl_ldgr_id as data_gnrl_ldgr_id,
        src.data_wbs_elmnt_id as data_wbs_elmnt_id,
        TRIM(src.data_auto_rcv_in) as data_auto_rcv_in,
        src.data_sap_goods_issue_skip_rsn_id as data_sap_goods_issue_skip_rsn_id,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_addr_id',
            'src.data_dsny_fac_typ_id',
            'src.data_ship_ctct_id',
            'src.data_fac_id',
            'src.data_dsny_fac_nm',
            'src.data_dsny_fac_avail_for_bulk_ord_in',
            'src.data_dsny_fac_for_rcv_gst_ord_in',
            'src.data_create_usr_id',
            'src.data_create_dts',
            'src.data_updt_usr_id',
            'src.data_logical_del_in',
            'src.data_rl_asgn_fac_in',
            'src.data_rtl_loc_in',
            'src.data_dsny_fac_short_nm',
            'src.data_cost_ctr_id',
            'src.data_bus_area_id',
            'src.data_gnrl_ldgr_id',
            'src.data_wbs_elmnt_id',
            'src.data_auto_rcv_in',
            'src.data_sap_goods_issue_skip_rsn_id',
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
    on src.data_dsny_fac_id = min_source_update_datetime.data_dsny_fac_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_dsny_fac_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final