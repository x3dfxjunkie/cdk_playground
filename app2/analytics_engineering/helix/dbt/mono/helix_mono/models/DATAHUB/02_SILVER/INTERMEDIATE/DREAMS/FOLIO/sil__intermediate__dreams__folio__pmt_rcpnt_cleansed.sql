{{
    config(
        materialized='incremental',
        unique_key= ['data_pmt_rcpnt_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_folio', 'pmt_rcpnt') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_pmt_rcpnt_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_pmt_rcpnt_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_addr_rfnd_nm_ovrd_in) as data_addr_rfnd_nm_ovrd_in,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        TRIM(src.data_memo_nm) as data_memo_nm,
        src.data_pmt_id as data_pmt_id,
        TRIM(src.data_pmt_rcpnt_addr_ln1_val) as data_pmt_rcpnt_addr_ln1_val,
        TRIM(src.data_pmt_rcpnt_addr_ln2_val) as data_pmt_rcpnt_addr_ln2_val,
        TRIM(src.data_pmt_rcpnt_cntry_cd) as data_pmt_rcpnt_cntry_cd,
        TRIM(src.data_pmt_rcpnt_cty_nm) as data_pmt_rcpnt_cty_nm,
        src.data_pmt_rcpnt_id as data_pmt_rcpnt_id,
        TRIM(src.data_pmt_rcpnt_nm) as data_pmt_rcpnt_nm,
        TRIM(src.data_pmt_rcpnt_pstl_cd) as data_pmt_rcpnt_pstl_cd,
        TRIM(src.data_pmt_rcpnt_rgn_cd) as data_pmt_rcpnt_rgn_cd,
        TRIM(src.data_pmt_rcpnt_rgn_nm) as data_pmt_rcpnt_rgn_nm,
        src.data_prge_dts as data_prge_dts,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_addr_rfnd_nm_ovrd_in',
            'src.data_create_dts',
            'src.data_create_usr_id_cd',
            'src.data_memo_nm',
            'src.data_pmt_id',
            'src.data_pmt_rcpnt_addr_ln1_val',
            'src.data_pmt_rcpnt_addr_ln2_val',
            'src.data_pmt_rcpnt_cntry_cd',
            'src.data_pmt_rcpnt_cty_nm',
            'src.data_pmt_rcpnt_nm',
            'src.data_pmt_rcpnt_pstl_cd',
            'src.data_pmt_rcpnt_rgn_cd',
            'src.data_pmt_rcpnt_rgn_nm',
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
    on src.data_pmt_rcpnt_id = min_source_update_datetime.data_pmt_rcpnt_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_pmt_rcpnt_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final