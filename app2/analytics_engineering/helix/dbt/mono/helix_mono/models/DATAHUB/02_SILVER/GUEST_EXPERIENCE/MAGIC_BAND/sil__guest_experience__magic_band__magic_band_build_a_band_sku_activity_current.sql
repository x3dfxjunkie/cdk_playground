-- define a cte for build_band_sku
with build_band_sku_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__build_band_sku_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for build_band_sku_actvy
build_band_sku_actvy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__build_band_sku_actvy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_dsny_prod
exprnc_band_dsny_prod_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_prod_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_typ
exprnc_band_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for top_color
top_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for bottom_color
bottom_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- join the ctes to get the final result
final as (
    select
        build_band_sku.data_build_band_sku_id as build_band_sku_id,
        build_band_sku.data_exprnc_band_dsny_prod_id as product_id,
        exprnc_band_dsny_prod.data_exprnc_band_typ_id as product_type_id,
        exprnc_band_typ.data_exprnc_band_typ_cd as product_type_code,
        exprnc_band_typ.data_exprnc_band_typ_ds as product_type_description,
        exprnc_band_dsny_prod.data_exprnc_band_top_color_id as top_color_id,
        top_color.data_exprnc_band_color_cd as top_color_code,
        top_color.data_exprnc_band_color_nm as top_color_name,
        exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id as bottom_color_id,
        bottom_color.data_exprnc_band_color_cd as bottom_color_code,
        bottom_color.data_exprnc_band_color_nm as bottom_color_name,
        build_band_sku.data_build_band_sku_cd as sku_code,
        build_band_sku.data_build_band_sku_type as sku_type,
        build_band_sku_actvy.data_build_band_sku_actvy_id as sku_activity_id,
        build_band_sku_actvy.data_build_band_sku_del_in as sku_deleted_indicator,
        build_band_sku_actvy.data_create_dts as activity_create_datetime,
        build_band_sku.data_create_usr_id as source_system_create_user_id,
        build_band_sku.data_create_dts as source_system_create_datetime,
        build_band_sku.data_updt_usr_id as source_system_update_user_id,
        build_band_sku.data_updt_dts as source_system_update_datetime,
        build_band_sku.data_logical_del_in as source_system_logical_delete_indicator
    from
        build_band_sku_cte build_band_sku
        left outer join build_band_sku_actvy_cte build_band_sku_actvy
        on build_band_sku_actvy.data_exprnc_band_dsny_prod_id = build_band_sku.data_exprnc_band_dsny_prod_id
        and build_band_sku_actvy.data_build_band_sku_cd = build_band_sku.data_build_band_sku_cd
        left outer join exprnc_band_dsny_prod_cte exprnc_band_dsny_prod
        on exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id = build_band_sku.data_exprnc_band_dsny_prod_id
        left outer join exprnc_band_typ_cte exprnc_band_typ
        on exprnc_band_typ.data_exprnc_band_typ_id = exprnc_band_dsny_prod.data_exprnc_band_typ_id
        left outer join top_color_cte top_color
        on top_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_top_color_id
        left outer join bottom_color_cte bottom_color
        on bottom_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id
) -- select from the final result gcte
select
    *
from
    final
