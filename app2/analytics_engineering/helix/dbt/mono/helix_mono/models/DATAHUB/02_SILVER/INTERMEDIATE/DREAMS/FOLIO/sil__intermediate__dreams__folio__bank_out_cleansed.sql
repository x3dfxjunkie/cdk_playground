{{
    config(
        materialized='incremental',
        unique_key= ['data_bank_out_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_dreams_folio', 'bank_out') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_bank_out_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_bank_out_id
),

-- cleansing the table
renamed as (
    select
        src.data_bank_out_id as data_bank_out_id,
        TRIM(src.data_bank_out_typ_nm) as data_bank_out_typ_nm,
        src.data_bank_in_id as data_bank_in_id,
        src.data_bank_out_acct_dt as data_bank_out_acct_dt,
        TRIM(src.data_dpst_bag_id) as data_dpst_bag_id,
        src.data_bank_out_dts as data_bank_out_dts,
        src.data_bank_out_comp_dts as data_bank_out_comp_dts,
        src.data_rgstr_am as data_rgstr_am,
        TRIM(src.data_rgstr_crncy_cd) as data_rgstr_crncy_cd,
        src.data_tot_cash_am as data_tot_cash_am,
        TRIM(src.data_tot_csh_crncy_cd) as data_tot_csh_crncy_cd,
        src.data_tot_non_csh_am as data_tot_non_csh_am,
        TRIM(src.data_tot_non_csh_crncy_cd) as data_tot_non_csh_crncy_cd,
        src.data_tot_edc_am as data_tot_edc_am,
        TRIM(src.data_tot_edc_crncy_cd) as data_tot_edc_crncy_cd,
        TRIM(src.data_create_usr_id_cd) as data_create_usr_id_cd,
        src.data_create_dts as data_create_dts,
        TRIM(src.data_updt_usr_id_cd) as data_updt_usr_id_cd,
        src.data_updt_dts as data_updt_dts,
        src.data_jdo_seq_nb as data_jdo_seq_nb,
        src.data_prge_dts as data_prge_dts,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_bank_out_typ_nm',
            'src.data_bank_in_id',
            'src.data_bank_out_acct_dt',
            'src.data_dpst_bag_id',
            'src.data_bank_out_dts',
            'src.data_bank_out_comp_dts',
            'src.data_rgstr_am',
            'src.data_rgstr_crncy_cd',
            'src.data_tot_cash_am',
            'src.data_tot_csh_crncy_cd',
            'src.data_tot_non_csh_am',
            'src.data_tot_non_csh_crncy_cd',
            'src.data_tot_edc_am',
            'src.data_tot_edc_crncy_cd',
            'src.data_create_usr_id_cd',
            'src.data_create_dts',
            'src.data_updt_usr_id_cd',
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
    on src.data_bank_out_id = min_source_update_datetime.data_bank_out_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_bank_out_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final