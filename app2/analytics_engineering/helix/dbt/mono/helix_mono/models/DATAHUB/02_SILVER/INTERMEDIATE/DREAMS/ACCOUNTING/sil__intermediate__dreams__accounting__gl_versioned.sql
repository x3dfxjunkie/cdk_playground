{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_gl_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__dreams__accounting__gl_cleansed'),
            join_columns=['data_gl_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__dreams__accounting__gl_cleansed') }}
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
            partition by data_gl_id
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
        partition_columns = ['data_gl_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_acct_dt,
        data_bus_org_id,
        data_chrg_acct_ctr_bus_area_cd,
        data_chrg_acct_ctr_co_cd,
        data_cmps_id,
        data_create_dts,
        data_create_usr_id_cd,
        data_crncy_iso_cd,
        data_ext_src_ref_val,
        data_gl_am,
        data_gl_id,
        data_gl_natr_in,
        data_jdo_seq_nb,
        data_prge_dts,
        data_prm_pty_nm,
        data_sap_acct_nm,
        data_sap_cost_ctr_cd,
        data_sap_dstr_chan_cd,
        data_sap_dstr_chan_nm,
        data_sap_gl_acct_nb,
        data_sap_iss_cd,
        data_sap_mtrl_cd,
        data_sap_prft_ctr_cd,
        data_sap_tax_cd,
        data_sap_wbs_cd,
        data_src_acct_ctr_co_cd,
        data_src_acct_ctr_id,
        data_src_bus_area_cd,
        data_tax_exmpt_in,
        data_trdg_ptnr_bus_area_cd,
        data_trdg_ptnr_co_cd,
        data_updt_dts,
        data_updt_usr_id_cd,
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