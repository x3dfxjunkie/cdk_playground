{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_profile_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__west__cli_passenger_profile_cleansed'),
            join_columns=['data_profile_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__west__cli_passenger_profile_cleansed') }}
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
            partition by data_profile_id
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
        partition_columns = ['data_profile_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_unavailable,
        data_maide_nname,
        data_redress_number,
        data_maiden_name,
        data_known_traveller_number,
        data_sanitize,
        data_ptoi_info,
        data_profile_id,
        data_title,
        data_first_name,
        data_last_name,
        data_date_of_birth,
        data_sex,
        data_type,
        data_note,
        data_profession,
        data_marital_status,
        data_smoker,
        data_citizanship1,
        data_citizenship2,
        data_primary_pp_no,
        data_primary_pp_isue_date,
        data_primary_pp_exp_date,
        data_primary_pp_issue_city,
        data_primary_pp_issue_country,
        data_secondary_pp_no,
        data_secondary_pp_issue_date,
        data_secondary_pp_exp_date,
        data_secondary_pp_issue_city,
        data_secondary_pp_issue_country,
        data_self_employed,
        data_company_name,
        data_income,
        data_salutation,
        data_cti_reference,
        data_club_member,
        data_primary_citizenship,
        data_secondary_pp_first_name,
        data_secondary_pp_last_name,
        data_primary_pp_first_name,
        data_primary_pp_last_name,
        data_alien_reg_no,
        data_seat_request,
        data_meal_request,
        data_other_request,
        data_secondary_citizenship,
        data_primary_issuing_office,
        data_secondary_issuing_office,
        data_pref_holiday,
        data_pref_destination,
        data_visa_output,
        data_date_of_birth_unknown,
        data_locale,
        data_user_set_dob,
        data_middle_name,
        data_primary_pp_middle_name,
        data_secondary_pp_middle_name,
        data_dummypasenger,
        data_care_of,
        data_last_modified_time,
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