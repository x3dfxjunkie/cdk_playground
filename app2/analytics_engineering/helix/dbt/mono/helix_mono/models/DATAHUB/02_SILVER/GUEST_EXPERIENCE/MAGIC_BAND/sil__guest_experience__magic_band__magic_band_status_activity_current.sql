-- define a cte for exprnc_band_sts_actv
with exprnc_band_sts_actv_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_sts_actvy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_sts
exprnc_band_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_sts_ctgy
exprnc_band_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for ffld_exprnc_band
ffld_exprnc_band_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__ffld_exprnc_band_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band
exprnc_band_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_versioned') }}
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
-- join ctes to get the final result
final as (
    select
        exprnc_band_sts_actv.data_exprnc_band_sts_actvy_id as magic_band_status_activity_id,
        exprnc_band_sts_actv.data_exprnc_band_sts_id as status_id,
        exprnc_band_sts.data_exprnc_band_sts_cd as status_code,
        exprnc_band_sts.data_exprnc_band_sts_ds as status_description,
        exprnc_band_sts.data_exprnc_band_sts_ctgy_id as status_category_id,
        exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_cd as status_category_code,
        exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_ds as status_category_description,
        exprnc_band_sts_actv.data_ffld_exprnc_band_id as fulfilled_magic_band_id,
        ffld_exprnc_band.data_exprnc_band_id as magic_band_id,
        exprnc_band.data_exprnc_band_uniq_id as magic_band_unique_id,
        exprnc_band.data_exprnc_band_dsny_prod_id as product_id,
        exprnc_band_dsny_prod.data_exprnc_band_typ_id as product_type_id,
        exprnc_band_typ.data_exprnc_band_typ_cd as product_type_code,
        exprnc_band_typ.data_exprnc_band_typ_ds as product_type_description,
        exprnc_band_dsny_prod.data_exprnc_band_top_color_id as top_color_id,
        top_color.data_exprnc_band_color_cd as top_color_code,
        top_color.data_exprnc_band_color_nm as top_color_name,
        exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id as bottom_color_id,
        bottom_color.data_exprnc_band_color_cd as bottom_color_code,
        bottom_color.data_exprnc_band_color_nm as bottom_color_name,
        exprnc_band_sts_actv.data_exprnc_band_txn_id as magic_band_transaction_id,
        exprnc_band_sts_actv.data_exprnc_band_sts_chng_rsn_tx as status_change_reason_value,
        exprnc_band_sts_actv.data_exprnc_band_sts_updt_dts as status_update_datetime,
        cast(
            exprnc_band_sts_actv.data_exprnc_band_sts_updt_dts as date
        ) as status_update_date,
        cast(
            exprnc_band_sts_actv.data_exprnc_band_sts_updt_dts as time
        ) as status_update_time,
        exprnc_band_sts_actv.data_create_usr_id as source_system_create_user_id,
        exprnc_band_sts_actv.data_create_dts as source_system_create_datetime,
        exprnc_band_sts_actv.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_sts_actv.data_updt_dts as source_system_update_datetime,
        exprnc_band_sts_actv.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_sts_actv_cte exprnc_band_sts_actv
        inner join exprnc_band_sts_cte exprnc_band_sts
        on exprnc_band_sts_actv.data_exprnc_band_sts_id = exprnc_band_sts.data_exprnc_band_sts_id
        inner join exprnc_band_sts_ctgy_cte exprnc_band_sts_ctgy
        on exprnc_band_sts.data_exprnc_band_sts_ctgy_id = exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_id
        inner join ffld_exprnc_band_cte ffld_exprnc_band
        on exprnc_band_sts_actv.data_ffld_exprnc_band_id = ffld_exprnc_band.data_ffld_exprnc_band_id
        inner join exprnc_band_cte exprnc_band
        on ffld_exprnc_band.data_exprnc_band_id = exprnc_band.data_exprnc_band_id
        left join exprnc_band_dsny_prod_cte exprnc_band_dsny_prod
        on exprnc_band.data_exprnc_band_dsny_prod_id = exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id
        left join exprnc_band_typ_cte exprnc_band_typ
        on exprnc_band_dsny_prod.data_exprnc_band_typ_id = exprnc_band_typ.data_exprnc_band_typ_id
        left join top_color_cte top_color
        on exprnc_band_dsny_prod.data_exprnc_band_top_color_id = top_color.data_exprnc_band_color_id
        left join bottom_color_cte bottom_color
        on exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id = bottom_color.data_exprnc_band_color_id
)
select
    *
from
    final
