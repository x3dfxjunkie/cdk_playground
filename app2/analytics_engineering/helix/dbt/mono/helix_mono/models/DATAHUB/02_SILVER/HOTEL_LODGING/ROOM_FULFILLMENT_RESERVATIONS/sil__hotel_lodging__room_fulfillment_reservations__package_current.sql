-- define a cte for pkg
with pkg_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__pkg_t_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for p
p_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__prod_t_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for mp
mp_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__mkt_pkg_t_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- join ctes to get the final result
final as(
    select
        distinct pkg.data_pkg_id as package_id,
        mp.data_pkg_cd as market_package_code,
        pkg.data_pkg_prod_grp_nm as package_product_group_name,
        pkg.data_plan_typ_nm as package_plan_type_name,
        pkg.data_pkg_prod_comm_typ_nm as package_product_commission_type_name,
        pkg.data_hybrd_mkt_cd as hybrid_market_code,
        pkg.data_hybrd_mkt_long_nm as hybrid_market_long_name,
        pkg.data_mkt_offer_cd as market_offer_code,
        pkg.data_mkt_offer_nm as market_offer_name,
        pkg.data_pkg_actv_in as package_active_indicator,
        pkg.data_pkg_guar_in as package_guaranteed_indicator,
        pkg.data_pkg_prod_cls_nm as package_product_class_name,
        pkg.data_pkg_prod_grp_id as package_product_group_id,
        p.data_prod_id as product_id,
        p.data_prod_yr_nb as product_year_number,
        p.data_prod_typ_nm as product_type_name,
        p.data_prod_intrnl_nm as product_internal_name,
        p.data_prod_intrnl_ds as product_internal_description,
        p.data_prod_bkng_strt_dts as product_booking_start_dts,
        mp.data_pkg_min_nght_cn as package_minimum_night_count,
        mp.data_pkg_max_nght_cn as package_maximum_night_count,
        mp.data_pkg_rm_only_in as package_room_only_indicator,
        mp.data_pkg_rack_in as package_rack_indicator,
        mp.data_pkg_fsell_in as package_freesell_indicator,
        mp.data_arvl_base_in as arrival_based_pricing_indicator
    from
        pkg_cte pkg
        inner join p_cte p
        on pkg.data_pkg_id = p.data_prod_id
        left join mp_cte mp
        on pkg.data_pkg_id = mp.data_pkg_id
)

select * from final
