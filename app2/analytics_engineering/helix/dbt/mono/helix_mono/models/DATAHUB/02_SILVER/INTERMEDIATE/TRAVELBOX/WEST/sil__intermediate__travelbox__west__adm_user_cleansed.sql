{{
    config(
        materialized='incremental',
        unique_key= ['data_user_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'adm_user') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_user_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_user_id
),

-- cleansing the table
renamed as (
    select
        src.data_created_time as data_created_time,
        src.data_created_user as data_created_user,
        src.data_last_modified_user as data_last_modified_user,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_notes) as data_notes,
        TRIM(src.data_created_by_agent) as data_created_by_agent,
        src.data_user_id as data_user_id,
        TRIM(src.data_username) as data_username,
        TRIM(src.data_password) as data_password,
        TRIM(src.data_firstname) as data_firstname,
        TRIM(src.data_lastname) as data_lastname,
        TRIM(src.data_initials) as data_initials,
        TRIM(src.data_sex) as data_sex,
        src.data_dob as data_dob,
        src.data_logins as data_logins,
        TRIM(src.data_agent_preference) as data_agent_preference,
        TRIM(src.data_telephone) as data_telephone,
        TRIM(src.data_email) as data_email,
        TRIM(src.data_extension) as data_extension,
        TRIM(src.data_status) as data_status,
        TRIM(src.data_display_name) as data_display_name,
        src.data_question_id as data_question_id,
        TRIM(src.data_answer) as data_answer,
        src.data_pwd_change_date as data_pwd_change_date,
        TRIM(src.data_default_password) as data_default_password,
        TRIM(src.data_default_answer) as data_default_answer,
        TRIM(src.data_default_currency) as data_default_currency,
        TRIM(src.data_default_div) as data_default_div,
        TRIM(src.data_default_com) as data_default_com,
        TRIM(src.data_agent_initials) as data_agent_initials,
        TRIM(src.data_agent_sign) as data_agent_sign,
        TRIM(src.data_psudo_city) as data_psudo_city,
        TRIM(src.data_b2_b_user) as data_b2_b_user,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_created_time',
            'src.data_created_user',
            'src.data_last_modified_user',
            'src.data_last_modified_time',
            'src.data_notes',
            'src.data_created_by_agent',
            'src.data_username',
            'src.data_password',
            'src.data_firstname',
            'src.data_lastname',
            'src.data_initials',
            'src.data_sex',
            'src.data_dob',
            'src.data_logins',
            'src.data_agent_preference',
            'src.data_telephone',
            'src.data_email',
            'src.data_extension',
            'src.data_status',
            'src.data_display_name',
            'src.data_question_id',
            'src.data_answer',
            'src.data_pwd_change_date',
            'src.data_default_password',
            'src.data_default_answer',
            'src.data_default_currency',
            'src.data_default_div',
            'src.data_default_com',
            'src.data_agent_initials',
            'src.data_agent_sign',
            'src.data_psudo_city',
            'src.data_b2_b_user',
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
    on src.data_user_id = min_source_update_datetime.data_user_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_user_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final