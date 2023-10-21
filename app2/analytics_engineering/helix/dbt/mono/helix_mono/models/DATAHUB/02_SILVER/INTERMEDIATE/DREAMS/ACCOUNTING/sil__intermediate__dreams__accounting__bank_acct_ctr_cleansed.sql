{{
    config(
        materialized='incremental',
        unique_key= ['data_bank_acct_ctr_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_accounting', 'bank_acct_ctr') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_bank_acct_ctr_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_bank_acct_ctr_id
),

-- cleansing the table
renamed as (
    select
        src.data_bank_acct_ctr_id as data_bank_acct_ctr_id,
        src.data_acct_ctr_id as data_acct_ctr_id,
        TRIM(src.data_dsny_sys_cd) as data_dsny_sys_cd,
        TRIM(src.data_tcr_loc_in) as data_tcr_loc_in,
        TRIM(src.data_gst_fc_in) as data_gst_fc_in,
        TRIM(src.data_bank_out_in) as data_bank_out_in,
        src.data_ovr_shrt_csh_am as data_ovr_shrt_csh_am,
        TRIM(src.data_ovr_shrt_crncy_cd) as data_ovr_shrt_crncy_cd,
        TRIM(src.data_barcd_prt_in) as data_barcd_prt_in,
        TRIM(src.data_till_dspns_in) as data_till_dspns_in,
        src.data_strts_term_nb as data_strts_term_nb,
        TRIM(src.data_rgstr_nb_vl) as data_rgstr_nb_vl,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        src.data_updt_dts as data_updt_dts,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        TRIM(src.data_cc_mrcht_nm) as data_cc_mrcht_nm,
        TRIM(src.data_cc_addr_mrcht_ln1_val) as data_cc_addr_mrcht_ln1_val,
        TRIM(src.data_cc_addr_mrcht_ln2_val) as data_cc_addr_mrcht_ln2_val,
        TRIM(src.data_cc_mrcht_cty_nm) as data_cc_mrcht_cty_nm,
        TRIM(src.data_cc_mrcht_pstl_cd) as data_cc_mrcht_pstl_cd,
        TRIM(src.data_cc_mrcht_rgn_cd) as data_cc_mrcht_rgn_cd,
        TRIM(src.data_cc_mrcht_cntry_cd) as data_cc_mrcht_cntry_cd,
        TRIM(src.data_cc_mrcht_phn_nb_val) as data_cc_mrcht_phn_nb_val,
        TRIM(src.data_cc_mrcht_rgn_nm) as data_cc_mrcht_rgn_nm,
        TRIM(src.data_chg_acct_enbl_in) as data_chg_acct_enbl_in,
        TRIM(src.data_gst_fc_mrcht_ref_val) as data_gst_fc_mrcht_ref_val,
        TRIM(src.data_non_gst_fc_mrcht_ref_val) as data_non_gst_fc_mrcht_ref_val,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_acct_ctr_id',
            'src.data_dsny_sys_cd',
            'src.data_tcr_loc_in',
            'src.data_gst_fc_in',
            'src.data_bank_out_in',
            'src.data_ovr_shrt_csh_am',
            'src.data_ovr_shrt_crncy_cd',
            'src.data_barcd_prt_in',
            'src.data_till_dspns_in',
            'src.data_strts_term_nb',
            'src.data_rgstr_nb_vl',
            'src.data_create_usr_id_cd',
            'src.data_create_dts',
            'src.data_updt_usr_id_cd',
            'src.data_jdo_seq_nb',
            'src.data_cc_mrcht_nm',
            'src.data_cc_addr_mrcht_ln1_val',
            'src.data_cc_addr_mrcht_ln2_val',
            'src.data_cc_mrcht_cty_nm',
            'src.data_cc_mrcht_pstl_cd',
            'src.data_cc_mrcht_rgn_cd',
            'src.data_cc_mrcht_cntry_cd',
            'src.data_cc_mrcht_phn_nb_val',
            'src.data_cc_mrcht_rgn_nm',
            'src.data_chg_acct_enbl_in',
            'src.data_gst_fc_mrcht_ref_val',
            'src.data_non_gst_fc_mrcht_ref_val',
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
    on src.data_bank_acct_ctr_id = min_source_update_datetime.data_bank_acct_ctr_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_bank_acct_ctr_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final