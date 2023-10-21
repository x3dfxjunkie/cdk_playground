{{
    config(
        materialized='incremental',
        unique_key= ['data_prod_lnk_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_price', 'prod_lnk_t') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_prod_lnk_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_prod_lnk_id
),

-- cleansing the table
renamed as (
    select
        src.data_entrprs_meal_prd_id as data_entrprs_meal_prd_id,
        src.data_prge_dts as data_prge_dts,
        src.data_prmy_prod_id as data_prmy_prod_id,
        src.data_prod_lnk_end_dt as data_prod_lnk_end_dt,
        src.data_prod_lnk_id as data_prod_lnk_id,
        src.data_prod_lnk_strt_dt as data_prod_lnk_strt_dt,
        TRIM(src.data_prod_lnk_typ_nm) as data_prod_lnk_typ_nm,
        src.data_sec_prod_id as data_sec_prod_id,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_entrprs_meal_prd_id',
            'src.data_prge_dts',
            'src.data_prmy_prod_id',
            'src.data_prod_lnk_end_dt',
            'src.data_prod_lnk_strt_dt',
            'src.data_prod_lnk_typ_nm',
            'src.data_sec_prod_id',
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
    on src.data_prod_lnk_id = min_source_update_datetime.data_prod_lnk_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_prod_lnk_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final