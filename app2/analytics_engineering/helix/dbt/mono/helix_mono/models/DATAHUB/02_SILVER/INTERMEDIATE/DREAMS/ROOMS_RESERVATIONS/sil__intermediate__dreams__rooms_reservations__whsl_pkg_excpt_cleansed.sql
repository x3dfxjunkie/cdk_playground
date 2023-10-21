{{
    config(
        materialized='incremental',
        unique_key= ['data_pkg_excpt_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_rooms_reservations', 'whsl_pkg_excpt') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_pkg_excpt_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_pkg_excpt_id
),

-- cleansing the table
renamed as (
    select
        src.data_transact_commit_timestamp as data_transact_commit_timestamp,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        src.data_updt_dts as data_updt_dts,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        src.data_pkg_excpt_id as data_pkg_excpt_id,
        TRIM(src.data_pkg_excpt_typ_nm) as data_pkg_excpt_typ_nm,
        TRIM(src.data_pkg_excpt_sts_nm) as data_pkg_excpt_sts_nm,
        TRIM(src.data_pkg_excpt_st_nm) as data_pkg_excpt_st_nm,
        src.data_tp_id as data_tp_id,
        src.data_tps_id as data_tps_id,
        src.data_tc_grp_nb as data_tc_grp_nb,
        TRIM(src.data_grp_nm) as data_grp_nm,
        TRIM(src.data_grp_cd) as data_grp_cd,
        src.data_pkg_ttl_am as data_pkg_ttl_am,
        TRIM(src.data_pkg_ttl_crncy_cd) as data_pkg_ttl_crncy_cd,
        src.data_chld_cn as data_chld_cn,
        src.data_adlt_cn as data_adlt_cn,
        TRIM(src.data_rm_typ_nm) as data_rm_typ_nm,
        src.data_arvl_dt as data_arvl_dt,
        TRIM(src.data_pkg_cd) as data_pkg_cd,
        TRIM(src.data_guest_lst_nm) as data_guest_lst_nm,
        TRIM(src.data_guest_frst_nm) as data_guest_frst_nm,
        src.data_pkg_excpt_cls_dt as data_pkg_excpt_cls_dt,
        TRIM(src.data_transact_seq) as data_transact_seq,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_transact_commit_timestamp',
            'src.data_create_usr_id_cd',
            'src.data_create_dts',
            'src.data_updt_usr_id_cd',
            'src.data_jdo_seq_nb',
            'src.data_pkg_excpt_typ_nm',
            'src.data_pkg_excpt_sts_nm',
            'src.data_pkg_excpt_st_nm',
            'src.data_tp_id',
            'src.data_tps_id',
            'src.data_tc_grp_nb',
            'src.data_grp_nm',
            'src.data_grp_cd',
            'src.data_pkg_ttl_am',
            'src.data_pkg_ttl_crncy_cd',
            'src.data_chld_cn',
            'src.data_adlt_cn',
            'src.data_rm_typ_nm',
            'src.data_arvl_dt',
            'src.data_pkg_cd',
            'src.data_guest_lst_nm',
            'src.data_guest_frst_nm',
            'src.data_pkg_excpt_cls_dt',
            'src.data_transact_seq',
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
    on src.data_pkg_excpt_id = min_source_update_datetime.data_pkg_excpt_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_pkg_excpt_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final