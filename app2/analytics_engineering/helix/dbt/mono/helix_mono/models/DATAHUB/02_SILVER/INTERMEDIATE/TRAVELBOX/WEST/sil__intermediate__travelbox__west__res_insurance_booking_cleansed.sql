{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_item_no', 'data_product_code','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'res_insurance_booking') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_booking_id,
        data_item_no,
        data_product_code,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_item_no,
        data_product_code
),

-- cleansing the table
renamed as (
    select
        src.data_original_book_date as data_original_book_date,
        src.data_booking_id as data_booking_id,
        src.data_item_no as data_item_no,
        TRIM(src.data_product_code) as data_product_code,
        TRIM(src.data_policy_code) as data_policy_code,
        TRIM(src.data_family) as data_family,
        TRIM(src.data_annual) as data_annual,
        src.data_seniors as data_seniors,
        src.data_tax as data_tax,
        src.data_region_group_no as data_region_group_no,
        src.data_min_duration as data_min_duration,
        src.data_max_duration as data_max_duration,
        src.data_min_price as data_min_price,
        src.data_max_price as data_max_price,
        TRIM(src.data_valid_products) as data_valid_products,
        TRIM(src.data_air_only) as data_air_only,
        src.data_senior_adult as data_senior_adult,
        TRIM(src.data_policy_name) as data_policy_name,
        src.data_last_modified_time as data_last_modified_time,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_original_book_date',
            'src.data_policy_code',
            'src.data_family',
            'src.data_annual',
            'src.data_seniors',
            'src.data_tax',
            'src.data_region_group_no',
            'src.data_min_duration',
            'src.data_max_duration',
            'src.data_min_price',
            'src.data_max_price',
            'src.data_valid_products',
            'src.data_air_only',
            'src.data_senior_adult',
            'src.data_policy_name',
            'src.data_last_modified_time',
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
    on src.data_booking_id = min_source_update_datetime.data_booking_id
    and src.data_item_no = min_source_update_datetime.data_item_no
    and src.data_product_code = min_source_update_datetime.data_product_code
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_item_no, data_product_code, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final