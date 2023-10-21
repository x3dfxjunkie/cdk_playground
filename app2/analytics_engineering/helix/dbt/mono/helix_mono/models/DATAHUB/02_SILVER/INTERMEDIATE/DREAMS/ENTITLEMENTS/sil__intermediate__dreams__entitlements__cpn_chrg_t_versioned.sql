{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_cpn_chrg_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__dreams__entitlements__cpn_chrg_t_cleansed'),
            join_columns=['data_cpn_chrg_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}",
        snowflake_warehouse='DSE_QUERY_LST_WH'
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__dreams__entitlements__cpn_chrg_t_cleansed') }}
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
            partition by data_cpn_chrg_id
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
        partition_columns = ['data_cpn_chrg_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_aprv_by_nm,
        data_chrg_am,
        data_chrg_am_crncy_cd,
        data_chrg_by_nm,
        data_chrg_ds,
        data_chrg_ffl_dts,
        data_chrg_pst_dt,
        data_chrg_rpst_in,
        data_cpn_chrg_id,
        data_cpn_pty_cn,
        data_create_dts,
        data_create_usr_id_cd,
        data_dup_chrg_in,
        data_exprnc_card_nb,
        data_incognito,
        data_jdo_seq_nb,
        data_prge_dts,
        data_rev_cls_id,
        data_rev_cls_nm,
        data_src_acct_ctr_id,
        data_txn_acct_ctr_id,
        data_txn_idvl_pty_id,
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