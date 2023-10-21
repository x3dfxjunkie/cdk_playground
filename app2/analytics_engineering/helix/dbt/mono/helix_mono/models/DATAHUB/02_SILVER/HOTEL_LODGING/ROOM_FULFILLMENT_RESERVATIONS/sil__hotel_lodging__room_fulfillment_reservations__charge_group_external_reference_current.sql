with cger_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__chrg_grp_extnl_ref_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
er_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__extnl_ref_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
final_cte as (
    select
        distinct cg.data_chrg_grp_id as charge_group_id,
        cg.data_prmy_extnl_ref_in as primary_external_reference,
        er.data_extnl_src_nm as external_charge_group_source_name,
        er.data_extnl_ref_val as external_charge_group_reference_value,
        cg.data_updt_dts as source_update_datetime
    from
        cger_cte cg
        inner join er_cte er
        on cg.data_extnl_ref_id = er.data_extnl_ref_id
)
select
    *
from
    final_cte
