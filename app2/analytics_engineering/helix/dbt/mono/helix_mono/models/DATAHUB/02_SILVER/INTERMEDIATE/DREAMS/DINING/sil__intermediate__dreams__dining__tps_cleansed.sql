{{
    config(
        materialized='incremental',
        unique_key= ['data_tps_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_dining', 'tps') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_tps_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_tps_id
),

-- cleansing the table
renamed as (
    select
        src.data_tp_id as data_tp_id,
        src.data_tps_id as data_tps_id,
        TRIM(src.data_trvl_sts_nm) as data_trvl_sts_nm,
        TRIM(src.data_vip_lvl_nm) as data_vip_lvl_nm,
        TRIM(src.data_trvl_agcy_pty_id) as data_trvl_agcy_pty_id,
        TRIM(src.data_trvl_agt_pty_id) as data_trvl_agt_pty_id,
        TRIM(src.data_prmy_pty_id) as data_prmy_pty_id,
        TRIM(src.data_tps_guar_in) as data_tps_guar_in,
        TRIM(src.data_tps_secur_vl) as data_tps_secur_vl,
        TRIM(src.data_tps_ctct_nm) as data_tps_ctct_nm,
        src.data_tps_cncl_dts as data_tps_cncl_dts,
        src.data_tps_cncl_nb as data_tps_cncl_nb,
        src.data_tps_cnfm_updt_dts as data_tps_cnfm_updt_dts,
        TRIM(src.data_tps_cnfrm_usr_id_cd) as data_tps_cnfrm_usr_id_cd,
        TRIM(src.data_tps_ppty_sync_in) as data_tps_ppty_sync_in,
        TRIM(src.data_src_acct_ctr_id) as data_src_acct_ctr_id,
        src.data_tps_arvl_dt as data_tps_arvl_dt,
        src.data_tps_dprt_dt as data_tps_dprt_dt,
        src.data_tps_est_arvl_tm as data_tps_est_arvl_tm,
        src.data_tps_est_dprt_tm as data_tps_est_dprt_tm,
        TRIM(src.data_onst_phn_nb) as data_onst_phn_nb,
        TRIM(src.data_web_txfr_cd) as data_web_txfr_cd,
        TRIM(src.data_dnis_nb) as data_dnis_nb,
        TRIM(src.data_trms_cndtns_vers_nb) as data_trms_cndtns_vers_nb,
        TRIM(src.data_syw_opt_in) as data_syw_opt_in,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        src.data_updt_dts as data_updt_dts,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        TRIM(src.data_onst_msg_in) as data_onst_msg_in,
        src.data_prge_dts as data_prge_dts,
        TRIM(src.data_incognito) as data_incognito,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_tp_id',
            'src.data_trvl_sts_nm',
            'src.data_vip_lvl_nm',
            'src.data_trvl_agcy_pty_id',
            'src.data_trvl_agt_pty_id',
            'src.data_prmy_pty_id',
            'src.data_tps_guar_in',
            'src.data_tps_secur_vl',
            'src.data_tps_ctct_nm',
            'src.data_tps_cncl_dts',
            'src.data_tps_cncl_nb',
            'src.data_tps_cnfm_updt_dts',
            'src.data_tps_cnfrm_usr_id_cd',
            'src.data_tps_ppty_sync_in',
            'src.data_src_acct_ctr_id',
            'src.data_tps_arvl_dt',
            'src.data_tps_dprt_dt',
            'src.data_tps_est_arvl_tm',
            'src.data_tps_est_dprt_tm',
            'src.data_onst_phn_nb',
            'src.data_web_txfr_cd',
            'src.data_dnis_nb',
            'src.data_trms_cndtns_vers_nb',
            'src.data_syw_opt_in',
            'src.data_create_usr_id_cd',
            'src.data_create_dts',
            'src.data_updt_usr_id_cd',
            'src.data_jdo_seq_nb',
            'src.data_onst_msg_in',
            'src.data_prge_dts',
            'src.data_incognito',
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
    on src.data_tps_id = min_source_update_datetime.data_tps_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_tps_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final