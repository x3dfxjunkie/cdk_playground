with exprnc_band_lnk_actvy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_actvy_versioned') }}
),
exprnc_band_lnk_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_lnk_versioned') }}
),
exprnc_band_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_versioned') }}
),
exprnc_band_dsny_prod_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_prod_versioned') }}
),
exprnc_band_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_typ_versioned') }}
),
top_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
),
bottom_color_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
),

final as (
    select
        exprnc_band_lnk_actvy.data_exprnc_band_lnk_actvy_id as guest_link_activity_id,
        exprnc_band_lnk_actvy.data_exprnc_band_lnk_id as guest_link_id,
        exprnc_band_lnk.data_exprnc_band_lnk_uniq_id as magic_band_guest_link_unique_id,
        exprnc_band_lnk.data_gst_src_sys_native_id as guest_source_system_native_id,
        exprnc_band_lnk.data_src_sys_tx as source_system_value,
        exprnc_band_lnk.data_gst_prfl_frst_nm as guest_profile_first_name,
        exprnc_band_lnk.data_gst_prfl_lst_nm as guest_profile_last_name,
        exprnc_band_lnk_actvy.data_exprnc_band_id as magic_band_id,
        exprnc_band.data_exprnc_band_uniq_id as magic_band_unique_identifier,
        exprnc_band.data_exprnc_band_dsny_prod_id as product_id,
        exprnc_band_dsny_prod.data_exprnc_band_typ_id as product_type_id,
        exprnc_band_typ.data_exprnc_band_typ_cd as product_type_code,
        exprnc_band_typ.data_exprnc_band_typ_ds as product_type_description,
        exprnc_band_dsny_prod.data_exprnc_band_top_color_id as top_color_id,
        top_color.data_exprnc_band_color_cd as top_color_code,
        top_color.data_exprnc_band_color_nm as top_color_name,
        exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id as bottom_color_id,
        bottom_color.data_exprnc_band_color_cd as bottom_color_code,
        bottom_color.data_exprnc_band_color_nm as bottom_color_name,
        exprnc_band_lnk_actvy.data_exprnc_band_txn_id as magic_band_transaction_id,
        exprnc_band_lnk_actvy.data_exprnc_band_src_sys_native_id as external_system_native_id,
        exprnc_band_lnk_actvy.data_exprnc_band_txn_src_sys_tx as external_system_value,
        exprnc_band_lnk_actvy.data_exprnc_band_asgn_dts as assignment_datetime,
        cast(exprnc_band_lnk_actvy.data_exprnc_band_asgn_dts as date) as assignment_date,
        cast(exprnc_band_lnk_actvy.data_exprnc_band_asgn_dts as time) as assignment_time,
        exprnc_band_lnk_actvy.data_create_usr_id as source_system_create_user_id,
        exprnc_band_lnk_actvy.data_create_dts as source_system_create_datetime,
        exprnc_band_lnk_actvy.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_lnk_actvy.data_updt_dts as source_system_update_datetime,
        exprnc_band_lnk_actvy.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_lnk_actvy_cte as exprnc_band_lnk_actvy
        inner join exprnc_band_lnk_cte as exprnc_band_lnk
        on exprnc_band_lnk_actvy.data_exprnc_band_lnk_id = exprnc_band_lnk.data_exprnc_band_lnk_id
        inner join exprnc_band_cte as exprnc_band
        on exprnc_band_lnk_actvy.data_exprnc_band_id = exprnc_band.data_exprnc_band_id
        left join exprnc_band_dsny_prod_cte as exprnc_band_dsny_prod
        on exprnc_band.data_exprnc_band_dsny_prod_id = exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id
        left join exprnc_band_typ_cte as exprnc_band_typ
        on exprnc_band_dsny_prod.data_exprnc_band_typ_id = exprnc_band_typ.data_exprnc_band_typ_id
        left join top_color_cte as top_color
        on exprnc_band_dsny_prod.data_exprnc_band_top_color_id = top_color.data_exprnc_band_color_id
        left join bottom_color_cte as bottom_color
        on exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id = bottom_color.data_exprnc_band_color_id
)
select * from final
