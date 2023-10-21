-- define a cte for ror
with ft_cte as (
    select * from {{ ref('sil__intermediate__dreams__folio__folio_txn_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a cte for ir
ftti_cte as (
    select * from {{ ref('sil__intermediate__dreams__folio__folio_txn_txn_item_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- join ft and ftti ctes to get the final result
final as (
    select
        distinct ft.data_folio_txn_id as folio_transaction_id,
        ftti.data_folio_txn_item_id_vl as folio_item_id_value,
        ftti.data_folio_txn_item_typ_nm as folio_transaction_type_item_name,
        ft.data_folio_txn_typ_nm as folio_transaction_type_name,
        ft.data_folio_txn_dts as folio_transaction_datetime,
        to_date(ft.data_folio_txn_dts) as folio_transaction_date,
        ftti.data_txn_proc_typ_nm as transaction_procedure_type_name,
        ft.data_create_usr_id_cd as create_user_id,
        ft.data_create_dts as create_datetime,
        to_date(ft.data_create_dts) as create_date
    from ft_cte ft
    inner join ftti_cte ftti on ft.data_folio_txn_id = ftti.data_folio_txn_id
)

-- select from the final result cte
select * from final