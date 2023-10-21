{{
    config(
        materialized='incremental',
        unique_key= ['data_contract_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'acc_contract') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_contract_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_contract_id
),

-- cleansing the table
renamed as (
    select
        src.data_supp_comm as data_supp_comm,
        TRIM(src.data_date_wise_supplier) as data_date_wise_supplier,
        TRIM(src.data_trackable) as data_trackable,
        TRIM(src.data_tax_override) as data_tax_override,
        TRIM(src.data_deleted) as data_deleted,
        TRIM(src.data_voucher_code) as data_voucher_code,
        src.data_last_modified_timestamp as data_last_modified_timestamp,
        src.data_ext_avail_source as data_ext_avail_source,
        src.data_override_price as data_override_price,
        src.data_contract_id as data_contract_id,
        src.data_contract_group_id as data_contract_group_id,
        src.data_version as data_version,
        src.data_parent_version as data_parent_version,
        src.data_status as data_status,
        src.data_stage as data_stage,
        src.data_valid_from as data_valid_from,
        src.data_valid_to as data_valid_to,
        src.data_sales_from as data_sales_from,
        src.data_sales_to as data_sales_to,
        src.data_entered_on as data_entered_on,
        src.data_entered_by as data_entered_by,
        src.data_modified_on as data_modified_on,
        src.data_modified_by as data_modified_by,
        TRIM(src.data_prorata) as data_prorata,
        TRIM(src.data_eclc_allowed) as data_eclc_allowed,
        TRIM(src.data_eclc_guranteed) as data_eclc_guranteed,
        src.data_checkin_time as data_checkin_time,
        src.data_checkout_time as data_checkout_time,
        TRIM(src.data_sell_alone) as data_sell_alone,
        TRIM(src.data_nett_currency) as data_nett_currency,
        TRIM(src.data_rate_type) as data_rate_type,
        TRIM(src.data_gross_default_currency) as data_gross_default_currency,
        TRIM(src.data_customer_pay_hotel) as data_customer_pay_hotel,
        TRIM(src.data_pay_hotel_gross) as data_pay_hotel_gross,
        src.data_errata_group as data_errata_group,
        TRIM(src.data_preffered_board_basis) as data_preffered_board_basis,
        src.data_allocation_contract_id as data_allocation_contract_id,
        TRIM(src.data_stage_reason) as data_stage_reason,
        TRIM(src.data_tax_exempt) as data_tax_exempt,
        TRIM(src.data_room_wise_or_pax_wise) as data_room_wise_or_pax_wise,
        src.data_calculation_weight as data_calculation_weight,
        TRIM(src.data_document_send_to_accom) as data_document_send_to_accom,
        TRIM(src.data_group_rates) as data_group_rates,
        TRIM(src.data_rate_plan_code) as data_rate_plan_code,
        TRIM(src.data_rate_plan_name) as data_rate_plan_name,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_supp_comm',
            'src.data_date_wise_supplier',
            'src.data_trackable',
            'src.data_tax_override',
            'src.data_deleted',
            'src.data_voucher_code',
            'src.data_last_modified_timestamp',
            'src.data_ext_avail_source',
            'src.data_override_price',
            'src.data_contract_group_id',
            'src.data_version',
            'src.data_parent_version',
            'src.data_status',
            'src.data_stage',
            'src.data_valid_from',
            'src.data_valid_to',
            'src.data_sales_from',
            'src.data_sales_to',
            'src.data_entered_on',
            'src.data_entered_by',
            'src.data_modified_on',
            'src.data_modified_by',
            'src.data_prorata',
            'src.data_eclc_allowed',
            'src.data_eclc_guranteed',
            'src.data_checkin_time',
            'src.data_checkout_time',
            'src.data_sell_alone',
            'src.data_nett_currency',
            'src.data_rate_type',
            'src.data_gross_default_currency',
            'src.data_customer_pay_hotel',
            'src.data_pay_hotel_gross',
            'src.data_errata_group',
            'src.data_preffered_board_basis',
            'src.data_allocation_contract_id',
            'src.data_stage_reason',
            'src.data_tax_exempt',
            'src.data_room_wise_or_pax_wise',
            'src.data_calculation_weight',
            'src.data_document_send_to_accom',
            'src.data_group_rates',
            'src.data_rate_plan_code',
            'src.data_rate_plan_name',
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
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_contract_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final