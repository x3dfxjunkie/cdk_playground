-- define a cte for pexprnc_band_enttlc
with exprnc_band_enttl_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_enttl_versioned') }}
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
        exprnc_band_enttl.data_exprnc_band_enttl_id as entitlement_id,
        exprnc_band_enttl.data_exprnc_band_enttl_cd as entitlement_code,
        exprnc_band_enttl.data_dflt_exprnc_band_dsny_prod_id as default_product_id,
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
        exprnc_band_enttl.data_exprnc_band_enttl_ds as entitlement_description,
        exprnc_band_enttl.data_exprnc_band_enttl_rank_nb as entitlement_rank_number,
        exprnc_band_enttl.data_ship_imdt_avail_in as immediate_shipment_available_indicator,
        exprnc_band_enttl.data_create_usr_id as source_system_create_user_id,
        exprnc_band_enttl.data_create_dts as source_system_create_datetime,
        exprnc_band_enttl.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_enttl.data_updt_dts as source_system_update_datetime,
        exprnc_band_enttl.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_enttl_cte exprnc_band_enttl
        join exprnc_band_dsny_prod_cte exprnc_band_dsny_prod
        on exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id = exprnc_band_enttl.data_dflt_exprnc_band_dsny_prod_id
        join exprnc_band_typ_cte exprnc_band_typ
        on exprnc_band_typ.data_exprnc_band_typ_id = exprnc_band_dsny_prod.data_exprnc_band_typ_id
        join top_color_cte top_color
        on top_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_top_color_id
        join bottom_color_cte bottom_color
        on bottom_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id
)
select
    *
from
    final
