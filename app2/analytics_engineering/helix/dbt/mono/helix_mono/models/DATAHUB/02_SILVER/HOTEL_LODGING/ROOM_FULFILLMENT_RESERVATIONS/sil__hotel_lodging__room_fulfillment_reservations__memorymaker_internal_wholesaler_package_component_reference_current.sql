with ter_cte as (
    select
        *
    from
        {{ ref ('sil__intermediate__dreams__rooms_reservations__tc_extnl_ref_versioned') }}
    where
        data_tc_extnl_ref_typ_nm = 'linkage'
        and metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

final as (
    select
        data_tc_id as component_id,
        data_tc_extnl_ref_vl as reference_id,
        data_create_usr_id_cd as create_user_id,
        data_create_dts as create_datetime,
        to_date(data_create_dts) as create_date,
        data_updt_usr_id_cd as update_user_id,
        data_updt_dts as update_datetime,
        to_date(data_updt_dts) as update_date
    from
        ter_cte
)
select * from final
