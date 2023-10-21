{{
    config(
        materialized='incremental',
        unique_key= ['data_ap_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_accounting', 'rfnd_ap') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_ap_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_ap_id
),

-- cleansing the table
renamed as (
    select
        src.data_acct_dt as data_acct_dt,
        src.data_ap_am as data_ap_am,
        src.data_ap_dts as data_ap_dts,
        src.data_ap_id as data_ap_id,
        TRIM(src.data_ap_ptnr_addr_ln1_tx) as data_ap_ptnr_addr_ln1_tx,
        TRIM(src.data_ap_ptnr_addr_ln2_tx) as data_ap_ptnr_addr_ln2_tx,
        TRIM(src.data_ap_ptnr_city_nm) as data_ap_ptnr_city_nm,
        TRIM(src.data_ap_ptnr_cntry_cd) as data_ap_ptnr_cntry_cd,
        TRIM(src.data_ap_ptnr_nm) as data_ap_ptnr_nm,
        TRIM(src.data_ap_ptnr_pstl_cd) as data_ap_ptnr_pstl_cd,
        TRIM(src.data_ap_ptnr_rgn_cd) as data_ap_ptnr_rgn_cd,
        TRIM(src.data_ap_ptnr_rgn_nm) as data_ap_ptnr_rgn_nm,
        src.data_bus_org_id as data_bus_org_id,
        src.data_cmps_id as data_cmps_id,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        TRIM(src.data_crncy_iso_cd) as data_crncy_iso_cd,
        TRIM(src.data_doc_typ_cd) as data_doc_typ_cd,
        TRIM(src.data_fac_id) as data_fac_id,
        TRIM(src.data_orig_doc_id) as data_orig_doc_id,
        src.data_prge_dts as data_prge_dts,
        src.data_rfnd_ap_intfc_id as data_rfnd_ap_intfc_id,
        src.data_rfnd_pmt_id as data_rfnd_pmt_id,
        TRIM(src.data_sap_bus_area_cd) as data_sap_bus_area_cd,
        TRIM(src.data_sap_cost_ctr_cd) as data_sap_cost_ctr_cd,
        TRIM(src.data_sap_co_cd) as data_sap_co_cd,
        TRIM(src.data_sap_gl_acct_nb) as data_sap_gl_acct_nb,
        TRIM(src.data_sap_prft_ctr_cd) as data_sap_prft_ctr_cd,
        TRIM(src.data_sap_wbs_cd) as data_sap_wbs_cd,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_acct_dt',
            'src.data_ap_am',
            'src.data_ap_dts',
            'src.data_ap_ptnr_addr_ln1_tx',
            'src.data_ap_ptnr_addr_ln2_tx',
            'src.data_ap_ptnr_city_nm',
            'src.data_ap_ptnr_cntry_cd',
            'src.data_ap_ptnr_nm',
            'src.data_ap_ptnr_pstl_cd',
            'src.data_ap_ptnr_rgn_cd',
            'src.data_ap_ptnr_rgn_nm',
            'src.data_bus_org_id',
            'src.data_cmps_id',
            'src.data_create_dts',
            'src.data_create_usr_id_cd',
            'src.data_crncy_iso_cd',
            'src.data_doc_typ_cd',
            'src.data_fac_id',
            'src.data_orig_doc_id',
            'src.data_prge_dts',
            'src.data_rfnd_ap_intfc_id',
            'src.data_rfnd_pmt_id',
            'src.data_sap_bus_area_cd',
            'src.data_sap_cost_ctr_cd',
            'src.data_sap_co_cd',
            'src.data_sap_gl_acct_nb',
            'src.data_sap_prft_ctr_cd',
            'src.data_sap_wbs_cd',
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
    on src.data_ap_id = min_source_update_datetime.data_ap_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_ap_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final