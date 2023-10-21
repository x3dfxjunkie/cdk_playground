{{
    config(
        materialized='incremental',
        unique_key= ['data_code','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'fee_type') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_code,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_code
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_code) as data_code,
        TRIM(src.data_name) as data_name,
        TRIM(src.data_commissionable) as data_commissionable,
        TRIM(src.data_auto) as data_auto,
        TRIM(src.data_itemwise) as data_itemwise,
        TRIM(src.data_amtwise) as data_amtwise,
        TRIM(src.data_taxable) as data_taxable,
        src.data_days2_dept as data_days2_dept,
        TRIM(src.data_per_person) as data_per_person,
        TRIM(src.data_client_type) as data_client_type,
        TRIM(src.data_dist_channel) as data_dist_channel,
        src.data_bookings_from as data_bookings_from,
        src.data_bookings_to as data_bookings_to,
        TRIM(src.data_var_commisn) as data_var_commisn,
        TRIM(src.data_reversible) as data_reversible,
        src.data_travel_start_date as data_travel_start_date,
        src.data_travel_end_date as data_travel_end_date,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_name',
            'src.data_commissionable',
            'src.data_auto',
            'src.data_itemwise',
            'src.data_amtwise',
            'src.data_taxable',
            'src.data_days2_dept',
            'src.data_per_person',
            'src.data_client_type',
            'src.data_dist_channel',
            'src.data_bookings_from',
            'src.data_bookings_to',
            'src.data_var_commisn',
            'src.data_reversible',
            'src.data_travel_start_date',
            'src.data_travel_end_date',
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
    on src.data_code = min_source_update_datetime.data_code
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_code, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final