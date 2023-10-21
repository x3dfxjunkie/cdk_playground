-- define a cte for tp
with tp_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for tpl
tpl_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_lctr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for tplx
tplx_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_lctr_xref_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for tpal
tpal_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_addr_lctr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- join lnr, lnrt and lnrc ctes to get the final result
final as (
    select
        tp.data_txn_pty_id as transactional_party_id,
        tpl.data_txn_pty_lctr_id as transactional_locator_id,
        tp.data_txn_pty_typ_nm as transaction_type_name,
        tpl.data_lctr_typ_nm as locator_type_name,
        tpl.data_txn_pty_lctr_prmy_in as primary_locator_indicator,
        tpl.data_cnfrm_in as confirmation_indicator,
        tpl.data_allow_bill_in as allow_bill_indicator,
        tpal.data_addr_ln1_tx as address_line_one_text,
        tpal.data_addr_ln2 as address_line_two_text,
        tpal.data_city_nm as city_name,
        tpal.data_rgn_cd as region_code,
        tpal.data_pstl_cd as postal_code,
        tpl.data_cntry_nm as country_name,
        tpl.data_lctr_usg_typ_nm as locator_usage_type_name,
        tplx.data_lctr_extnl_src_nm as locator_extnl_src_nm,
        tplx.data_lctr_extnl_ref_vl as reference_id,
        tpal.data_allow_mail_in as allow_mail_indicator
    from
        tp_cte tp
        inner join tpl_cte tpl
        on tp.data_txn_pty_id = tpl.data_txn_pty_id
        inner join tplx_cte tplx
        on tpl.data_txn_pty_lctr_id = tplx.data_txn_pty_lctr_id
        inner join tpal_cte tpal
        on tpl.data_txn_pty_lctr_id = tpal.data_txn_pty_addr_lctr_id
) 
-- select from the final result cte
select
    *
from
    final
