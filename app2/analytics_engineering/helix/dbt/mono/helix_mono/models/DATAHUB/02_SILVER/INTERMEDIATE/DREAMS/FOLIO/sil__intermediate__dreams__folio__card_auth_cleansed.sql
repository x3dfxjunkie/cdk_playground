{{
    config(
        materialized='incremental',
        unique_key= ['data_card_auth_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_folio', 'card_auth') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_card_auth_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_card_auth_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_auth_ref_vl) as data_auth_ref_vl,
        TRIM(src.data_avs_resp_cd) as data_avs_resp_cd,
        src.data_card_auth_am as data_card_auth_am,
        TRIM(src.data_card_auth_cd) as data_card_auth_cd,
        TRIM(src.data_card_auth_crncy_cd) as data_card_auth_crncy_cd,
        src.data_card_auth_dts as data_card_auth_dts,
        src.data_card_auth_id as data_card_auth_id,
        TRIM(src.data_card_entry_mode_cd) as data_card_entry_mode_cd,
        TRIM(src.data_card_exp_dt) as data_card_exp_dt,
        src.data_cc_mrcht_ctgy_nb as data_cc_mrcht_ctgy_nb,
        TRIM(src.data_cc_mrcht_nb) as data_cc_mrcht_nb,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        TRIM(src.data_e_cmrc_indctn_cd) as data_e_cmrc_indctn_cd,
        src.data_int_preauth_amt as data_int_preauth_amt,
        TRIM(src.data_mc_bnknt_dt) as data_mc_bnknt_dt,
        TRIM(src.data_mc_bnknt_ref_nb) as data_mc_bnknt_ref_nb,
        src.data_pmt_card_id as data_pmt_card_id,
        TRIM(src.data_pmt_man_auth_in) as data_pmt_man_auth_in,
        src.data_prge_dts as data_prge_dts,
        TRIM(src.data_strts_auth_typ_nm) as data_strts_auth_typ_nm,
        TRIM(src.data_strts_card_cls_cd) as data_strts_card_cls_cd,
        src.data_strts_trmnl_nb as data_strts_trmnl_nb,
        TRIM(src.data_strts_txn_ds_cd) as data_strts_txn_ds_cd,
        TRIM(src.data_visa_auth_chrctr_cd) as data_visa_auth_chrctr_cd,
        TRIM(src.data_visa_txn_id) as data_visa_txn_id,
        TRIM(src.data_visa_vld_cd) as data_visa_vld_cd,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_auth_ref_vl',
            'src.data_avs_resp_cd',
            'src.data_card_auth_am',
            'src.data_card_auth_cd',
            'src.data_card_auth_crncy_cd',
            'src.data_card_auth_dts',
            'src.data_card_entry_mode_cd',
            'src.data_card_exp_dt',
            'src.data_cc_mrcht_ctgy_nb',
            'src.data_cc_mrcht_nb',
            'src.data_create_dts',
            'src.data_create_usr_id_cd',
            'src.data_e_cmrc_indctn_cd',
            'src.data_int_preauth_amt',
            'src.data_mc_bnknt_dt',
            'src.data_mc_bnknt_ref_nb',
            'src.data_pmt_card_id',
            'src.data_pmt_man_auth_in',
            'src.data_prge_dts',
            'src.data_strts_auth_typ_nm',
            'src.data_strts_card_cls_cd',
            'src.data_strts_trmnl_nb',
            'src.data_strts_txn_ds_cd',
            'src.data_visa_auth_chrctr_cd',
            'src.data_visa_txn_id',
            'src.data_visa_vld_cd',
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
    on src.data_card_auth_id = min_source_update_datetime.data_card_auth_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_card_auth_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final