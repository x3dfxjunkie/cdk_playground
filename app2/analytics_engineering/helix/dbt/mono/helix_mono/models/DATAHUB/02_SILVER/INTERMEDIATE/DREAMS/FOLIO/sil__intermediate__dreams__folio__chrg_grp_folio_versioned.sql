{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_chrg_grp_folio_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__dreams__folio__chrg_grp_folio_cleansed'),
            join_columns=['data_chrg_grp_folio_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__dreams__folio__chrg_grp_folio_cleansed') }}
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
            partition by data_chrg_grp_folio_id
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
        partition_columns = ['data_chrg_grp_folio_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_folio_acct_typ_nm,
        data_folio_sts_nm,
        data_respb_pty_id,
        data_prmy_pty_gst_nm,
        data_sml_bal_wrtoff_in,
        data_zero_bal_verif_in,
        data_settl_frq_typ_nm,
        data_updt_usr_id_cd,
        data_updt_dts,
        data_incognito,
        data_chrg_grp_folio_id,
        data_root_chrg_grp_id,
        data_dflt_chrg_grp_id,
        data_folio_actv_in,
        data_onsite_in,
        data_prmy_folio_in,
        data_pmt_ownr_in,
        data_chrg_grp_folio_strt_dt,
        data_chrg_grp_folio_end_dt,
        data_create_usr_id_cd,
        data_create_dts,
        data_jdo_seq_nb,
        data_folio_acct_lim_am,
        data_folio_acct_lim_crncy_cd,
        data_dpst_ext_dt,
        data_tax_exmpt_id,
        data_bill_pty_id,
        data_prge_dts,
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