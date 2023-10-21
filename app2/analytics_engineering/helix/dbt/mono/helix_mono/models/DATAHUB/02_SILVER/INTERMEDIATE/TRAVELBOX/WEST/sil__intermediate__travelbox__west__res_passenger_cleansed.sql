{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_passenger_no','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'res_passenger') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_booking_id,
        data_passenger_no,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_passenger_no
),

-- cleansing the table
renamed as (
    select
        src.data_booking_id as data_booking_id,
        src.data_per_person_price as data_per_person_price,
        TRIM(src.data_primary_pp_for_booking) as data_primary_pp_for_booking,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_eligible_insurance) as data_eligible_insurance,
        TRIM(src.data_travel_status) as data_travel_status,
        src.data_passenger_no as data_passenger_no,
        src.data_profile_id as data_profile_id,
        TRIM(src.data_type) as data_type,
        TRIM(src.data_lead) as data_lead,
        TRIM(src.data_note) as data_note,
        src.data_per_person_tax as data_per_person_tax,
        TRIM(src.data_active_for_booking) as data_active_for_booking,
        TRIM(src.data_assistance) as data_assistance,
        TRIM(src.data_record_med_cond) as data_record_med_cond,
        TRIM(src.data_critical_med_condition) as data_critical_med_condition,
        TRIM(src.data_third_party_insurance) as data_third_party_insurance,
        TRIM(src.data_optional_insurance) as data_optional_insurance,
        TRIM(src.data_send_visa_app_to_lead) as data_send_visa_app_to_lead,
        TRIM(src.data_sub_type) as data_sub_type,
        TRIM(src.data_refuse_insurance) as data_refuse_insurance,
        TRIM(src.data_passenger_category) as data_passenger_category,
        TRIM(src.data_first_night_street) as data_first_night_street,
        TRIM(src.data_first_night_country) as data_first_night_country,
        TRIM(src.data_first_night_state) as data_first_night_state,
        TRIM(src.data_first_night_city) as data_first_night_city,
        TRIM(src.data_first_night_post_code) as data_first_night_post_code,
        TRIM(src.data_endorsed_pp_for_booking) as data_endorsed_pp_for_booking,
        src.data_endorsed_passenger_no as data_endorsed_passenger_no,
        TRIM(src.data_visa_req) as data_visa_req,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_per_person_price',
            'src.data_primary_pp_for_booking',
            'src.data_last_modified_time',
            'src.data_eligible_insurance',
            'src.data_travel_status',
            'src.data_profile_id',
            'src.data_type',
            'src.data_lead',
            'src.data_note',
            'src.data_per_person_tax',
            'src.data_active_for_booking',
            'src.data_assistance',
            'src.data_record_med_cond',
            'src.data_critical_med_condition',
            'src.data_third_party_insurance',
            'src.data_optional_insurance',
            'src.data_send_visa_app_to_lead',
            'src.data_sub_type',
            'src.data_refuse_insurance',
            'src.data_passenger_category',
            'src.data_first_night_street',
            'src.data_first_night_country',
            'src.data_first_night_state',
            'src.data_first_night_city',
            'src.data_first_night_post_code',
            'src.data_endorsed_pp_for_booking',
            'src.data_endorsed_passenger_no',
            'src.data_visa_req',
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
    and src.data_passenger_no = min_source_update_datetime.data_passenger_no
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_passenger_no, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final