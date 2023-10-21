with cte_ca as (

    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__chrg_alloc_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte_cgf as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__chrg_grp_folio_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte_rc as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__rev_cls_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte_f as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__fac_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte_b as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__bill_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte_cg as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__charge_account__chrg_grp_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte_fp as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__folio_prfl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
final_cte as (
    select
        distinct coalesce (
            cte_ca.data_chrg_grp_folio_id,
            cte_cgf.data_chrg_grp_folio_id
        ) folio_id,
        cte_ca.data_own_chrg_grp_id as root_charge_group_id,
        cte_ca.data_pick_chrg_grp_id as charge_group_id,
        cte_ca.data_bill_id as bill_id,
        cte_b.data_bill_cd_nm as bill_code_name,
        cte_b.data_bill_cd_ds as bill_code_description,
        cte_ca.data_bill_chrg_grp_id as bill_charge_group_id,
        cte_cg.data_chrg_grp_ds as bill_charge_group_description,
        cte_ca.data_txn_idvl_pty_id as transaction_individual_party_id,
        cte_ca.data_rev_cls_id as revenue_class_id,
        cte_rc.data_rev_cls_nm as revenue_class_name,
        cte_rc.data_rev_cls_actv_in as revenue_class_active_indicator,
        cte_ca.data_txn_fac_id as transaction_facility_id,
        cte_f.data_fac_nm as transaction_facility_name,
        cte_ca.data_alloc_strt_dt as allocation_start_date,
        cte_ca.data_alloc_end_dt as allocation_end_date,
        cte_ca.data_splt_typ_nm as split_type_name,
        cte_ca.data_splt_vl as split_value,
        cte_ca.data_pick_all_in as pick_all_in,
        cte_ca.data_folio_prfl_id as folio_profile_id,
        cte_fp.data_dflt_settl_meth_id as default_settlement_method_id,
        cte_ca.data_chrg_alloc_inactv_dt as charge_allocation_inactive_date,
        cte_ca.data_create_usr_id_cd as create_user_id,
        cte_ca.data_create_dts as create_datetime,
        to_date(
            cte_ca.data_create_dts
        ) as create_date,
        cte_ca.data_updt_usr_id_cd as source_update_user_id,
        cte_ca.data_updt_dts as sourc_update_datetime,
        to_date(
            cte_ca.data_updt_dts
        ) as source_update_date
    from
        cte_ca
        inner join cte_cgf
        on cte_ca.data_own_chrg_grp_id = cte_cgf.data_root_chrg_grp_id
        left join cte_b
        on cte_ca.data_bill_id = cte_b.data_bill_id
        left join cte_rc
        on cte_ca.data_rev_cls_id = cte_rc.data_rev_cls_id
        left join cte_f
        on cte_ca.data_txn_fac_id = cte_f.data_fac_id
        left join cte_cg
        on cte_ca.data_bill_chrg_grp_id = cte_cg.data_chrg_grp_id
        left join cte_fp
        on cte_ca.data_folio_prfl_id = cte_fp.data_folio_prfl_id
)
select
    *
from
    final_cte
