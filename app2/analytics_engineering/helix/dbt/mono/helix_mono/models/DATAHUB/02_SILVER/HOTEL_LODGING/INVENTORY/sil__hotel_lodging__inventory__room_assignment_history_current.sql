WITH rm_hist_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rm_hist_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
rsrc_own_ref_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_own_ref_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
rsrc_own_cte AS (
    SELECT
        *
    FROM
       {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_own_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
rm_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rm_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
FINAL AS (
    SELECT
        rh.data_rm_hist_id room_history_id,
        rh.data_fac_id facility_id,
        rh.data_rm_id_vl room_number,
        rm.data_rm_ds room_description,
        rh.data_rm_hist_actn_ds room_history_action_description,
        rm.data_rsrc_id reservable_resource_id,
        rm.data_rsrc_invtry_typ_id reservable_inventory_type_id,
        rm.data_max_adlt_ocpncy_cn maximum_adult_occupancy_count,
        rm.data_tot_ocpncy_cn total_occupancy_count,
        rm.data_cntn_in connecting_room_indicator,
        ro.data_asgn_ownr_id assigned_owner_id,
        ror.data_rsrc_own_id reservable_resource_owner_id,
        rh.data_tc_ref_vl travel_component_id,
        COALESCE(
            rh.data_prmy_gst_nm,
            ro.data_own_ds
        ) primary_guest_name,
        COALESCE(
            rh.data_arvl_dts,
            ro.data_own_frm_dts
        ) arrival_datetime,
        COALESCE(
            rh.data_dprt_dts,
            ro.data_own_end_dts
        ) departure_datetime,
        ro.data_adlt_cn adult_count,
        ro.data_chld_cn child_count,
        ro.data_bkng_dt booking_date,
        rh.data_updt_dts AS source_update_datetime,
        ror.data_extnl_own_ref_val external_owner_reference_value,
        ror.data_own_ref_typ_nm owner_reference_type_name,
        rh.data_grp_id_vl group_id_value,
        rh.data_tp_ref_vl travel_plan_reference_value,
        rh.data_ocpncy_sts_nm occupancy_status_name,
        rh.data_hskp_sts_nm housekeeping_status_name,
        rh.data_shr_in sharewith_indicator
    FROM
        rm_hist_cte rh
        LEFT JOIN rsrc_own_ref_cte ror
        ON ror.data_extnl_own_ref_val = rh.data_tc_ref_vl
        LEFT JOIN rsrc_own_cte ro
        ON ro.data_rsrc_own_id = ror.data_rsrc_own_id
        LEFT JOIN rm_cte rm
        ON rh.data_fac_id = rm.data_rsrt_fac_id
)
SELECT
    *
FROM
    FINAL
