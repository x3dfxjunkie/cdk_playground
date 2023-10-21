-- define a cte for exprnc_band_rplmt_lnk
with exprnc_band_rplmt_lnk_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_rplmt_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for original_exprnc_band
original_exprnc_band_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for original_prod
original_prod_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_prod_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for original_typ
original_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for original_top_color
original_top_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for original_bottom_color
original_bottom_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for replacement_exprnc_band
replacement_exprnc_band_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for replacement_prod
replacement_prod_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_prod_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for replacement_typ
replacement_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for replacement_top_color
replacement_top_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for replacement_bottom_color
replacement_bottom_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_rplmt_mech
exprnc_band_rplmt_mech_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_rplmt_mech_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for original_exprnc_band_lnk
original_exprnc_band_lnk_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for replacement_exprnc_band_lnk
replacement_exprnc_band_lnk_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- join ctes to get the final result
final as (
    select
        exprnc_band_rplmt_lnk.data_exprnc_band_rplmt_lnk_id as magic_band_replacement_link_id,
        exprnc_band_rplmt_lnk.data_prnt_exprnc_band_id as original_magic_band_id,
        original_exprnc_band.data_exprnc_band_dsny_prod_id as original_product_id,
        original_prod.data_exprnc_band_typ_id as original_product_type_id,
        original_typ.data_exprnc_band_typ_cd as original_product_type_code,
        original_typ.data_exprnc_band_typ_ds as original_product_type_description,
        original_prod.data_exprnc_band_top_color_id as original_product_top_color_id,
        original_top_color.data_exprnc_band_color_cd as original_product_top_color_code,
        original_top_color.data_exprnc_band_color_nm as original_product_top_color_name,
        original_prod.data_exprnc_band_bottom_color_id as original_product_bottom_color_id,
        original_bottom_color.data_exprnc_band_color_cd as original_product_bottom_color_cd,
        original_bottom_color.data_exprnc_band_color_nm as original_product_bottom_color_name,
        original_exprnc_band.data_exprnc_band_uniq_id as original_magic_band_unique_identifier,
        original_exprnc_band.data_exprnc_band_prt_nm as original_magic_band_printed_name,
        original_exprnc_band.data_curr_exprnc_band_lnk_id as original_current_guest_link_id,
        original_exprnc_band_lnk.data_exprnc_band_lnk_uniq_id as original_magic_band_guest_link_unique_identifier,
        original_exprnc_band_lnk.data_gst_src_sys_native_id as original_external_system_guest_identifier_value,
        original_exprnc_band_lnk.data_src_sys_tx as original_external_system_guest_identifier_name,
        original_exprnc_band_lnk.data_gst_prfl_frst_nm as original_guest_profile_first_name,
        original_exprnc_band_lnk.data_gst_prfl_lst_nm as original_guest_profile_last_name,
        exprnc_band_rplmt_lnk.data_chld_exprnc_band_id as replacement_magic_band_id,
        replacement_exprnc_band.data_exprnc_band_dsny_prod_id as replacement_magic_band_product_id,
        replacement_prod.data_exprnc_band_typ_id as replacement_magic_band_type_id,
        replacement_typ.data_exprnc_band_typ_cd as replacement_magic_band_type_code,
        replacement_typ.data_exprnc_band_typ_ds as replacement_magic_band_type_description,
        replacement_prod.data_exprnc_band_top_color_id as replacement_magic_band_top_color_id,
        replacement_top_color.data_exprnc_band_color_cd as replacement_magic_band_top_color_cd,
        replacement_top_color.data_exprnc_band_color_nm as replacement_magic_band_top_color_name,
        replacement_prod.data_exprnc_band_bottom_color_id as replacement_magic_band_bottom_color_id,
        replacement_bottom_color.data_exprnc_band_color_cd as replacement_magic_band_bottom_color_code,
        replacement_bottom_color.data_exprnc_band_color_nm as replacement_magic_band_bottom_color_name,
        replacement_exprnc_band.data_exprnc_band_uniq_id as replacement_magic_band_unique_identifier,
        replacement_exprnc_band.data_exprnc_band_prt_nm as replacement_magic_band_printed_name,
        replacement_exprnc_band.data_curr_exprnc_band_lnk_id as replacement_current_guest_link_id,
        replacement_exprnc_band_lnk.data_exprnc_band_lnk_uniq_id as replacement_current_guest_link_unique_identifier,
        replacement_exprnc_band_lnk.data_gst_src_sys_native_id as replacement_external_system_guest_identifier_value,
        replacement_exprnc_band_lnk.data_src_sys_tx as replacement_external_system_guest_identifier_name,
        replacement_exprnc_band_lnk.data_gst_prfl_frst_nm as replacement_guest_profile_first_name,
        replacement_exprnc_band_lnk.data_gst_prfl_lst_nm as replacement_guest_profile_last_name,
        exprnc_band_rplmt_lnk.data_exprnc_band_rplmt_mech_id as magic_band_replacement_mechanism_id,
        exprnc_band_rplmt_mech.data_exprnc_band_rplmt_mech_cd as replacement_mechanism_code,
        exprnc_band_rplmt_mech.data_exprnc_band_rplmt_mech_ds as replacement_mechanism_description,
        exprnc_band_rplmt_lnk.data_create_dts as source_system_create_datetime,
        exprnc_band_rplmt_lnk.data_create_usr_id as source_system_create_user_id,
        exprnc_band_rplmt_lnk.data_updt_dts as source_system_update_datetime,
        exprnc_band_rplmt_lnk.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_rplmt_lnk.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_rplmt_lnk_cte exprnc_band_rplmt_lnk
        join original_exprnc_band_cte original_exprnc_band
        on original_exprnc_band.data_exprnc_band_id = exprnc_band_rplmt_lnk.data_prnt_exprnc_band_id
        join original_prod_cte original_prod
        on original_prod.data_exprnc_band_dsny_prod_id = original_exprnc_band.data_exprnc_band_dsny_prod_id
        join original_typ_cte original_typ
        on original_typ.data_exprnc_band_typ_id = original_prod.data_exprnc_band_typ_id
        join original_top_color_cte original_top_color
        on original_top_color.data_exprnc_band_color_id = original_prod.data_exprnc_band_top_color_id
        join original_bottom_color_cte original_bottom_color
        on original_bottom_color.data_exprnc_band_color_id = original_prod.data_exprnc_band_bottom_color_id
        join replacement_exprnc_band_cte replacement_exprnc_band
        on replacement_exprnc_band.data_exprnc_band_id = exprnc_band_rplmt_lnk.data_chld_exprnc_band_id
        join replacement_prod_cte replacement_prod
        on replacement_prod.data_exprnc_band_dsny_prod_id = replacement_exprnc_band.data_exprnc_band_dsny_prod_id
        join replacement_typ_cte replacement_typ
        on replacement_typ.data_exprnc_band_typ_id = replacement_prod.data_exprnc_band_typ_id
        join replacement_top_color_cte replacement_top_color
        on replacement_top_color.data_exprnc_band_color_id = replacement_prod.data_exprnc_band_top_color_id
        join replacement_bottom_color_cte replacement_bottom_color
        on replacement_bottom_color.data_exprnc_band_color_id = replacement_prod.data_exprnc_band_bottom_color_id
        join exprnc_band_rplmt_mech_cte exprnc_band_rplmt_mech
        on exprnc_band_rplmt_mech.data_exprnc_band_rplmt_mech_id = exprnc_band_rplmt_lnk.data_exprnc_band_rplmt_mech_id
        join original_exprnc_band_lnk_cte original_exprnc_band_lnk
        on original_exprnc_band_lnk.data_exprnc_band_lnk_id = original_exprnc_band.data_curr_exprnc_band_lnk_id
        join replacement_exprnc_band_lnk_cte replacement_exprnc_band_lnk
        on replacement_exprnc_band_lnk.data_exprnc_band_lnk_id = replacement_exprnc_band.data_curr_exprnc_band_lnk_id
)
select
    *
from
    final
