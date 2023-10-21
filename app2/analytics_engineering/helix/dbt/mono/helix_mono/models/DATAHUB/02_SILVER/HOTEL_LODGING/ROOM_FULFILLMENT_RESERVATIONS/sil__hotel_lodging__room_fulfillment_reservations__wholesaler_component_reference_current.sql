with ter_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__tc_extnl_ref_versioned') }}
    where
        data_tc_extnl_ref_typ_nm = 'reservation'
        and metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

grp_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__group_management__grp_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

final as (
    select
        distinct ter.data_tc_id as component_id,
        ter.data_tc_extnl_src_nm as wholesaler_id,
        grp.data_grp_nm as wholesaler_name,
        data_tc_extnl_ref_vl as reference_id,
        ter.data_create_usr_id_cd as create_user_id,
        ter.data_create_dts as create_datetime,
        to_date(
            ter.data_create_dts
        ) as create_date,
        ter.data_updt_usr_id_cd as update_user_id,
        ter.data_updt_dts as update_datetime,
        to_date(
            ter.data_updt_dts
        ) as update_date
    from
        ter_cte as ter
        inner join grp_cte as grp
        on ter.data_tc_extnl_src_nm = grp.data_grp_cd
)

select * from final
