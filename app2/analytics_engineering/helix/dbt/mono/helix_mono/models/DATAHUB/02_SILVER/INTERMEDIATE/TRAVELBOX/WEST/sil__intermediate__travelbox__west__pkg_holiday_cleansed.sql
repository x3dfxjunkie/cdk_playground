{{
    config(
        materialized='incremental',
        unique_key= ['data_package_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'pkg_holiday') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_package_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_package_id
),

-- cleansing the table
renamed as (
    select
        src.data_template_type as data_template_type,
        src.data_last_modified_timestamp as data_last_modified_timestamp,
        TRIM(src.data_block_code) as data_block_code,
        TRIM(src.data_bp_override) as data_bp_override,
        src.data_prod_defn_id as data_prod_defn_id,
        TRIM(src.data_prod_defn_temp_grp_code) as data_prod_defn_temp_grp_code,
        TRIM(src.data_rate_category_code) as data_rate_category_code,
        TRIM(src.data_offer_group_code) as data_offer_group_code,
        TRIM(src.data_offer_group_name) as data_offer_group_name,
        src.data_time_to_publish as data_time_to_publish,
        src.data_last_audited_time as data_last_audited_time,
        src.data_package_id as data_package_id,
        src.data_pkg_group_id as data_pkg_group_id,
        src.data_version as data_version,
        src.data_parent_version as data_parent_version,
        TRIM(src.data_product_type) as data_product_type,
        TRIM(src.data_holiday_type) as data_holiday_type,
        src.data_valid_from as data_valid_from,
        src.data_valid_to as data_valid_to,
        src.data_sales_from as data_sales_from,
        src.data_sales_to as data_sales_to,
        src.data_status as data_status,
        src.data_stage as data_stage,
        TRIM(src.data_stage_reason) as data_stage_reason,
        TRIM(src.data_original_package) as data_original_package,
        src.data_average_margin as data_average_margin,
        TRIM(src.data_description) as data_description,
        src.data_entered_by as data_entered_by,
        src.data_entered_on as data_entered_on,
        src.data_modified_on as data_modified_on,
        src.data_modified_by as data_modified_by,
        TRIM(src.data_costing_currency) as data_costing_currency,
        src.data_ext_main_pkg_duration as data_ext_main_pkg_duration,
        TRIM(src.data_company) as data_company,
        TRIM(src.data_calc_cli_group) as data_calc_cli_group,
        TRIM(src.data_calc_dist_channel) as data_calc_dist_channel,
        TRIM(src.data_calc_type) as data_calc_type,
        src.data_calc_pricing_method as data_calc_pricing_method,
        TRIM(src.data_element_level_margin_markup) as data_element_level_margin_markup,
        TRIM(src.data_calc_brand) as data_calc_brand,
        src.data_minimum_margin as data_minimum_margin,
        TRIM(src.data_minimum_margin_amount_type) as data_minimum_margin_amount_type,
        src.data_calc_pax_base as data_calc_pax_base,
        TRIM(src.data_division) as data_division,
        TRIM(src.data_dep_date_exist) as data_dep_date_exist,
        TRIM(src.data_constant_air_tax) as data_constant_air_tax,
        TRIM(src.data_cms_code) as data_cms_code,
        TRIM(src.data_children_as_adult) as data_children_as_adult,
        src.data_no_of_pax as data_no_of_pax,
        src.data_separate_itin_no_next_val as data_separate_itin_no_next_val,
        src.data_calc_booking_date as data_calc_booking_date,
        TRIM(src.data_calc_cost_dep_date_only) as data_calc_cost_dep_date_only,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_template_type',
            'src.data_last_modified_timestamp',
            'src.data_block_code',
            'src.data_bp_override',
            'src.data_prod_defn_id',
            'src.data_prod_defn_temp_grp_code',
            'src.data_rate_category_code',
            'src.data_offer_group_code',
            'src.data_offer_group_name',
            'src.data_time_to_publish',
            'src.data_last_audited_time',
            'src.data_pkg_group_id',
            'src.data_version',
            'src.data_parent_version',
            'src.data_product_type',
            'src.data_holiday_type',
            'src.data_valid_from',
            'src.data_valid_to',
            'src.data_sales_from',
            'src.data_sales_to',
            'src.data_status',
            'src.data_stage',
            'src.data_stage_reason',
            'src.data_original_package',
            'src.data_average_margin',
            'src.data_description',
            'src.data_entered_by',
            'src.data_entered_on',
            'src.data_modified_on',
            'src.data_modified_by',
            'src.data_costing_currency',
            'src.data_ext_main_pkg_duration',
            'src.data_company',
            'src.data_calc_cli_group',
            'src.data_calc_dist_channel',
            'src.data_calc_type',
            'src.data_calc_pricing_method',
            'src.data_element_level_margin_markup',
            'src.data_calc_brand',
            'src.data_minimum_margin',
            'src.data_minimum_margin_amount_type',
            'src.data_calc_pax_base',
            'src.data_division',
            'src.data_dep_date_exist',
            'src.data_constant_air_tax',
            'src.data_cms_code',
            'src.data_children_as_adult',
            'src.data_no_of_pax',
            'src.data_separate_itin_no_next_val',
            'src.data_calc_booking_date',
            'src.data_calc_cost_dep_date_only',
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
    on src.data_package_id = min_source_update_datetime.data_package_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_package_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final