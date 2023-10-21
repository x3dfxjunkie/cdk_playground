with rf_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_feat_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(
            metadata_operation
        ) != 'DELETE'
),
rm_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rm_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(
            metadata_operation
        ) != 'DELETE'
),
f_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__feat_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(
            metadata_operation
        ) != 'DELETE'
),
-- join ctes to get the final result
final as (
    select
        rf.data_rsrc_id as reservable_resource_id,
        rm.data_rsrt_fac_id,
        rm.data_rsrc_invtry_typ_id,
        rf.data_feat_id as feature_id,
        f.data_feat_typ_nm as feature_type_name,
        f.data_feat_nm as feature_name,
        f.data_feat_ds as feature_description
    from
        rf_cte rf
        inner join rm_cte rm
        on rf.data_rsrc_id = rm.data_rsrc_id
        inner join f_cte f
        on rf.data_feat_id = f.data_feat_id
)
select
    *
from
    final
