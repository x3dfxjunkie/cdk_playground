{{
    config(
        materialized='incremental',
        unique_key= ['data_exprnc_band_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_xbms_wdw', 'exprnc_band') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_exprnc_band_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_exprnc_band_id
),

-- cleansing the table
renamed as (
    select
        src.data_exprnc_band_id as data_exprnc_band_id,
        src.data_exprnc_band_dsny_prod_id as data_exprnc_band_dsny_prod_id,
        TRIM(src.data_exprnc_band_uniq_id) as data_exprnc_band_uniq_id,
        src.data_exprnc_band_req_id as data_exprnc_band_req_id,
        src.data_exprnc_band_ord_id as data_exprnc_band_ord_id,
        src.data_fflmt_shipmt_id as data_fflmt_shipmt_id,
        src.data_exprnc_band_pkg_id as data_exprnc_band_pkg_id,
        TRIM(src.data_exprnc_band_prt_nm) as data_exprnc_band_prt_nm,
        TRIM(src.data_exprnc_band_gst_cnfirm_in) as data_exprnc_band_gst_cnfirm_in,
        src.data_exprnc_band_seq_nb as data_exprnc_band_seq_nb,
        TRIM(src.data_exprnc_band_cstm_prt_nm_in) as data_exprnc_band_cstm_prt_nm_in,
        TRIM(src.data_create_usr_id) as data_create_usr_id,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id) as data_updt_usr_id,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_logical_del_in) as data_logical_del_in,
        src.data_curr_exprnc_band_lnk_id as data_curr_exprnc_band_lnk_id,
        TRIM(src.data_exprnc_band_rtl_in) as data_exprnc_band_rtl_in,
        TRIM(src.data_exprnc_band_ovrd_prt_nm) as data_exprnc_band_ovrd_prt_nm,
        src.data_orig_exprnc_band_lnk_id as data_orig_exprnc_band_lnk_id,
        TRIM(src.data_opt_out_in) as data_opt_out_in,
        src.data_exprnc_band_opt_out_rsn_id as data_exprnc_band_opt_out_rsn_id,
        TRIM(src.data_exprnc_band_gst_sku_ovrd_in) as data_exprnc_band_gst_sku_ovrd_in,
        src.data_incog_req_id as data_incog_req_id,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_exprnc_band_dsny_prod_id',
            'src.data_exprnc_band_uniq_id',
            'src.data_exprnc_band_req_id',
            'src.data_exprnc_band_ord_id',
            'src.data_fflmt_shipmt_id',
            'src.data_exprnc_band_pkg_id',
            'src.data_exprnc_band_prt_nm',
            'src.data_exprnc_band_gst_cnfirm_in',
            'src.data_exprnc_band_seq_nb',
            'src.data_exprnc_band_cstm_prt_nm_in',
            'src.data_create_usr_id',
            'src.data_create_dts',
            'src.data_updt_usr_id',
            'src.data_logical_del_in',
            'src.data_curr_exprnc_band_lnk_id',
            'src.data_exprnc_band_rtl_in',
            'src.data_exprnc_band_ovrd_prt_nm',
            'src.data_orig_exprnc_band_lnk_id',
            'src.data_opt_out_in',
            'src.data_exprnc_band_opt_out_rsn_id',
            'src.data_exprnc_band_gst_sku_ovrd_in',
            'src.data_incog_req_id',
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
    on src.data_exprnc_band_id = min_source_update_datetime.data_exprnc_band_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_exprnc_band_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final