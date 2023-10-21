with cte_chargedata as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__chrg_extnl_ref_versioned') }} 
    where
        data_extnl_src_nm = 'dreams_tcg'
        and metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

cte_final as (
    select
        cer.data_chrg_id as charge_id,
        cast(cer.data_chrg_extnl_ref_vl as number(38, 0)) as reference_id,
        cer.data_create_usr_id_cd as create_user_id,
        cer.data_create_dts as create_datetime,
        to_date(cer.data_create_dts) as create_date,
        cer.data_updt_usr_id_cd as update_user_id,
        cer.data_updt_dts as update_datetime,
        to_date(cer.data_updt_dts) as update_date
    from
        cte_chargedata cer
    
)

select *
from cte_final
