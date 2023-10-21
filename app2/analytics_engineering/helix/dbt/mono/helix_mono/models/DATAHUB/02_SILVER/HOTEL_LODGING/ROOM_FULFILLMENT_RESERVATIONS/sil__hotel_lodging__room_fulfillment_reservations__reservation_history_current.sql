WITH res_hist_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__rooms_reservations__res_hist_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
        AND data_res_hist_proc_ds <> 'Sync'
),
tps_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__rooms_reservations__tps_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
        AND data_src_acct_ctr_id IN (2,7047)
),

final AS (
    SELECT
        DISTINCT rh.data_res_hist_id AS reservation_history_id,
        rh.data_tps_id AS travel_plan_segment_id,
        rh.data_tc_grp_nm AS travel_component_group_number,
        rh.data_tc_id AS travel_component_id,
        rh.data_res_hist_proc_ds AS reservation_history_procedure_description,
        rh.data_proc_dts AS procedure_datetime,
        TO_DATE(
            rh.data_proc_dts
        ) AS procedure_date,
        rh.data_res_hist_tx AS reservation_history_text,
        tps.data_tps_arvl_dt AS travel_plan_segment_arrival_date,
        tps.data_tps_dprt_dt AS travel_plan_departure_date
    FROM
        res_hist_cte rh
        INNER JOIN tps_cte tps
        ON rh.data_tps_id = tps.data_tps_id
)

SELECT * FROM final

