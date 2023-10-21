with exprnc_band_dsny_prod_cte as (
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

final as (
    select
        exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id as magic_band_disney_product_id,
        concat(
            exprnc_band_typ.data_exprnc_band_typ_cd,
            top_color.data_exprnc_band_color_cd,
            bottom_color.data_exprnc_band_color_cd
        ) as stockeeping_unit_code,
        concat(
            exprnc_band_typ.data_exprnc_band_typ_ds,
            top_color.data_exprnc_band_color_nm,
            bottom_color.data_exprnc_band_color_nm
        ) as stockeeping_unit_description,
        exprnc_band_dsny_prod.data_exprnc_band_typ_id as product_type_id,
        exprnc_band_typ.data_exprnc_band_typ_cd as product_type_code,
        exprnc_band_typ.data_exprnc_band_typ_ds as product_type_description,
        exprnc_band_typ.data_avail_to_gst_in as type_available_to_guest_indicator,
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
        cast(
            exprnc_band_dsny_prod.data_exprnc_band_prod_avail_fr_dts as date
        ) availability_start_date,
        cast(
            exprnc_band_dsny_prod.data_exprnc_band_prod_avail_to_dts as date
        ) availability_end_date,
        exprnc_band_dsny_prod.data_create_usr_id as source_system_create_user_id,
        exprnc_band_dsny_prod.data_create_dts as source_system_create_datetime,
        exprnc_band_dsny_prod.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_dsny_prod.data_updt_dts as source_system_update_datetime,
        exprnc_band_dsny_prod.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_dsny_prod_cte as exprnc_band_dsny_prod
        join exprnc_band_typ_cte as exprnc_band_typ
        on exprnc_band_typ.data_exprnc_band_typ_id = exprnc_band_dsny_prod.data_exprnc_band_typ_id
        join top_color_cte as top_color
        on top_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_top_color_id
        join bottom_color_cte as bottom_color
        on bottom_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id
)

select * from final
