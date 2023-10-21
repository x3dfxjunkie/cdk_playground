{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_card_settl_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__dreams__accounting__card_settl_cleansed'),
            join_columns=['data_card_settl_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__dreams__accounting__card_settl_cleansed') }}
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
            partition by data_card_settl_id
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
        partition_columns = ['data_card_settl_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_card_settl_id,
        data_card_settl_dts,
        data_pmt_meth_typ_nm,
        data_crdt_txn_typ_nm,
        data_cmps_id,
        data_bus_org_id,
        data_sap_in,
        data_acct_dt,
        data_acm_res_arr_dt,
        data_card_settl_card_nb,
        data_acm_res_nb,
        data_acm_res_night_cn,
        data_acm_gst_nm,
        data_post_dts,
        data_chrg_acct_ctr_div_cd,
        data_chrg_acct_ctr_sls_org_cd,
        data_chrg_acct_ctr_prft_ctr_cd,
        data_acct_ctr_id,
        data_bank_acct_ctr_id,
        data_chrg_acct_ctr_id,
        data_card_auth_id,
        data_card_settl_auth_am,
        data_crncy_iso_cd,
        data_data_orig_cd,
        data_pmt_id,
        data_dprt_dt,
        data_sap_dstr_chan_cd,
        data_cc_mrcht_nb,
        data_cc_mrcht_ctgy_nb,
        data_rtrv_ref_nb,
        data_rfnd_in,
        data_create_usr_id_cd,
        data_create_dts,
        data_card_auth_cd,
        data_strts_auth_typ_nm,
        data_card_exp_dt,
        data_transact_commit_timestamp,
        data_transact_seq,
        data_strts_card_cls_cd,
        data_avs_resp_cd,
        data_rtl_cust_nb,
        data_int_preauth_amt,
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