-- define a cte for rstsq
with rstsq_cte as (
    select
        *
    from {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrt_seq_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'

),

-- define a cte for rmsq
rmsq_cte as (
    select
        *
    from {{ ref('sil__intermediate__dreams__resource_inventory_management__rm_seq_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'

),

-- join rstsq and rmsq ctes to get the final result
final as (
    select
        rmsq.data_rsrc_id as reservable_resource_id,
        rmsq.data_rm_seq_nb as room_sequence_number,
        rstsq.data_rsrt_seq_id as resort_sequence_id,
        rstsq.data_rsrt_fac_id as facility_id,
        rstsq.data_seq_nm as sequence_name

    from rstsq_cte rstsq
    inner join rmsq_cte rmsq on rmsq.data_rsrt_seq_id = rstsq.data_rsrt_seq_id

)

-- select from the final result cte
select * from final
