-- Define a CTE for GRP
WITH grp_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__group_management__grp_versioned')}}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
-- Define a CTE for GPR
gpr_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__group_management__grp_pty_rl_versioned')}}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
-- Define a CTE for GA
ga_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__group_management__grp_atritn_versioned')}}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
-- Define a CTE for BF
bf_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__group_management__blk_fac_versioned')}}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
-- Define a CTE for GB
gb_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__group_management__grp_blk_versioned')}}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
-- Join C, TAC and TAC CTEs to get the final result
FINAL AS (
    SELECT
        grp.data_grp_cd AS group_code,
        grp.data_grp_nm AS group_name,
        grp.data_grp_whsl_in AS group_wholesale_indicator,
        grp.data_grp_stg_nm AS group_stage_name,
        grp.data_opty_typ_nm AS opportunity_type_name,
        grp.data_grp_bus_src_nm AS group_business_source_name,
        grp.data_sls_dept_nm AS sales_dept_name,
        grp.data_sls_mgr_nm AS sales_manager_name,
        gpr.data_rl_nm AS role_name,
        gpr.data_pty_id AS transactional_party_id,
        grp.data_grp_arvl_dt AS group_arrival_date,
        grp.data_grp_dprt_dt AS group_departure_date,
        grp.data_grp_peak_arvl_dt AS group_peak_arrival_date,
        grp.data_grp_peak_dprt_dt AS group_peak_departure_date,
        grp.data_grp_run_hs_in AS group_run_of_house_indicator,
        ga.data_grp_atritn_dy_cn AS group_attrition_day_count,
        ga.data_grp_atritn_dt AS group_attrition_date,
        ga.data_grp_atritn_pc AS group_attrition_percentage,
        ga.data_grp_atritn_tx AS group_attrition_notes,
        grp.data_grp_peak_rm_cn AS group_peak_room_count,
        grp.data_grp_tot_rm_cn AS group_total_room_count,
        grp.data_hm_fac_id AS home_facility_id,
        grp.data_grp_bk_hm_fac_frst_in AS group_book_home_facility_first_indicator,
        bf.data_blk_cd AS room_block_code,
        gb.data_grp_blk_ppty_sync_in AS group_block_property_sync_indicator,
        grp.data_grp_dlgt_bkng_meth_nm AS group_delegate_booking_method_name,
        grp.data_dlvr_meth_nm AS confirmation_delivery_method_name,
        grp.data_grp_cnfirm_dest_nm AS group_confirmation_destination_name,
        grp.data_gro_nm AS group_office_name,
        grp.data_gro_agt_nm AS group_office_agent_name,
        grp.data_srvc_mgr_nm AS service_manager_name,
        grp.data_sls_phn_nb AS sales_phone_number,
        grp.data_srvc_mgr_nm AS service_manager_name,
        grp.data_grp_peak_arvl_tm_tx AS group_peak_arrival_team_notes,
        grp.data_grp_exprs_chk_out_in AS group_express_check_out_indicator,
        grp.data_grp_hide_rt_in AS group_hide_rate_indicator,
        grp.data_grp_comm_allow_in AS group_commission_allow_indicator,
        grp.data_grp_byps_auto_cncl_in AS group_bypass_auto_cancel_indicator,
        grp.data_grp_byps_dpst_in AS group_bypass_deposit_indicator,
        grp.data_grp_byps_cncl_fee_in AS group_bypass_cancellation_fee_indicator,
        grp.data_grp_byps_mod_fee_in AS group_bypass_modification_fee_indicator,
        grp.data_grp_res_guar_in AS group_reservation_guaranteed_indicator,
        grp.data_grp_dlgt_wrtoff_in AS group_delegate_writeoff_indicator,
        grp.data_grp_addl_adlt_am AS group_additional_adult_amount,
        grp.data_create_dts AS create_datetime,
        grp.data_updt_dts AS source_update_datetime
    FROM
        grp_cte grp
        LEFT JOIN gpr_cte gpr
        ON grp.data_grp_cd = gpr.data_grp_cd
        LEFT JOIN ga_cte ga
        ON grp.data_grp_cd = ga.data_grp_cd
        LEFT JOIN bf_cte bf
        ON grp.data_grp_cd = bf.data_blk_cd
        AND grp.data_hm_fac_id = bf.data_fac_id
        AND bf.data_fac_id <> 0
        LEFT JOIN gb_cte gb
        ON grp.data_grp_cd = gb.data_grp_cd
)
-- Select from the final result CTE
SELECT
    *
FROM
    FINAL
