with profile_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__profile__prfl_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
 prfl_crtra_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__profile__prfl_crtra_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
final as (
    select
        distinct prfl.data_prfl_id profile_id,
        pc.data_acm_fac_id facility_id,
        null as data_fac_short_nm,
        pc.data_rsrc_invtry_typ_cd room_inventory_type_code,
        pc.data_all_fac_in all_facilities_indicator,
        pc.data_all_rsrc_invtry_typ_in all_resource_inventory_type_indicator,
        prfl.data_prfl_val_cd profile_value_code,
        prfl.data_prfl_val_ds profile_value_description,
        prfl.data_prfl_typ_nm profile_type_name,
        prfl.data_extnl_ref_vl external_reference_value,
        prfl.data_prfl_actv_in profile_active_indicator,
        pc.data_dflt_prfl_in default_profile_indicator,
        pc.data_all_pkg_in all_packages_indicator
    from
        profile_cte prfl
        inner join prfl_crtra_cte pc
        on prfl.data_prfl_id = pc.data_prfl_id
)
select
    *
from
    final
