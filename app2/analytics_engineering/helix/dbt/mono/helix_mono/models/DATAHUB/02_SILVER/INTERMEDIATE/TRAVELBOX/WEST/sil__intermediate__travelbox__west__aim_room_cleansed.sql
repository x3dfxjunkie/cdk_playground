{{
    config(
        materialized='incremental',
        unique_key= ['data_code', 'data_supplier_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'aim_room') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_code,
        data_supplier_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_code,
        data_supplier_id
),

-- cleansing the table
renamed as (
    select
        src.data_last_modified_timestamp as data_last_modified_timestamp,
        TRIM(src.data_short_name) as data_short_name,
        TRIM(src.data_inherit_price) as data_inherit_price,
        TRIM(src.data_costing_board_basis) as data_costing_board_basis,
        TRIM(src.data_import_contract) as data_import_contract,
        TRIM(src.data_limited_inventory) as data_limited_inventory,
        TRIM(src.data_rate_category_group) as data_rate_category_group,
        TRIM(src.data_code) as data_code,
        TRIM(src.data_ext_system_code) as data_ext_system_code,
        src.data_supplier_id as data_supplier_id,
        TRIM(src.data_name) as data_name,
        TRIM(src.data_base_room_code) as data_base_room_code,
        TRIM(src.data_accessible_room_ind) as data_accessible_room_ind,
        TRIM(src.data_virtual_room_ind) as data_virtual_room_ind,
        TRIM(src.data_base_room_ind) as data_base_room_ind,
        TRIM(src.data_bedding_type) as data_bedding_type,
        TRIM(src.data_room_category) as data_room_category,
        src.data_min_occ as data_min_occ,
        src.data_max_occ as data_max_occ,
        src.data_std_occ as data_std_occ,
        src.data_effective_start_date as data_effective_start_date,
        src.data_effective_end_date as data_effective_end_date,
        src.data_sequence_no as data_sequence_no,
        TRIM(src.data_description) as data_description,
        src.data_created_date as data_created_date,
        src.data_last_modified_date as data_last_modified_date,
        TRIM(src.data_created_user) as data_created_user,
        TRIM(src.data_last_modified_user) as data_last_modified_user,
        TRIM(src.data_occupancy_type) as data_occupancy_type,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_last_modified_timestamp',
            'src.data_short_name',
            'src.data_inherit_price',
            'src.data_costing_board_basis',
            'src.data_import_contract',
            'src.data_limited_inventory',
            'src.data_rate_category_group',
            'src.data_ext_system_code',
            'src.data_name',
            'src.data_base_room_code',
            'src.data_accessible_room_ind',
            'src.data_virtual_room_ind',
            'src.data_base_room_ind',
            'src.data_bedding_type',
            'src.data_room_category',
            'src.data_min_occ',
            'src.data_max_occ',
            'src.data_std_occ',
            'src.data_effective_start_date',
            'src.data_effective_end_date',
            'src.data_sequence_no',
            'src.data_description',
            'src.data_created_date',
            'src.data_last_modified_date',
            'src.data_created_user',
            'src.data_last_modified_user',
            'src.data_occupancy_type',
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
    and src.data_supplier_id = min_source_update_datetime.data_supplier_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_code, data_supplier_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final