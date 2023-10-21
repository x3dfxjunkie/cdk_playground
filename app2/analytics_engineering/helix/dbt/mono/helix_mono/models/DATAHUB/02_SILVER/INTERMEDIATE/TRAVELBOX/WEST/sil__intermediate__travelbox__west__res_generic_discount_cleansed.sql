{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_discount_no', 'data_item_no', 'data_product_code','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'res_generic_discount') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_booking_id,
        data_discount_no,
        data_item_no,
        data_product_code,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_discount_no,
        data_item_no,
        data_product_code
),

-- cleansing the table
renamed as (
    select
        src.data_booking_id as data_booking_id,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        src.data_discount_no as data_discount_no,
        TRIM(src.data_reference) as data_reference,
        TRIM(src.data_description) as data_description,
        src.data_net_adult as data_net_adult,
        src.data_gross_adult as data_gross_adult,
        src.data_gross_child as data_gross_child,
        src.data_gross_infant as data_gross_infant,
        src.data_net_child as data_net_child,
        src.data_net_infant as data_net_infant,
        src.data_payment_scheme as data_payment_scheme,
        src.data_cnx_scheme as data_cnx_scheme,
        src.data_amd_scheme as data_amd_scheme,
        TRIM(src.data_commissionable) as data_commissionable,
        src.data_non_paying_pax as data_non_paying_pax,
        src.data_ancillary_pax as data_ancillary_pax,
        TRIM(src.data_manually_added) as data_manually_added,
        src.data_last_modified_time as data_last_modified_time,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_reference',
            'src.data_description',
            'src.data_net_adult',
            'src.data_gross_adult',
            'src.data_gross_child',
            'src.data_gross_infant',
            'src.data_net_child',
            'src.data_net_infant',
            'src.data_payment_scheme',
            'src.data_cnx_scheme',
            'src.data_amd_scheme',
            'src.data_commissionable',
            'src.data_non_paying_pax',
            'src.data_ancillary_pax',
            'src.data_manually_added',
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
    and src.data_discount_no = min_source_update_datetime.data_discount_no
    and src.data_item_no = min_source_update_datetime.data_item_no
    and src.data_product_code = min_source_update_datetime.data_product_code
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_discount_no, data_item_no, data_product_code, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final