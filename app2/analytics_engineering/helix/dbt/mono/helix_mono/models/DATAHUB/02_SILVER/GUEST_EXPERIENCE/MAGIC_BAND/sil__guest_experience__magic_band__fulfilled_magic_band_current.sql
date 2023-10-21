-- define a cte for ffld_exprnc_band
with ffld_enprnc_band_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__ffld_exprnc_band_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band
exprnc_band_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_sts
exprnc_band_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_sts_ctgy
exprnc_band_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_config
exprnc_band_config_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_config_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_manu_tool
exprnc_band_manu_tool_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_manu_tool_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_mdle_config
exprnc_band_mdle_config_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_config_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_mdle
exprnc_band_mdle_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_vndr
exprnc_band_vndr_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for exprnc_band_vndr_rl
exprnc_band_vndr_rl_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_rl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- define a cte for dsny_fac
dsny_fac_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- join the ctes to get the final result
final as (
    select
        ffld_exprnc_band.data_ffld_exprnc_band_id as fulfilled_magic_band_id,
        ffld_exprnc_band.data_exprnc_band_id as magic_band_id,
        ffld_exprnc_band.data_exprnc_band_public_id as public_id,
        ffld_exprnc_band.data_exprnc_band_secure_id as secure_id,
        ffld_exprnc_band.data_exprnc_band_extnl_nb as external_number,
        ffld_exprnc_band.data_exprnc_band_short_rnge_tag_nb as short_range_tag_number,
        ffld_exprnc_band.data_exprnc_band_long_rnge_tag_nb as long_range_tag_number,
        ffld_exprnc_band.data_exprnc_band_lot_nb as lot_number,
        exprnc_band.data_curr_exprnc_band_lnk_id as current_guest_link_id,
        exprnc_band.data_orig_exprnc_band_lnk_id as original_guest_link_id,
        exprnc_band.data_exprnc_band_uniq_id as magic_band_unique_identifier,
        exprnc_band.data_exprnc_band_seq_nb as magic_band_sequence_number,
        exprnc_band.data_exprnc_band_gst_cnfirm_in as guest_confirmation_indicator,
        exprnc_band.data_exprnc_band_cstm_prt_nm_in as customized_print_name_indicator,
        exprnc_band.data_exprnc_band_rtl_in as retail_indicator,
        exprnc_band.data_opt_out_in as guest_opt_out_indicator,
        exprnc_band.data_exprnc_band_prt_nm as printed_name,
        exprnc_band.data_exprnc_band_ovrd_prt_nm as override_printed_name,
        ffld_exprnc_band.data_curr_exprnc_band_sts_id as current_magic_band_status_id,
        exprnc_band_sts.data_exprnc_band_sts_cd as current_status_code,
        exprnc_band_sts.data_exprnc_band_sts_ds as current_status_description,
        exprnc_band_sts.data_exprnc_band_sts_ctgy_id as current_magic_band_status_category_id,
        exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_cd as current_satatus_category_code,
        exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_ds as current_status_category_description,
        ffld_exprnc_band.data_exprnc_band_config_id as configuration_id,
        exprnc_band_config.data_exprnc_band_config_ds as configuration_description,
        exprnc_band_config.data_avail_to_gst_in as available_to_guest_indicator,
        exprnc_band_config.data_exprnc_band_config_cnfirm_in as configuration_confirmation_indicator,
        exprnc_band_config.data_exprnc_band_mdle_config_id as module_configuration_id,
        exprnc_band_mdle_config.data_exprnc_band_mdle_id as module_id,
        exprnc_band_mdle_config.data_exprnc_band_mdle_vrsn_id as module_version_id,
        exprnc_band_mdle.data_exprnc_band_mdle_cd as module_code,
        exprnc_band_mdle.data_exprnc_band_mdle_ds as module_description,
        exprnc_band_mdle.data_avail_to_gst_in as module_available_to_guest_indicator,
        dsny_fac.data_fac_id as facility_id,
        dsny_fac.data_dsny_fac_nm as facility_name,
        exprnc_band_config.data_exprnc_band_manu_tool_id as manufacture_tool_id,
        exprnc_band_manu_tool.data_exprnc_band_manu_tool_cd as manufacture_tool_code,
        exprnc_band_manu_tool.data_exprnc_band_manu_tool_ds as manufacture_tool_description,
        exprnc_band_config.data_exprnc_band_vndr_id as vendor_id,
        exprnc_band_vndr.data_exprnc_band_vndr_cd as vendor_code,
        exprnc_band_vndr.data_exprnc_band_vndr_nm as vendor_name,
        exprnc_band_vndr.data_exprnc_band_vndr_rl_id as vendor_role_id,
        exprnc_band_vndr_rl.data_exprnc_band_vndr_rl_cd as vendor_role_code,
        exprnc_band_vndr_rl.data_exprnc_band_vndr_rl_ds as vendor_role_description,
        ffld_exprnc_band.data_shipmt_case_id as shipment_case_id,
        ffld_exprnc_band.data_create_usr_id as source_system_create_user_id,
        ffld_exprnc_band.data_create_dts as source_system_create_datetime,
        ffld_exprnc_band.data_updt_usr_id as source_system_update_user_id,
        ffld_exprnc_band.data_updt_dts as source_system_update_datetime,
        ffld_exprnc_band.data_logical_del_in as source_system_logical_delete_indicator
    from
        ffld_enprnc_band_cte ffld_exprnc_band
        left outer join exprnc_band_cte exprnc_band
        on ffld_exprnc_band.data_exprnc_band_id = exprnc_band.data_exprnc_band_id
        inner join exprnc_band_sts_cte exprnc_band_sts
        on ffld_exprnc_band.data_curr_exprnc_band_sts_id = exprnc_band_sts.data_exprnc_band_sts_id
        inner join exprnc_band_sts_ctgy_cte exprnc_band_sts_ctgy
        on exprnc_band_sts.data_exprnc_band_sts_ctgy_id = exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_id
        inner join exprnc_band_config_cte exprnc_band_config
        on ffld_exprnc_band.data_exprnc_band_config_id = exprnc_band_config.data_exprnc_band_config_id
        inner join exprnc_band_manu_tool_cte exprnc_band_manu_tool
        on exprnc_band_config.data_exprnc_band_manu_tool_id = exprnc_band_manu_tool.data_exprnc_band_manu_tool_id
        inner join exprnc_band_mdle_config_cte exprnc_band_mdle_config
        on exprnc_band_config.data_exprnc_band_mdle_config_id = exprnc_band_mdle_config.data_exprnc_band_mdle_config_id
        inner join exprnc_band_mdle_cte exprnc_band_mdle
        on exprnc_band_mdle.data_exprnc_band_mdle_id = exprnc_band_mdle_config.data_exprnc_band_mdle_id
        inner join exprnc_band_vndr_cte exprnc_band_vndr
        on exprnc_band_config.data_exprnc_band_vndr_id = exprnc_band_vndr.data_exprnc_band_vndr_id
        inner join exprnc_band_vndr_rl_cte exprnc_band_vndr_rl
        on exprnc_band_vndr.data_exprnc_band_vndr_rl_id = exprnc_band_vndr_rl.data_exprnc_band_vndr_rl_id
        left outer join dsny_fac_cte dsny_fac
        on ffld_exprnc_band.data_curr_dsny_fac_id = dsny_fac.data_dsny_fac_id
) 

-- select from the final result cte
select * from final
