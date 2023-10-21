{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_grp_cd','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__dreams__group_management__grp_cleansed'),
            join_columns=['data_grp_cd'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__dreams__group_management__grp_cleansed') }}
    {% if is_incremental() %}
    -- this filter will only be applied on an incremental run

        where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

-- adding the row_number column (rn) for ordering the incremental data by metadata_timestamp
renamed as (
    select
        *,
        row_number() over (
            partition by data_grp_cd
                order by
                    metadata_timestamp desc
        ) as rn
    from
        cleansed
),

-- adding version start and end dates metadata columns
versioned as (
    {{ macro_create_versions(
        cleansed_table = 'renamed',
        timestamp_column = 'metadata_timestamp',
        partition_columns = ['data_grp_cd']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_grp_cd,
        data_hm_fac_id,
        data_grp_dlgt_bkng_meth_nm,
        data_gro_nm,
        data_grp_bus_src_nm,
        data_grp_free_tm_lvl_nm,
        data_dlvr_meth_nm,
        data_opty_typ_nm,
        data_grp_acct_typ_nm,
        data_grp_stg_nm,
        data_grp_bk_hm_fac_frst_in,
        data_grp_cl_acpt_dt,
        data_grp_ctf_dt,
        data_grp_arvl_dt,
        data_grp_peak_arvl_dt,
        data_grp_peak_dprt_dt,
        data_grp_dprt_dt,
        data_grp_peak_rm_cn,
        data_grp_tot_rm_cn,
        data_grp_vchr_in,
        data_grp_comp_in,
        data_grp_run_hs_in,
        data_grp_exprs_chk_out_in,
        data_grp_hide_rt_in,
        data_grp_comm_allow_in,
        data_grp_disc_promo_allow_in,
        data_grp_sprd_dpst_in,
        data_grp_rvrt_dpst_in,
        data_grp_byps_auto_cncl_in,
        data_grp_byps_dpst_in,
        data_grp_byps_cncl_fee_in,
        data_grp_byps_mod_fee_in,
        data_grp_auto_cnfirm_in,
        data_grp_exprs_lug_in,
        data_grp_res_guar_in,
        data_grp_whsl_in,
        data_grp_dlgt_wrtoff_in,
        data_grp_rsr_in,
        data_grp_addl_adlt_am,
        data_grp_nm,
        data_gro_agt_nm,
        data_sls_dept_nm,
        data_sls_mgr_nm,
        data_sls_phn_nb,
        data_srvc_dept_nm,
        data_srvc_mgr_nm,
        data_gsrvc_phn_nb,
        data_grp_comm_am_tx,
        data_grp_comm_pc_tx,
        data_rp_comm_rt_tx,
        data_create_dts,
        data_create_usr_id_cd,
        data_updt_dts,
        data_updt_usr_id_cd,
        data_jdo_seq_nb,
        data_grp_cnfirm_dest_nm,
        data_grp_min_los_nb_tx,
        data_grp_dlgt_chg_priv_in,
        data_grp_peak_arvl_tm_tx,
        data_grp_peak_dprt_tm_tx,
        metadata_checksum,
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
        metadata_version_start_datetime,
        metadata_version_end_datetime,
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
    from versioned
)

select * from final