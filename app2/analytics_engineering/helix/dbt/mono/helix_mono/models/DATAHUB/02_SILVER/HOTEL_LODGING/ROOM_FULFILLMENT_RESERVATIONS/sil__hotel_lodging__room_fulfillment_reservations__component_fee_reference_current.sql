with cte_cer as (

    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__chrg_extnl_ref_versioned') }}
    where
        data_extnl_src_nm = 'dreams_tcfee'
        and metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte_fc as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__fee_chrg_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte_final as (
    select
        cer.data_chrg_id as charge_id,
        fc.data_fee_nm as fee_name,
        cer.data_chrg_extnl_ref_vl as reference_id,
        cer.data_create_usr_id_cd as create_user_id,
        cer.data_create_dts as create_datetime,
        to_date(
            cer.data_create_dts
        ) as create_date,
        cer.data_updt_usr_id_cd as update_user_id,
        cer.data_updt_dts as update_datetime,
        to_date(
            cer.data_updt_dts
        ) as update_date
    from
        cte_cer cer
        inner join cte_fc fc
        on cer.data_chrg_id = fc.data_fee_chrg_id
)
select
    *
from
    cte_final
