-- define a cte for xb_exprnc_band_req
with xb_exprnc_band_req_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for xb_exprnc_band_req_rsn
xb_exprnc_band_req_rsn_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_rsn_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for xb_exprnc_band_req_sts
xb_exprnc_band_req_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for xb_exprnc_band_req_sts_ctgy
xb_exprnc_band_req_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for xb_ship_srvc
xb_ship_srvc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__ship_srvc_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for xb_exprnc_band_req_typ
xb_exprnc_band_req_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for xb_addr
xb_addr_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__addr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for xb_cntry
xb_cntry_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__cntry_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for xb_exprnc_band_req_lnk
xb_exprnc_band_req_lnk_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for parent_request
parent_request_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for parent_request_type
parent_request_type_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for parent_request_reason
parent_request_reason_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_rsn_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for parent_request_status
parent_request_status_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for parent_request_status_category
parent_request_status_category_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- join ctes to get the final result
final as (
    select
        xb_exprnc_band_req.data_exprnc_band_req_id as request_id,
        xb_exprnc_band_req.data_exprnc_band_req_uniq_id as request_unique_identifier,
        xb_exprnc_band_req_lnk.data_prnt_exprnc_band_req_id as parent_request_id,
        parent_request.data_exprnc_band_req_uniq_id as parent_request_unique_identifier,
        xb_exprnc_band_req.data_ship_srvc_id as shipping_service_id,
        xb_ship_srvc.data_ship_srvc_cd as shipping_service_code,
        xb_ship_srvc.data_ship_srvc_fflmt_vndr_cd as shipping_service_fulfillment_vendor_code,
        xb_ship_srvc.data_ship_srvc_ds as shipping_service_description,
        xb_ship_srvc.data_ship_srvc_dlvr_di as shipping_service_delivery_date_interval,
        xb_exprnc_band_req.data_exprnc_band_req_typ_id as request_type_id,
        xb_exprnc_band_req_typ.data_exprnc_band_req_typ_cd as request_type_code,
        xb_exprnc_band_req_typ.data_exprnc_band_req_typ_ds as request_type_description,
        xb_exprnc_band_req.data_addr_id as address_id,
        xb_addr.data_cntry_id as country_id,
        xb_cntry.data_cntry_cd as country_code,
        xb_cntry.data_cnty_iso3166_alpha3_cd as country_iso_3166_alpha_3_code,
        xb_cntry.data_cntry_nm as country_name,
        xb_addr.data_addr1_tx as address_1_value,
        xb_addr.data_addr2_tx as address_2_value,
        xb_addr.data_addr3_tx as address_3_value,
        xb_addr.data_addr4_tx as address_4_value,
        xb_addr.data_addr_cty_nm as address_city_name,
        xb_addr.data_addr_st_nm as address_state_name,
        xb_addr.data_addr_pstl_cd as address_postal_code,
        xb_addr.data_exprnc_band_rcpnt_phn_nb as recipient_phone_number,
        xb_addr.data_exprnc_band_rcpnt_nm as recipient_name,
        xb_exprnc_band_req.data_exprnc_band_req_rsn_id as request_reason_id,
        xb_exprnc_band_req_rsn.data_exprnc_band_req_rsn_cd as reason_code,
        xb_exprnc_band_req_rsn.data_exprnc_band_req_rsn_ds as reason_description,
        xb_exprnc_band_req.data_exprnc_band_addr_confirmed_in as address_confirmed_indicator,
        xb_exprnc_band_req.data_curr_exprnc_band_req_sts_id as current_request_status_id,
        xb_exprnc_band_req_sts.data_exprnc_band_req_sts_ctgy_id as status_category_id,
        xb_exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_cd as status_category_code,
        xb_exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_ds as status_category_description,
        xb_exprnc_band_req_sts.data_exprnc_band_req_sts_cd as status_code,
        xb_exprnc_band_req_sts.data_exprnc_band_req_sts_ds as status_description,
        parent_request.data_exprnc_band_req_typ_id as parent_request_type_id,
        parent_request_type.data_exprnc_band_req_typ_cd as parent_request_type_code,
        parent_request_type.data_exprnc_band_req_typ_ds as parent_request_type_description,
        parent_request.data_exprnc_band_req_rsn_id as parent_request_reason_id,
        parent_request_reason.data_exprnc_band_req_rsn_cd as parent_request_reason_code,
        parent_request_reason.data_exprnc_band_req_rsn_ds as parent_request_reason_description,
        parent_request.data_curr_exprnc_band_req_sts_id as current_parent_request_status_id,
        parent_request_status.data_exprnc_band_req_sts_ctgy_id as parent_request_status_category_id,
        parent_request_status_category.data_exprnc_band_req_sts_ctgy_cd as parent_request_status_category_code,
        parent_request_status_category.data_exprnc_band_req_sts_ctgy_ds as parent_request_status_category_description,
        parent_request_status.data_exprnc_band_req_sts_cd as parent_request_status_code,
        parent_request_status.data_exprnc_band_req_sts_ds as parent_request_status_description,
        xb_exprnc_band_req.data_create_usr_id as source_system_create_user_id,
        xb_exprnc_band_req.data_create_dts as source_system_create_datetime,
        xb_exprnc_band_req.data_updt_usr_id as source_system_update_user_id,
        xb_exprnc_band_req.data_updt_dts as source_system_update_datetime,
        xb_exprnc_band_req.data_logical_del_in as source_system_logical_delete_indicator
    from
        xb_exprnc_band_req_cte xb_exprnc_band_req
        join xb_exprnc_band_req_rsn_cte xb_exprnc_band_req_rsn
        on xb_exprnc_band_req_rsn.data_exprnc_band_req_rsn_id = xb_exprnc_band_req.data_exprnc_band_req_rsn_id
        join xb_exprnc_band_req_sts_cte xb_exprnc_band_req_sts
        on xb_exprnc_band_req_sts.data_exprnc_band_req_sts_id = xb_exprnc_band_req.data_curr_exprnc_band_req_sts_id
        join xb_exprnc_band_req_sts_ctgy_cte xb_exprnc_band_req_sts_ctgy
        on xb_exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_id = xb_exprnc_band_req_sts.data_exprnc_band_req_sts_ctgy_id
        left outer join xb_ship_srvc_cte xb_ship_srvc
        on xb_ship_srvc.data_ship_srvc_id = xb_exprnc_band_req.data_ship_srvc_id
        join xb_exprnc_band_req_typ_cte xb_exprnc_band_req_typ
        on xb_exprnc_band_req_typ.data_exprnc_band_req_typ_id = xb_exprnc_band_req.data_exprnc_band_req_typ_id
        left outer join xb_addr_cte xb_addr
        on xb_addr.data_addr_id = xb_exprnc_band_req.data_addr_id
        left outer join xb_cntry_cte xb_cntry
        on xb_cntry.data_cntry_id = xb_addr.data_cntry_id
        left outer join xb_exprnc_band_req_lnk_cte xb_exprnc_band_req_lnk
        on xb_exprnc_band_req_lnk.data_exprnc_band_req_id = xb_exprnc_band_req.data_exprnc_band_req_id
        left outer join parent_request_cte parent_request
        on parent_request.data_exprnc_band_req_id = xb_exprnc_band_req_lnk.data_prnt_exprnc_band_req_id
        left outer join parent_request_type_cte parent_request_type
        on parent_request_type.data_exprnc_band_req_typ_id = parent_request.data_exprnc_band_req_typ_id
        left outer join parent_request_reason_cte parent_request_reason
        on parent_request_reason.data_exprnc_band_req_rsn_id = parent_request.data_exprnc_band_req_rsn_id
        left outer join parent_request_status_cte parent_request_status
        on parent_request_status.data_exprnc_band_req_sts_id = parent_request.data_curr_exprnc_band_req_sts_id
        left outer join parent_request_status_category_cte parent_request_status_category
        on parent_request_status_category.data_exprnc_band_req_sts_ctgy_id = parent_request_status.data_exprnc_band_req_sts_ctgy_id
)
select
    *
from
    final
