with exprnc_band_dsnx_fac_txfr_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_fac_txfr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
dsny_fac_band_invtry_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_band_invtry_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
dsny_fac_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
ffld_exprnc_band_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__ffld_exprnc_band_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
dest_dsny_fac_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__dsny_fac_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_sts_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_sts_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
exprnc_band_sts_ctgy_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__xbms__wdw__exprnc_band_sts_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final as (
    select
        exprnc_band_dsny_fac_txfr.data_exprnc_band_dsny_fac_txfr_id as facility_transfer_id,
        exprnc_band_dsny_fac_txfr.data_dsny_fac_band_invtry_id as facility_inventory_id,
        dsny_fac_band_invtry.data_dsny_fac_id as inventory_facility_id,
        dsny_fac.data_dsny_fac_nm as inventory_facility_name,
        dsny_fac.data_fac_id as inventory_enterprise_facility_id,
        dsny_fac_band_invtry.data_ffld_exprnc_band_id as fulfilled_magic_band_id,
        ffld_exprnc_band.data_exprnc_band_id as magic_band_id,
        ffld_exprnc_band.data_curr_exprnc_band_sts_id as current_magic_band_status_id,
        exprnc_band_sts.data_exprnc_band_sts_ctgy_id as current_magic_band_status_category_id,
        exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_cd as current_magic_band_status_category_code,
        exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_ds as current_magic_band_status_category_description,
        exprnc_band_sts.data_exprnc_band_sts_cd as current_magic_band_status_code,
        exprnc_band_sts.data_exprnc_band_sts_ds as current_magic_band_status_description,
        dsny_fac_band_invtry.data_exprnc_band_txn_id as magic_band_transaction_id,
        dsny_fac_band_invtry.data_exprnc_band_frst_rec_fac_dts as facility_inventory_start_datetime,
        cast(dsny_fac_band_invtry.data_exprnc_band_frst_rec_fac_dts as date) as facility_inventory_start_date,
        cast(dsny_fac_band_invtry.data_exprnc_band_frst_rec_fac_dts as time) as facility_inventory_start_time,
        dsny_fac_band_invtry.data_exprnc_band_rec_lvg_fac_dts as facility_inventory_end_datetime,
        cast(dsny_fac_band_invtry.data_exprnc_band_rec_lvg_fac_dts as date) as facility_inventory_end_date,
        cast(dsny_fac_band_invtry.data_exprnc_band_rec_lvg_fac_dts as time) as facility_inventory_end_time,
        dsny_fac_band_invtry.data_fac_shipmt_case_nb as facility_shipment_case_number,
        exprnc_band_dsny_fac_txfr.data_dest_dsny_fac_id as destination_facility_id,
        dest_dsny_fac.data_dsny_fac_nm as destination_facility_name,
        dest_dsny_fac.data_fac_id as destination_enterprise_facility_id,
        exprnc_band_dsny_fac_txfr.data_txfr_expect_dlvr_dt as transfer_expected_delivery_date,
        exprnc_band_dsny_fac_txfr.data_create_usr_id as source_system_create_user_id,
        exprnc_band_dsny_fac_txfr.data_create_dts as source_system_create_datetime,
        exprnc_band_dsny_fac_txfr.data_updt_usr_id as source_system_update_user_id,
        exprnc_band_dsny_fac_txfr.data_updt_dts as source_system_update_datetime,
        exprnc_band_dsny_fac_txfr.data_logical_del_in as source_system_logical_delete_indicator
    from
        exprnc_band_dsnx_fac_txfr_cte as exprnc_band_dsny_fac_txfr
        inner join dsny_fac_band_invtry_cte as dsny_fac_band_invtry
        on dsny_fac_band_invtry.data_dsny_fac_band_invtry_id = exprnc_band_dsny_fac_txfr.data_dsny_fac_band_invtry_id
        inner join dsny_fac_cte as dsny_fac
        on dsny_fac.data_dsny_fac_id = dsny_fac_band_invtry.data_dsny_fac_id
        inner join ffld_exprnc_band_cte as ffld_exprnc_band
        on ffld_exprnc_band.data_ffld_exprnc_band_id = dsny_fac_band_invtry.data_ffld_exprnc_band_id
        inner join dest_dsny_fac_cte as dest_dsny_fac
        on dest_dsny_fac.data_dsny_fac_id = exprnc_band_dsny_fac_txfr.data_dest_dsny_fac_id
        inner join exprnc_band_sts_cte as exprnc_band_sts
        on exprnc_band_sts.data_exprnc_band_sts_id = ffld_exprnc_band.data_curr_exprnc_band_sts_id
        inner join exprnc_band_sts_ctgy_cte as exprnc_band_sts_ctgy
        on exprnc_band_sts_ctgy.data_exprnc_band_sts_ctgy_id = exprnc_band_sts.data_exprnc_band_sts_ctgy_id
)
select * from final
