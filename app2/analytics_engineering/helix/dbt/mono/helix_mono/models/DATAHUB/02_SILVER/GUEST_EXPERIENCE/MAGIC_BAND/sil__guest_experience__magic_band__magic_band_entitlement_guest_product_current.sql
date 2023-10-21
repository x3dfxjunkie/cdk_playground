with exprnc_band_enttl_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_enttl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_enttl_gst_lnk_cte as (
    select
        exprnc_band_enttl_gst_lnk.data_exprnc_band_enttl_gst_lnk_id,
        exprnc_band_enttl_gst_lnk.data_exprnc_band_enttl_id,
        exprnc_band_enttl_gst_lnk.data_exprnc_band_enttl_rsn_id,
        exprnc_band_enttl_gst_lnk.data_gst_id,
        exprnc_band_enttl_gst_lnk.data_create_usr_id,
        exprnc_band_enttl_gst_lnk.data_create_dts,
        exprnc_band_enttl_gst_lnk.data_updt_usr_id,
        exprnc_band_enttl_gst_lnk.data_updt_dts,
        exprnc_band_enttl_gst_lnk.data_logical_del_in
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_enttl_gst_lnk_versioned') }}
        exprnc_band_enttl_gst_lnk qualify row_number() over (
            partition by data_exprnc_band_enttl_id,
            data_exprnc_band_enttl_rsn_id,
            data_gst_id
            order by
                data_updt_dts desc
        ) = 1
),
exprnc_band_lnk_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_enttl_rsn_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_enttl_rsn_versioned') }}
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
exprnc_band_enttl_prod_cte as (
    select
        exprnc_band_enttl_prod.data_exprnc_band_enttl_prod_id,
        exprnc_band_enttl_prod.data_exprnc_band_dsny_prod_id,
        exprnc_band_enttl_prod.data_exprnc_band_enttl_id,
        exprnc_band_enttl_prod.data_create_usr_id,
        exprnc_band_enttl_prod.data_create_dts,
        exprnc_band_enttl_prod.data_updt_usr_id,
        exprnc_band_enttl_prod.data_updt_dts,
        exprnc_band_enttl_prod.data_logical_del_in
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_enttl_prod_versioned') }}
        exprnc_band_enttl_prod qualify row_number() over (
            partition by data_exprnc_band_dsny_prod_id,
            data_exprnc_band_enttl_id
            order by
                data_updt_dts desc
        ) = 1
),
enttl_dsny_prod_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_prod_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
enttl_band_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
enttl_top_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
enttl_bottom_color_cte as (
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
        exprnc_band_enttl.data_exprnc_band_enttl_id magic_band_entitlement_id,
        exprnc_band_enttl.data_exprnc_band_enttl_cd magic_band_entitlement_code,
        exprnc_band_enttl.data_dflt_exprnc_band_dsny_prod_id default_product_id,
        exprnc_band_dsny_prod.data_exprnc_band_typ_id default_product_type_id,
        exprnc_band_typ.data_exprnc_band_typ_cd default_product_type_code,
        exprnc_band_typ.data_exprnc_band_typ_ds default_product_type_description,
        exprnc_band_typ.data_avail_to_gst_in default_product_type_available_to_guest_indicator,
        exprnc_band_dsny_prod.data_exprnc_band_top_color_id default_product_top_color_id,
        top_color.data_exprnc_band_color_cd default_product_top_color_code,
        top_color.data_exprnc_band_color_nm default_product_top_color_name,
        top_color.data_avail_to_gst_in default_product_top_color_available_to_guest_indicator,
        exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id default_product_bottom_color_id,
        bottom_color.data_exprnc_band_color_cd default_product_bottom_color_code,
        bottom_color.data_exprnc_band_color_nm default_product_bottom_color_name,
        bottom_color.data_avail_to_gst_in default_product_bottom_color_available_to_guest_indicator,
        exprnc_band_dsny_prod.data_exprnc_band_erlst_fflmt_dy_cn default_product_minimum_fulfillment_day_count,
        exprnc_band_dsny_prod.data_exprnc_band_shipmt_to_rsrt_in default_product_ship_to_resort_indicator,
        cast(
            exprnc_band_dsny_prod.data_exprnc_band_prod_avail_fr_dts as date
        ) default_product_availability_start_date,
        cast(
            exprnc_band_dsny_prod.data_exprnc_band_prod_avail_to_dts as date
        ) default_product_availability_end_date,
        exprnc_band_enttl.data_exprnc_band_enttl_ds entitlement_description,
        exprnc_band_enttl.data_exprnc_band_enttl_rank_nb entitlement_rank_number,
        exprnc_band_enttl.data_ship_imdt_avail_in entitlement_shipping_immediately_available_indicator,
        exprnc_band_enttl_gst_lnk.data_gst_id entitlement_guest_link_id,
        exprnc_band_enttl_gst_lnk.data_exprnc_band_enttl_rsn_id guest_link_reason_id,
        exprnc_band_enttl_rsn.data_exprnc_band_enttl_rsn_cd guest_link_reason_code,
        exprnc_band_enttl_rsn.data_exprnc_band_enttl_rsn_ds guest_link_reason_description,
        exprnc_band_lnk.data_exprnc_band_lnk_uniq_id guest_link_unique_id,
        exprnc_band_lnk.data_gst_src_sys_native_id supplemental_guest_identifier,
        exprnc_band_lnk.data_src_sys_tx supplemental_guest_identifier_name,
        exprnc_band_lnk.data_gst_prfl_frst_nm guest_profile_first_name,
        exprnc_band_lnk.data_gst_prfl_lst_nm guest_profile_last_name,
        enttl_dsny_prod.data_exprnc_band_dsny_prod_id entitlement_product_id,
        enttl_dsny_prod.data_exprnc_band_typ_id entitlement_product_type_id,
        enttl_band_typ.data_exprnc_band_typ_cd entitlement_product_type_code,
        enttl_band_typ.data_exprnc_band_typ_ds entitlement_product_type_description,
        enttl_band_typ.data_avail_to_gst_in entitlement_product_type_available_to_guest_indicator,
        enttl_dsny_prod.data_exprnc_band_top_color_id entitlement_product_top_color_id,
        enttl_top_color.data_exprnc_band_color_cd entitlement_product_top_color_code,
        enttl_top_color.data_exprnc_band_color_nm entitlement_product_top_color_name,
        enttl_top_color.data_avail_to_gst_in entitlement_product_top_color_available_to_guest_indicator,
        enttl_dsny_prod.data_exprnc_band_bottom_color_id entitlement_product_bottom_color_id,
        enttl_bottom_color.data_exprnc_band_color_cd entitlement_product_bottom_color_code,
        enttl_bottom_color.data_exprnc_band_color_nm entitlement_product_bottom_color_name,
        enttl_bottom_color.data_avail_to_gst_in entitlement_product_bottom_color_available_to_guest_indicator,
        enttl_dsny_prod.data_exprnc_band_erlst_fflmt_dy_cn entitlement_product_minimum_fulfillment_day_count,
        enttl_dsny_prod.data_exprnc_band_shipmt_to_rsrt_in entitlement_product_ship_to_resort_indicator,
        cast(
            enttl_dsny_prod.data_exprnc_band_prod_avail_fr_dts as date
        ) entitlement_product_availability_start_date,
        cast(
            enttl_dsny_prod.data_exprnc_band_prod_avail_to_dts as date
        ) entitlement_product_availability_end_date,
        exprnc_band_enttl.data_create_usr_id source_system_create_user_id,
        exprnc_band_enttl.data_create_dts source_system_create_datetime,
        exprnc_band_enttl.data_updt_usr_id source_system_update_user_id,
        exprnc_band_enttl.data_updt_dts source_system_update_datetime,
        exprnc_band_enttl.data_logical_del_in source_system_logical_delete_indicator
    from
        exprnc_band_enttl_cte exprnc_band_enttl
        join exprnc_band_enttl_gst_lnk_cte exprnc_band_enttl_gst_lnk
        on exprnc_band_enttl_gst_lnk.data_exprnc_band_enttl_id = exprnc_band_enttl.data_exprnc_band_enttl_id
        join exprnc_band_lnk_cte exprnc_band_lnk
        on exprnc_band_lnk.data_exprnc_band_lnk_id = exprnc_band_enttl_gst_lnk.data_gst_id
        left outer join exprnc_band_enttl_rsn_cte exprnc_band_enttl_rsn
        on exprnc_band_enttl_rsn.data_exprnc_band_enttl_rsn_id = exprnc_band_enttl_gst_lnk.data_exprnc_band_enttl_rsn_id
        join exprnc_band_dsny_prod_cte exprnc_band_dsny_prod
        on exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id = exprnc_band_enttl.data_dflt_exprnc_band_dsny_prod_id
        join exprnc_band_typ_cte exprnc_band_typ
        on exprnc_band_typ.data_exprnc_band_typ_id = exprnc_band_dsny_prod.data_exprnc_band_typ_id
        join top_color_cte top_color
        on top_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_top_color_id
        join bottom_color_cte bottom_color
        on bottom_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id
        join exprnc_band_enttl_prod_cte exprnc_band_enttl_prod
        on exprnc_band_enttl_prod.data_exprnc_band_enttl_id = exprnc_band_enttl.data_exprnc_band_enttl_id
        join enttl_dsny_prod_cte enttl_dsny_prod
        on enttl_dsny_prod.data_exprnc_band_dsny_prod_id = exprnc_band_enttl_prod.data_exprnc_band_dsny_prod_id
        join enttl_band_typ_cte enttl_band_typ
        on enttl_band_typ.data_exprnc_band_typ_id = enttl_dsny_prod.data_exprnc_band_typ_id
        join enttl_top_color_cte enttl_top_color
        on enttl_top_color.data_exprnc_band_color_id = enttl_dsny_prod.data_exprnc_band_top_color_id
        join enttl_bottom_color_cte enttl_bottom_color
        on enttl_bottom_color.data_exprnc_band_color_id = enttl_dsny_prod.data_exprnc_band_bottom_color_id
)
select
    *
from
    final
