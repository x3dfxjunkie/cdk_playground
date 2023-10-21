with ci_cte as (
    select
        *
    --from latest_datahub.silver.sil_dreams_folio_chrg_item_versioned
    from {{ ref('sil__intermediate__dreams__folio__chrg_item_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a cte for fi (folio_item)
fi_cte as (
    select
        *
    --from latest_datahub.silver.sil_dreams_folio_folio_item_versioned
    from {{ ref('sil__intermediate__dreams__folio__folio_item_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a cte for cid (charge_item_deposit)
cid_cte as (
    select
        *
    --from latest_datahub.silver.sil_dreams_folio_chrg_item_dpst_versioned
    from {{ ref('sil__intermediate__dreams__folio__chrg_item_dpst_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- select from the final result by joining the ctes
final as (
    select
        ci.data_chrg_item_id as charge_item_id,
        ci.data_chrg_id as charge_id,
        fi.data_folio_id as folio_id,
        fi.data_folio_item_typ_nm as folio_item_type_name,
        fi.data_folio_item_am as folio_item_amount,
        ci.data_chrg_item_am as charge_item_amount,
        cid.data_chrg_item_dpst_am as charge_item_deposit_amount,
        cid.data_chrg_item_dpst_due_dt as charge_item_deposit_due_date,
        ci.data_chrg_item_typ_nm as charge_item_type_name,
        ci.data_rev_typ_nm as revenue_type_name,
        ci.data_rev_typ_id as revenue_type_id,
        ci.data_tax_item_in as tax_item_indicator,
        ci.data_splt_chrg_item_in as split_charge_item_indicator,
        ci.data_chrg_item_inactv_dts as charge_item_inactive_datetime,
        to_date(ci.data_chrg_item_inactv_dts) as charge_item_inactive_date,
        ci.data_chrg_item_crncy_cd as charge_item_currency_code,
        ci.data_create_usr_id_cd as create_user_id,
        ci.data_create_dts as create_date_time,
        to_date(ci.data_create_dts) as create_date,
        ci.data_updt_usr_id_cd as source_update_user_id,
        ci.data_updt_dts as source_update_datetime,
        to_date(ci.data_updt_dts) as source_update_date
from ci_cte ci
inner join fi_cte fi on ci.data_chrg_item_id = fi.data_folio_item_id
left join cid_cte cid on ci.data_chrg_item_id = cid.data_chrg_item_id

)

-- select from the final result cte
select * from final

