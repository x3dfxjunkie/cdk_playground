{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_card_auth_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__dreams__folio__card_auth_cleansed'),
            join_columns=['data_card_auth_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__dreams__folio__card_auth_cleansed') }}
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
            partition by data_card_auth_id
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
        partition_columns = ['data_card_auth_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_auth_ref_vl,
        data_avs_resp_cd,
        data_card_auth_am,
        data_card_auth_cd,
        data_card_auth_crncy_cd,
        data_card_auth_dts,
        data_card_auth_id,
        data_card_entry_mode_cd,
        data_card_exp_dt,
        data_cc_mrcht_ctgy_nb,
        data_cc_mrcht_nb,
        data_create_dts,
        data_create_usr_id_cd,
        data_e_cmrc_indctn_cd,
        data_int_preauth_amt,
        data_mc_bnknt_dt,
        data_mc_bnknt_ref_nb,
        data_pmt_card_id,
        data_pmt_man_auth_in,
        data_prge_dts,
        data_strts_auth_typ_nm,
        data_strts_card_cls_cd,
        data_strts_trmnl_nb,
        data_strts_txn_ds_cd,
        data_visa_auth_chrctr_cd,
        data_visa_txn_id,
        data_visa_vld_cd,
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