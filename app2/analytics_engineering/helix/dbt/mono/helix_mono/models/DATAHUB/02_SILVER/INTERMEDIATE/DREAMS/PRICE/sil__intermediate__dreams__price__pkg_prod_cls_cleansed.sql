{{
    config(
        materialized='incremental',
        unique_key= ['data_pkg_prod_cls_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_price', 'pkg_prod_cls') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_pkg_prod_cls_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_pkg_prod_cls_id
),

-- cleansing the table
renamed as (
    select
        src.data_glb_sqnc_rowid as data_glb_sqnc_rowid,
        TRIM(src.data_cmd) as data_cmd,
        src.data_prttn_dt as data_prttn_dt,
        TRIM(src.data_scn) as data_scn,
        TRIM(src.data_edtn_nm) as data_edtn_nm,
        src.data_etl_dts_dpp as data_etl_dts_dpp,
        src.data_dc_dts as data_dc_dts,
        src.data_pkg_prod_cls_id as data_pkg_prod_cls_id,
        src.data_pkg_id as data_pkg_id,
        TRIM(src.data_enttl_frq_nm) as data_enttl_frq_nm,
        TRIM(src.data_enttl_meth_nm) as data_enttl_meth_nm,
        src.data_prod_cls_id as data_prod_cls_id,
        TRIM(src.data_pkg_prod_cls_slct_in) as data_pkg_prod_cls_slct_in,
        TRIM(src.data_pkg_prod_cls_opt_in) as data_pkg_prod_cls_opt_in,
        src.data_pkg_prod_cls_cn as data_pkg_prod_cls_cn,
        src.data_pkg_prod_cls_min_nb as data_pkg_prod_cls_min_nb,
        src.data_pkg_prod_cls_max_nb as data_pkg_prod_cls_max_nb,
        src.data_create_dts as data_create_dts,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        src.data_jdo_cls_nb as data_jdo_cls_nb,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        src.data_prge_dts as data_prge_dts,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_glb_sqnc_rowid',
            'src.data_cmd',
            'src.data_prttn_dt',
            'src.data_scn',
            'src.data_edtn_nm',
            'src.data_etl_dts_dpp',
            'src.data_dc_dts',
            'src.data_pkg_id',
            'src.data_enttl_frq_nm',
            'src.data_enttl_meth_nm',
            'src.data_prod_cls_id',
            'src.data_pkg_prod_cls_slct_in',
            'src.data_pkg_prod_cls_opt_in',
            'src.data_pkg_prod_cls_cn',
            'src.data_pkg_prod_cls_min_nb',
            'src.data_pkg_prod_cls_max_nb',
            'src.data_create_dts',
            'src.data_create_usr_id_cd',
            'src.data_updt_usr_id_cd',
            'src.data_jdo_cls_nb',
            'src.data_jdo_seq_nb',
            'src.data_prge_dts',
            'src.dms_operation']) }} as metadata_checksum,
        metadata_timestamp,
        metadata_record_type,
        metadata_operation,
        metadata_partition_key_type,
        metadata_schema_name,
        metadata_table_name,
        metadata_transaction_id,
        SYSDATE() as metadata_insert_datetime,
        '{{ env_var('DBT_SYNTHETIC_ID', "dbt") }}' as metadata_batch_user,
        landing_id,
        landing_file_name,
        landing_file_row_number,
        landing_file_last_modified,
        landing_timestamp

    from source src
    inner join min_source_update_datetime
    on src.data_pkg_prod_cls_id = min_source_update_datetime.data_pkg_prod_cls_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_pkg_prod_cls_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final