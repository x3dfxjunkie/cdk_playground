-- define a cte for tacc
with tacc_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__trvl_agcy_chrg_com_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for tacm
tacm_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__ta_acm_comm_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for rc
rc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__rev_cls_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for sa
sa_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__sap_acct_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for sc
sc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__sap_co_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for sba
sba_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__sap_bus_area_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for scc
scc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__sap_cost_ctr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- join tacc, tacm, rc, sa, sc, sba and scc ctes to get the final result
final as (
    select
        tacc.data_trvl_agcy_chrg_comm_id as travel_agency_charge_commission_id,
        tacc.data_trvl_agcy_comm_id as travel_agency_commission_id,
        tacm.data_fac_id as facility_id,
        null as facility_name,
        tacm.data_acm_comm_strt_dt as accommodation_commission_start_date,
        tacm.data_acm_comm_end_dt as accommodation_commission_end_date,
        tacc.data_chrg_id as charge_id,
        tacc.data_rev_cls_id as revenue_class_id,
        rc.data_rev_cls_nm as revenue_class_name,
        tacc.data_pkg_id as package_id,
        tacc.data_chrg_unit_cn as charge_unit_count,
        tacm.data_rm_id_vl as room_number,
        tacc.data_comm_unit_ds as commission_unit_description,
        tacc.data_base_chrg_am as base_charge_amount,
        tacc.data_ptntl_comm_am as potential_commission_amount,
        tacc.data_calc_comm_am as calculated_commission_amount,
        tacc.data_pd_comm_am as paid_commission_amount,
        tacc.data_sap_gl_acct_nb as sap_general_ledger_account_number,
        sa.data_sap_gl_acct_nm as sap_general_ledger_account_name,
        tacc.data_sap_co_cd as sap_company_code,
        sc.data_sap_co_nm as sap_company_name,
        tacc.data_sap_bus_area_cd as sap_business_area_code,
        sba.data_sap_bus_area_nm as sap_business_area_name,
        tacc.data_sap_cost_ctr_cd as sap_cost_center_code,
        null as sap_cost_center_name,
        tacc.data_create_usr_id_cd as create_user_id,
        tacc.data_create_dts as create_datetime,
        to_date(
            tacc.data_create_dts
        ) as create_date,
        tacc.data_updt_usr_id_cd as source_update_user_id,
        tacc.data_updt_dts as source_update_datetime,
        to_date(
            tacc.data_updt_dts
        ) as source_update_date
    from
        tacc_cte tacc
        left join tacm_cte tacm
        on tacc.data_trvl_agcy_chrg_comm_id = tacm.data_trvl_agcy_acm_comm_id
        left join rc_cte rc
        on tacc.data_rev_cls_id = rc.data_rev_cls_id
        left join sa_cte sa
        on tacc.data_sap_gl_acct_nb = sa.data_sap_gl_acct_nb
        left join sc_cte sc
        on tacc.data_sap_co_cd = sc.data_sap_co_cd
        left join sba_cte sba
        on tacc.data_sap_bus_area_cd = sba.data_sap_bus_area_cd
        left join scc_cte scc
        on tacc.data_sap_cost_ctr_cd = scc.data_sap_cost_ctr_cd
) -- select from the final result cte
select
    *
from
    final
