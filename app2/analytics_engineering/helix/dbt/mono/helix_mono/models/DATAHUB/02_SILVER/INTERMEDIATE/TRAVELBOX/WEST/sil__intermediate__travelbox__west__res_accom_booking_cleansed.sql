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
    from {{ source('brz_travelbox_west', 'res_accom_booking') }}

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
        src.data_last_modified_time as data_last_modified_time,
        src.data_ext_reservation_id as data_ext_reservation_id,
        TRIM(src.data_location) as data_location,
        src.data_ec_cost as data_ec_cost,
        src.data_lc_cost as data_lc_cost,
        TRIM(src.data_valid_for_reprice) as data_valid_for_reprice,
        TRIM(src.data_accom_type) as data_accom_type,
        src.data_min_combinable_hotel as data_min_combinable_hotel,
        TRIM(src.data_hotel_address) as data_hotel_address,
        src.data_max_release_day as data_max_release_day,
        src.data_h2_h_price_diff as data_h2_h_price_diff,
        TRIM(src.data_non_refundable) as data_non_refundable,
        src.data_supplement_category_id as data_supplement_category_id,
        src.data_booking_id as data_booking_id,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        src.data_reservation_id as data_reservation_id,
        src.data_accom_id as data_accom_id,
        src.data_nights as data_nights,
        src.data_joined_contract_id as data_joined_contract_id,
        TRIM(src.data_foreign_accom_id) as data_foreign_accom_id,
        TRIM(src.data_special_requests) as data_special_requests,
        TRIM(src.data_hotel_name) as data_hotel_name,
        TRIM(src.data_star_rating) as data_star_rating,
        TRIM(src.data_early_checkin) as data_early_checkin,
        TRIM(src.data_late_checkout) as data_late_checkout,
        src.data_ec_price as data_ec_price,
        src.data_lc_price as data_lc_price,
        src.data_ext_night_price as data_ext_night_price,
        src.data_ec_time as data_ec_time,
        src.data_lc_time as data_lc_time,
        src.data_multihire_no as data_multihire_no,
        TRIM(src.data_meal_scheme) as data_meal_scheme,
        src.data_pre_post_supplier as data_pre_post_supplier,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_last_modified_time',
            'src.data_ext_reservation_id',
            'src.data_location',
            'src.data_ec_cost',
            'src.data_lc_cost',
            'src.data_valid_for_reprice',
            'src.data_accom_type',
            'src.data_min_combinable_hotel',
            'src.data_hotel_address',
            'src.data_max_release_day',
            'src.data_h2_h_price_diff',
            'src.data_non_refundable',
            'src.data_supplement_category_id',
            'src.data_reservation_id',
            'src.data_accom_id',
            'src.data_nights',
            'src.data_joined_contract_id',
            'src.data_foreign_accom_id',
            'src.data_special_requests',
            'src.data_hotel_name',
            'src.data_star_rating',
            'src.data_early_checkin',
            'src.data_late_checkout',
            'src.data_ec_price',
            'src.data_lc_price',
            'src.data_ext_night_price',
            'src.data_ec_time',
            'src.data_lc_time',
            'src.data_multihire_no',
            'src.data_meal_scheme',
            'src.data_pre_post_supplier',
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