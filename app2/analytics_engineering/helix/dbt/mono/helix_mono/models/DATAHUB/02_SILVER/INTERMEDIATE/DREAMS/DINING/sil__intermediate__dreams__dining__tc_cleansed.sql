{{
    config(
        materialized='incremental',
        unique_key= ['data_tc_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_dining', 'tc') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_tc_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_tc_id
),

-- cleansing the table
renamed as (
    select
        src.data_tc_id as data_tc_id,
        TRIM(src.data_tc_typ_nm) as data_tc_typ_nm,
        src.data_tc_grp_nb as data_tc_grp_nb,
        src.data_prod_id as data_prod_id,
        src.data_rev_cls_id as data_rev_cls_id,
        src.data_tc_strt_dts as data_tc_strt_dts,
        src.data_tc_end_dts as data_tc_end_dts,
        src.data_tc_bk_dts as data_tc_bk_dts,
        TRIM(src.data_tc_slct_in) as data_tc_slct_in,
        TRIM(src.data_prod_typ_nm) as data_prod_typ_nm,
        src.data_comnctn_chan_id as data_comnctn_chan_id,
        src.data_sls_chan_id as data_sls_chan_id,
        src.data_fac_id as data_fac_id,
        TRIM(src.data_trvl_sts_nm) as data_trvl_sts_nm,
        TRIM(src.data_upgrd_typ_nm) as data_upgrd_typ_nm,
        TRIM(src.data_tc_chrg_in) as data_tc_chrg_in,
        src.data_asgn_own_id as data_asgn_own_id,
        TRIM(src.data_tc_invtry_in) as data_tc_invtry_in,
        src.data_srvc_prd_id as data_srvc_prd_id,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        src.data_updt_dts as data_updt_dts,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        src.data_prnt_tc_id as data_prnt_tc_id,
        src.data_tc_chkin_dts as data_tc_chkin_dts,
        TRIM(src.data_blk_cd) as data_blk_cd,
        src.data_trvl_agcy_pty_id as data_trvl_agcy_pty_id,
        src.data_upgrd_tc_id as data_upgrd_tc_id,
        src.data_prge_dts as data_prge_dts,
        src.data_tc_chkot_dts as data_tc_chkot_dts,
        src.data_tc_cncl_dts as data_tc_cncl_dts,
        src.data_tc_lst_sty_dt as data_tc_lst_sty_dt,
        TRIM(src.data_tc_req_fac_tx) as data_tc_req_fac_tx,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_tc_typ_nm',
            'src.data_tc_grp_nb',
            'src.data_prod_id',
            'src.data_rev_cls_id',
            'src.data_tc_strt_dts',
            'src.data_tc_end_dts',
            'src.data_tc_bk_dts',
            'src.data_tc_slct_in',
            'src.data_prod_typ_nm',
            'src.data_comnctn_chan_id',
            'src.data_sls_chan_id',
            'src.data_fac_id',
            'src.data_trvl_sts_nm',
            'src.data_upgrd_typ_nm',
            'src.data_tc_chrg_in',
            'src.data_asgn_own_id',
            'src.data_tc_invtry_in',
            'src.data_srvc_prd_id',
            'src.data_create_usr_id_cd',
            'src.data_create_dts',
            'src.data_updt_usr_id_cd',
            'src.data_jdo_seq_nb',
            'src.data_prnt_tc_id',
            'src.data_tc_chkin_dts',
            'src.data_blk_cd',
            'src.data_trvl_agcy_pty_id',
            'src.data_upgrd_tc_id',
            'src.data_prge_dts',
            'src.data_tc_chkot_dts',
            'src.data_tc_cncl_dts',
            'src.data_tc_lst_sty_dt',
            'src.data_tc_req_fac_tx',
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
    on src.data_tc_id = min_source_update_datetime.data_tc_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_tc_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final