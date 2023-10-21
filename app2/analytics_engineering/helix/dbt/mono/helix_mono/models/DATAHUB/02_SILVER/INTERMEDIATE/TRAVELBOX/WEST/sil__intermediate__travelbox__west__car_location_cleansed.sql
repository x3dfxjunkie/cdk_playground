{{
    config(
        materialized='incremental',
        unique_key= ['data_location_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'car_location') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_location_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_location_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_web_enable) as data_web_enable,
        src.data_destination_id as data_destination_id,
        src.data_h2_h_id as data_h2_h_id,
        src.data_created_by as data_created_by,
        src.data_created_on as data_created_on,
        src.data_modified_by as data_modified_by,
        src.data_verified_by as data_verified_by,
        src.data_verified_on as data_verified_on,
        src.data_imported_by as data_imported_by,
        src.data_imported_on as data_imported_on,
        TRIM(src.data_operator) as data_operator,
        TRIM(src.data_location_group_code) as data_location_group_code,
        src.data_location_id as data_location_id,
        src.data_supplier_id as data_supplier_id,
        TRIM(src.data_location_type) as data_location_type,
        TRIM(src.data_code) as data_code,
        TRIM(src.data_name) as data_name,
        TRIM(src.data_address) as data_address,
        TRIM(src.data_city) as data_city,
        TRIM(src.data_state) as data_state,
        TRIM(src.data_zip_code) as data_zip_code,
        TRIM(src.data_country) as data_country,
        TRIM(src.data_region) as data_region,
        TRIM(src.data_phone) as data_phone,
        TRIM(src.data_fax) as data_fax,
        TRIM(src.data_email) as data_email,
        TRIM(src.data_seasonal_opening) as data_seasonal_opening,
        TRIM(src.data_image_path) as data_image_path,
        src.data_image_width as data_image_width,
        src.data_image_height as data_image_height,
        TRIM(src.data_currency) as data_currency,
        src.data_out_of_hour_charge as data_out_of_hour_charge,
        src.data_errata_group as data_errata_group,
        TRIM(src.data_pickup_procedure) as data_pickup_procedure,
        TRIM(src.data_dropoff_procedure) as data_dropoff_procedure,
        TRIM(src.data_default_location) as data_default_location,
        TRIM(src.data_latitude) as data_latitude,
        TRIM(src.data_longitude) as data_longitude,
        TRIM(src.data_airport) as data_airport,
        src.data_modified_on as data_modified_on,
        TRIM(src.data_active) as data_active,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_web_enable',
            'src.data_destination_id',
            'src.data_h2_h_id',
            'src.data_created_by',
            'src.data_created_on',
            'src.data_modified_by',
            'src.data_verified_by',
            'src.data_verified_on',
            'src.data_imported_by',
            'src.data_imported_on',
            'src.data_operator',
            'src.data_location_group_code',
            'src.data_supplier_id',
            'src.data_location_type',
            'src.data_code',
            'src.data_name',
            'src.data_address',
            'src.data_city',
            'src.data_state',
            'src.data_zip_code',
            'src.data_country',
            'src.data_region',
            'src.data_phone',
            'src.data_fax',
            'src.data_email',
            'src.data_seasonal_opening',
            'src.data_image_path',
            'src.data_image_width',
            'src.data_image_height',
            'src.data_currency',
            'src.data_out_of_hour_charge',
            'src.data_errata_group',
            'src.data_pickup_procedure',
            'src.data_dropoff_procedure',
            'src.data_default_location',
            'src.data_latitude',
            'src.data_longitude',
            'src.data_airport',
            'src.data_modified_on',
            'src.data_active',
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
    on src.data_location_id = min_source_update_datetime.data_location_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_location_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final