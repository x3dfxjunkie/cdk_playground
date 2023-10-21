{{
    config(
        materialized='incremental',
        unique_key= ['data_acct_rcv_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_accounting', 'acct_rcv') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_acct_rcv_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_acct_rcv_id
),

-- cleansing the table
renamed as (
    select
        src.data_acct_rcv_id as data_acct_rcv_id,
        src.data_sap_div_cd as data_sap_div_cd,
        src.data_sap_sls_org_cd as data_sap_sls_org_cd,
        TRIM(src.data_sap_cust_nb) as data_sap_cust_nb,
        src.data_cmps_id as data_cmps_id,
        src.data_bus_org_id as data_bus_org_id,
        TRIM(src.data_fac_nm) as data_fac_nm,
        src.data_sls_grp_id as data_sls_grp_id,
        src.data_sls_ofc_id as data_sls_ofc_id,
        TRIM(src.data_ord_typ_nm) as data_ord_typ_nm,
        src.data_ar_dt as data_ar_dt,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        src.data_updt_dts as data_updt_dts,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        src.data_sap_dstr_chan_cd as data_sap_dstr_chan_cd,
        TRIM(src.data_sap_prft_ctr_cd) as data_sap_prft_ctr_cd,
        src.data_pmt_id as data_pmt_id,
        src.data_transact_commit_timestamp as data_transact_commit_timestamp,
        TRIM(src.data_transact_seq) as data_transact_seq,
        TRIM(src.data_ar_prtnr_nm) as data_ar_prtnr_nm,
        TRIM(src.data_ar_addr_ln1_tx) as data_ar_addr_ln1_tx,
        TRIM(src.data_ar_city_nm) as data_ar_city_nm,
        TRIM(src.data_ar_pstl_cd) as data_ar_pstl_cd,
        TRIM(src.data_ar_cntry_cd) as data_ar_cntry_cd,
        TRIM(src.data_ar_rgn_nm) as data_ar_rgn_nm,
        src.data_ar_intfc_id as data_ar_intfc_id,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_sap_div_cd',
            'src.data_sap_sls_org_cd',
            'src.data_sap_cust_nb',
            'src.data_cmps_id',
            'src.data_bus_org_id',
            'src.data_fac_nm',
            'src.data_sls_grp_id',
            'src.data_sls_ofc_id',
            'src.data_ord_typ_nm',
            'src.data_ar_dt',
            'src.data_create_usr_id_cd',
            'src.data_create_dts',
            'src.data_updt_usr_id_cd',
            'src.data_jdo_seq_nb',
            'src.data_sap_dstr_chan_cd',
            'src.data_sap_prft_ctr_cd',
            'src.data_pmt_id',
            'src.data_transact_commit_timestamp',
            'src.data_transact_seq',
            'src.data_ar_prtnr_nm',
            'src.data_ar_addr_ln1_tx',
            'src.data_ar_city_nm',
            'src.data_ar_pstl_cd',
            'src.data_ar_cntry_cd',
            'src.data_ar_rgn_nm',
            'src.data_ar_intfc_id',
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
    on src.data_acct_rcv_id = min_source_update_datetime.data_acct_rcv_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_acct_rcv_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final