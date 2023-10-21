-- define a cte for cer
with cer_cte as (
    select * from {{ ref('sil__intermediate__dreams__folio__chrg_extnl_ref_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
    and data_extnl_src_nm = 'dscs'
),

-- define a cte for ec
ec_cte as (
    select * from {{ ref('sil__intermediate__dreams__folio__evt_chrg_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a cte for ft
ft_cte as (
    select * from {{ ref('sil__intermediate__dreams__accounting__fnc_typ_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a cte for rc
rc_cte as (
    select * from {{ ref('sil__intermediate__dreams__accounting__rpt_ctgy_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),


final as (
    select
        cer.data_chrg_id as charge_id,
        cer.data_chrg_extnl_ref_vl as reference_id,
        ec.data_fnc_typ_id as fnc_typ_id,
        ft.data_fnc_typ_nm as fnc_typ_nm,
        ec.data_rpt_ctgy_id as rpt_ctgy_id,
        rc.data_rpt_ctgy_nm as rpt_ctgy_nm,
        ec.data_evt_dt as evt_dt,
        ec.data_evt_loc_nm as evt_loc_nm,
        cer.data_create_usr_id_cd as create_user_id,
        cer.data_create_dts as create_datetime,
        to_date(cer.data_create_dts) as create_date,
        cer.data_updt_usr_id_cd as update_user_id,
        cer.data_updt_dts as update_datetime,
        to_date(cer.data_updt_dts) as update_date
    from cer_cte cer
    inner join ec_cte ec on cer.data_chrg_id = ec.data_evt_chrg_id
    inner join ft_cte ft on ec.data_fnc_typ_id = ft.data_fnc_typ_id
    inner join rc_cte rc on ec.data_rpt_ctgy_id = rc.data_rpt_ctgy_id
)

-- select from the final result cte
select * from final