-- define a cte for exprnc_band_req_sts_actv
with exprnc_band_req_sts_actv_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_actvy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_req
exprnc_band_req_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_req_sts
exprnc_band_req_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_req_typ
exprnc_band_req_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_req_rsn
exprnc_band_req_rsn_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_rsn_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_req_sts_ctgy
exprnc_band_req_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
final as(
    select
        exprnc_band_req_sts_actv.data_exprnc_band_req_sts_actvy_id as request_status_activity_id,
        exprnc_band_req_sts_actv.data_exprnc_band_req_id as request_id,
        exprnc_band_req_sts_actv.data_exprnc_band_req_sts_id as request_status_id,
        exprnc_band_req_sts.data_exprnc_band_req_sts_cd as request_status_code,
        exprnc_band_req_sts.data_exprnc_band_req_sts_ds as request_status_description,
        exprnc_band_req_sts.data_exprnc_band_req_sts_ctgy_id as request_status_category_id,
        exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_cd as request_status_category_code,
        exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_ds as request_status_category_description,
        exprnc_band_req.data_exprnc_band_req_uniq_id as magic_band_request_unique_id,
        exprnc_band_req.data_ship_srvc_id as shipping_service_id,
        exprnc_band_req.data_addr_id as address_id,
        exprnc_band_req.data_exprnc_band_addr_confirmed_in as address_confirmed_indicator,
        exprnc_band_req.data_exprnc_band_req_typ_id as request_type_id,
        exprnc_band_req_typ.data_exprnc_band_req_typ_cd as request_type_code,
        exprnc_band_req_typ.data_exprnc_band_req_typ_ds as request_type_description,
        exprnc_band_req.data_exprnc_band_req_rsn_id as request_reason_id,
        exprnc_band_req_rsn.data_exprnc_band_req_rsn_cd as request_reason_code,
        exprnc_band_req_rsn.data_exprnc_band_req_rsn_ds as request_reason_description,
        exprnc_band_req_sts_actv.data_exprnc_band_req_sts_updt_dts as request_status_update_datetime,
        cast(
            exprnc_band_req_sts_actv.data_exprnc_band_req_sts_updt_dts as date
        ) as request_status_update_date,
        cast(
            exprnc_band_req_sts_actv.data_exprnc_band_req_sts_updt_dts as time
        ) as request_status_update_time,
        exprnc_band_req_sts_actv.data_create_usr_id as source_system_create_user_id,
        exprnc_band_req_sts_actv.data_create_dts as source_system_create_datetime,
        exprnc_band_req_sts_actv.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_req_sts_actv.data_updt_dts as source_system_update_datetime,
        exprnc_band_req_sts_actv.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_req_sts_actv_cte exprnc_band_req_sts_actv
        inner join exprnc_band_req_cte exprnc_band_req
        on exprnc_band_req_sts_actv.data_exprnc_band_req_id = exprnc_band_req.data_exprnc_band_req_id
        inner join exprnc_band_req_sts_cte exprnc_band_req_sts
        on exprnc_band_req_sts_actv.data_exprnc_band_req_sts_id = exprnc_band_req_sts.data_exprnc_band_req_sts_id
        left join exprnc_band_req_typ_cte exprnc_band_req_typ
        on exprnc_band_req.data_exprnc_band_req_typ_id = exprnc_band_req_typ.data_exprnc_band_req_typ_id
        left join exprnc_band_req_rsn_cte exprnc_band_req_rsn
        on exprnc_band_req.data_exprnc_band_req_rsn_id = exprnc_band_req_rsn.data_exprnc_band_req_rsn_id
        left join exprnc_band_req_sts_ctgy_cte exprnc_band_req_sts_ctgy
        on exprnc_band_req_sts.data_exprnc_band_req_sts_ctgy_id = exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_id
)
select
    *
from
    final
