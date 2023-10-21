-- define a cte for cg
with cg_cte as (
    select * from {{ ref('sil__intermediate__dreams__folio__chrg_grp_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a cte for ncg
ncg_cte as (
    select * from {{ ref('sil__intermediate__dreams__folio__node_chrg_grp_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- join c, tac and tac ctes to get the final result
final as (
    select
        distinct cg.data_chrg_grp_id as charge_group_id,
        cg.data_chrg_grp_typ_nm as charge_type_name,
        cg.data_chrg_grp_strt_dts as chrg_grp_strt_dts,
        cg.data_chrg_grp_end_dts as chrg_grp_end_dts,
        cg.data_chrg_grp_sts_nm as charge_group_status_name,
        cg.data_chrg_grp_ds as charge_group_description,
        cg.data_chrg_grp_strt_dts as charge_group_start_datetime,
        to_date(data_chrg_grp_strt_dts) as charge_group_start_date,
        cg.data_chrg_grp_end_dts as charge_group_end_datetime,
        to_date(data_chrg_grp_end_dts) as charge_group_end_date,
        cg.data_txn_fac_id as transaction_facility_id,
        cg.data_src_acct_ctr_id as source_account_center_id,
        cg.data_grp_dlgt_sml_bal_wrtoff_in as group_delegate_small_balance_writeoff_indicator,
        ncg.data_bill_chrg_grp_id as bill_charge_group_id,
        ncg.data_ancstr_chrg_grp_id as ancestor_charge_group_id,
        ncg.data_guar_typ_nm as guarantee_type_name,
        ncg.data_pkg_excpt_in as package_exception_indicator
    from cg_cte cg
    left join ncg_cte ncg on cg.data_chrg_grp_id = ncg.data_node_chrg_grp_id
)

-- select from the final result cte
select * from final