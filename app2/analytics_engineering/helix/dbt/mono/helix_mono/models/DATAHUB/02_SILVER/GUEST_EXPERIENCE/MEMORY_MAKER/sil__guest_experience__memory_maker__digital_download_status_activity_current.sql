-- define a cte for lvl_n_chng
with lvl_n_chng_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_chng_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for lvl_n_enttl_sts
lvl_n_enttl_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_enttl_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for revenue_status
revenue_status_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_enttl_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for lvl_n_enttl
lvl_n_enttl_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_enttl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- join the ctes to get the final result
final as (
    select
        lvl_n_chng.data_lvl_n_enttl_id as digital_download_entitlement_id,
        lvl_n_enttl.data_lvl_n_enttl_typ as entitlement_type,
        lvl_n_enttl.data_lvl_n_iss_typ_id as issue_type_id,
        lvl_n_enttl.data_tkt_void_typ_cd as ticket_void_type_code,
        cast(
            lvl_n_enttl.data_lvl_n_enttl_purch_dt as date
        ) as purchase_date,
        lvl_n_enttl.data_lvl_n_enttl_sls_price as sales_price,
        lvl_n_enttl.data_lvl_n_enttl_sls_tax as sales_tax,
        lvl_n_enttl.data_lvl_n_iss_rsn_tx as issue_reason_value,
        cast(
            lvl_n_enttl.data_rsrt_res_strt_dt as date
        ) as resort_reservation_start_date,
        cast(
            lvl_n_enttl.data_rsrt_res_end_dt as date
        ) as resort_reservation_end_date,
        lvl_n_chng.data_lvl_n_enttl_chng_dt as change_datetime,
        cast(
            lvl_n_chng.data_lvl_n_enttl_chng_dt as date
        ) as change_date,
        cast(
            lvl_n_chng.data_lvl_n_enttl_chng_dt as time
        ) as change_time,
        lvl_n_chng.data_lvl_n_enttl_sts_id as status_id,
        lvl_n_enttl_sts.data_lvl_n_enttl_sts_nm as status_name,
        lvl_n_chng.data_lvl_n_rl_id as guest_role_id,
        lvl_n_chng.data_lvl_n_lnk_id as guest_id,
        lvl_n_chng.data_lvl_n_enttl_strt_dt as entitlement_start_timestamp,
        cast(
            lvl_n_chng.data_lvl_n_enttl_strt_dt as date
        ) as entitlement_start_date,
        cast(
            lvl_n_chng.data_lvl_n_enttl_strt_dt as time
        ) as entitlement_start_time,
        cast(
            lvl_n_chng.data_lvl_n_enttl_end_dt as date
        ) as entitlement_end_date,
        cast(
            lvl_n_chng.data_lvl_n_enttl_exp_dt as date
        ) as entitlement_expiration_date,
        lvl_n_chng.data_settl_dt as settlement_datetime,
        cast(
            lvl_n_chng.data_settl_dt as date
        ) as settlement_date,
        cast(
            lvl_n_chng.data_settl_dt as time
        ) as settlement_time,
        lvl_n_chng.data_onln_engagement_dt as initial_online_engagement_datetime,
        cast(
            lvl_n_chng.data_onln_engagement_dt as date
        ) as initial_online_engagement_date,
        cast(
            lvl_n_chng.data_onln_engagement_dt as time
        ) as initial_online_engagement_time,
        cast(
            lvl_n_chng.data_lvl_n_captr_dt as date
        ) as initial_capture_date,
        lvl_n_chng.data_lvl_n_rdmpt_dt as redemption_datetime,
        cast(
            lvl_n_chng.data_lvl_n_rdmpt_dt as date
        ) as redemption_date,
        cast(
            lvl_n_chng.data_lvl_n_rdmpt_dt as date
        ) as redemption_time,
        lvl_n_chng.data_lvl_n_rvn_sts_id as entitlement_revenue_status_id,
        revenue_status.data_lvl_n_enttl_sts_nm as entitlement_revenue_status_name,
        lvl_n_chng.data_lvl_n_rvn_dts as entitlement_revenue_datetime,
        lvl_n_chng.data_lvl_n_rvn_in as entitlement_revenue_recognition_indicator,
        lvl_n_chng.data_create_dts as source_system_create_datetime,
        lvl_n_chng.data_create_usr_id as source_system_create_user_id,
        lvl_n_chng.data_updt_dts as source_system_update_datetime,
        lvl_n_chng.data_updt_usr_id as source_system_update_user_id,
        lvl_n_chng.data_lgcl_del_in as source_system_logical_delete_indicator
    from
        lvl_n_chng_cte lvl_n_chng
        join lvl_n_enttl_sts_cte lvl_n_enttl_sts
        on lvl_n_enttl_sts.data_lvl_n_enttl_sts_id = lvl_n_chng.data_lvl_n_enttl_sts_id
        join revenue_status_cte revenue_status
        on revenue_status.data_lvl_n_enttl_sts_id = lvl_n_chng.data_lvl_n_rvn_sts_id
        join lvl_n_enttl_cte lvl_n_enttl
        on lvl_n_enttl.data_lvl_n_enttl_id = lvl_n_chng.data_lvl_n_enttl_id
) -- select from the final result gcte
select
    *
from
    final
