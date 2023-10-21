with exprnc_band_mdle_config_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_config_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_mdle_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_mdle_vrsn_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_vrsn_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final as (
    select
        exprnc_band_mdle_config.data_exprnc_band_mdle_config_id as module_configuration_id,
        exprnc_band_mdle_config.data_exprnc_band_mdle_id as module_id,
        exprnc_band_mdle.data_exprnc_band_mdle_cd as module_code,
        exprnc_band_mdle.data_exprnc_band_mdle_ds as module_description,
        exprnc_band_mdle.data_avail_to_gst_in as module_available_to_guest_indicator,
        exprnc_band_mdle_config.data_exprnc_band_mdle_vrsn_id as module_version_id,
        exprnc_band_mdle_vrsn.data_exprnc_band_mdle_vrsn_cd as module_version_code,
        exprnc_band_mdle_vrsn.data_exprnc_band_mdle_vrsn_ds as module_version_description,
        exprnc_band_mdle_vrsn.data_avail_to_gst_in as module_version_available_to_guest_indicator,
        exprnc_band_mdle_config.data_create_usr_id as source_system_create_user_id,
        exprnc_band_mdle_config.data_create_dts as source_system_create_datetime,
        exprnc_band_mdle_config.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_mdle_config.data_updt_dts as source_system_update_datetime,
        exprnc_band_mdle_config.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_mdle_config_cte as exprnc_band_mdle_config
        join exprnc_band_mdle_cte as exprnc_band_mdle
        on exprnc_band_mdle_config.data_exprnc_band_mdle_id = exprnc_band_mdle.data_exprnc_band_mdle_id
        join exprnc_band_mdle_vrsn_cte as exprnc_band_mdle_vrsn
        on exprnc_band_mdle_config.data_exprnc_band_mdle_vrsn_id = exprnc_band_mdle_vrsn.data_exprnc_band_mdle_vrsn_id
)
select * from final
