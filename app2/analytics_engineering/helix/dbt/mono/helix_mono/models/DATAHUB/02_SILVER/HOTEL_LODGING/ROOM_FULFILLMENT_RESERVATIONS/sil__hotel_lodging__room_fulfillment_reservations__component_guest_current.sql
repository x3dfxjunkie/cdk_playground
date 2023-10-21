with dining_tc_gst_cte as (
    select
        *
    from {{ ref('sil__intermediate__dreams__dining__tc_gst_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

final as (
    select distinct
        data_txn_idvl_pty_id as transaction_individual_party_id,
        data_tc_id as travel_component_id,
        data_age_typ_nm as age_type_name,
        data_age_nb as age_number
    from dining_tc_gst_cte

)

select * from final