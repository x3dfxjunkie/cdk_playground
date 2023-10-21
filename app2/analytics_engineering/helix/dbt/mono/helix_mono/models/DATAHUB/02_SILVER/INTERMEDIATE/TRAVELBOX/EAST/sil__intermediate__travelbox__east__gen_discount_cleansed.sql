{{
    config(
        materialized='incremental',
        unique_key= ['data_contract_id', 'data_discount_no','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'gen_discount') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_contract_id,
        data_discount_no,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_contract_id,
        data_discount_no
),

-- cleansing the table
renamed as (
    select
        src.data_history_id as data_history_id,
        TRIM(src.data_advanced_view) as data_advanced_view,
        src.data_discount_calculation_order as data_discount_calculation_order,
        src.data_pass_percentage as data_pass_percentage,
        src.data_min_days as data_min_days,
        src.data_search_type as data_search_type,
        src.data_stay_from as data_stay_from,
        src.data_stay_to as data_stay_to,
        TRIM(src.data_stay_days) as data_stay_days,
        src.data_payment_scheme as data_payment_scheme,
        src.data_cnx_scheme as data_cnx_scheme,
        src.data_amd_scheme as data_amd_scheme,
        TRIM(src.data_booked_from_to) as data_booked_from_to,
        TRIM(src.data_commissionable) as data_commissionable,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_price_only) as data_price_only,
        TRIM(src.data_category_all_select) as data_category_all_select,
        src.data_contract_id as data_contract_id,
        TRIM(src.data_type) as data_type,
        src.data_discount_no as data_discount_no,
        TRIM(src.data_reference) as data_reference,
        TRIM(src.data_description) as data_description,
        src.data_booked_from as data_booked_from,
        src.data_booked_to as data_booked_to,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_history_id',
            'src.data_advanced_view',
            'src.data_discount_calculation_order',
            'src.data_pass_percentage',
            'src.data_min_days',
            'src.data_search_type',
            'src.data_stay_from',
            'src.data_stay_to',
            'src.data_stay_days',
            'src.data_payment_scheme',
            'src.data_cnx_scheme',
            'src.data_amd_scheme',
            'src.data_booked_from_to',
            'src.data_commissionable',
            'src.data_last_modified_time',
            'src.data_price_only',
            'src.data_category_all_select',
            'src.data_type',
            'src.data_reference',
            'src.data_description',
            'src.data_booked_from',
            'src.data_booked_to',
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
    on src.data_contract_id = min_source_update_datetime.data_contract_id
    and src.data_discount_no = min_source_update_datetime.data_discount_no
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_contract_id, data_discount_no, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final