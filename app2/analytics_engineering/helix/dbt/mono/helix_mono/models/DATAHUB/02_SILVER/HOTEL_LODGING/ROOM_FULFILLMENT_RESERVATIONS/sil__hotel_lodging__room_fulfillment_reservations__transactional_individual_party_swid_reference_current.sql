with cte1 as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte2 as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_extnl_ref_versioned') }}
    where
        data_pty_extnl_src_nm = 'swid'
        and metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- final query cte with aliases
finalquerycte as (
    select
        cte1.data_txn_pty_id as transaction_individual_party_id,
        cte2.data_pty_extnl_src_nm as party_external_source_name,
        cte2.data_txn_pty_extnl_ref_val as reference_id,
        cte1.data_create_dts as create_datetime,
        cte1.data_updt_dts as source_update_datetime
    from
        cte1
        inner join cte2
        on cte1.data_txn_pty_id = cte2.data_txn_pty_id
)
select
    *
from
    finalquerycte
