-- define a cte for ror
with ror_cte as (
    select
        data_rsrc_own_id,
        data_extnl_own_ref_val
    --from latest_datahub.silver.sil_dreams_resource_inventory_management_rsrc_own_ref_versioned
    from {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_own_ref_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
    and data_own_ref_typ_nm = 'inventory_request'
),

-- define a cte for ir
ir_cte as (
    select
        data_rsrc_id,
        cast(data_rsrc_invtry_req_id as varchar(40)) as data_rsrc_invtry_req_id,
        data_invtry_req_typ_nm,
        data_invtry_req_sts_nm,
        data_invtry_req_strt_dts,
        data_invtry_req_end_dts
    --from latest_datahub.silver.sil_dreams_resource_inventory_management_invtry_req_versioned
    from {{ ref('sil__intermediate__dreams__resource_inventory_management__invtry_req_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- join ror and ir ctes to get the final result
final as (
    select
        ror.data_rsrc_own_id as reservable_resource_owner_id,
        ir.data_rsrc_id as reservable_resource_id,
        ir.data_invtry_req_typ_nm as inventory_request_type_name,
        ir.data_invtry_req_sts_nm as inventory_request_status_name,
        ir.data_invtry_req_strt_dts as inventory_request_start_datetime,
        ir.data_invtry_req_end_dts as inventory_request_end_datetime
    from ror_cte ror
    inner join ir_cte ir on ror.data_extnl_own_ref_val = ir.data_rsrc_invtry_req_id

)

-- select from the final result cte
select * from final