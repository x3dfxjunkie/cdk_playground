{{
    config(
        materialized='incremental',
        unique_key= ['data_prod_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_price', 'prod_t') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_prod_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_prod_id
),

-- cleansing the table
renamed as (
    select
        src.data_acct_rev_cls_id as data_acct_rev_cls_id,
        TRIM(src.data_dest) as data_dest,
        src.data_entrprs_prod_id as data_entrprs_prod_id,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        src.data_max_adv_purch_day_ct as data_max_adv_purch_day_ct,
        src.data_min_adv_purch_day_ct as data_min_adv_purch_day_ct,
        src.data_offer_idx_nb as data_offer_idx_nb,
        src.data_prge_dts as data_prge_dts,
        src.data_prod_bkng_end_dts as data_prod_bkng_end_dts,
        src.data_prod_bkng_strt_dts as data_prod_bkng_strt_dts,
        TRIM(src.data_prod_cd) as data_prod_cd,
        src.data_prod_cls_id as data_prod_cls_id,
        src.data_prod_create_dts as data_prod_create_dts,
        src.data_prod_di as data_prod_di,
        TRIM(src.data_prod_dt_in) as data_prod_dt_in,
        src.data_prod_exp_dts as data_prod_exp_dts,
        TRIM(src.data_prod_extnl_nm) as data_prod_extnl_nm,
        TRIM(src.data_prod_extrnl_ds) as data_prod_extrnl_ds,
        src.data_prod_id as data_prod_id,
        TRIM(src.data_prod_intrnl_ds) as data_prod_intrnl_ds,
        TRIM(src.data_prod_intrnl_nm) as data_prod_intrnl_nm,
        TRIM(src.data_prod_rsrvbl_in) as data_prod_rsrvbl_in,
        TRIM(src.data_prod_typ_nm) as data_prod_typ_nm,
        src.data_prod_updt_dts as data_prod_updt_dts,
        src.data_prod_usg_end_dts as data_prod_usg_end_dts,
        src.data_prod_usg_strt_dts as data_prod_usg_strt_dts,
        src.data_prod_yr_nb as data_prod_yr_nb,
        TRIM(src.data_sor) as data_sor,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_acct_rev_cls_id',
            'src.data_dest',
            'src.data_entrprs_prod_id',
            'src.data_jdo_seq_nb',
            'src.data_max_adv_purch_day_ct',
            'src.data_min_adv_purch_day_ct',
            'src.data_offer_idx_nb',
            'src.data_prge_dts',
            'src.data_prod_bkng_end_dts',
            'src.data_prod_bkng_strt_dts',
            'src.data_prod_cd',
            'src.data_prod_cls_id',
            'src.data_prod_create_dts',
            'src.data_prod_di',
            'src.data_prod_dt_in',
            'src.data_prod_exp_dts',
            'src.data_prod_extnl_nm',
            'src.data_prod_extrnl_ds',
            'src.data_prod_intrnl_ds',
            'src.data_prod_intrnl_nm',
            'src.data_prod_rsrvbl_in',
            'src.data_prod_typ_nm',
            'src.data_prod_updt_dts',
            'src.data_prod_usg_end_dts',
            'src.data_prod_usg_strt_dts',
            'src.data_prod_yr_nb',
            'src.data_sor',
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
    on src.data_prod_id = min_source_update_datetime.data_prod_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_prod_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final