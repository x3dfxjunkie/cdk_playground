with dsny_fac_band_invtry_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_band_invtry_versioned') }}
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
ffld_exprnc_band_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__ffld_exprnc_band_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
ffld_band_curr_fac_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_dsny_prod_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_prod_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
top_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
bottom_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
current_exprnc_band_lnk_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final as (
    select
        dsny_fac_band_invtry.data_dsny_fac_band_invtry_id as facility_band_inventory_id,
        dsny_fac_band_invtry.data_dsny_fac_id as facility_id,
        dsny_fac.data_addr_id as address_id,
        disney_fac_addr.data_cntry_id as country_id,
        disney_fac_cntry.data_cntry_cd as country_code,
        disney_fac_cntry.data_cnty_iso3166_alpha3_cd as country_iso_3166_alpha_3_code,
        disney_fac_cntry.data_cntry_nm as country_name,
        disney_fac_addr.data_addr1_tx as address_1_value,
        disney_fac_addr.data_addr2_tx as address_2_value,
        disney_fac_addr.data_addr3_tx as address_3_value,
        disney_fac_addr.data_addr4_tx as address_4_value,
        disney_fac_addr.data_addr_cty_nm as city_name,
        disney_fac_addr.data_addr_st_nm as state_name,
        disney_fac_addr.data_addr_pstl_cd as postal_code,
        disney_fac_addr.data_exprnc_band_rcpnt_phn_nb as recipient_phone_number,
        disney_fac_addr.data_exprnc_band_rcpnt_nm as recipient_name,
        dsny_fac.data_dsny_fac_typ_id as facility_type_id,
        dsny_fac_typ.data_dsny_fac_typ_cd as facility_type_code,
        dsny_fac_typ.data_dsny_fac_typ_ds as facility_type_description,
        dsny_fac.data_ship_ctct_id as shipment_contact_id,
        dsny_fac.data_fac_id as enterprise_id,
        dsny_fac.data_dsny_fac_nm as facility_name,
        dsny_fac.data_dsny_fac_avail_for_bulk_ord_in as available_for_bulk_order_indicator,
        dsny_fac.data_dsny_fac_for_rcv_gst_ord_in as guest_order_indicator,
        dsny_fac_band_invtry.data_ffld_exprnc_band_id as fulfilled_magic_band_id,
        ffld_exprnc_band.data_exprnc_band_id as magic_band_id,
        exprnc_band.data_exprnc_band_dsny_prod_id as product_id,
        exprnc_band_dsny_prod.data_exprnc_band_typ_id as product_type_id,
        exprnc_band_typ.data_exprnc_band_typ_cd as product_facility_type_code,
        exprnc_band_typ.data_exprnc_band_typ_ds as product_facility_type_description,
        exprnc_band_typ.data_avail_to_gst_in as product_type_available_to_guest_indicator,
        exprnc_band_dsny_prod.data_exprnc_band_top_color_id as top_color_id,
        top_color.data_exprnc_band_color_cd as top_color_code,
        top_color.data_exprnc_band_color_nm as top_color_name,
        top_color.data_avail_to_gst_in as top_color_available_to_guest_indicator,
        exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id as bottom_color_id,
        bottom_color.data_exprnc_band_color_cd as bottom_color_code,
        bottom_color.data_exprnc_band_color_nm as bottom_color_name,
        bottom_color.data_avail_to_gst_in as bottom_color_available_to_guest_indicator,
        exprnc_band_dsny_prod.data_exprnc_band_erlst_fflmt_dy_cn as minimum_fulfillment_day_count,
        exprnc_band_dsny_prod.data_exprnc_band_shipmt_to_rsrt_in as ship_to_resort_indicator,
        cast(exprnc_band_dsny_prod.data_exprnc_band_prod_avail_fr_dts as date) as availability_start_date,
        cast(exprnc_band_dsny_prod.data_exprnc_band_prod_avail_to_dts as date) as availability_end_date,
        exprnc_band.data_exprnc_band_uniq_id as magic_band_unique_identifier,
        exprnc_band.data_exprnc_band_prt_nm as printed_name,
        exprnc_band.data_exprnc_band_gst_cnfirm_in as guest_confirmation_indicator,
        exprnc_band.data_exprnc_band_seq_nb as sequence_number,
        exprnc_band.data_exprnc_band_cstm_prt_nm_in as custom_printed_name_indicator,
        exprnc_band.data_curr_exprnc_band_lnk_id as current_guest_link_id,
        current_exprnc_band_lnk.data_exprnc_band_lnk_uniq_id as magic_band_link_unique_identifier,
        current_exprnc_band_lnk.data_gst_src_sys_native_id as guest_source_system_native_id,
        current_exprnc_band_lnk.data_src_sys_tx as source_system_value,
        current_exprnc_band_lnk.data_gst_prfl_frst_nm as guest_profile_first_name,
        current_exprnc_band_lnk.data_gst_prfl_lst_nm as guest_profile_last_name,
        exprnc_band.data_exprnc_band_rtl_in as retail_indicator,
        ffld_exprnc_band.data_curr_exprnc_band_sts_id as current_status_id,
        exprnc_band_sts.data_exprnc_band_sts_ctgy_id as current_status_category_id,
        exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_cd as current_status_category_code,
        exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_ds as current_status_category_description,
        exprnc_band_sts.data_exprnc_band_sts_cd as current_status_code,
        exprnc_band_sts.data_exprnc_band_sts_ds as current_status_description,
        ffld_exprnc_band.data_curr_dsny_fac_id as current_facility_id,
        ffld_band_curr_fac.data_fac_id as current_enterprise_facility_id,
        ffld_band_curr_fac.data_dsny_fac_nm as current_facility_name,
        ffld_exprnc_band.data_exprnc_band_public_id as public_id,
        ffld_exprnc_band.data_exprnc_band_extnl_nb as external_number,
        ffld_exprnc_band.data_exprnc_band_secure_id as secure_id,
        ffld_exprnc_band.data_exprnc_band_short_rnge_tag_nb as short_range_tag_number,
        ffld_exprnc_band.data_exprnc_band_long_rnge_tag_nb as long_range_tag_number,
        ffld_exprnc_band.data_exprnc_band_lot_nb as lot_number,
        dsny_fac_band_invtry.data_exprnc_band_txn_id as transaction_id,
        dsny_fac_band_invtry.data_exprnc_band_frst_rec_fac_dts as facility_inventory_start_datetime,
        cast(dsny_fac_band_invtry.data_exprnc_band_frst_rec_fac_dts as date) as facility_inventory_start_date,
        cast(dsny_fac_band_invtry.data_exprnc_band_frst_rec_fac_dts as time) as facility_inventory_start_time,
        dsny_fac_band_invtry.data_exprnc_band_rec_lvg_fac_dts as facility_inventory_end_datetime,
        cast(dsny_fac_band_invtry.data_exprnc_band_rec_lvg_fac_dts as date) as facility_inventory_end_date,
        cast(dsny_fac_band_invtry.data_exprnc_band_rec_lvg_fac_dts as time) as facility_inventory_end_time,
        dsny_fac_band_invtry.data_fac_shipmt_case_nb as facility_shipment_case_nb,
        dsny_fac_band_invtry.data_create_usr_id as source_system_create_user_id,
        dsny_fac_band_invtry.data_create_dts as source_system_create_datetime,
        dsny_fac_band_invtry.data_updt_usr_id as source_system_update_user_id,
        dsny_fac_band_invtry.data_updt_dts as source_system_udpate_datetime
    from
        dsny_fac_band_invtry_cte as dsny_fac_band_invtry
        left outer join dsny_fac_cte as dsny_fac
        on dsny_fac.data_dsny_fac_id = dsny_fac_band_invtry.data_dsny_fac_id
        left outer join disney_fac_addr_cte as disney_fac_addr
        on disney_fac_addr.data_addr_id = dsny_fac.data_addr_id
        left outer join disney_fac_cntry_cte as disney_fac_cntry
        on disney_fac_cntry.data_cntry_id = disney_fac_addr.data_cntry_id
        left outer join dsny_fac_typ_cte as dsny_fac_typ
        on dsny_fac_typ.data_dsny_fac_typ_id = dsny_fac.data_dsny_fac_typ_id
        inner join ffld_exprnc_band_cte as ffld_exprnc_band
        on ffld_exprnc_band.data_ffld_exprnc_band_id = dsny_fac_band_invtry.data_ffld_exprnc_band_id
        inner join ffld_band_curr_fac_cte as ffld_band_curr_fac
        on ffld_band_curr_fac.data_dsny_fac_id = ffld_exprnc_band.data_curr_dsny_fac_id
        inner join exprnc_band_sts_cte as exprnc_band_sts
        on exprnc_band_sts.data_exprnc_band_sts_id = ffld_exprnc_band.data_curr_exprnc_band_sts_id
        inner join exprnc_band_sts_ctgy_cte as exprnc_band_sts_ctgy
        on exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_id = exprnc_band_sts.data_exprnc_band_sts_ctgy_id
        inner join exprnc_band_cte as exprnc_band
        on exprnc_band.data_exprnc_band_id = ffld_exprnc_band.data_exprnc_band_id
        join exprnc_band_dsny_prod_cte as exprnc_band_dsny_prod
        on exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id = exprnc_band.data_exprnc_band_dsny_prod_id
        join exprnc_band_typ_cte as exprnc_band_typ
        on exprnc_band_typ.data_exprnc_band_typ_id = exprnc_band_dsny_prod.data_exprnc_band_typ_id
        join top_color_cte as top_color
        on top_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_top_color_id
        join bottom_color_cte as bottom_color
        on bottom_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id
        left outer join current_exprnc_band_lnk_cte as current_exprnc_band_lnk
        on current_exprnc_band_lnk.data_exprnc_band_lnk_id = exprnc_band.data_curr_exprnc_band_lnk_id
)
select * from final
