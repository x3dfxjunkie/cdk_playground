{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_item_no', 'data_product_code', 'data_room_no','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_east', 'res_accom_room') }}

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
        data_room_no,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_item_no,
        data_product_code,
        data_room_no
),

-- cleansing the table
renamed as (
    select
        src.data_booking_id as data_booking_id,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        src.data_room_no as data_room_no,
        TRIM(src.data_room_type) as data_room_type,
        src.data_allocation_contract as data_allocation_contract,
        src.data_contract_id as data_contract_id,
        src.data_adult as data_adult,
        src.data_child as data_child,
        src.data_infant as data_infant,
        src.data_cost as data_cost,
        src.data_price as data_price,
        src.data_rooms as data_rooms,
        src.data_discount as data_discount,
        src.data_adult_cost as data_adult_cost,
        src.data_child_cost as data_child_cost,
        src.data_infant_cost as data_infant_cost,
        src.data_adult_price as data_adult_price,
        src.data_child_price as data_child_price,
        src.data_infant_price as data_infant_price,
        src.data_allot_group_no as data_allot_group_no,
        TRIM(src.data_on_request) as data_on_request,
        src.data_pppn_adult_price as data_pppn_adult_price,
        src.data_pppn_child_price as data_pppn_child_price,
        src.data_pppn_infant_price as data_pppn_infant_price,
        src.data_pppn_adult_cost as data_pppn_adult_cost,
        src.data_pppn_child_cost as data_pppn_child_cost,
        src.data_pppn_infant_cost as data_pppn_infant_cost,
        TRIM(src.data_bedding) as data_bedding,
        TRIM(src.data_occupancy_code) as data_occupancy_code,
        TRIM(src.data_markup_ref) as data_markup_ref,
        src.data_availability_type as data_availability_type,
        src.data_non_paying_pax as data_non_paying_pax,
        src.data_ancillary_pax as data_ancillary_pax,
        TRIM(src.data_manually_added) as data_manually_added,
        src.data_unit_cost as data_unit_cost,
        src.data_unit_price as data_unit_price,
        src.data_adt_manual_override_price as data_adt_manual_override_price,
        src.data_chd_manual_override_price as data_chd_manual_override_price,
        src.data_inf_manual_override_price as data_inf_manual_override_price,
        src.data_adt_manual_override_cost as data_adt_manual_override_cost,
        src.data_chd_manual_override_cost as data_chd_manual_override_cost,
        src.data_inf_manual_override_cost as data_inf_manual_override_cost,
        TRIM(src.data_special_rate_applied) as data_special_rate_applied,
        src.data_last_modified_time as data_last_modified_time,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_room_type',
            'src.data_allocation_contract',
            'src.data_contract_id',
            'src.data_adult',
            'src.data_child',
            'src.data_infant',
            'src.data_cost',
            'src.data_price',
            'src.data_rooms',
            'src.data_discount',
            'src.data_adult_cost',
            'src.data_child_cost',
            'src.data_infant_cost',
            'src.data_adult_price',
            'src.data_child_price',
            'src.data_infant_price',
            'src.data_allot_group_no',
            'src.data_on_request',
            'src.data_pppn_adult_price',
            'src.data_pppn_child_price',
            'src.data_pppn_infant_price',
            'src.data_pppn_adult_cost',
            'src.data_pppn_child_cost',
            'src.data_pppn_infant_cost',
            'src.data_bedding',
            'src.data_occupancy_code',
            'src.data_markup_ref',
            'src.data_availability_type',
            'src.data_non_paying_pax',
            'src.data_ancillary_pax',
            'src.data_manually_added',
            'src.data_unit_cost',
            'src.data_unit_price',
            'src.data_adt_manual_override_price',
            'src.data_chd_manual_override_price',
            'src.data_inf_manual_override_price',
            'src.data_adt_manual_override_cost',
            'src.data_chd_manual_override_cost',
            'src.data_inf_manual_override_cost',
            'src.data_special_rate_applied',
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
    and src.data_room_no = min_source_update_datetime.data_room_no
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_item_no, data_product_code, data_room_no, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final