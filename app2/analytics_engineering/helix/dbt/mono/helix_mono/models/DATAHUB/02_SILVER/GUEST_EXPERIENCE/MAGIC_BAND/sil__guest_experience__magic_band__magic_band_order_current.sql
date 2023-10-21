with exprnc_band_ord_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_versioned') }}
),
exprnc_band_req_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_req_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_req_rsn_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_rsn_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_req_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_req_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_fflmt_ord_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_fflmt_ord_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_fflmt_ord_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_fflmt_ord_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_vndr_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_vndr_rl_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_rl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
vendor_ship_ctct_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__ship_ctct_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
order_ship_svc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__ship_srvc_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
dsny_fac_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
disney_fac_addr_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__addr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
disney_fac_cntry_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__cntry_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
dsny_fac_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
ship_ctct_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__ship_ctct_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_ord_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_ord_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
ord_address_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__addr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
ord_cntry_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__cntry_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final as (
    select
        exprnc_band_ord.data_exprnc_band_ord_id as order_id,
        exprnc_band_ord.data_exprnc_band_req_id as request_id,
        exprnc_band_req.data_exprnc_band_req_typ_id as request_type_id,
        exprnc_band_req_typ.data_exprnc_band_req_typ_cd as request_type_code,
        exprnc_band_req_typ.data_exprnc_band_req_typ_ds as request_type_description,
        exprnc_band_req.data_exprnc_band_req_rsn_id as request_reason_id,
        exprnc_band_req_rsn.data_exprnc_band_req_rsn_cd as request_reason_code,
        exprnc_band_req_rsn.data_exprnc_band_req_rsn_ds as request_reason_description,
        exprnc_band_req.data_curr_exprnc_band_req_sts_id as current_request_status_id,
        exprnc_band_req_sts.data_exprnc_band_req_sts_ctgy_id as current_request_status_category_id,
        exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_cd as current_request_status_category_code,
        exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_ds as current_request_status_category_description,
        exprnc_band_req_sts.data_exprnc_band_req_sts_cd as current_request_status_code,
        exprnc_band_req_sts.data_exprnc_band_req_sts_ds as current_request_status_description,
        exprnc_band_ord.data_exprnc_band_fflmt_ord_id as fulfillment_order_id,
        exprnc_band_fflmt_ord.data_exprnc_band_vndr_id as fulfillment_vendor_id,
        exprnc_band_vndr.data_exprnc_band_vndr_rl_id as vendor_role_id,
        exprnc_band_vndr_rl.data_exprnc_band_vndr_rl_cd as vendor_role_code,
        exprnc_band_vndr_rl.data_exprnc_band_vndr_rl_ds as vendor_role_description,
        exprnc_band_vndr.data_ship_ctct_id as vendor_shipment_contact_id,
        vendor_ship_ctct.data_ship_ctct_full_nm as vendor_shipment_contact_full_name,
        vendor_ship_ctct.data_ship_ctct_ttl_nm as vendor_shipment_contact_title_name,
        vendor_ship_ctct.data_ship_ctct_eml_addr_tx as vendor_shipment_contact_email_address_value,
        exprnc_band_vndr.data_exprnc_band_vndr_nm as vendor_name,
        exprnc_band_vndr.data_exprnc_band_vndr_cd as vendor_code,
        exprnc_band_vndr.data_exprnc_band_vndr_avail_po_in as vendor_available_purchase_order_indicator,
        exprnc_band_vndr.data_sap_id as vendor_sap_id,
        exprnc_band_vndr.data_gst_ship_strt_ti as vendor_guest_shipment_start_day_count,
        exprnc_band_vndr.data_gst_ship_end_ti as vendor_guest_shipment_end_day_count,
        exprnc_band_fflmt_ord.data_exprnc_band_fflmt_ord_sts_id as fulfillment_order_status_id,
        exprnc_band_fflmt_ord_sts.data_exprnc_band_fflmt_ord_sts_cd as fulfillment_order_status_code,
        exprnc_band_fflmt_ord_sts.data_exprnc_band_fflmt_ord_sts_ds as fulfillment_order_status_description,
        exprnc_band_fflmt_ord.data_exprnc_band_fflmt_ord_submt_dt as fulfillment_order_submit_date,
        exprnc_band_ord.data_ship_srvc_id as order_shipping_service_id,
        order_ship_svc.data_ship_srvc_cd as order_shipping_service_code,
        order_ship_svc.data_ship_srvc_fflmt_vndr_cd as order_shipping_fulfillment_vendor_code,
        order_ship_svc.data_ship_srvc_ds as order_shipping_service_description,
        order_ship_svc.data_ship_srvc_dlvr_di as order_shipping_service_delivery_date_interval,
        exprnc_band_ord.data_exprnc_band_ord_uniq_id as order_unique_identifier,
        exprnc_band_ord.data_addr_id as order_address_id,
        ord_address.data_cntry_id as order_country_id,
        ord_cntry.data_cntry_cd as order_country_code,
        ord_cntry.data_cnty_iso3166_alpha3_cd as order_country_iso_3166_alpha_3_code,
        ord_cntry.data_cntry_nm as order_country_name,
        ord_address.data_addr1_tx as order_address_1_value,
        ord_address.data_addr2_tx as order_address_2_value,
        ord_address.data_addr3_tx as order_address_3_value,
        ord_address.data_addr4_tx as order_address_4_value,
        ord_address.data_addr_cty_nm as order_city_name,
        ord_address.data_addr_st_nm as order_state_name,
        ord_address.data_addr_pstl_cd as order_postal_code,
        ord_address.data_exprnc_band_rcpnt_phn_nb as order_recipient_phone_number,
        ord_address.data_exprnc_band_rcpnt_nm as order_recipient_name,
        exprnc_band_ord.data_rsrt_shipmt_dsny_fac_id as resort_shipment_facility_id,
        dsny_fac.data_addr_id as facility_address_id,
        disney_fac_addr.data_cntry_id as facility_country_id,
        disney_fac_cntry.data_cntry_cd as facility_country_code,
        disney_fac_cntry.data_cnty_iso3166_alpha3_cd as facility_country_iso_3166_alpha_3_code,
        disney_fac_cntry.data_cntry_nm as facility_country_name,
        disney_fac_addr.data_addr1_tx as facility_address_1_value,
        disney_fac_addr.data_addr2_tx as facility_address_2_value,
        disney_fac_addr.data_addr3_tx as facility_address_3_value,
        disney_fac_addr.data_addr4_tx as facility_address_4_value,
        disney_fac_addr.data_addr_cty_nm as facility_city_name,
        disney_fac_addr.data_addr_st_nm as facility_state_name,
        disney_fac_addr.data_addr_pstl_cd as facility_postal_code,
        disney_fac_addr.data_exprnc_band_rcpnt_phn_nb as facility_recipient_phone_number,
        disney_fac_addr.data_exprnc_band_rcpnt_nm as facility_recipient_name,
        dsny_fac.data_dsny_fac_typ_id as facility_type_id,
        dsny_fac_typ.data_dsny_fac_typ_cd as facility_type_code,
        dsny_fac_typ.data_dsny_fac_typ_ds as facility_type_description,
        dsny_fac.data_ship_ctct_id as facility_shipment_contact_id,
        ship_ctct.data_ship_ctct_full_nm as shipment_contact_full_name,
        ship_ctct.data_ship_ctct_ttl_nm as shipment_contact_title_name,
        ship_ctct.data_ship_ctct_eml_addr_tx as shipment_contact_email_address_value,
        dsny_fac.data_fac_id as enterprise_facility_id,
        dsny_fac.data_dsny_fac_nm as facility_name,
        dsny_fac.data_dsny_fac_avail_for_bulk_ord_in as facility_available_for_bulk_order_indicator,
        dsny_fac.data_dsny_fac_for_rcv_gst_ord_in as facility_guest_order_indicator,
        exprnc_band_ord.data_exprnc_band_ord_expect_ship_dt as order_expected_shipping_date,
        exprnc_band_ord.data_exprnc_band_ord_expect_dlvr_dt as order_expected_delivery_date,
        exprnc_band_ord.data_exprnc_band_ord_actl_dlvr_dt as order_actual_delivery_date,
        exprnc_band_ord.data_curr_exprnc_band_ord_sts_id as order_status_id,
        exprnc_band_ord_sts.data_exprnc_band_ord_sts_ctgy_id as order_status_category_id,
        exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_cd as order_status_category_code,
        exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_ds as order_status_category_description,
        exprnc_band_ord_sts.data_exprnc_band_ord_sts_cd as order_status_code,
        exprnc_band_ord_sts.data_exprnc_band_ord_sts_ds as order_status_description,
        exprnc_band_ord.data_create_usr_id as source_system_create_user_id,
        exprnc_band_ord.data_create_dts as source_system_create_datetime,
        exprnc_band_ord.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_ord.data_updt_dts as source_system_update_datetime,
        exprnc_band_ord.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_ord_cte exprnc_band_ord
        left outer join exprnc_band_req_cte exprnc_band_req
        on exprnc_band_ord.data_exprnc_band_req_id = exprnc_band_req.data_exprnc_band_req_id
        left outer join exprnc_band_req_typ_cte exprnc_band_req_typ
        on exprnc_band_req_typ.data_exprnc_band_req_typ_id = exprnc_band_req.data_exprnc_band_req_typ_id
        left outer join exprnc_band_req_rsn_cte exprnc_band_req_rsn
        on exprnc_band_req_rsn.data_exprnc_band_req_rsn_id = exprnc_band_req.data_exprnc_band_req_rsn_id
        left outer join exprnc_band_req_sts_cte exprnc_band_req_sts
        on exprnc_band_req_sts.data_exprnc_band_req_sts_id = exprnc_band_req.data_curr_exprnc_band_req_sts_id
        left outer join exprnc_band_req_sts_ctgy_cte exprnc_band_req_sts_ctgy
        on exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_id = exprnc_band_req_sts.data_exprnc_band_req_sts_ctgy_id
        left outer join exprnc_band_fflmt_ord_cte exprnc_band_fflmt_ord
        on exprnc_band_fflmt_ord.data_exprnc_band_fflmt_ord_id = exprnc_band_ord.data_exprnc_band_fflmt_ord_id
        left outer join exprnc_band_fflmt_ord_sts_cte exprnc_band_fflmt_ord_sts
        on exprnc_band_fflmt_ord_sts.data_exprnc_band_fflmt_ord_sts_id = exprnc_band_fflmt_ord.data_exprnc_band_fflmt_ord_sts_id
        left outer join exprnc_band_vndr_cte exprnc_band_vndr
        on exprnc_band_vndr.data_exprnc_band_vndr_id = exprnc_band_fflmt_ord.data_exprnc_band_vndr_id
        left outer join exprnc_band_vndr_rl_cte exprnc_band_vndr_rl
        on exprnc_band_vndr_rl.data_exprnc_band_vndr_rl_id = exprnc_band_vndr.data_exprnc_band_vndr_rl_id
        left outer join vendor_ship_ctct_cte vendor_ship_ctct
        on vendor_ship_ctct.data_ship_ctct_id = exprnc_band_vndr.data_ship_ctct_id
        left outer join order_ship_svc_cte order_ship_svc
        on order_ship_svc.data_ship_srvc_id = exprnc_band_ord.data_ship_srvc_id
        left outer join dsny_fac_cte dsny_fac
        on dsny_fac.data_dsny_fac_id = exprnc_band_ord.data_rsrt_shipmt_dsny_fac_id
        left outer join disney_fac_addr_cte disney_fac_addr
        on disney_fac_addr.data_addr_id = dsny_fac.data_addr_id
        left outer join disney_fac_cntry_cte disney_fac_cntry
        on disney_fac_cntry.data_cntry_id = disney_fac_addr.data_cntry_id
        left outer join dsny_fac_typ_cte dsny_fac_typ
        on dsny_fac_typ.data_dsny_fac_typ_id = dsny_fac.data_dsny_fac_typ_id
        left outer join ship_ctct_cte ship_ctct
        on ship_ctct.data_ship_ctct_id = dsny_fac.data_ship_ctct_id
        left outer join exprnc_band_ord_sts_cte exprnc_band_ord_sts
        on exprnc_band_ord_sts.data_exprnc_band_ord_sts_id = exprnc_band_ord.data_curr_exprnc_band_ord_sts_id
        left outer join exprnc_band_ord_sts_ctgy_cte exprnc_band_ord_sts_ctgy
        on exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_id = exprnc_band_ord_sts.data_exprnc_band_ord_sts_ctgy_id
        left outer join ord_address_cte ord_address
        on ord_address.data_addr_id = exprnc_band_ord.data_addr_id
        left outer join ord_cntry_cte ord_cntry
        on ord_cntry.data_cntry_id = ord_address.data_cntry_id
)
select * from final
