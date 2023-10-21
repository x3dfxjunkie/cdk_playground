{{
    config(
        materialized='incremental',
        unique_key= ['data_exprnc_band_dsny_prod_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_xbms_wdw', 'exprnc_band_dsny_prod') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_exprnc_band_dsny_prod_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_exprnc_band_dsny_prod_id
),

-- cleansing the table
renamed as (
    select
        src.data_exprnc_band_dsny_prod_id as data_exprnc_band_dsny_prod_id,
        src.data_exprnc_band_typ_id as data_exprnc_band_typ_id,
        src.data_exprnc_band_top_color_id as data_exprnc_band_top_color_id,
        src.data_exprnc_band_bottom_color_id as data_exprnc_band_bottom_color_id,
        TRIM(src.data_exprnc_band_erlst_fflmt_dy_cn) as data_exprnc_band_erlst_fflmt_dy_cn,
        TRIM(src.data_exprnc_band_shipmt_to_rsrt_in) as data_exprnc_band_shipmt_to_rsrt_in,
        src.data_exprnc_band_prod_avail_fr_dts as data_exprnc_band_prod_avail_fr_dts,
        src.data_exprnc_band_prod_avail_to_dts as data_exprnc_band_prod_avail_to_dts,
        TRIM(src.data_create_usr_id) as data_create_usr_id,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id) as data_updt_usr_id,
        src.data_updt_dts as data_updt_dts,
        TRIM(src.data_logical_del_in) as data_logical_del_in,
        TRIM(src.data_avail_to_gst_ord_extnl_part_in) as data_avail_to_gst_ord_extnl_part_in,
        TRIM(src.data_dflt_for_grp_in) as data_dflt_for_grp_in,
        TRIM(src.data_avail_to_reord_extnl_part_in) as data_avail_to_reord_extnl_part_in,
        TRIM(src.data_avail_to_gmr_extnl_part_in) as data_avail_to_gmr_extnl_part_in,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_exprnc_band_typ_id',
            'src.data_exprnc_band_top_color_id',
            'src.data_exprnc_band_bottom_color_id',
            'src.data_exprnc_band_erlst_fflmt_dy_cn',
            'src.data_exprnc_band_shipmt_to_rsrt_in',
            'src.data_exprnc_band_prod_avail_fr_dts',
            'src.data_exprnc_band_prod_avail_to_dts',
            'src.data_create_usr_id',
            'src.data_create_dts',
            'src.data_updt_usr_id',
            'src.data_logical_del_in',
            'src.data_avail_to_gst_ord_extnl_part_in',
            'src.data_dflt_for_grp_in',
            'src.data_avail_to_reord_extnl_part_in',
            'src.data_avail_to_gmr_extnl_part_in',
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
    on src.data_exprnc_band_dsny_prod_id = min_source_update_datetime.data_exprnc_band_dsny_prod_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_exprnc_band_dsny_prod_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final