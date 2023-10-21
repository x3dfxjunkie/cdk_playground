{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_bank_acct_ctr_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__dreams__accounting__bank_acct_ctr_cleansed'),
            join_columns=['data_bank_acct_ctr_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__dreams__accounting__bank_acct_ctr_cleansed') }}
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
            partition by data_bank_acct_ctr_id
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
        partition_columns = ['data_bank_acct_ctr_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_bank_acct_ctr_id,
        data_acct_ctr_id,
        data_dsny_sys_cd,
        data_tcr_loc_in,
        data_gst_fc_in,
        data_bank_out_in,
        data_ovr_shrt_csh_am,
        data_ovr_shrt_crncy_cd,
        data_barcd_prt_in,
        data_till_dspns_in,
        data_strts_term_nb,
        data_rgstr_nb_vl,
        data_create_usr_id_cd,
        data_create_dts,
        data_updt_usr_id_cd,
        data_updt_dts,
        data_jdo_seq_nb,
        data_cc_mrcht_nm,
        data_cc_addr_mrcht_ln1_val,
        data_cc_addr_mrcht_ln2_val,
        data_cc_mrcht_cty_nm,
        data_cc_mrcht_pstl_cd,
        data_cc_mrcht_rgn_cd,
        data_cc_mrcht_cntry_cd,
        data_cc_mrcht_phn_nb_val,
        data_cc_mrcht_rgn_nm,
        data_chg_acct_enbl_in,
        data_gst_fc_mrcht_ref_val,
        data_non_gst_fc_mrcht_ref_val,
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