{{
    config(
        materialized='incremental',
        unique_key= ['data_profile_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'cli_passenger_profile') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_profile_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_profile_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_unavailable) as data_unavailable,
        TRIM(src.data_maide_nname) as data_maide_nname,
        TRIM(src.data_redress_number) as data_redress_number,
        TRIM(src.data_maiden_name) as data_maiden_name,
        TRIM(src.data_known_traveller_number) as data_known_traveller_number,
        TRIM(src.data_sanitize) as data_sanitize,
        src.data_ptoi_info as data_ptoi_info,
        src.data_profile_id as data_profile_id,
        TRIM(src.data_title) as data_title,
        TRIM(src.data_first_name) as data_first_name,
        TRIM(src.data_last_name) as data_last_name,
        src.data_date_of_birth as data_date_of_birth,
        TRIM(src.data_sex) as data_sex,
        TRIM(src.data_type) as data_type,
        TRIM(src.data_note) as data_note,
        TRIM(src.data_profession) as data_profession,
        src.data_marital_status as data_marital_status,
        TRIM(src.data_smoker) as data_smoker,
        TRIM(src.data_citizanship1) as data_citizanship1,
        TRIM(src.data_citizenship2) as data_citizenship2,
        TRIM(src.data_primary_pp_no) as data_primary_pp_no,
        src.data_primary_pp_isue_date as data_primary_pp_isue_date,
        src.data_primary_pp_exp_date as data_primary_pp_exp_date,
        TRIM(src.data_primary_pp_issue_city) as data_primary_pp_issue_city,
        TRIM(src.data_primary_pp_issue_country) as data_primary_pp_issue_country,
        TRIM(src.data_secondary_pp_no) as data_secondary_pp_no,
        src.data_secondary_pp_issue_date as data_secondary_pp_issue_date,
        src.data_secondary_pp_exp_date as data_secondary_pp_exp_date,
        TRIM(src.data_secondary_pp_issue_city) as data_secondary_pp_issue_city,
        TRIM(src.data_secondary_pp_issue_country) as data_secondary_pp_issue_country,
        TRIM(src.data_self_employed) as data_self_employed,
        TRIM(src.data_company_name) as data_company_name,
        TRIM(src.data_income) as data_income,
        TRIM(src.data_salutation) as data_salutation,
        src.data_cti_reference as data_cti_reference,
        TRIM(src.data_club_member) as data_club_member,
        TRIM(src.data_primary_citizenship) as data_primary_citizenship,
        TRIM(src.data_secondary_pp_first_name) as data_secondary_pp_first_name,
        TRIM(src.data_secondary_pp_last_name) as data_secondary_pp_last_name,
        TRIM(src.data_primary_pp_first_name) as data_primary_pp_first_name,
        TRIM(src.data_primary_pp_last_name) as data_primary_pp_last_name,
        TRIM(src.data_alien_reg_no) as data_alien_reg_no,
        TRIM(src.data_seat_request) as data_seat_request,
        TRIM(src.data_meal_request) as data_meal_request,
        TRIM(src.data_other_request) as data_other_request,
        TRIM(src.data_secondary_citizenship) as data_secondary_citizenship,
        TRIM(src.data_primary_issuing_office) as data_primary_issuing_office,
        TRIM(src.data_secondary_issuing_office) as data_secondary_issuing_office,
        TRIM(src.data_pref_holiday) as data_pref_holiday,
        src.data_pref_destination as data_pref_destination,
        TRIM(src.data_visa_output) as data_visa_output,
        TRIM(src.data_date_of_birth_unknown) as data_date_of_birth_unknown,
        TRIM(src.data_locale) as data_locale,
        TRIM(src.data_user_set_dob) as data_user_set_dob,
        TRIM(src.data_middle_name) as data_middle_name,
        TRIM(src.data_primary_pp_middle_name) as data_primary_pp_middle_name,
        TRIM(src.data_secondary_pp_middle_name) as data_secondary_pp_middle_name,
        TRIM(src.data_dummypasenger) as data_dummypasenger,
        TRIM(src.data_care_of) as data_care_of,
        src.data_last_modified_time as data_last_modified_time,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_unavailable',
            'src.data_maide_nname',
            'src.data_redress_number',
            'src.data_maiden_name',
            'src.data_known_traveller_number',
            'src.data_sanitize',
            'src.data_ptoi_info',
            'src.data_title',
            'src.data_first_name',
            'src.data_last_name',
            'src.data_date_of_birth',
            'src.data_sex',
            'src.data_type',
            'src.data_note',
            'src.data_profession',
            'src.data_marital_status',
            'src.data_smoker',
            'src.data_citizanship1',
            'src.data_citizenship2',
            'src.data_primary_pp_no',
            'src.data_primary_pp_isue_date',
            'src.data_primary_pp_exp_date',
            'src.data_primary_pp_issue_city',
            'src.data_primary_pp_issue_country',
            'src.data_secondary_pp_no',
            'src.data_secondary_pp_issue_date',
            'src.data_secondary_pp_exp_date',
            'src.data_secondary_pp_issue_city',
            'src.data_secondary_pp_issue_country',
            'src.data_self_employed',
            'src.data_company_name',
            'src.data_income',
            'src.data_salutation',
            'src.data_cti_reference',
            'src.data_club_member',
            'src.data_primary_citizenship',
            'src.data_secondary_pp_first_name',
            'src.data_secondary_pp_last_name',
            'src.data_primary_pp_first_name',
            'src.data_primary_pp_last_name',
            'src.data_alien_reg_no',
            'src.data_seat_request',
            'src.data_meal_request',
            'src.data_other_request',
            'src.data_secondary_citizenship',
            'src.data_primary_issuing_office',
            'src.data_secondary_issuing_office',
            'src.data_pref_holiday',
            'src.data_pref_destination',
            'src.data_visa_output',
            'src.data_date_of_birth_unknown',
            'src.data_locale',
            'src.data_user_set_dob',
            'src.data_middle_name',
            'src.data_primary_pp_middle_name',
            'src.data_secondary_pp_middle_name',
            'src.data_dummypasenger',
            'src.data_care_of',
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
    on src.data_profile_id = min_source_update_datetime.data_profile_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_profile_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final