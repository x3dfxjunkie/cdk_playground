{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_contract_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__west__gen_contract_cleansed'),
            join_columns=['data_contract_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__west__gen_contract_cleansed') }}
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
            partition by data_contract_id
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
        partition_columns = ['data_contract_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_accom_id,
        data_include_inf_book_count,
        data_external_pricing,
        data_pricing_engine,
        data_ext_avail,
        data_voucher_code,
        data_last_modified_timestamp,
        data_special_pricing,
        data_special_pricing_method,
        data_pricing_override,
        data_usage_override,
        data_bundle_product,
        data_prod_defn_id,
        data_prod_defn_temp_grp_code,
        data_ext_avail_source,
        data_contract_id,
        data_contract_group_id,
        data_version,
        data_parent_version,
        data_status,
        data_stage,
        data_valid_from,
        data_valid_to,
        data_sales_from,
        data_sales_to,
        data_entered_by,
        data_entered_on,
        data_modified_by,
        data_modified_on,
        data_nett_currency,
        data_rate_type,
        data_default_gross_currency,
        data_prorata,
        data_sell_alone,
        data_pay_supplier_gross,
        data_customer_pay_supplier,
        data_errata_group,
        data_gen_product,
        data_starting_days,
        data_price_guaranteed,
        data_country,
        data_tourist_region,
        data_city,
        data_resort,
        data_stage_reason,
        data_tax_exempt,
        data_tax_override,
        data_airport,
        data_duration_type,
        data_item_wise,
        data_term_and_condition,
        data_state,
        data_accom_code,
        data_accom_name,
        data_content_supplier_id,
        data_content_supplier_code,
        data_content_supplier_name,
        data_send_documents_to_supplier,
        data_group_rates,
        data_date_wise_supplier,
        data_trackable,
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