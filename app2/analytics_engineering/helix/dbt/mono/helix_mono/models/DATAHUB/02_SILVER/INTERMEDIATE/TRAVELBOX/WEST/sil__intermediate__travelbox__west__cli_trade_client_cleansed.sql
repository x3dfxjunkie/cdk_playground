{{
    config(
        materialized='incremental',
        unique_key= ['data_client_id','metadata_checksum'],
        on_schema_change='append_new_columns'
    )
}}

-- source is the bronze table
with source as (
    select *, case when metadata_operation = 'delete' then 'D' else 'S' end as dms_operation
    from {{ source('brz_travelbox_west', 'cli_trade_client') }}

    {% if is_incremental() %}

    -- this filter will only be applied on an incremental run
    where metadata_timestamp > (select max(metadata_timestamp) from {{ this }})

    {% endif %}
),

min_source_update_datetime as
(
    select
        data_client_id,
        min(metadata_timestamp) as min_metadata_timestamp
    from
        source
    group by
        data_client_id
),

-- cleansing the table
renamed as (
    select
        TRIM(src.data_accept_ebook_details) as data_accept_ebook_details,
        TRIM(src.data_atol_agent) as data_atol_agent,
        TRIM(src.data_nett_rate) as data_nett_rate,
        TRIM(src.data_client_rating) as data_client_rating,
        TRIM(src.data_tal_no) as data_tal_no,
        TRIM(src.data_abn_no) as data_abn_no,
        src.data_deposit_scheme as data_deposit_scheme,
        TRIM(src.data_comp_reg) as data_comp_reg,
        TRIM(src.data_issue_invoice) as data_issue_invoice,
        TRIM(src.data_collect_from_client) as data_collect_from_client,
        TRIM(src.data_issue_itinerary) as data_issue_itinerary,
        TRIM(src.data_issue_voucher) as data_issue_voucher,
        TRIM(src.data_show_commission) as data_show_commission,
        TRIM(src.data_gsa_number) as data_gsa_number,
        src.data_gsa_join_date as data_gsa_join_date,
        TRIM(src.data_self_billing) as data_self_billing,
        src.data_amendement_scheme as data_amendement_scheme,
        src.data_canx_scheme as data_canx_scheme,
        src.data_option_scheme as data_option_scheme,
        TRIM(src.data_booking_ref_type) as data_booking_ref_type,
        TRIM(src.data_booking_ref_compulsary) as data_booking_ref_compulsary,
        TRIM(src.data_partner) as data_partner,
        TRIM(src.data_search_in_call_centre) as data_search_in_call_centre,
        TRIM(src.data_logo) as data_logo,
        TRIM(src.data_credit_limit_ho) as data_credit_limit_ho,
        TRIM(src.data_wra_agents) as data_wra_agents,
        TRIM(src.data_gsa_client) as data_gsa_client,
        src.data_payment_group as data_payment_group,
        src.data_head_office_id as data_head_office_id,
        TRIM(src.data_tax_reg_no) as data_tax_reg_no,
        src.data_area as data_area,
        TRIM(src.data_language_code) as data_language_code,
        TRIM(src.data_payment_method) as data_payment_method,
        TRIM(src.data_credit_agent_id) as data_credit_agent_id,
        TRIM(src.data_include_tax_on_comm) as data_include_tax_on_comm,
        TRIM(src.data_sales_allowed) as data_sales_allowed,
        TRIM(src.data_documents_allowed) as data_documents_allowed,
        TRIM(src.data_exclude_partner_emailing) as data_exclude_partner_emailing,
        TRIM(src.data_trade_client_type) as data_trade_client_type,
        TRIM(src.data_accept_edocs) as data_accept_edocs,
        TRIM(src.data_atol_cert_not_required) as data_atol_cert_not_required,
        TRIM(src.data_atol_name) as data_atol_name,
        TRIM(src.data_mail_method) as data_mail_method,
        TRIM(src.data_enable_client_markup) as data_enable_client_markup,
        TRIM(src.data_client_level) as data_client_level,
        src.data_last_modified_time as data_last_modified_time,
        TRIM(src.data_com_nett_gross_override) as data_com_nett_gross_override,
        TRIM(src.data_profile_type) as data_profile_type,
        TRIM(src.data_block_code) as data_block_code,
        src.data_hybrid_market_id as data_hybrid_market_id,
        src.data_client_id as data_client_id,
        TRIM(src.data_head_office) as data_head_office,
        TRIM(src.data_head_office_ref) as data_head_office_ref,
        TRIM(src.data_remit_commission_ho) as data_remit_commission_ho,
        TRIM(src.data_division) as data_division,
        TRIM(src.data_town) as data_town,
        TRIM(src.data_multiple) as data_multiple,
        src.data_promotion as data_promotion,
        TRIM(src.data_web) as data_web,
        TRIM(src.data_brochure_request) as data_brochure_request,
        src.data_agreement_status as data_agreement_status,
        TRIM(src.data_comission_from_ho) as data_comission_from_ho,
        src.data_comm_group as data_comm_group,
        min_source_update_datetime.min_metadata_timestamp as min_metadata_timestamp,
        {{ macro_generate_checksum([
            'src.data_accept_ebook_details',
            'src.data_atol_agent',
            'src.data_nett_rate',
            'src.data_client_rating',
            'src.data_tal_no',
            'src.data_abn_no',
            'src.data_deposit_scheme',
            'src.data_comp_reg',
            'src.data_issue_invoice',
            'src.data_collect_from_client',
            'src.data_issue_itinerary',
            'src.data_issue_voucher',
            'src.data_show_commission',
            'src.data_gsa_number',
            'src.data_gsa_join_date',
            'src.data_self_billing',
            'src.data_amendement_scheme',
            'src.data_canx_scheme',
            'src.data_option_scheme',
            'src.data_booking_ref_type',
            'src.data_booking_ref_compulsary',
            'src.data_partner',
            'src.data_search_in_call_centre',
            'src.data_logo',
            'src.data_credit_limit_ho',
            'src.data_wra_agents',
            'src.data_gsa_client',
            'src.data_payment_group',
            'src.data_head_office_id',
            'src.data_tax_reg_no',
            'src.data_area',
            'src.data_language_code',
            'src.data_payment_method',
            'src.data_credit_agent_id',
            'src.data_include_tax_on_comm',
            'src.data_sales_allowed',
            'src.data_documents_allowed',
            'src.data_exclude_partner_emailing',
            'src.data_trade_client_type',
            'src.data_accept_edocs',
            'src.data_atol_cert_not_required',
            'src.data_atol_name',
            'src.data_mail_method',
            'src.data_enable_client_markup',
            'src.data_client_level',
            'src.data_last_modified_time',
            'src.data_com_nett_gross_override',
            'src.data_profile_type',
            'src.data_block_code',
            'src.data_hybrid_market_id',
            'src.data_head_office',
            'src.data_head_office_ref',
            'src.data_remit_commission_ho',
            'src.data_division',
            'src.data_town',
            'src.data_multiple',
            'src.data_promotion',
            'src.data_web',
            'src.data_brochure_request',
            'src.data_agreement_status',
            'src.data_comission_from_ho',
            'src.data_comm_group',
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
    on src.data_client_id = min_source_update_datetime.data_client_id
),

-- removing duplicates from incremental set
final as (
    {{ dbt_utils.deduplicate(
        relation = 'renamed',
        partition_by = 'data_client_id, metadata_checksum',
        order_by = "metadata_timestamp desc",
    ) }}
)

select * from final