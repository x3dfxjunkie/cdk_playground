with lvl_n_rl_cte as (
    select *
    from {{ ref('sil__intermediate__level__n_wdw__lvl_n_rl_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


lvl_n_rl_typ_cte as (
    select *
    from {{ ref('sil__intermediate__level__n_wdw__lvl_n_rl_typ_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


lvl_n_rl_ctgy_cte as (
    select *
    from {{ ref('sil__intermediate__level__n_wdw__lvl_n_rl_ctgy_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final as (
    select
        lvl_n_rl.data_lvl_n_rl_id as digital_download_role_id,
        lvl_n_rl.data_lvl_n_rl_nm as role_name,
        lvl_n_rl.data_lvl_n_rl_typ_id as role_type_id,
        lvl_n_rl_typ.data_lvl_n_rl_typ_nm as role_type_name,
        lvl_n_rl_typ.data_lvl_n_rl_ctgy_id as role_category_id,
        lvl_n_rl_ctgy.data_lvl_n_rl_ctgy_nm as role_category_name,
        lvl_n_rl.data_create_dts as source_system_create_datetime,
        lvl_n_rl.data_create_usr_id as source_system_create_user_id,
        lvl_n_rl.data_updt_dts as source_system_update_datetime,
        lvl_n_rl.data_updt_usr_id as source_system_update_user_id
    from
    lvl_n_rl_cte lvl_n_rl
    join lvl_n_rl_typ_cte lvl_n_rl_typ on lvl_n_rl_typ.data_lvl_n_rl_typ_id = lvl_n_rl.data_lvl_n_rl_typ_id 
    join lvl_n_rl_ctgy_cte lvl_n_rl_ctgy on lvl_n_rl_ctgy.data_lvl_n_rl_ctgy_id = lvl_n_rl_typ.data_lvl_n_rl_ctgy_id
)

select * from final