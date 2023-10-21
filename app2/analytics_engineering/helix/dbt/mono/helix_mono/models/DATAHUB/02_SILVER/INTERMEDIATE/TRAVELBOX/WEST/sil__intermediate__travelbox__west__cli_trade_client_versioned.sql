{{
    config(

        materialized='incremental',
        on_schema_change = 'append_new_columns',
        unique_key = ['data_client_id','metadata_checksum'],
        pre_hook = "{{ macro_update_target_version_endtime(
            cleansed_table = ref('sil__intermediate__travelbox__west__cli_trade_client_cleansed'),
            join_columns=['data_client_id'],
            timestamp_column='min_metadata_timestamp'
        ) }}"
    )
}}

-- source is the cleansed table
with cleansed as (
    select * from {{ ref('sil__intermediate__travelbox__west__cli_trade_client_cleansed') }}
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
            partition by data_client_id
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
        partition_columns = ['data_client_id']
    ) }}
),

-- creating the final versioned table with new metadata columns
final as (
    select
        data_accept_ebook_details,
        data_atol_agent,
        data_nett_rate,
        data_client_rating,
        data_tal_no,
        data_abn_no,
        data_deposit_scheme,
        data_comp_reg,
        data_issue_invoice,
        data_collect_from_client,
        data_issue_itinerary,
        data_issue_voucher,
        data_show_commission,
        data_gsa_number,
        data_gsa_join_date,
        data_self_billing,
        data_amendement_scheme,
        data_canx_scheme,
        data_option_scheme,
        data_booking_ref_type,
        data_booking_ref_compulsary,
        data_partner,
        data_search_in_call_centre,
        data_logo,
        data_credit_limit_ho,
        data_wra_agents,
        data_gsa_client,
        data_payment_group,
        data_head_office_id,
        data_tax_reg_no,
        data_area,
        data_language_code,
        data_payment_method,
        data_credit_agent_id,
        data_include_tax_on_comm,
        data_sales_allowed,
        data_documents_allowed,
        data_exclude_partner_emailing,
        data_trade_client_type,
        data_accept_edocs,
        data_atol_cert_not_required,
        data_atol_name,
        data_mail_method,
        data_enable_client_markup,
        data_client_level,
        data_last_modified_time,
        data_com_nett_gross_override,
        data_profile_type,
        data_block_code,
        data_hybrid_market_id,
        data_client_id,
        data_head_office,
        data_head_office_ref,
        data_remit_commission_ho,
        data_division,
        data_town,
        data_multiple,
        data_promotion,
        data_web,
        data_brochure_request,
        data_agreement_status,
        data_comission_from_ho,
        data_comm_group,
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