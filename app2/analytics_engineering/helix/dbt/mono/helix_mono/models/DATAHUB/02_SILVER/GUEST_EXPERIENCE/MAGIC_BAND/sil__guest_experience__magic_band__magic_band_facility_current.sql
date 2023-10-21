with cte_xb_dsny_fac as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
cte_xb_dsny_fac_typ as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
cte_xb_addr as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__addr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
cte_xb_cntry as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__cntry_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
cte_parent_facility as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
cte_child_facility as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final as (
    select
        distinct xb_dsny_fac.data_dsny_fac_id as facility_id,
        xb_dsny_fac.data_fac_id as enterprise_facility_id,
        xb_dsny_fac.data_dsny_fac_nm as facility_name,
        xb_dsny_fac.data_ship_ctct_id as shipment_contact_id,
        xb_dsny_fac.data_dsny_fac_avail_for_bulk_ord_in as available_for_bulk_order_indicator,
        xb_dsny_fac.data_dsny_fac_for_rcv_gst_ord_in as guest_order_indicator,
        xb_dsny_fac.data_rl_asgn_fac_in as role_assignment_facility_indicator,
        xb_dsny_fac.data_addr_id as address_id,
        xb_cntry.data_cntry_id as country_id,
        xb_cntry.data_cntry_cd as country_code,
        xb_cntry.data_cnty_iso3166_alpha3_cd as country_iso_3166_alpha_3_code,
        xb_cntry.data_cntry_nm as country_name,
        xb_addr.data_addr1_tx as address_1_value,
        xb_addr.data_addr2_tx as address_2_value,
        xb_addr.data_addr3_tx as address_3_value,
        xb_addr.data_addr4_tx as address_4_value,
        xb_addr.data_addr_cty_nm as city_name,
        xb_addr.data_addr_st_nm as state_name,
        xb_addr.data_addr_pstl_cd as postal_code,
        xb_addr.data_exprnc_band_rcpnt_phn_nb as recipient_phone_number,
        xb_addr.data_exprnc_band_rcpnt_nm as recipient_name,
        xb_dsny_fac.data_dsny_fac_typ_id as facility_type_id,
        xb_dsny_fac_typ.data_dsny_fac_typ_cd as facility_type_code,
        xb_dsny_fac_typ.data_dsny_fac_typ_ds as facility_type_description,
        parent_facility.data_prnt_dsny_fac_id as parent_facility_id,
        child_facility.data_chld_dsny_fac_id as child_facility_id,
        xb_dsny_fac.data_logical_del_in as source_system_logical_delete_indicator,
        xb_dsny_fac.data_create_usr_id as source_system_create_user_id,
        xb_dsny_fac.data_create_dts as source_system_create_datetime,
        xb_dsny_fac.data_updt_usr_id as source_system_update_user_id,
        xb_dsny_fac.data_updt_dts as source_system_update_datetime
    from
        cte_xb_dsny_fac as xb_dsny_fac
        inner join cte_xb_dsny_fac_typ as xb_dsny_fac_typ
        on xb_dsny_fac.data_dsny_fac_typ_id = xb_dsny_fac_typ.data_dsny_fac_typ_id
        left outer join cte_xb_addr as xb_addr
        on xb_dsny_fac.data_addr_id = xb_addr.data_addr_id
        left outer join cte_xb_cntry as xb_cntry
        on xb_addr.data_cntry_id = xb_cntry.data_cntry_id
        left outer join cte_parent_facility as parent_facility
        on xb_dsny_fac.data_dsny_fac_id = parent_facility.data_prnt_dsny_fac_id
        left outer join cte_child_facility as child_facility
        on xb_dsny_fac.data_dsny_fac_id = child_facility.data_chld_dsny_fac_id
)

select * from final
