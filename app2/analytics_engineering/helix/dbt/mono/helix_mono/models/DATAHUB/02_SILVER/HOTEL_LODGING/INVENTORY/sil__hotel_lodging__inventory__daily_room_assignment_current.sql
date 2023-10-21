with rsrc_asgn_req_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_req_versioned') }}
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
final as (
    select
        ra.data_rsrc_id as room_id,
        rar.data_asgn_ownr_id as assigned_owner_id,
        ra.data_rsrc_asgn_req_id as room_assigned_request_id,
        rar.data_asgn_req_dt as assigned_request_date,
        ra.data_rsrc_asgn_req_id as room_assigned_request_id,
        rar.data_asgn_req_dt as assigned_request_date,
        ra.data_asgn_sts_nm as assigned_status_name,
        rar.data_rt_ctgy_nm as room_rate_category,
        ra.data_tmp_asgn_sts_end_dts as temporary_assignment_status_end_datetime,
        ra.data_asgn_lck_in as assignment_locked_indicator,
        ra.data_tmp_sts_usr_nm as temporary_status_user_id,
        rar.data_create_usr_id_cd as create_user_id,
        rar.data_create_dts as create_datetime,
        to_date(
            rar.data_create_dts
        ) as create_date,
        rar.data_updt_usr_id_cd as update_user_id,
        rar.data_updt_dts as source_update_datetime,
        to_date(
            rar.data_updt_dts
        ) as source_update_date
    from
        rsrc_asgn_req_cte rar
        inner join rsrc_asgn_cte ra
        on ra.data_rsrc_asgn_req_id = rar.data_rsrc_asgn_req_id
)

select * from final