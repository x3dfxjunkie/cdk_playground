with
    cte_xbms_wdw_exprnc_band_vndr as (
        select
            *
        from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_versioned') }}
        where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'

    ),

    cte_xbms_wdw_exprnc_band_vndr_rl as (
        select
            *
        from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_rl_versioned') }}
        where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    ),

    cte_xbms_wdw_ship_ctct as (
        select
            *
        from  {{ ref('sil__intermediate__xbms__wdw__ship_ctct_versioned') }}
        where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    ),

    cte_xbms_wdw_addr as (
        select
            *
        from  {{ ref('sil__intermediate__xbms__wdw__addr_versioned') }}
        where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    ),

    cte_xbms_wdw_cntry as (
        select
           *
        from  {{ ref('sil__intermediate__xbms__wdw__cntry_versioned') }}
        where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    ),

    final_query as (
        select
            v.data_exprnc_band_vndr_id as vendor_id,
            v.data_exprnc_band_vndr_nm as vendor_name,
            v.data_exprnc_band_vndr_cd as vendor_code,
            v.data_exprnc_band_vndr_avail_po_in as vendor_available_purchase_order_indicator,
            v.data_sap_id as vendor_data_sap_id,
            v.data_gst_ship_strt_ti as guest_shipment_start_time,
            v.data_gst_ship_end_ti as guest_shipment_end_time,
            r.data_exprnc_band_vndr_rl_cd as vendor_role_code,
            r.data_exprnc_band_vndr_rl_ds as vendor_role_description,
            c.data_ship_ctct_full_nm as shipment_contact_full_name,
            c.data_ship_ctct_ttl_nm as shipment_contact_title_name,
            c.data_ship_ctct_eml_addr_tx as shipment_contact_email_address_value,
            a.data_addr1_tx as address_line_1,
            a.data_addr2_tx as address_line_2,
            a.data_addr3_tx as address_line_3,
            a.data_addr4_tx as address_line_4,
            a.data_addr_cty_nm as city_name,
            a.data_addr_st_nm as state_name,
            a.data_addr_pstl_cd as postal_code,
            a.data_exprnc_band_rcpnt_phn_nb as recepient_phone_number,
            a.data_exprnc_band_rcpnt_nm as recepient_name,
            cn.data_cntry_cd as country_code,
            cn.data_cnty_iso3166_alpha3_cd as country_iso_3166_alpha_3_code,
            cn.data_cntry_nm as country_name,
            v.data_logical_del_in as source_system_logical_delete_indicator,
            v.data_create_usr_id as source_system_create_user_id,
            v.data_create_dts as source_system_create_datetime,
            v.data_updt_usr_id as source_system_update_user_id,
            v.data_updt_dts as source_system_update_datetime
        from
            cte_xbms_wdw_exprnc_band_vndr v
            inner join cte_xbms_wdw_exprnc_band_vndr_rl r
            on v.data_exprnc_band_vndr_rl_id = r.data_exprnc_band_vndr_rl_id
            inner join cte_xbms_wdw_ship_ctct c
            on v.data_ship_ctct_id = c.data_ship_ctct_id
            inner join cte_xbms_wdw_addr a
            on v.data_addr_id = a.data_addr_id
            left outer join cte_xbms_wdw_cntry cn
            on a.data_cntry_id = cn.data_cntry_id
    )

select * from final_query
