-- define a cte for lvl_n_enttl
with lvl_n_enttl_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_enttl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for cntnt_cache
cntnt_cache_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__cntnt_cache_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for lvl_n_iss_typ
lvl_n_iss_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_iss_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for lvl_n_enttl_lnk
lvl_n_enttl_lnk_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_enttl_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for lvl_n_rl
lvl_n_rl_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_rl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for lvl_n_rl_typ
lvl_n_rl_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_rl_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for lvl_n_rl_ctgy
lvl_n_rl_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__level__n_wdw__lvl_n_rl_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a final cte
final as(
    select
        distinct lvl_n_enttl.data_lvl_n_enttl_id as digital_download_entitlement_id,
        lvl_n_enttl_lnk.data_lvl_n_lnk_id as guest_id,
        lvl_n_enttl_lnk.data_lvl_n_enttl_lnk_strt_dt as guest_link_start_datetime,
        cast(
            lvl_n_enttl_lnk.data_lvl_n_enttl_lnk_strt_dt as date
        ) as guest_link_start_date,
        cast(
            lvl_n_enttl_lnk.data_lvl_n_enttl_lnk_strt_dt as time
        ) as guest_link_start_time,
        lvl_n_enttl_lnk.data_lvl_n_enttl_lnk_end_dt as guest_link_end_datetime,
        cast(
            lvl_n_enttl_lnk.data_lvl_n_enttl_lnk_end_dt as date
        ) as end_date,
        cast(
            lvl_n_enttl_lnk.data_lvl_n_enttl_lnk_end_dt as time
        ) as end_time,
        lvl_n_enttl_lnk.data_lvl_n_rl_id as guest_role_id,
        lvl_n_rl.data_lvl_n_rl_nm as guest_role_name,
        lvl_n_rl.data_lvl_n_rl_typ_id as guest_role_type_id,
        lvl_n_rl_typ.data_lvl_n_rl_typ_nm as guest_role_type_name,
        lvl_n_rl_typ.data_lvl_n_rl_ctgy_id as guest_role_category_id,
        lvl_n_rl_ctgy.data_lvl_n_rl_ctgy_nm as guest_role_category_name,
        lvl_n_enttl.data_lvl_n_enttl_typ as entitlement_type,
        lvl_n_enttl.data_cntnt_cache_id as product_content_id,
        cntnt_cache.data_entrprs_cntnt_typ_nm as enterprise_product_content_type_name,
        cntnt_cache.data_entrprs_cntnt_id as enterprise_product_content_id,
        cntnt_cache.data_cntnt_attr_nm as product_content_attribute_name,
        cntnt_cache.data_cntnt_attr_tx as product_content_attribute_value,
        lvl_n_enttl.data_lvl_n_iss_typ_id as issue_type_id,
        lvl_n_iss_typ.data_lvl_n_iss_typ_ds as issue_type_description,
        lvl_n_enttl.data_tkt_void_typ_cd as ticket_void_type_code,
        cast(
            lvl_n_enttl.data_lvl_n_enttl_purch_dt as date
        ) as purchase_date,
        cast(
            lvl_n_enttl.data_lvl_n_exp_dt as date
        ) as expiration_date,
        lvl_n_enttl.data_lvl_n_enttl_sls_price as sales_price,
        lvl_n_enttl.data_lvl_n_enttl_sls_tax as sales_tax,
        lvl_n_enttl.data_lvl_n_iss_rsn_tx as issue_reason_value,
        cast(
            lvl_n_enttl.data_rsrt_res_strt_dt as date
        ) as resort_reservation_start_date,
        cast(
            lvl_n_enttl.data_rsrt_res_end_dt as date
        ) as resort_reservation_end_date,
        lvl_n_enttl.data_create_usr_id as source_system_create_user_id,
        lvl_n_enttl.data_create_dts as source_system_create_datetime,
        lvl_n_enttl.data_updt_usr_id as source_system_update_user_id,
        lvl_n_enttl.data_updt_dts as source_system_update_datetime,
        lvl_n_enttl.data_lgcl_del_in as source_system_logical_delete_indicator
    from
        lvl_n_enttl_cte lvl_n_enttl
        join cntnt_cache_cte cntnt_cache
        on cntnt_cache.data_cntnt_cache_id = lvl_n_enttl.data_cntnt_cache_id
        join lvl_n_iss_typ_cte lvl_n_iss_typ
        on lvl_n_iss_typ.data_lvl_n_iss_typ_id = lvl_n_enttl.data_lvl_n_iss_typ_id
        join lvl_n_enttl_lnk_cte lvl_n_enttl_lnk
        on lvl_n_enttl_lnk.data_lvl_n_enttl_id = lvl_n_enttl.data_lvl_n_enttl_id
        join lvl_n_rl_cte lvl_n_rl
        on lvl_n_rl.data_lvl_n_rl_id = lvl_n_enttl_lnk.data_lvl_n_rl_id
        join lvl_n_rl_typ_cte lvl_n_rl_typ
        on lvl_n_rl_typ.data_lvl_n_rl_typ_id = lvl_n_rl.data_lvl_n_rl_typ_id
        join lvl_n_rl_ctgy_cte lvl_n_rl_ctgy
        on lvl_n_rl_ctgy.data_lvl_n_rl_ctgy_id = lvl_n_rl_typ.data_lvl_n_rl_ctgy_id
) -- select from the final result cte
select
    *
from
    final
