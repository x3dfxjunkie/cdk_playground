with rsrc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
rsrc_asgn_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
rsrc_asgn_ownr_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_ownr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
rsrc_invtry_typ_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_invtry_typ_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
rsrc_asgn_req_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_req_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
rsrc_own_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_own_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

final as (
    select
        distinct coalesce(
            rao.data_auto_asgn_rsrc_id,
            r.data_rsrc_id
        ) as room_id,
        r.data_asgn_ownr_id as assigned_owner_id,
        ro.data_rsrc_own_id as room_owner_id,
        ra.data_rsrc_asgn_req_id as room_assignment_request_id,
        rao.data_fac_id as facility_id,
        null as fac_short_nm,
        rit.data_rsrc_invtry_typ_cd as room_type_code,
        rao.data_auto_asgn_rsrc_id as automatic_assignment_room_id,
        rao.data_rsrc_invtry_typ_id as room_inventory_type_id,
        rao.data_dvc_own_lnk_id as disney_vacation_club_owner_link_id,
        rao.data_whsl_in as wholesaler_indicator,
        rao.data_asgn_ownr_typ_nm as assignment_owner_type_name,
        rao.data_dvc_res_typ_nm as disney_vacation_club_reservation_type_name,
        rao.data_ownr_sts_nm as owner_status_name,
        rao.data_ownr_strt_dts as owner_start_dts,
        rao.data_vip_in as vip_in,
        rao.data_ownr_rsrt_trfr_in as owner_resort_transfer_indicator,
        rao.data_ownr_end_dts as owner_end_dts,
        rao.data_grp_id_vl as group_id,
        rao.data_blk_cd as block_code,
        rao.data_spcl_need_req_in as special_needs_requested_indicator,
        ro.data_own_ds as owner_description,
        ro.data_own_frm_dts as owner_from_dts,
        ro.data_own_end_dts as owner_to_dts,
        ro.data_orig_shr_ocpnt_in as original_sharewith_occupant_indicator,
        ro.data_onln_chkin_in as online_checkin_indicator,
        ro.data_adlt_cn as adult_count,
        ro.data_chld_cn as child_count,
        ro.data_bkng_dt as booking_date
    from
        rsrc_cte r
        inner join rsrc_asgn_cte ra
        on r.data_rsrc_id = ra.data_rsrc_id
        inner join rsrc_asgn_ownr_cte rao
        on r.data_asgn_ownr_id = rao.data_asgn_ownr_id
        inner join rsrc_invtry_typ_cte rit
        on rao.data_rsrc_invtry_typ_id = rit.data_rsrc_invtry_typ_id
        left join rsrc_asgn_req_cte rar
        on rao.data_asgn_ownr_id = rar.data_asgn_ownr_id
        left join rsrc_own_cte ro
        on rao.data_asgn_ownr_id = ro.data_asgn_ownr_id
)

select * from final