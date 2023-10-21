with exprnc_band_link_cte as (

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
        exprnc_band_link.data_exprnc_band_lnk_id guest_link_id,
        exprnc_band_link.data_exprnc_band_lnk_uniq_id guest_link_unique_identifier,
        exprnc_band_link.data_gst_src_sys_native_id external_system_guest_identifier_value,
        exprnc_band_link.data_src_sys_tx external_system_guest_identifier_name,
        exprnc_band_link.data_gst_prfl_frst_nm guest_first_name,
        exprnc_band_link.data_gst_prfl_lst_nm guest_last_name,
        exprnc_band_link.data_create_usr_id source_system_create_user_id,
        exprnc_band_link.data_create_dts source_system_create_datetime,
        exprnc_band_link.data_updt_usr_id source_system_update_user_id,
        exprnc_band_link.data_updt_dts source_system_update_datetime,
        exprnc_band_link.data_logical_del_in source_system_logical_delete_indicator
    from
        exprnc_band_link_cte exprnc_band_link
)

select
    *
from
    final
