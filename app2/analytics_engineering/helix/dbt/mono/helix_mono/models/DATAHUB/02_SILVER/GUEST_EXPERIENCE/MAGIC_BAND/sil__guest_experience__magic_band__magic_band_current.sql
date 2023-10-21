-- define a cte for exprnc_band
with exprnc_band_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_versioned') }}
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
-- define a cte for exprnc_band_req
exprnc_band_req_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_versioned') }}
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
-- define a cte for exprnc_band_req_sts
exprnc_band_req_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_req_sts_versioned') }}
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
-- define a cte for exprnc_band_ord
exprnc_band_ord_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_pkg
exprnc_band_pkg_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_pkg_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for pkg_cmpnt
pkg_cmpnt_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__pkg_cmpnt_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for pkg_cmpnt_typ
pkg_cmpnt_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__pkg_cmpnt_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for pkg_cmpnt_rl
pkg_cmpnt_rl_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__pkg_cmpnt_rl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for pkg_cmpnt_cnstrct_rule
pkg_cmpnt_cnstrct_rule_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__pkg_cmpnt_cnstrct_rule_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for current_exprnc_band_lnk
current_exprnc_band_lnk_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_versioned') }}
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
-- define a cte for exprnc_band_opt_out_rsn
exprnc_band_opt_out_rsn_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_opt_out_rsn_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_ord_sts
exprnc_band_ord_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_ord_sts_ctgy
exprnc_band_ord_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_ord_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- join the ctes to get the final result
final as (
    select
        exprnc_band.data_exprnc_band_id as magic_band_id,
        exprnc_band.data_exprnc_band_dsny_prod_id as product_id,
        exprnc_band_dsny_prod.data_exprnc_band_typ_id as product_type_id,
        exprnc_band_typ.data_exprnc_band_typ_cd as product_type_code,
        exprnc_band_typ.data_exprnc_band_typ_ds as product_type_description,
        exprnc_band_typ.data_avail_to_gst_in as product_type_available_to_guest_indicator,
        exprnc_band_dsny_prod.data_exprnc_band_top_color_id as top_color_id,
        top_color.data_exprnc_band_color_cd as top_color_code,
        top_color.data_exprnc_band_color_nm as top_color_name,
        top_color.data_avail_to_gst_in as top_color_available_to_guest_indicator,
        exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id as bottom_color_id,
        bottom_color.data_exprnc_band_color_cd as bottom_color_code,
        bottom_color.data_exprnc_band_color_nm as bottom_color_name,
        bottom_color.data_avail_to_gst_in as bottom_color_available_to_guest_indiactor,
        exprnc_band_dsny_prod.data_exprnc_band_erlst_fflmt_dy_cn as product_minimum_fulfillment_day_count,
        exprnc_band_dsny_prod.data_exprnc_band_shipmt_to_rsrt_in as product_ship_to_resort_indicator,
        cast(
            exprnc_band_dsny_prod.data_exprnc_band_prod_avail_fr_dts as date
        ) as product_availability_start_date,
        cast(
            exprnc_band_dsny_prod.data_exprnc_band_prod_avail_to_dts as date
        ) as product_availability_end_datetime,
        exprnc_band.data_exprnc_band_uniq_id as magic_band_unique_identifier,
        exprnc_band.data_exprnc_band_req_id as request_id,
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
        exprnc_band_ord.data_exprnc_band_ord_uniq_id as order_unique_identifier,
        exprnc_band_ord.data_exprnc_band_ord_expect_ship_dt as order_expected_shipping_date,
        exprnc_band_ord.data_exprnc_band_ord_expect_dlvr_dt as order_expected_delivery_date,
        exprnc_band_ord.data_exprnc_band_ord_actl_dlvr_dt as order_actual_delivery_date,
        exprnc_band_ord.data_curr_exprnc_band_ord_sts_id as order_status_id,
        exprnc_band_ord_sts.data_exprnc_band_ord_sts_ctgy_id as order_status_category_id,
        exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_cd as order_status_category_code,
        exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_ds as order_status_category_description,
        exprnc_band_ord_sts.data_exprnc_band_ord_sts_cd as order_status_code,
        exprnc_band_ord_sts.data_exprnc_band_ord_sts_ds as order_status_description,
        exprnc_band.data_exprnc_band_pkg_id as package_id,
        exprnc_band_pkg.data_pkg_cmpnt_id as package_component_id,
        pkg_cmpnt.data_pkg_cmpnt_typ_id as package_component_type_id,
        pkg_cmpnt_typ.data_pkg_cmpnt_rl_id as package_component_role_id,
        pkg_cmpnt_rl.data_pkg_cmpnt_rl_cd as package_component_role_cd,
        pkg_cmpnt_rl.data_pkg_cmpnt_rl_ds as package_component_role_description,
        pkg_cmpnt_typ.data_pkg_cmpnt_cnstrct_rule_id as package_component_construction_rule_id,
        pkg_cmpnt_cnstrct_rule.data_pkg_cmpnt_cnstrct_rule_cd as package_component_construction_rule_code,
        pkg_cmpnt_cnstrct_rule.data_pkg_cmpnt_cnstrct_rule_ds as package_component_construction_rule_description,
        pkg_cmpnt_typ.data_pkg_cmpnt_typ_nm as package_component_type_name,
        pkg_cmpnt_typ.data_pkg_cmpnt_typ_actv_in as package_component_type_active_indicator,
        pkg_cmpnt.data_pkg_cmpnt_nm as package_component_name,
        pkg_cmpnt.data_avail_to_gst_in as package_component_available_to_guest_indicator,
        pkg_cmpnt.data_pkg_cmpnt_min_cpcty_cn as package_component_minimum_capacity_count,
        pkg_cmpnt.data_pkg_cmpnt_max_cpcty_cn as package_component_maximum_capacity_count,
        pkg_cmpnt.data_pkg_cmpnt_actv_in as package_component_active_indicator,
        exprnc_band_pkg.data_pkg_seq_nb as package_sequence_number,
        exprnc_band.data_exprnc_band_prt_nm as printed_name,
        exprnc_band.data_exprnc_band_gst_cnfirm_in as guest_confirmation_indicator,
        exprnc_band.data_exprnc_band_seq_nb as magic_band_sequence_number,
        exprnc_band.data_exprnc_band_cstm_prt_nm_in as customized_print_name_indicator,
        exprnc_band.data_curr_exprnc_band_lnk_id as current_guest_link_id,
        current_exprnc_band_lnk.data_exprnc_band_lnk_uniq_id as current_guest_link_unique_id,
        current_exprnc_band_lnk.data_gst_src_sys_native_id as current_guest_source_system_native_id,
        current_exprnc_band_lnk.data_src_sys_tx as current_guest_source_system_value,
        current_exprnc_band_lnk.data_gst_prfl_frst_nm as current_guest_profile_first_name,
        current_exprnc_band_lnk.data_gst_prfl_lst_nm as current_guest_profile_last_name,
        exprnc_band.data_orig_exprnc_band_lnk_id as original_guest_link_id,
        original_exprnc_band_lnk.data_exprnc_band_lnk_uniq_id as original_guest_link_unique_id,
        original_exprnc_band_lnk.data_gst_src_sys_native_id as original_guest_source_system_native_id,
        original_exprnc_band_lnk.data_src_sys_tx as original_guest_source_system_value,
        original_exprnc_band_lnk.data_gst_prfl_frst_nm as original_guest_profile_first_name,
        original_exprnc_band_lnk.data_gst_prfl_lst_nm as original_guest_profile_last_name,
        exprnc_band.data_exprnc_band_rtl_in as retail_indicator,
        exprnc_band.data_opt_out_in as guest_data_opt_out_indicator,
        exprnc_band.data_exprnc_band_opt_out_rsn_id as opt_out_reason_id,
        exprnc_band_opt_out_rsn.data_exprnc_band_opt_out_rsn_cd as opt_out_reason_code,
        exprnc_band_opt_out_rsn.data_exprnc_band_opt_out_rsn_ds as opt_out_reason_description,
        exprnc_band.data_exprnc_band_ovrd_prt_nm as override_printed_name,
        exprnc_band.data_create_usr_id as source_system_create_user_id,
        exprnc_band.data_create_dts as source_system_create_datetime,
        exprnc_band.data_updt_usr_id as source_system_update_user_id,
        exprnc_band.data_updt_dts as source_system_update_datetime,
        exprnc_band.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_cte exprnc_band
        join exprnc_band_dsny_prod_cte exprnc_band_dsny_prod
        on exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id = exprnc_band.data_exprnc_band_dsny_prod_id
        join exprnc_band_typ_cte exprnc_band_typ
        on exprnc_band_typ.data_exprnc_band_typ_id = exprnc_band_dsny_prod.data_exprnc_band_typ_id
        join top_color_cte top_color
        on top_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_top_color_id
        join bottom_color_cte bottom_color
        on bottom_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id
        left outer join exprnc_band_req_cte exprnc_band_req
        on exprnc_band_req.data_exprnc_band_req_id = exprnc_band.data_exprnc_band_req_id
        left outer join exprnc_band_req_typ_cte exprnc_band_req_typ
        on exprnc_band_req_typ.data_exprnc_band_req_typ_id = exprnc_band_req.data_exprnc_band_req_typ_id
        left outer join exprnc_band_req_rsn_cte exprnc_band_req_rsn
        on exprnc_band_req_rsn.data_exprnc_band_req_rsn_id = exprnc_band_req.data_exprnc_band_req_rsn_id
        left outer join exprnc_band_req_sts_cte exprnc_band_req_sts
        on exprnc_band_req_sts.data_exprnc_band_req_sts_id = exprnc_band_req.data_curr_exprnc_band_req_sts_id
        left outer join exprnc_band_req_sts_ctgy_cte exprnc_band_req_sts_ctgy
        on exprnc_band_req_sts_ctgy.data_exprnc_band_req_sts_ctgy_id = exprnc_band_req_sts.data_exprnc_band_req_sts_ctgy_id
        left outer join exprnc_band_ord_cte exprnc_band_ord
        on exprnc_band_ord.data_exprnc_band_ord_id = exprnc_band.data_exprnc_band_ord_id
        left outer join exprnc_band_pkg_cte exprnc_band_pkg
        on exprnc_band_pkg.data_exprnc_band_pkg_id = exprnc_band.data_exprnc_band_pkg_id
        left outer join pkg_cmpnt_cte pkg_cmpnt
        on pkg_cmpnt.data_pkg_cmpnt_id = exprnc_band_pkg.data_pkg_cmpnt_id
        left outer join pkg_cmpnt_typ_cte pkg_cmpnt_typ
        on pkg_cmpnt_typ.data_pkg_cmpnt_typ_id = pkg_cmpnt.data_pkg_cmpnt_typ_id
        left outer join pkg_cmpnt_rl_cte pkg_cmpnt_rl
        on pkg_cmpnt_rl.data_pkg_cmpnt_rl_id = pkg_cmpnt_typ.data_pkg_cmpnt_rl_id
        left outer join pkg_cmpnt_cnstrct_rule_cte pkg_cmpnt_cnstrct_rule
        on pkg_cmpnt_cnstrct_rule.data_pkg_cmpnt_cnstrct_rule_id = pkg_cmpnt_typ.data_pkg_cmpnt_cnstrct_rule_id
        left outer join current_exprnc_band_lnk_cte current_exprnc_band_lnk
        on current_exprnc_band_lnk.data_exprnc_band_lnk_id = exprnc_band.data_curr_exprnc_band_lnk_id
        left outer join original_exprnc_band_lnk_cte original_exprnc_band_lnk
        on original_exprnc_band_lnk.data_exprnc_band_lnk_id = exprnc_band.data_orig_exprnc_band_lnk_id
        left outer join exprnc_band_opt_out_rsn_cte exprnc_band_opt_out_rsn
        on exprnc_band_opt_out_rsn.data_exprnc_band_opt_out_rsn_id = exprnc_band.data_exprnc_band_opt_out_rsn_id
        left outer join exprnc_band_ord_sts_cte exprnc_band_ord_sts
        on exprnc_band_ord_sts.data_exprnc_band_ord_sts_id = exprnc_band_ord.data_curr_exprnc_band_ord_sts_id
        left outer join exprnc_band_ord_sts_ctgy_cte exprnc_band_ord_sts_ctgy
        on exprnc_band_ord_sts_ctgy.data_exprnc_band_ord_sts_ctgy_id = exprnc_band_ord_sts.data_exprnc_band_ord_sts_ctgy_id
) -- select from the final result cte
select
    *
from
    final
