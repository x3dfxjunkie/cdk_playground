{{
    config(
        materialized='incremental',
        unique_key= ['data_chrg_grp_folio_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_folio', 'chrg_grp_folio') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_chrg_grp_folio_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_chrg_grp_folio_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_folio_acct_typ_nm) as data_folio_acct_typ_nm,
        TRIM(src.data_folio_sts_nm) as data_folio_sts_nm,
        src.data_respb_pty_id as data_respb_pty_id,
        TRIM(src.data_prmy_pty_gst_nm) as data_prmy_pty_gst_nm,
        TRIM(src.data_sml_bal_wrtoff_in) as data_sml_bal_wrtoff_in,
        TRIM(src.data_zero_bal_verif_in) as data_zero_bal_verif_in,
        TRIM(src.data_settl_frq_typ_nm) as data_settl_frq_typ_nm,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_incognito) as data_incognito,
        src.data_chrg_grp_folio_id as data_chrg_grp_folio_id,
        src.data_root_chrg_grp_id as data_root_chrg_grp_id,
        src.data_dflt_chrg_grp_id as data_dflt_chrg_grp_id,
        TRIM(src.data_folio_actv_in) as data_folio_actv_in,
        TRIM(src.data_onsite_in) as data_onsite_in,
        TRIM(src.data_prmy_folio_in) as data_prmy_folio_in,
        TRIM(src.data_pmt_ownr_in) as data_pmt_ownr_in,
        src.data_chrg_grp_folio_strt_dt as data_chrg_grp_folio_strt_dt,
        src.data_chrg_grp_folio_end_dt as data_chrg_grp_folio_end_dt,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_create_dts as data_create_dts,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        src.data_folio_acct_lim_am as data_folio_acct_lim_am,
        TRIM(src.data_folio_acct_lim_crncy_cd) as data_folio_acct_lim_crncy_cd,
        src.data_dpst_ext_dt as data_dpst_ext_dt,
        src.data_tax_exmpt_id as data_tax_exmpt_id,
        src.data_bill_pty_id as data_bill_pty_id,
        src.data_prge_dts as data_prge_dts,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_folio_acct_typ_nm',
            'src.data_folio_sts_nm',
            'src.data_respb_pty_id',
            'src.data_prmy_pty_gst_nm',
            'src.data_sml_bal_wrtoff_in',
            'src.data_zero_bal_verif_in',
            'src.data_settl_frq_typ_nm',
            'src.data_updt_usr_id_cd',
            'src.data_incognito',
            'src.data_root_chrg_grp_id',
            'src.data_dflt_chrg_grp_id',
            'src.data_folio_actv_in',
            'src.data_onsite_in',
            'src.data_prmy_folio_in',
            'src.data_pmt_ownr_in',
            'src.data_chrg_grp_folio_strt_dt',
            'src.data_chrg_grp_folio_end_dt',
            'src.data_create_usr_id_cd',
            'src.data_create_dts',
            'src.data_jdo_seq_nb',
            'src.data_folio_acct_lim_am',
            'src.data_folio_acct_lim_crncy_cd',
            'src.data_dpst_ext_dt',
            'src.data_tax_exmpt_id',
            'src.data_bill_pty_id',
            'src.data_prge_dts',
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
    on src.data_chrg_grp_folio_id = min_source_update_datetime.data_chrg_grp_folio_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_chrg_grp_folio_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final