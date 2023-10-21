{{
    config(
        materialized='incremental',
        unique_key= ['data_exprnc_band_req_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_xbms_wdw', 'exprnc_band_fac_req') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_exprnc_band_req_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_exprnc_band_req_id
),

-- cleansing the table
renamed as (
    select
        src.data_exprnc_band_req_id as data_exprnc_band_req_id,
        src.data_dsny_fac_id as data_dsny_fac_id,
        src.data_exprnc_band_vndr_id as data_exprnc_band_vndr_id,
        TRIM(src.data_exprnc_band_req_ds) as data_exprnc_band_req_ds,
        src.data_pkg_cmpnt_id as data_pkg_cmpnt_id,
        src.data_fac_req_expect_dlvr_dt as data_fac_req_expect_dlvr_dt,
        src.data_cost_ctr_id as data_cost_ctr_id,
        src.data_wbs_elmnt_id as data_wbs_elmnt_id,
        src.data_gnrl_ldgr_id as data_gnrl_ldgr_id,
        src.data_ovrd_exprnc_band_sts_id as data_ovrd_exprnc_band_sts_id,
        TRIM(src.data_avail_gi_in) as data_avail_gi_in,
        TRIM(src.data_exprnc_band_req_hld_in) as data_exprnc_band_req_hld_in,
        src.data_curr_req_hld_rsn_id as data_curr_req_hld_rsn_id,
        TRIM(src.data_merch_po_nb) as data_merch_po_nb,
        TRIM(src.data_exprnc_band_req_on_dmnd_in) as data_exprnc_band_req_on_dmnd_in,
        TRIM(src.data_bab_shipmt_nb) as data_bab_shipmt_nb,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_dsny_fac_id',
            'src.data_exprnc_band_vndr_id',
            'src.data_exprnc_band_req_ds',
            'src.data_pkg_cmpnt_id',
            'src.data_fac_req_expect_dlvr_dt',
            'src.data_cost_ctr_id',
            'src.data_wbs_elmnt_id',
            'src.data_gnrl_ldgr_id',
            'src.data_ovrd_exprnc_band_sts_id',
            'src.data_avail_gi_in',
            'src.data_exprnc_band_req_hld_in',
            'src.data_curr_req_hld_rsn_id',
            'src.data_merch_po_nb',
            'src.data_exprnc_band_req_on_dmnd_in',
            'src.data_bab_shipmt_nb',
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
    on src.data_exprnc_band_req_id = min_source_update_datetime.data_exprnc_band_req_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_exprnc_band_req_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final