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
-- define a cte for top
top_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_org_pty_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for tper
tper_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_extnl_ref_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
        and data_pty_extnl_src_nm = 'iatanumber'
),
-- join ctes to get the final result
final as(
    select
        tp.data_txn_pty_id as transaction_party_id,
        tp.data_txn_pty_typ_nm as transaction_party_type_name,
        top.data_txn_org_nm as transaction_organization_name,
        tper.data_pty_extnl_src_nm as party_external_source_name,
        tper.data_txn_pty_extnl_ref_val as reference_id,
        tp.data_create_dts as create_datetime,
        tp.data_updt_dts as source_update_datetime
    from
        tp_cte tp
        inner join top_cte top
        on tp.data_txn_pty_id = top.data_txn_org_pty_id
        inner join tper_cte tper
        on top.data_txn_org_pty_id = tper.data_txn_pty_id
)

select * from final