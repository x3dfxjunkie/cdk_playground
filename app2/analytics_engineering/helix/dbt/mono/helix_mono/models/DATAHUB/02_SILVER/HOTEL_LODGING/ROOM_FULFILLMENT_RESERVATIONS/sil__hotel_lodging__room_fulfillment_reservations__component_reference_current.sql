-- define a cte for the folio chrg_extnl_ref table
with folio_cer_cte as (
    select
        *
    from {{ ref('sil__intermediate__dreams__folio__chrg_extnl_ref_versioned') }}
    where data_extnl_src_nm = 'dreams_tc'
    and metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- get the final result by using the cte
final as (
    select data_chrg_id as charge_id,
    cast(data_chrg_extnl_ref_vl as number(38,0)) as reference_id,
    data_create_usr_id_cd as create_user_id,
    data_create_dts  as create_datetime,
    to_date(data_create_dts) as create_date,
    data_updt_usr_id_cd as update_user_id,
    data_updt_dts as update_datetime,
    to_date(data_updt_dts) as update_date
    from folio_cer_cte

)

-- select from the final result cte
select * from final