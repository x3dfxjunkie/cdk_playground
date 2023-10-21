-- define a cte for exprnc_band_ord_sts_actv
with exprnc_band_ord_sts_actv_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_sts_actvy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_ord
exprnc_band_ord_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_ord_sts
exprnc_band_ord_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_ord_sts_ctgy
exprnc_band_ord_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- join ctes to get the final result
final as (
    select
        exprnc_band_ord_sts_actv.data_exprnc_band_ord_sts_actvy_id as order_status_activity_id,
        exprnc_band_ord_sts_actv.data_exprnc_band_ord_id as order_id,
        exprnc_band_ord.data_exprnc_band_ord_uniq_id as order_unique_identifier,
        exprnc_band_ord.data_exprnc_band_ord_expect_ship_dt as expected_ship_date,
        exprnc_band_ord.data_exprnc_band_ord_expect_dlvr_dt as expected_delivery_date,
        exprnc_band_ord.data_exprnc_band_ord_actl_dlvr_dt as actual_delivery_date,
        exprnc_band_ord_sts_actv.data_exprnc_band_ord_sts_id as order_status_id,
        exprnc_band_ord_sts.data_exprnc_band_ord_sts_cd as status_code,
        exprnc_band_ord_sts.data_exprnc_band_ord_sts_ds as status_description,
        exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_id as magic_band_order_status_category_id,
        exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_cd as category_code,
        exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_ds as category_description,
        exprnc_band_ord_sts_actv.data_exprnc_band_ord_sts_err_nb as status_error_number,
        exprnc_band_ord_sts_actv.data_exprnc_band_ord_sts_err_ds as status_error_description,
        exprnc_band_ord_sts_actv.data_exprnc_band_ord_sts_updt_dts as status_update_datetime,
        cast(
            exprnc_band_ord_sts_actv.data_exprnc_band_ord_sts_updt_dts as date
        ) as status_update_date,
        cast(
            exprnc_band_ord_sts_actv.data_exprnc_band_ord_sts_updt_dts as time
        ) as status_update_time,
        exprnc_band_ord_sts_actv.data_logical_del_in as source_system_logical_delete_indicator,
        exprnc_band_ord_sts_actv.data_create_usr_id as source_system_create_user_id,
        exprnc_band_ord_sts_actv.data_create_dts as source_system_create_datetime,
        exprnc_band_ord_sts_actv.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_ord_sts_actv.data_updt_dts as source_system_update_datetime
    from
        exprnc_band_ord_sts_actv_cte exprnc_band_ord_sts_actv
        inner join exprnc_band_ord_cte exprnc_band_ord
        on exprnc_band_ord_sts_actv.data_exprnc_band_ord_id = exprnc_band_ord.data_exprnc_band_ord_id
        inner join exprnc_band_ord_sts_cte exprnc_band_ord_sts
        on exprnc_band_ord_sts_actv.data_exprnc_band_ord_sts_id = exprnc_band_ord_sts.data_exprnc_band_ord_sts_id
        inner join exprnc_band_ord_sts_ctgy_cte exprnc_band_ord_sts_ctgy
        on exprnc_band_ord_sts.data_exprnc_band_ord_sts_ctgy_id = exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_id
)
select
    *
from
    final
