{{
    config(
        materialized='incremental',
        unique_key= ['data_pmt_card_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_folio', 'pmt_card') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_pmt_card_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_pmt_card_id
),

-- cleansing the table
renamed as (
    select
        src.data_pmt_card_id as data_pmt_card_id,
        TRIM(src.data_strts_rtrv_ref_nb) as data_strts_rtrv_ref_nb,
        TRIM(src.data_umsk_card_nb) as data_umsk_card_nb,
        TRIM(src.data_pmt_card_hld_nm) as data_pmt_card_hld_nm,
        TRIM(src.data_pmt_card_hld_addr_ln1_vl) as data_pmt_card_hld_addr_ln1_vl,
        TRIM(src.data_pmt_card_hld_cty_nm) as data_pmt_card_hld_cty_nm,
        TRIM(src.data_pmt_card_hld_rgn_cd) as data_pmt_card_hld_rgn_cd,
        TRIM(src.data_pmt_card_hld_pstl_cd) as data_pmt_card_hld_pstl_cd,
        TRIM(src.data_pmt_card_hld_cntry_cd) as data_pmt_card_hld_cntry_cd,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_pmt_crd_use_sts_nm) as data_pmt_crd_use_sts_nm,
        TRIM(src.data_rrn_key_nb) as data_rrn_key_nb,
        TRIM(src.data_pmt_card_brnd_nm) as data_pmt_card_brnd_nm,
        TRIM(src.data_card_exp_dt) as data_card_exp_dt,
        TRIM(src.data_pmt_dev_trmnl_id) as data_pmt_dev_trmnl_id,
        TRIM(src.data_pmt_card_hld_addr_ln2_vl) as data_pmt_card_hld_addr_ln2_vl,
        TRIM(src.data_pmt_card_hld_rgn_nm) as data_pmt_card_hld_rgn_nm,
        TRIM(src.data_strts_sts_cd) as data_strts_sts_cd,
        src.data_prge_dts as data_prge_dts,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_strts_rtrv_ref_nb',
            'src.data_umsk_card_nb',
            'src.data_pmt_card_hld_nm',
            'src.data_pmt_card_hld_addr_ln1_vl',
            'src.data_pmt_card_hld_cty_nm',
            'src.data_pmt_card_hld_rgn_cd',
            'src.data_pmt_card_hld_pstl_cd',
            'src.data_pmt_card_hld_cntry_cd',
            'src.data_create_usr_id_cd',
            'src.data_create_dts',
            'src.data_pmt_crd_use_sts_nm',
            'src.data_rrn_key_nb',
            'src.data_pmt_card_brnd_nm',
            'src.data_card_exp_dt',
            'src.data_pmt_dev_trmnl_id',
            'src.data_pmt_card_hld_addr_ln2_vl',
            'src.data_pmt_card_hld_rgn_nm',
            'src.data_strts_sts_cd',
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
    on src.data_pmt_card_id = min_source_update_datetime.data_pmt_card_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_pmt_card_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final