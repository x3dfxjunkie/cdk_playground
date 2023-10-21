with tp_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

tpl_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_lctr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

tplx_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_lctr_xref_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

tppl_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_phn_lctr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

final as (
    select
        tp.data_txn_pty_id as transactional_party_id,
        tpl.data_txn_pty_lctr_id as transactional_locator_id,
        tp.data_txn_pty_typ_nm as transaction_type_name,
        tpl.data_lctr_typ_nm as locator_type_name,
        tpl.data_txn_pty_lctr_prmy_in as primary_locator_indicator,
        tpl.data_cnfrm_in as confirmation_indicator,
        tpl.data_allow_bill_in as allow_bill_indicator,
        tppl.data_phn_nb as phone_number,
        tppl.data_phn_dev_typ_nm as phone_device_type_name,
        tpl.data_lctr_usg_typ_nm as locator_usage_type_name,
        tplx.data_lctr_extnl_src_nm as locator_extnl_src_nm,
        tplx.data_lctr_extnl_ref_vl as reference_id,
        tppl.data_allow_phn_in as allow_phone_indicator
    from
        tp_cte as tp
        inner join tpl_cte as tpl
        on tp.data_txn_pty_id = tpl.data_txn_pty_id
        inner join tplx_cte as tplx
        on tpl.data_txn_pty_lctr_id = tplx.data_txn_pty_lctr_id
        inner join tppl_cte as tppl
        on tpl.data_txn_pty_lctr_id = tppl.data_txn_pty_phn_lctr_id
)

select * from final