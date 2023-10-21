with grp_cmt_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__group_management__grp_cmt_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
grp_cmt_rte_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__group_management__grp_cmt_rte_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
grp_cmt_typ_rte_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__group_management__grp_cmt_typ_rte_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

final as (
    select
        distinct gc.data_grp_cd as group_code,
        gc.data_grp_cmt_id as group_comment_id,
        gc.data_grp_cmt_tx as group_comment_notes,
        gcr.data_grp_cmt_typ_rte_id as group_comment_type_route_id,
        gctr.data_grp_cmt_lvl_nm as group_comment_level_name,
        gctr.data_grp_cmt_sect_nm as group_comment_section_name,
        gctr.data_grp_cmt_typ_nm as group_comment_type_name,
        gctr.data_rte_nm as route_name,
        gc.data_create_dts as create_datetime,
        gc.data_updt_dts as source_update_datetime,
        gc.data_create_usr_id_cd as create_user_id,
        gc.data_updt_usr_id_cd as update_user_id
    from
        grp_cmt_cte as gc
        inner join grp_cmt_rte_cte as gcr
        on gc.data_grp_cmt_id = gcr.data_grp_cmt_id
        inner join grp_cmt_typ_rte_cte as gctr
        on gcr.data_grp_cmt_typ_rte_id = gctr.data_grp_cmt_typ_rte_id
    order by
        data_updt_dts desc
)

select * from final