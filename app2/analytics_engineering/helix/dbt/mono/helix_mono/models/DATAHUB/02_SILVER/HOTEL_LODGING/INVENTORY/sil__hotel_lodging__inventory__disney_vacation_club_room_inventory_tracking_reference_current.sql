-- define a cte for ror
with ror_cte as (
    select * from {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_own_ref_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a final cte
final as(
    select
        ror.data_rsrc_own_id as room_owner_id,
        ror.data_extnl_own_ref_val as reference_id,
        ror.data_create_dts as create_datetime,
        to_date(ror.data_create_dts) as create_date,
        ror.data_create_usr_id_cd as create_usr_id_cd
    from ror_cte ror
    where ror.data_own_ref_typ_nm = 'invtry_tracking_id'
)

-- select from the final result cte
select * from final