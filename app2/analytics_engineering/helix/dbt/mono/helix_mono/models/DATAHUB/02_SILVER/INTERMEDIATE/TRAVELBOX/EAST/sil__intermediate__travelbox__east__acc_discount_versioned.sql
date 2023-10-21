{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_contract_id', 'data_discount_no','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__east__acc_discount_cleansed'),
            join_columns=['data_contract_id', 'data_discount_no'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__east__acc_discount_cleansed') }}
    {% if is_incremental() %}
    -- this filter will only be applied on an incremental run

        where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

-- adding the row_number column (rn) for ordering the incremental data by metadata_timestamp
renamed as (
    select
        *,
        row_number() over (
            partition by data_contract_id, data_discount_no
                order by
                    metadata_timestamp desc
        ) as rn
    from
        cleansed
),

-- adding version start and end dates metadata columns
versioned as (
    {{ macro_create_versions(
        cleansed_table = 'renamed',
        timestamp_column = 'metadata_timestamp',
        partition_columns = ['data_contract_id', 'data_discount_no']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_last_modified_time,
        data_entered_on,
        data_entered_by,
        data_modified_on,
        data_modified_by,
        data_contract_id,
        data_discount_no,
        data_reference,
        data_type,
        data_description,
        data_pass_percentage,
        data_discount_calculation_order,
        data_doc_notes,
        data_doc_types,
        data_pass_percentage_bak,
        data_payment_scheme,
        data_cnx_scheme,
        data_amd_scheme,
        data_sales_from,
        data_sales_to,
        data_booked_from_to,
        data_commissionable,
        data_discountable_suppliments,
        metadata_checksum,
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
        metadata_version_start_datetime,
        metadata_version_end_datetime,
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
    from versioned
)

select * from final