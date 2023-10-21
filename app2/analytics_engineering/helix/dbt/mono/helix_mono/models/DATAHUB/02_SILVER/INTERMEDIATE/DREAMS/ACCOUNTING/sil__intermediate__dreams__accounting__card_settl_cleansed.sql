{{
    config(
        materialized='incremental',
        unique_key= ['data_card_settl_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_accounting', 'card_settl') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_card_settl_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_card_settl_id
),

-- cleansing the table
renamed as (
    select
        src.data_card_settl_id as data_card_settl_id,
        src.data_card_settl_dts as data_card_settl_dts,
        TRIM(src.data_pmt_meth_typ_nm) as data_pmt_meth_typ_nm,
        TRIM(src.data_crdt_txn_typ_nm) as data_crdt_txn_typ_nm,
        src.data_cmps_id as data_cmps_id,
        src.data_bus_org_id as data_bus_org_id,
        TRIM(src.data_sap_in) as data_sap_in,
        src.data_acct_dt as data_acct_dt,
        src.data_acm_res_arr_dt as data_acm_res_arr_dt,
        TRIM(src.data_card_settl_card_nb) as data_card_settl_card_nb,
        TRIM(src.data_acm_res_nb) as data_acm_res_nb,
        src.data_acm_res_night_cn as data_acm_res_night_cn,
        TRIM(src.data_acm_gst_nm) as data_acm_gst_nm,
        src.data_post_dts as data_post_dts,
        TRIM(src.data_chrg_acct_ctr_div_cd) as data_chrg_acct_ctr_div_cd,
        TRIM(src.data_chrg_acct_ctr_sls_org_cd) as data_chrg_acct_ctr_sls_org_cd,
        TRIM(src.data_chrg_acct_ctr_prft_ctr_cd) as data_chrg_acct_ctr_prft_ctr_cd,
        src.data_acct_ctr_id as data_acct_ctr_id,
        src.data_bank_acct_ctr_id as data_bank_acct_ctr_id,
        src.data_chrg_acct_ctr_id as data_chrg_acct_ctr_id,
        src.data_card_auth_id as data_card_auth_id,
        src.data_card_settl_auth_am as data_card_settl_auth_am,
        TRIM(src.data_crncy_iso_cd) as data_crncy_iso_cd,
        TRIM(src.data_data_orig_cd) as data_data_orig_cd,
        src.data_pmt_id as data_pmt_id,
        src.data_dprt_dt as data_dprt_dt,
        TRIM(src.data_sap_dstr_chan_cd) as data_sap_dstr_chan_cd,
        TRIM(src.data_cc_mrcht_nb) as data_cc_mrcht_nb,
        src.data_cc_mrcht_ctgy_nb as data_cc_mrcht_ctgy_nb,
        TRIM(src.data_rtrv_ref_nb) as data_rtrv_ref_nb,
        TRIM(src.data_rfnd_in) as data_rfnd_in,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_card_auth_cd) as data_card_auth_cd,
        TRIM(src.data_strts_auth_typ_nm) as data_strts_auth_typ_nm,
        TRIM(src.data_card_exp_dt) as data_card_exp_dt,
        src.data_transact_commit_timestamp as data_transact_commit_timestamp,
        TRIM(src.data_transact_seq) as data_transact_seq,
        TRIM(src.data_strts_card_cls_cd) as data_strts_card_cls_cd,
        TRIM(src.data_avs_resp_cd) as data_avs_resp_cd,
        TRIM(src.data_rtl_cust_nb) as data_rtl_cust_nb,
        src.data_int_preauth_amt as data_int_preauth_amt,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_card_settl_dts',
            'src.data_pmt_meth_typ_nm',
            'src.data_crdt_txn_typ_nm',
            'src.data_cmps_id',
            'src.data_bus_org_id',
            'src.data_sap_in',
            'src.data_acct_dt',
            'src.data_acm_res_arr_dt',
            'src.data_card_settl_card_nb',
            'src.data_acm_res_nb',
            'src.data_acm_res_night_cn',
            'src.data_acm_gst_nm',
            'src.data_post_dts',
            'src.data_chrg_acct_ctr_div_cd',
            'src.data_chrg_acct_ctr_sls_org_cd',
            'src.data_chrg_acct_ctr_prft_ctr_cd',
            'src.data_acct_ctr_id',
            'src.data_bank_acct_ctr_id',
            'src.data_chrg_acct_ctr_id',
            'src.data_card_auth_id',
            'src.data_card_settl_auth_am',
            'src.data_crncy_iso_cd',
            'src.data_data_orig_cd',
            'src.data_pmt_id',
            'src.data_dprt_dt',
            'src.data_sap_dstr_chan_cd',
            'src.data_cc_mrcht_nb',
            'src.data_cc_mrcht_ctgy_nb',
            'src.data_rtrv_ref_nb',
            'src.data_rfnd_in',
            'src.data_create_usr_id_cd',
            'src.data_create_dts',
            'src.data_card_auth_cd',
            'src.data_strts_auth_typ_nm',
            'src.data_card_exp_dt',
            'src.data_transact_commit_timestamp',
            'src.data_transact_seq',
            'src.data_strts_card_cls_cd',
            'src.data_avs_resp_cd',
            'src.data_rtl_cust_nb',
            'src.data_int_preauth_amt',
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
    on src.data_card_settl_id = min_source_update_datetime.data_card_settl_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_card_settl_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final