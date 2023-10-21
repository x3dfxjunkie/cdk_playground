{{
    config(
        materialized='incremental',
        unique_key= ['data_booking_id', 'data_index_no', 'data_item_no', 'data_product_code','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'res_booking_item_cnx') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_booking_id,
        data_index_no,
        data_item_no,
        data_product_code,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_booking_id,
        data_index_no,
        data_item_no,
        data_product_code
),

-- cleansing the table
renamed as (
    select
        src.data_passenger_no as data_passenger_no,
        src.data_cost_in_contract as data_cost_in_contract,
        TRIM(src.data_cnx_charge_commissionable) as data_cnx_charge_commissionable,
        src.data_cnx_user as data_cnx_user,
        src.data_cnx_notification_sent_user as data_cnx_notification_sent_user,
        src.data_cnx_confirmation_received_user as data_cnx_confirmation_received_user,
        src.data_cnx_conf_received_user as data_cnx_conf_received_user,
        src.data_cnx_adt_cost as data_cnx_adt_cost,
        src.data_cnx_chd_cost as data_cnx_chd_cost,
        src.data_cnx_inf_cost as data_cnx_inf_cost,
        src.data_cnx_calculated_date as data_cnx_calculated_date,
        TRIM(src.data_tbx_only) as data_tbx_only,
        src.data_cause_id as data_cause_id,
        TRIM(src.data_charge_type) as data_charge_type,
        TRIM(src.data_reason_type) as data_reason_type,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_reversible) as data_reversible,
        src.data_booking_id as data_booking_id,
        TRIM(src.data_product_code) as data_product_code,
        src.data_item_no as data_item_no,
        src.data_index_no as data_index_no,
        src.data_cnx_reason_id as data_cnx_reason_id,
        src.data_cnx_date as data_cnx_date,
        src.data_cnx_cost as data_cnx_cost,
        src.data_cnx_price as data_cnx_price,
        TRIM(src.data_cnx_notification_sent) as data_cnx_notification_sent,
        TRIM(src.data_cnx_notification_sent_method) as data_cnx_notification_sent_method,
        src.data_cnx_notification_sent_date as data_cnx_notification_sent_date,
        TRIM(src.data_cnx_confirmation_received) as data_cnx_confirmation_received,
        src.data_cnx_confirmation_received_date as data_cnx_confirmation_received_date,
        TRIM(src.data_cnx_confirmation_received_meth) as data_cnx_confirmation_received_meth,
        TRIM(src.data_note) as data_note,
        TRIM(src.data_cnx_conf_received) as data_cnx_conf_received,
        src.data_cnx_conf_received_date as data_cnx_conf_received_date,
        TRIM(src.data_cnx_conf_received_method) as data_cnx_conf_received_method,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_passenger_no',
            'src.data_cost_in_contract',
            'src.data_cnx_charge_commissionable',
            'src.data_cnx_user',
            'src.data_cnx_notification_sent_user',
            'src.data_cnx_confirmation_received_user',
            'src.data_cnx_conf_received_user',
            'src.data_cnx_adt_cost',
            'src.data_cnx_chd_cost',
            'src.data_cnx_inf_cost',
            'src.data_cnx_calculated_date',
            'src.data_tbx_only',
            'src.data_cause_id',
            'src.data_charge_type',
            'src.data_reason_type',
            'src.data_last_modified_time',
            'src.data_reversible',
            'src.data_cnx_reason_id',
            'src.data_cnx_date',
            'src.data_cnx_cost',
            'src.data_cnx_price',
            'src.data_cnx_notification_sent',
            'src.data_cnx_notification_sent_method',
            'src.data_cnx_notification_sent_date',
            'src.data_cnx_confirmation_received',
            'src.data_cnx_confirmation_received_date',
            'src.data_cnx_confirmation_received_meth',
            'src.data_note',
            'src.data_cnx_conf_received',
            'src.data_cnx_conf_received_date',
            'src.data_cnx_conf_received_method',
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
    and src.data_index_no = min_source_update_datetime.data_index_no
    and src.data_item_no = min_source_update_datetime.data_item_no
    and src.data_product_code = min_source_update_datetime.data_product_code
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_booking_id, data_index_no, data_item_no, data_product_code, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final