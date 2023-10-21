-- define a cte for exprnc_band_actvy
with exprnc_band_actvy_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_actvy_versioned') }}
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
-- define a cte for exprnc_band_dsny_prod
exprnc_band_dsny_prod_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_prod_versioned') }}
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
-- join the ctes to get the final result
final as (
    select
        exprnc_band_actvy.data_exprnc_band_actvy_id as activity_id,
        exprnc_band_actvy.data_exprnc_band_id as magic_band_id,
        exprnc_band.data_exprnc_band_seq_nb as magic_band_sequence_number,
        exprnc_band.data_curr_exprnc_band_lnk_id as current_guest_link_id,
        exprnc_band.data_exprnc_band_uniq_id as magic_band_unique_identifier,
        exprnc_band.data_exprnc_band_rtl_in as retail_indicator,
        exprnc_band_actvy.data_exprnc_band_dsny_prod_id as product_id,
        exprnc_band_dsny_prod.data_exprnc_band_erlst_fflmt_dy_cn as earliest_fulfillment_day_count,
        exprnc_band_dsny_prod.data_exprnc_band_shipmt_to_rsrt_in as ship_to_resort_indicator,
        cast(
            exprnc_band_dsny_prod.data_exprnc_band_prod_avail_fr_dts as date
        ) as product_available_from_date,
        cast(
            exprnc_band_dsny_prod.data_exprnc_band_prod_avail_to_dts as date
        ) as product_available_to_date,
        exprnc_band_actvy.data_exprnc_band_prt_nm as printed_name,
        exprnc_band_actvy.data_exprnc_band_gst_cnfirm_in as guest_confirmation_indicator,
        exprnc_band_actvy.data_exprnc_band_cstm_prt_nm_in as custom_printed_name_indicator,
        exprnc_band_actvy.data_exprnc_band_updt_dts as activity_update_datetime,
        cast(
            exprnc_band_actvy.data_exprnc_band_updt_dts as date
        ) as activity_update_date,
        cast(
            exprnc_band_actvy.data_exprnc_band_updt_dts as time
        ) as activity_update_time,
        exprnc_band_actvy.data_opt_out_in as opt_out_indicator,
        exprnc_band_actvy.data_exprnc_band_opt_out_rsn_id as opt_out_reason_id,
        exprnc_band_opt_out_rsn.data_exprnc_band_opt_out_rsn_cd as opt_out_reason_code,
        exprnc_band_opt_out_rsn.data_exprnc_band_opt_out_rsn_ds as opt_out_reason_description,
        exprnc_band_actvy.data_logical_del_in as source_system_logical_delete_indicator,
        exprnc_band_actvy.data_create_usr_id as source_system_create_user_id,
        exprnc_band_actvy.data_create_dts as source_system_create_datetime,
        exprnc_band_actvy.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_actvy.data_updt_dts as source_system_update_datetime
    from
        exprnc_band_actvy_cte exprnc_band_actvy
        inner join exprnc_band_cte exprnc_band
        on exprnc_band_actvy.data_exprnc_band_id = exprnc_band.data_exprnc_band_id
        inner join exprnc_band_dsny_prod_cte exprnc_band_dsny_prod
        on exprnc_band_actvy.data_exprnc_band_dsny_prod_id = exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id
        left outer join exprnc_band_opt_out_rsn_cte exprnc_band_opt_out_rsn
        on exprnc_band_opt_out_rsn.data_exprnc_band_opt_out_rsn_id = exprnc_band_actvy.data_exprnc_band_opt_out_rsn_id
) -- select from the final result gcte
select
    *
from
    final
