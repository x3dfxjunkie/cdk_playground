{{
    config(
        materialized='incremental',
        unique_key= ['data_contract_id', 'data_fare_no', 'data_room_apt_no','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'acc_fare') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_contract_id,
        data_fare_no,
        data_room_apt_no,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_contract_id,
        data_fare_no,
        data_room_apt_no
),

-- cleansing the table
renamed as (
    select
        src.data_contract_id as data_contract_id,
        src.data_room_apt_no as data_room_apt_no,
        src.data_fare_no as data_fare_no,
        TRIM(src.data_nett_rate) as data_nett_rate,
        src.data_season as data_season,
        TRIM(src.data_days) as data_days,
        src.data_nights as data_nights,
        TRIM(src.data_currency) as data_currency,
        src.data_single_fare as data_single_fare,
        src.data_twin_fare as data_twin_fare,
        src.data_unit_fare as data_unit_fare,
        src.data_extrabed_fare as data_extrabed_fare,
        src.data_teen_fare as data_teen_fare,
        src.data_child_fare as data_child_fare,
        src.data_infant_fare as data_infant_fare,
        src.data_foc_contract as data_foc_contract,
        src.data_foc_no as data_foc_no,
        src.data_child2_fare as data_child2_fare,
        src.data_teen2_fare as data_teen2_fare,
        src.data_child3_fare as data_child3_fare,
        src.data_child4_fare as data_child4_fare,
        src.data_child5_fare as data_child5_fare,
        src.data_single2_fare as data_single2_fare,
        src.data_twin2_fare as data_twin2_fare,
        src.data_extrabed2_fare as data_extrabed2_fare,
        src.data_min_pax as data_min_pax,
        src.data_max_pax as data_max_pax,
        src.data_last_modified_time as data_last_modified_time,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_nett_rate',
            'src.data_season',
            'src.data_days',
            'src.data_nights',
            'src.data_currency',
            'src.data_single_fare',
            'src.data_twin_fare',
            'src.data_unit_fare',
            'src.data_extrabed_fare',
            'src.data_teen_fare',
            'src.data_child_fare',
            'src.data_infant_fare',
            'src.data_foc_contract',
            'src.data_foc_no',
            'src.data_child2_fare',
            'src.data_teen2_fare',
            'src.data_child3_fare',
            'src.data_child4_fare',
            'src.data_child5_fare',
            'src.data_single2_fare',
            'src.data_twin2_fare',
            'src.data_extrabed2_fare',
            'src.data_min_pax',
            'src.data_max_pax',
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
    on src.data_contract_id = min_source_update_datetime.data_contract_id
    and src.data_fare_no = min_source_update_datetime.data_fare_no
    and src.data_room_apt_no = min_source_update_datetime.data_room_apt_no
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_contract_id, data_fare_no, data_room_apt_no, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final