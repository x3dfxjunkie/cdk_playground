{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_package_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__east__pkg_holiday_cleansed'),
            join_columns=['data_package_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__east__pkg_holiday_cleansed') }}
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
            partition by data_package_id
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
        partition_columns = ['data_package_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_calc_dist_channel,
        data_calc_type,
        data_calc_pricing_method,
        data_element_level_margin_markup,
        data_calc_brand,
        data_minimum_margin,
        data_minimum_margin_amount_type,
        data_calc_pax_base,
        data_division,
        data_dep_date_exist,
        data_constant_air_tax,
        data_cms_code,
        data_children_as_adult,
        data_no_of_pax,
        data_separate_itin_no_next_val,
        data_calc_booking_date,
        data_calc_cost_dep_date_only,
        data_ext_main_pkg_duration,
        data_template_type,
        data_last_modified_timestamp,
        data_block_code,
        data_bp_override,
        data_prod_defn_id,
        data_prod_defn_temp_grp_code,
        data_rate_category_code,
        data_offer_group_code,
        data_offer_group_name,
        data_time_to_publish,
        data_last_audited_time,
        data_package_id,
        data_pkg_group_id,
        data_version,
        data_parent_version,
        data_product_type,
        data_holiday_type,
        data_valid_from,
        data_valid_to,
        data_sales_from,
        data_sales_to,
        data_status,
        data_stage,
        data_stage_reason,
        data_original_package,
        data_average_margin,
        data_description,
        data_entered_by,
        data_entered_on,
        data_modified_on,
        data_modified_by,
        data_costing_currency,
        data_company,
        data_calc_cli_group,
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