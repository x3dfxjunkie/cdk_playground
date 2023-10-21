with res_mgmt_req_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__res_mgmt_req_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
res_mgmt_req_rte_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__res_mgmt_req_rte_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
prfl_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__profile__prfl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
tc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__tc_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

final as (
    select
        distinct rmr.data_res_mgmt_req_id as reservation_management_request_id,
        tc.data_tc_grp_nb as travel_component_group_number,
        rmr.data_tc_id as travel_component_id,
        tc.data_asgn_own_id as assigned_owner_id,
        tc.data_fac_id as facility_id,
        null as data_fac_short_nm,
        to_date(
            data_tc_strt_dts
        ) as travel_component_start_date,
        to_date(
            data_tc_end_dts
        ) as travel_component_end_date,
        rmr.data_res_mgmt_req_typ_nm as reservation_management_request_type_name,
        rmr.data_res_mgmt_prfl_id as reservation_management_request_profile_id,
        prfl.data_prfl_val_ds as profile_value_description,
        prfl.data_prfl_typ_nm as profile_type_name,
        rmrr.data_res_mgmt_rte_nm as reservation_management_route_name,
        rmr.data_res_mgmt_req_tx as reservation_management_request_text,
        rmr.data_cfdntl_in as confidential_indicator,
        rmr.data_gsr_in as guest_service_recovery_indicator,
        rmr.data_req_inactv_dts as request_inactive_dts
    from
        res_mgmt_req_cte rmr
        inner join res_mgmt_req_rte_cte rmrr
        on rmr.data_res_mgmt_req_id = rmrr.data_res_mgmt_req_id
        inner join prfl_cte prfl
        on rmr.data_res_mgmt_prfl_id = prfl.data_prfl_id
        inner join tc_cte tc
        on rmr.data_tc_id = tc.data_tc_id
)

select * from final

