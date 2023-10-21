{{
    config(
        materialized='incremental',
        unique_key= ['data_cpn_chrg_id','metadata_checksum'],
        on_schema_change='append_new_columns',
        snowflake_warehouse='DSE_QUERY_LST_WH'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'D' then 'D' else 'S' end as dms_operation 
    from {{ source('brz_dreams_entitlements', 'cpn_chrg_t') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_cpn_chrg_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_cpn_chrg_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_aprv_by_nm) as data_aprv_by_nm,
        src.data_chrg_am as data_chrg_am,
        TRIM(src.data_chrg_am_crncy_cd) as data_chrg_am_crncy_cd,
        TRIM(src.data_chrg_by_nm) as data_chrg_by_nm,
        TRIM(src.data_chrg_ds) as data_chrg_ds,
        src.data_chrg_ffl_dts as data_chrg_ffl_dts,
        src.data_chrg_pst_dt as data_chrg_pst_dt,
        TRIM(src.data_chrg_rpst_in) as data_chrg_rpst_in,
        src.data_cpn_chrg_id as data_cpn_chrg_id,
        src.data_cpn_pty_cn as data_cpn_pty_cn,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        TRIM(src.data_dup_chrg_in) as data_dup_chrg_in,
        TRIM(src.data_exprnc_card_nb) as data_exprnc_card_nb,
        TRIM(src.data_incognito) as data_incognito,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        src.data_prge_dts as data_prge_dts,
        src.data_rev_cls_id as data_rev_cls_id,
        TRIM(src.data_rev_cls_nm) as data_rev_cls_nm,
        src.data_src_acct_ctr_id as data_src_acct_ctr_id,
        src.data_txn_acct_ctr_id as data_txn_acct_ctr_id,
        src.data_txn_idvl_pty_id as data_txn_idvl_pty_id,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_aprv_by_nm',
            'src.data_chrg_am',
            'src.data_chrg_am_crncy_cd',
            'src.data_chrg_by_nm',
            'src.data_chrg_ds',
            'src.data_chrg_ffl_dts',
            'src.data_chrg_pst_dt',
            'src.data_chrg_rpst_in',
            'src.data_cpn_pty_cn',
            'src.data_create_dts',
            'src.data_create_usr_id_cd',
            'src.data_dup_chrg_in',
            'src.data_exprnc_card_nb',
            'src.data_incognito',
            'src.data_jdo_seq_nb',
            'src.data_prge_dts',
            'src.data_rev_cls_id',
            'src.data_rev_cls_nm',
            'src.data_src_acct_ctr_id',
            'src.data_txn_acct_ctr_id',
            'src.data_txn_idvl_pty_id',
            'src.data_updt_usr_id_cd',
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
    on src.data_cpn_chrg_id = min_source_update_datetime.data_cpn_chrg_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_cpn_chrg_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final