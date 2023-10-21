with exprnc_band_lnk_lnk_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_lnk_versioned') }}
),
primary_link_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
prior_link_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final as (
    select
        exprnc_band_lnk_lnk.data_exprnc_band_lnk_lnk_id as guest_link_history_id,
        exprnc_band_lnk_lnk.data_prmy_exprnc_band_lnk_id as primary_guest_link_id,
        primary_link.data_exprnc_band_lnk_uniq_id as primary_guest_link_unique_identifier,
        primary_link.data_gst_src_sys_native_id as primary_external_system_guest_identifier_value,
        primary_link.data_src_sys_tx as primary_external_system_guest_identifier_name,
        primary_link.data_gst_prfl_frst_nm as primary_guest_first_name,
        primary_link.data_gst_prfl_lst_nm as primary_guest_last_name,
        exprnc_band_lnk_lnk.data_prr_exprnc_band_lnk_id as prior_magic_band_link_id,
        prior_link.data_exprnc_band_lnk_uniq_id as prior_guest_link_unique_identifier,
        prior_link.data_gst_src_sys_native_id as prior_external_system_guest_identifier_value,
        prior_link.data_src_sys_tx as prior_external_system_guest_identifier_name,
        prior_link.data_gst_prfl_frst_nm as prior_guest_first_name,
        prior_link.data_gst_prfl_lst_nm as prior_guest_last_name,
        exprnc_band_lnk_lnk.data_create_usr_id as source_system_create_user_id,
        exprnc_band_lnk_lnk.data_create_dts as source_system_create_datetime,
        exprnc_band_lnk_lnk.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_lnk_lnk.data_updt_dts as source_system_update_datetime,
        exprnc_band_lnk_lnk.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_lnk_lnk_cte as exprnc_band_lnk_lnk
        join primary_link_cte as primary_link
        on primary_link.data_exprnc_band_lnk_id = exprnc_band_lnk_lnk.data_prmy_exprnc_band_lnk_id
        join prior_link_cte as prior_link
        on prior_link.data_exprnc_band_lnk_id = exprnc_band_lnk_lnk.data_prr_exprnc_band_lnk_id
)
select * from final
