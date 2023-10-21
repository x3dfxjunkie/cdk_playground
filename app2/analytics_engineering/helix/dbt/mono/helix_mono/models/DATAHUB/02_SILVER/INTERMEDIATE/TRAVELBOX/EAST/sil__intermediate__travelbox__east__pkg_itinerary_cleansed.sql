{{
    config(
        materialized='incremental',
        unique_key= ['data_itinerary_no', 'data_package_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'pkg_itinerary') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_itinerary_no,
        data_package_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_itinerary_no,
        data_package_id
),

-- cleansing the table
renamed as (
    select
        src.data_set_no as data_set_no,
        TRIM(src.data_hotel_code) as data_hotel_code,
        src.data_last_modified_time as data_last_modified_time,
        src.data_hotel_element_no as data_hotel_element_no,
        src.data_max_bkg_to_dep_days as data_max_bkg_to_dep_days,
        src.data_package_id as data_package_id,
        src.data_itinerary_no as data_itinerary_no,
        TRIM(src.data_code) as data_code,
        TRIM(src.data_name) as data_name,
        src.data_nights as data_nights,
        src.data_status as data_status,
        src.data_stage as data_stage,
        src.data_average_margin as data_average_margin,
        TRIM(src.data_stage_reason) as data_stage_reason,
        TRIM(src.data_extra_stays_only) as data_extra_stays_only,
        TRIM(src.data_package_stage) as data_package_stage,
        src.data_min_pax as data_min_pax,
        src.data_max_pax as data_max_pax,
        TRIM(src.data_variation_code) as data_variation_code,
        src.data_variation_no as data_variation_no,
        TRIM(src.data_dest_city_code) as data_dest_city_code,
        TRIM(src.data_commission_override) as data_commission_override,
        TRIM(src.data_threshold) as data_threshold,
        src.data_commission as data_commission,
        src.data_calc_pax_base as data_calc_pax_base,
        TRIM(src.data_dep_date_exist) as data_dep_date_exist,
        TRIM(src.data_push_sales_exist) as data_push_sales_exist,
        TRIM(src.data_special_offer_exist) as data_special_offer_exist,
        TRIM(src.data_blackout_exist) as data_blackout_exist,
        TRIM(src.data_ebr_discount_exist) as data_ebr_discount_exist,
        TRIM(src.data_visa_exist) as data_visa_exist,
        TRIM(src.data_cms_code) as data_cms_code,
        TRIM(src.data_iti_dest_city) as data_iti_dest_city,
        TRIM(src.data_country) as data_country,
        TRIM(src.data_tour_region) as data_tour_region,
        src.data_supplier_id as data_supplier_id,
        src.data_centers as data_centers,
        TRIM(src.data_resort) as data_resort,
        src.data_min_bkg_to_dep_days as data_min_bkg_to_dep_days,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_set_no',
            'src.data_hotel_code',
            'src.data_last_modified_time',
            'src.data_hotel_element_no',
            'src.data_max_bkg_to_dep_days',
            'src.data_code',
            'src.data_name',
            'src.data_nights',
            'src.data_status',
            'src.data_stage',
            'src.data_average_margin',
            'src.data_stage_reason',
            'src.data_extra_stays_only',
            'src.data_package_stage',
            'src.data_min_pax',
            'src.data_max_pax',
            'src.data_variation_code',
            'src.data_variation_no',
            'src.data_dest_city_code',
            'src.data_commission_override',
            'src.data_threshold',
            'src.data_commission',
            'src.data_calc_pax_base',
            'src.data_dep_date_exist',
            'src.data_push_sales_exist',
            'src.data_special_offer_exist',
            'src.data_blackout_exist',
            'src.data_ebr_discount_exist',
            'src.data_visa_exist',
            'src.data_cms_code',
            'src.data_iti_dest_city',
            'src.data_country',
            'src.data_tour_region',
            'src.data_supplier_id',
            'src.data_centers',
            'src.data_resort',
            'src.data_min_bkg_to_dep_days',
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
    on src.data_itinerary_no = min_source_update_datetime.data_itinerary_no
    and src.data_package_id = min_source_update_datetime.data_package_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_itinerary_no, data_package_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final