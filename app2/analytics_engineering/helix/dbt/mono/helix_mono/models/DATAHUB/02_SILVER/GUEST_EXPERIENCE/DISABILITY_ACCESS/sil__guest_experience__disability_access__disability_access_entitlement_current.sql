-- cte for enttl
with cte_enttl as (
    select
        *
    from {{ ref('sil__intermediate__das__wdw__enttl_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- cte for tnc
cte_tnc as (
    select
        *
	from {{ ref('sil__intermediate__das__wdw__tnc_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- cte for enttl_lnk
cte_enttl_lnk as (
    select
		*
	from {{ ref('sil__intermediate__das__wdw__enttl_lnk_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- cte for lnk
cte_lnk as (
    select
        *
	from {{ ref('sil__intermediate__das__wdw__lnk_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- cte for das_extnl_acct_lnk
cte_das_extnl_acct_lnk as (
    select
        *
	from {{ ref('sil__intermediate__das__wdw__extnl_acct_lnk_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- final cte with aliasing and joins
final as (
    select
        e.data_enttl_id as entitlement_id,
        e.data_enttl_strt_dts as start_datetime,
        cast(e.data_enttl_strt_dts as date) as start_date,
        cast(e.data_enttl_strt_dts as time) as start_time,
        e.data_enttl_end_dts as end_datetime,
        cast(e.data_enttl_end_dts as date) as end_date,
        cast(e.data_enttl_end_dts as time) as end_time,
        e.data_tnc_ver as terms_and_conditions_version,
        t.data_tnc_txt as terms_and_conditions_text,
        t.data_tnc_strt_dts as terms_and_conditions_start_datetime,
        t.data_tnc_end_dts as terms_and_conditions_end_datetime,
        e.data_max_fp_booking as maximum_experience_count,
        e_lnk.data_lnk_id as guest_id,
        das_extnl_acct_lnk.data_extnl_sys_entty_nm as supplemental_guest_id_name,
        das_extnl_acct_lnk.data_extnl_sys_entty_vl as supplemental_guest_id_value,
        lnk.data_titl as guest_title,
        lnk.data_frst_nm as guest_first_name,
        lnk.data_mi as guest_middle_initial,
        lnk.data_lst_nm as guest_last_name,
        lnk.data_suff as guest_suffix_name,
        e_lnk.data_enttl_lnk_strt_dts as guest_link_start_datetime,
        cast(e_lnk.data_enttl_lnk_strt_dts as date) as guest_link_start_date,
        cast(e_lnk.data_enttl_lnk_strt_dts as time) as guest_link_start_time,
        e_lnk.data_enttl_lnk_end_dts as guest_link_end_datetime,
        cast(e_lnk.data_enttl_lnk_end_dts as date) as guest_link_end_date,
        cast(e_lnk.data_enttl_lnk_end_dts as time) as guest_link_end_time,
        e_lnk.data_gwd_rl as guest_with_disability_role_indicator,
        e_lnk.data_under3 as guest_with_disability_infant_indicator,
        e_lnk.data_hs_opt_out as guest_with_disability_media_opt_out_indicator,
        e.data_create_usr_id as source_system_create_user_id,
        e.data_create_dts as source_system_create_datetime,
        e.data_updt_usr_id as source_system_update_user_id,
        e.data_updt_dts as source_system_update_datetime,
        e.data_lgcl_del_in as source_system_logical_delete_indicator
    from
        cte_enttl e
    inner join cte_tnc t on e.data_tnc_ver = t.data_version
    inner join cte_enttl_lnk e_lnk on e_lnk.data_enttl_id = e.data_enttl_id
    inner join cte_lnk lnk on lnk.data_lnk_id = e_lnk.data_lnk_id
    left join cte_das_extnl_acct_lnk das_extnl_acct_lnk on das_extnl_acct_lnk.data_lnk_id = lnk.data_lnk_id
)
-- select all columns from the final cte
select *
from final
