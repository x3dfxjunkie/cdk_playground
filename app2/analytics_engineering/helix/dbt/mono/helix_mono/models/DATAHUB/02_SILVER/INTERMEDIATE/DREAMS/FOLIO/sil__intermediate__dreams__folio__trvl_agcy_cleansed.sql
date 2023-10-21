{{
    config(
        materialized='incremental',
        unique_key= ['data_trvl_agcy_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_folio', 'trvl_agcy') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_trvl_agcy_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_trvl_agcy_id
),

-- cleansing the table
renamed as (
    select
        src.data_cmps_id as data_cmps_id,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        TRIM(src.data_glbl_tkt_comm_in) as data_glbl_tkt_comm_in,
        TRIM(src.data_iata_id) as data_iata_id,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        TRIM(src.data_sap_vndr_id) as data_sap_vndr_id,
        TRIM(src.data_trvl_agcy_actv_in) as data_trvl_agcy_actv_in,
        src.data_trvl_agcy_fm_create_dt as data_trvl_agcy_fm_create_dt,
        src.data_trvl_agcy_id as data_trvl_agcy_id,
        TRIM(src.data_trvl_agcy_nm) as data_trvl_agcy_nm,
        src.data_trvl_agcy_ods_id as data_trvl_agcy_ods_id,
        TRIM(src.data_trvl_agcy_pay_comm_in) as data_trvl_agcy_pay_comm_in,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_cmps_id',
            'src.data_create_dts',
            'src.data_create_usr_id_cd',
            'src.data_glbl_tkt_comm_in',
            'src.data_iata_id',
            'src.data_jdo_seq_nb',
            'src.data_sap_vndr_id',
            'src.data_trvl_agcy_actv_in',
            'src.data_trvl_agcy_fm_create_dt',
            'src.data_trvl_agcy_nm',
            'src.data_trvl_agcy_ods_id',
            'src.data_trvl_agcy_pay_comm_in',
            'src.data_updt_usr_id_cd',
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
    on src.data_trvl_agcy_id = min_source_update_datetime.data_trvl_agcy_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_trvl_agcy_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final