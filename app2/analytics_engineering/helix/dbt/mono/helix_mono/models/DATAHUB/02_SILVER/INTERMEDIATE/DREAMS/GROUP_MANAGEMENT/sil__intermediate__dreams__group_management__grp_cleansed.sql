{{
    config(
        materialized='incremental',
        unique_key= ['data_grp_cd','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_group_management', 'grp') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_grp_cd,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_grp_cd
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_grp_cd) as data_grp_cd,
        src.data_hm_fac_id as data_hm_fac_id,
        TRIM(src.data_grp_dlgt_bkng_meth_nm) as data_grp_dlgt_bkng_meth_nm,
        TRIM(src.data_gro_nm) as data_gro_nm,
        TRIM(src.data_grp_bus_src_nm) as data_grp_bus_src_nm,
        TRIM(src.data_grp_free_tm_lvl_nm) as data_grp_free_tm_lvl_nm,
        TRIM(src.data_dlvr_meth_nm) as data_dlvr_meth_nm,
        TRIM(src.data_opty_typ_nm) as data_opty_typ_nm,
        TRIM(src.data_grp_acct_typ_nm) as data_grp_acct_typ_nm,
        TRIM(src.data_grp_stg_nm) as data_grp_stg_nm,
        TRIM(src.data_grp_bk_hm_fac_frst_in) as data_grp_bk_hm_fac_frst_in,
        src.data_grp_cl_acpt_dt as data_grp_cl_acpt_dt,
        src.data_grp_ctf_dt as data_grp_ctf_dt,
        src.data_grp_arvl_dt as data_grp_arvl_dt,
        src.data_grp_peak_arvl_dt as data_grp_peak_arvl_dt,
        src.data_grp_peak_dprt_dt as data_grp_peak_dprt_dt,
        src.data_grp_dprt_dt as data_grp_dprt_dt,
        src.data_grp_peak_rm_cn as data_grp_peak_rm_cn,
        src.data_grp_tot_rm_cn as data_grp_tot_rm_cn,
        TRIM(src.data_grp_vchr_in) as data_grp_vchr_in,
        TRIM(src.data_grp_comp_in) as data_grp_comp_in,
        TRIM(src.data_grp_run_hs_in) as data_grp_run_hs_in,
        TRIM(src.data_grp_exprs_chk_out_in) as data_grp_exprs_chk_out_in,
        TRIM(src.data_grp_hide_rt_in) as data_grp_hide_rt_in,
        TRIM(src.data_grp_comm_allow_in) as data_grp_comm_allow_in,
        TRIM(src.data_grp_disc_promo_allow_in) as data_grp_disc_promo_allow_in,
        TRIM(src.data_grp_sprd_dpst_in) as data_grp_sprd_dpst_in,
        TRIM(src.data_grp_rvrt_dpst_in) as data_grp_rvrt_dpst_in,
        TRIM(src.data_grp_byps_auto_cncl_in) as data_grp_byps_auto_cncl_in,
        TRIM(src.data_grp_byps_dpst_in) as data_grp_byps_dpst_in,
        TRIM(src.data_grp_byps_cncl_fee_in) as data_grp_byps_cncl_fee_in,
        TRIM(src.data_grp_byps_mod_fee_in) as data_grp_byps_mod_fee_in,
        TRIM(src.data_grp_auto_cnfirm_in) as data_grp_auto_cnfirm_in,
        TRIM(src.data_grp_exprs_lug_in) as data_grp_exprs_lug_in,
        TRIM(src.data_grp_res_guar_in) as data_grp_res_guar_in,
        TRIM(src.data_grp_whsl_in) as data_grp_whsl_in,
        TRIM(src.data_grp_dlgt_wrtoff_in) as data_grp_dlgt_wrtoff_in,
        TRIM(src.data_grp_rsr_in) as data_grp_rsr_in,
        TRIM(src.data_grp_addl_adlt_am) as data_grp_addl_adlt_am,
        TRIM(src.data_grp_nm) as data_grp_nm,
        TRIM(src.data_gro_agt_nm) as data_gro_agt_nm,
        TRIM(src.data_sls_dept_nm) as data_sls_dept_nm,
        TRIM(src.data_sls_mgr_nm) as data_sls_mgr_nm,
        TRIM(src.data_sls_phn_nb) as data_sls_phn_nb,
        TRIM(src.data_srvc_dept_nm) as data_srvc_dept_nm,
        TRIM(src.data_srvc_mgr_nm) as data_srvc_mgr_nm,
        TRIM(src.data_gsrvc_phn_nb) as data_gsrvc_phn_nb,
        TRIM(src.data_grp_comm_am_tx) as data_grp_comm_am_tx,
        TRIM(src.data_grp_comm_pc_tx) as data_grp_comm_pc_tx,
        TRIM(src.data_rp_comm_rt_tx) as data_rp_comm_rt_tx,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        TRIM(src.data_grp_cnfirm_dest_nm) as data_grp_cnfirm_dest_nm,
        TRIM(src.data_grp_min_los_nb_tx) as data_grp_min_los_nb_tx,
        TRIM(src.data_grp_dlgt_chg_priv_in) as data_grp_dlgt_chg_priv_in,
        TRIM(src.data_grp_peak_arvl_tm_tx) as data_grp_peak_arvl_tm_tx,
        TRIM(src.data_grp_peak_dprt_tm_tx) as data_grp_peak_dprt_tm_tx,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_hm_fac_id',
            'src.data_grp_dlgt_bkng_meth_nm',
            'src.data_gro_nm',
            'src.data_grp_bus_src_nm',
            'src.data_grp_free_tm_lvl_nm',
            'src.data_dlvr_meth_nm',
            'src.data_opty_typ_nm',
            'src.data_grp_acct_typ_nm',
            'src.data_grp_stg_nm',
            'src.data_grp_bk_hm_fac_frst_in',
            'src.data_grp_cl_acpt_dt',
            'src.data_grp_ctf_dt',
            'src.data_grp_arvl_dt',
            'src.data_grp_peak_arvl_dt',
            'src.data_grp_peak_dprt_dt',
            'src.data_grp_dprt_dt',
            'src.data_grp_peak_rm_cn',
            'src.data_grp_tot_rm_cn',
            'src.data_grp_vchr_in',
            'src.data_grp_comp_in',
            'src.data_grp_run_hs_in',
            'src.data_grp_exprs_chk_out_in',
            'src.data_grp_hide_rt_in',
            'src.data_grp_comm_allow_in',
            'src.data_grp_disc_promo_allow_in',
            'src.data_grp_sprd_dpst_in',
            'src.data_grp_rvrt_dpst_in',
            'src.data_grp_byps_auto_cncl_in',
            'src.data_grp_byps_dpst_in',
            'src.data_grp_byps_cncl_fee_in',
            'src.data_grp_byps_mod_fee_in',
            'src.data_grp_auto_cnfirm_in',
            'src.data_grp_exprs_lug_in',
            'src.data_grp_res_guar_in',
            'src.data_grp_whsl_in',
            'src.data_grp_dlgt_wrtoff_in',
            'src.data_grp_rsr_in',
            'src.data_grp_addl_adlt_am',
            'src.data_grp_nm',
            'src.data_gro_agt_nm',
            'src.data_sls_dept_nm',
            'src.data_sls_mgr_nm',
            'src.data_sls_phn_nb',
            'src.data_srvc_dept_nm',
            'src.data_srvc_mgr_nm',
            'src.data_gsrvc_phn_nb',
            'src.data_grp_comm_am_tx',
            'src.data_grp_comm_pc_tx',
            'src.data_rp_comm_rt_tx',
            'src.data_create_dts',
            'src.data_create_usr_id_cd',
            'src.data_updt_usr_id_cd',
            'src.data_jdo_seq_nb',
            'src.data_grp_cnfirm_dest_nm',
            'src.data_grp_min_los_nb_tx',
            'src.data_grp_dlgt_chg_priv_in',
            'src.data_grp_peak_arvl_tm_tx',
            'src.data_grp_peak_dprt_tm_tx',
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
    on src.data_grp_cd = min_source_update_datetime.data_grp_cd
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_grp_cd, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final