{{
    config(
        materialized='incremental',
        unique_key= ['data_res_seg_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_xbms_wdw', 'res_seg') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_res_seg_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_res_seg_id
),

-- cleansing the table
renamed as (
    select
        src.data_res_seg_id as data_res_seg_id,
        src.data_dsny_fac_id as data_dsny_fac_id,
        src.data_res_seg_begin_dt as data_res_seg_begin_dt,
        src.data_res_seg_end_dt as data_res_seg_end_dt,
        TRIM(src.data_create_usr_id) as data_create_usr_id,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id) as data_updt_usr_id,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_logical_del_in) as data_logical_del_in,
        TRIM(src.data_trvl_plan_seg_id) as data_trvl_plan_seg_id,
        TRIM(src.data_trvl_cmpnt_id) as data_trvl_cmpnt_id,
        src.data_res_id as data_res_id,
        src.data_trvl_cmpnt_sts_id as data_trvl_cmpnt_sts_id,
        src.data_grp_mstr_rec_tm_id as data_grp_mstr_rec_tm_id,
        TRIM(src.data_res_seg_pkg_cd) as data_res_seg_pkg_cd,
        src.data_res_seg_pkg_prod_id as data_res_seg_pkg_prod_id,
        TRIM(src.data_res_seg_pkg_ds) as data_res_seg_pkg_ds,
        TRIM(src.data_res_seg_spcl_offer_in) as data_res_seg_spcl_offer_in,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_dsny_fac_id',
            'src.data_res_seg_begin_dt',
            'src.data_res_seg_end_dt',
            'src.data_create_usr_id',
            'src.data_create_dts',
            'src.data_updt_usr_id',
            'src.data_logical_del_in',
            'src.data_trvl_plan_seg_id',
            'src.data_trvl_cmpnt_id',
            'src.data_res_id',
            'src.data_trvl_cmpnt_sts_id',
            'src.data_grp_mstr_rec_tm_id',
            'src.data_res_seg_pkg_cd',
            'src.data_res_seg_pkg_prod_id',
            'src.data_res_seg_pkg_ds',
            'src.data_res_seg_spcl_offer_in',
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
    on src.data_res_seg_id = min_source_update_datetime.data_res_seg_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_res_seg_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final